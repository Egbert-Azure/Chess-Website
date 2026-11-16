"""Pass 2: pick puzzle moments from the quick scan and verify each one with a
deep three-line search. A position counts as a puzzle only if exactly one move
wins (or exactly one move saves the game).
Usage: python3 -I verify.py <games.pgn> <scan.jsonl> <out.json> [seconds]"""
import io, json, math, sys
from collections import defaultdict
import chess, chess.engine, chess.pgn

ME = "Schroeer, Egbert"
MATE = 100_000
PGN, SCAN, OUT = sys.argv[1:4]
SECS = float(sys.argv[4]) if len(sys.argv) > 4 else 4.0
EXTRA = sys.argv[5] if len(sys.argv) > 5 else None
VALUE = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0}


def wc(cp):
    """Winning chance from -1 to 1 (the curve Lichess uses)."""
    cp = max(-2000, min(2000, cp if abs(cp) < MATE - 5000 else math.copysign(2000, cp)))
    return 2 / (1 + math.exp(-0.00368208 * cp)) - 1


def cp(score):
    s = score.relative
    if s.is_mate():
        m = s.mate()
        return MATE - abs(m) * 100 if m > 0 else -MATE + abs(m) * 100
    return s.score()


def is_mate(v):
    return abs(v) >= MATE - 5000


# --- load games and scan -------------------------------------------------------
games = []
with open(PGN) as f:
    while (g := chess.pgn.read_game(f)) is not None:
        games.append(g)
rows = defaultdict(dict)
for line in open(SCAN):
    r = json.loads(line)
    rows[r["game"]][r["ply"]] = r


def trivial(board, move, last_move):
    """Recaptures and similar 'obvious' moves make poor puzzles."""
    if last_move and board.is_capture(move) and move.to_square == last_move.to_square:
        return True
    return False


def sacrifice(board, move):
    """True if the moved piece can be taken afterwards for less than it's worth."""
    piece = board.piece_at(move.from_square)
    captured = board.piece_at(move.to_square)
    after = board.copy()
    after.push(move)
    if after.is_checkmate():
        return False
    attackers = after.attackers(after.turn, move.to_square)
    if not attackers:
        return False
    cheapest = min(VALUE[after.piece_at(sq).piece_type] or 99 for sq in attackers)
    gain = VALUE[captured.piece_type] if captured else 0
    defended = bool(after.attackers(not after.turn, move.to_square))
    lost = VALUE[piece.piece_type]
    return (not defended and lost > gain) or (defended and cheapest < lost and lost - gain >= 2)


def hanging(board, square):
    """The piece on this square is attacked and either undefended or attackable by something cheaper."""
    piece = board.piece_at(square)
    attackers = board.attackers(not board.turn, square)
    if not piece or not attackers or piece.piece_type == chess.KING:
        return False
    cheapest = min(VALUE[board.piece_at(sq).piece_type] or 99 for sq in attackers)
    return not board.attackers(board.turn, square) or cheapest < VALUE[piece.piece_type]


def simple_grab(board, move):
    """Taking a piece that was simply left hanging."""
    if not board.is_capture(move) or board.is_en_passant(move):
        return False
    target = board.piece_at(move.to_square)
    mover = board.piece_at(move.from_square)
    return not board.attackers(not board.turn, move.to_square) or VALUE[target.piece_type] > VALUE[mover.piece_type]


