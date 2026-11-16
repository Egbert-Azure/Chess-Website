"""Independent final check of the shortlist:
1. the position really arises in the game (for 'what if': the game position
   before it, and the alternative is a legal move the opponent didn't play);
2. a fresh, longer engine search (20 s, three lines) still finds exactly one
   move that works. Results replace the earlier figures.
Usage: python3 -I finalcheck.py <games.pgn> <shortlist.json> <out.json>"""
import json, math, sys
import chess, chess.engine, chess.pgn

MATE = 100_000
games = []
with open(sys.argv[1]) as f:
    while (g := chess.pgn.read_game(f)) is not None:
        games.append(g)
picks = json.load(open(sys.argv[2]))


def cp(score):
    s = score.relative
    if s.is_mate():
        m = s.mate()
        return MATE - abs(m) * 100 if m > 0 else -MATE + abs(m) * 100
    return s.score()


def wc(v):
    v = max(-2000, min(2000, v if abs(v) < MATE - 5000 else math.copysign(2000, v)))
    return 2 / (1 + math.exp(-0.00368208 * v)) - 1


def fen_at(game, ply):
    b = game.board()
    for i, mv in enumerate(game.mainline_moves()):
        if i == ply:
            break
        b.push(mv)
    return b


eng = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")
eng.configure({"Threads": 2, "Hash": 1024})
ok_list, problems = [], []
for p in picks:
    g = games[p["game"]]
    label = f"{g.headers['White']} – {g.headers['Black']}, ply {p['ply']}"
    if p.get("whatif"):
        parent = fen_at(g, p["ply"] - 1)
        alt = chess.Move.from_uci(p["alt"])
        real = list(g.mainline_moves())[p["ply"] - 1]
        if parent.fen() != p["parent_fen"] or alt not in parent.legal_moves or alt == real or real.uci() != p["real"]:
            problems.append(f"{label}: 'what if' position doesn't match the game"); continue
        parent.push(alt)
        board = parent
    else:
        board = fen_at(g, p["ply"])
        played = list(g.mainline_moves())[p["ply"]]
        if played.uci() != p["played"]:
            problems.append(f"{label}: played move doesn't match"); continue
    if board.fen() != p["fen"]:
        problems.append(f"{label}: position doesn't match the game"); continue

    infos = eng.analyse(board, chess.engine.Limit(time=20), multipv=3)
    b1, b2 = cp(infos[0]["score"]), cp(infos[1]["score"]) if len(infos) > 1 else -MATE
    key = infos[0]["pv"][0]
    if p["kind"] == "mate":
        good = b1 >= MATE - 5000 and not b2 >= MATE - 5000
    elif p["kind"] == "win":
        if p.get("relaxed"):  # human games: a clear win (about +2.5) far ahead of the rest
            good = wc(b1) >= 0.42 and wc(b1) - wc(b2) >= 0.4
        else:
            good = wc(b1) >= 0.6 and wc(b1) - wc(b2) >= 0.5
    elif p.get("relaxed"):
        good = wc(b1) >= -0.25 and wc(b2) <= -0.42 and wc(b1) - wc(b2) >= 0.35
    else:
        good = wc(b1) >= -0.25 and wc(b2) <= -0.55 and wc(b1) - wc(b2) >= 0.4
    if not good or key.uci() != p["solution"]:
        problems.append(f"{label}: fails the 20-second check ({board.san(key)} {b1} / {b2})"); continue
    p.update({"deep1": b1, "deep2": b2, "depth": infos[0]["depth"], "line_san": board.variation_san(infos[0]["pv"][:7])})
    ok_list.append(p)
    print(f"ok  {label}: {p['solution_san']} {b1} vs {b2} (depth {infos[0]['depth']})", flush=True)
eng.quit()
json.dump(ok_list, open(sys.argv[3], "w"), indent=1, ensure_ascii=False)
for x in problems:
    print("DROPPED", x)
print(f"{len(ok_list)} of {len(picks)} confirmed")
