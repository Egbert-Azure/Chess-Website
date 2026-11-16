"""'What if' puzzles: positions where your opponent had to find one precise move.
For each natural alternative that loses, check whether you'd then have had
exactly one winning move. That position (after the alternative) is the puzzle.
Usage: python3 -I traps.py <games.pgn> <scan.jsonl> <out.json>"""
import json, math, sys
from collections import defaultdict
import chess, chess.engine, chess.pgn

ME = "Schroeer, Egbert"
MATE = 100_000
PGN, SCAN, OUT = sys.argv[1:4]
VALUE = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0}


def cp(score):
    s = score.relative
    if s.is_mate():
        m = s.mate()
        return MATE - abs(m) * 100 if m > 0 else -MATE + abs(m) * 100
    return s.score()


def wc(v):
    v = max(-2000, min(2000, v if abs(v) < MATE - 5000 else math.copysign(2000, v)))
    return 2 / (1 + math.exp(-0.00368208 * v)) - 1


games = []
with open(PGN) as f:
    while (g := chess.pgn.read_game(f)) is not None:
        games.append(g)
rows = defaultdict(dict)
for line in open(SCAN):
    r = json.loads(line)
    rows[r["game"]][r["ply"]] = r

spots = []
for gi, g in enumerate(games):
    me_white = g.headers["White"] == ME
    for ply, r in rows[gi].items():
        if "s1" not in r or r["s2"] is None or ply < 14:
            continue
        board = chess.Board(r["fen"])
        opp_to_move = (board.turn == chess.WHITE) != me_white
        if opp_to_move and not board.is_check() and r["s1"] >= -150 and r["s2"] <= -300:
            spots.append((gi, ply, r))
print(f"{len(spots)} positions where your opponent had a single good move", flush=True)

eng = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")
eng.configure({"Threads": 2, "Hash": 256})
found = []
for n, (gi, ply, r) in enumerate(spots, 1):
    board = chess.Board(r["fen"])
    infos = eng.analyse(board, chess.engine.Limit(time=1.0), multipv=3)
    for info in infos[1:]:
        alt = info["pv"][0]
        if cp(info["score"]) > -300 or alt.uci() == r["played"]:
            continue
        after = board.copy()
        after.push(alt)
        if after.is_game_over() or after.is_check():
            continue
        lines = eng.analyse(after, chess.engine.Limit(time=2.0), multipv=2)
        b1 = cp(lines[0]["score"])
        b2 = cp(lines[1]["score"]) if len(lines) > 1 else -MATE
        key = lines[0]["pv"][0]
        if wc(b1) < 0.6 or wc(b1) - wc(b2) < 0.5:
            continue
        # the refutation must not simply take back what the alternative captured
        if after.is_capture(key) and key.to_square == alt.to_square:
            continue
        found.append({"game": gi, "ply": ply + 1, "parent_fen": r["fen"], "fen": after.fen(), "kind": "win",
                      "alt": alt.uci(), "alt_san": board.san(alt), "real": r["played"],
                      "real_san": board.san(chess.Move.from_uci(r["played"])), "last": alt.uci(),
                      "s1": b1, "s2": b2, "me_to_move": True, "whatif": True})
    if n % 10 == 0:
        print(f"{n}/{len(spots)} checked, {len(found)} 'what if' puzzles so far", flush=True)
eng.quit()
json.dump(found, open(OUT, "w"), indent=1)
print(f"done: {len(found)} 'what if' candidates", flush=True)