# --- pass-1 candidates --------------------------------------------------------
cands = []
for gi, g in enumerate(games):
    plies = rows.get(gi, {})
    me_white = g.headers["White"] == ME
    moves = list(g.mainline_moves())
    for ply, r in sorted(plies.items()):
        if "s1" not in r or r["s2"] is None or ply < 14:
            continue
        board = chess.Board(r["fen"])
        if board.is_check():
            continue
        s1, s2 = r["s1"], r["s2"]
        prev = -plies[ply - 1]["s1"] if ply - 1 in plies and "s1" in plies[ply - 1] else 0
        kind = None
        if is_mate(s1) and s1 > 0 and not (is_mate(s2) and s2 > 0) and s1 >= MATE - 800:
            kind = "mate"
        elif s1 >= 250 and s2 <= 100 and prev < 200 and not (abs(s1) < MATE - 5000 and s1 > 1500 and prev > 600):
            kind = "win"
        elif -80 <= s1 <= 120 and s2 <= -250 and r["legal"] >= 4:
            kind = "save"
        if not kind:
            continue
        best = chess.Move.from_uci(r["best"])
        last = moves[ply - 1] if ply > 0 else None
        if trivial(board, best, last):
            continue
        if kind == "save":
            # Defending by trading or by moving a threatened piece out of the way is too obvious;
            # keep quiet defensive moves and defensive sacrifices.
            if board.is_capture(best) and not sacrifice(board, best):
                continue
            if hanging(board, best.from_square):
                continue
        cands.append({"game": gi, "ply": ply, "fen": r["fen"], "kind": kind, "played": r["played"], "s1": s1, "s2": s2,
                      "last": last.uci() if last else None,
                      "me_to_move": (board.turn == chess.WHITE) == me_white})
print(f"{len(cands)} candidates from the quick scan", flush=True)
if EXTRA:
    extra = json.load(open(EXTRA))
    cands += extra
    print(f"+ {len(extra)} 'what if' candidates", flush=True)
if SECS == 0:  # dry run: only show what the quick scan found
    from collections import Counter
    print(Counter((c["kind"], c["me_to_move"]) for c in cands))
    print(len({c["game"] for c in cands}), "games with candidates")
    sys.exit()

# --- deep verification ----------------------------------------------------------
eng = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")
eng.configure({"Threads": 2, "Hash": 512})
out = []
for n, c in enumerate(cands, 1):
    board = chess.Board(c["fen"])
    infos = eng.analyse(board, chess.engine.Limit(time=SECS), multipv=3)
    lines = [(cp(i["score"]), i["pv"]) for i in infos]
    b1, pv = lines[0]
    b2 = lines[1][0] if len(lines) > 1 else -MATE
    ok = False
    if c["kind"] == "mate":
        ok = is_mate(b1) and b1 > 0 and not (is_mate(b2) and b2 > 0)
    elif c["kind"] == "win":
        if c.get("relaxed"):  # human games: a clear win (about +2.5) far ahead of the rest
            ok = wc(b1) >= 0.42 and wc(b1) - wc(b2) >= 0.4
        else:
            ok = wc(b1) >= 0.6 and wc(b1) - wc(b2) >= 0.5
    elif c.get("relaxed"):  # lost games: one move holds, the others lose clearly (about -2.5)
        ok = wc(b1) >= -0.25 and wc(b2) <= -0.42 and wc(b1) - wc(b2) >= 0.35
    else:
        ok = wc(b1) >= -0.25 and wc(b2) <= -0.55 and wc(b1) - wc(b2) >= 0.4
    if ok:
        key = pv[0]
        g = games[c["game"]]
        c.update({
            "deep1": b1, "deep2": b2, "depth": infos[0]["depth"],
            "solution": key.uci(), "solution_san": board.san(key),
            "line_san": board.variation_san(pv[:7]),
            "found": (not c.get("whatif")) and c["played"] == key.uci(),
            "played_san": None if c.get("whatif") else board.san(chess.Move.from_uci(c["played"])),
            "sacrifice": sacrifice(board, key),
            "simple": simple_grab(board, key),
            "quiet": not board.is_capture(key) and not board.gives_check(key),
            "check": board.gives_check(key),
            "white": g.headers["White"], "black": g.headers["Black"], "result": g.headers["Result"],
            "event": g.headers.get("SiteEvent", ""), "date": g.headers.get("Date", ""), "source": g.headers.get("Source", ""),
            "move_no": board.fullmove_number, "to_move": "White" if board.turn else "Black",
            "pieces": len(board.piece_map()),
        })
        out.append(c)
    if n % 10 == 0:
        print(f"{n}/{len(cands)} verified, {len(out)} hold up", flush=True)
eng.quit()
json.dump(out, open(OUT, "w"), indent=1)
print(f"done: {len(out)} of {len(cands)} candidates are sound puzzles", flush=True)
