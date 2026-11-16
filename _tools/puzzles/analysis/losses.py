"""Extra candidates from the games Egbert lost: the turning point (his move where
exactly one move held, and he missed it) and the opponent's winning shot right
after it, plus any other position in those games where exactly one move wins,
mates or holds. Looser thresholds than the main scan, because in a lost game
the story is the moment it went wrong. The deep check in verify.py decides.
Usage: python3 -I losses.py <games.pgn> <scan.jsonl> <already_verified.json,...> <out.json>"""
import json, sys
import chess, chess.pgn

ME = "Schroeer, Egbert"
MATE = 100_000
VALUE = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0}

games = []
with open(sys.argv[1]) as f:
    while (g := chess.pgn.read_game(f)) is not None:
        games.append(g)


def lost(g):
    r, white = g.headers["Result"], g.headers["White"] == ME
    return (r == "0-1" and white) or (r == "1-0" and not white)


L = {i for i, g in enumerate(games) if lost(g)}
rows = {}
for line in open(sys.argv[2]):
    r = json.loads(line)
    if r["game"] in L:
        rows[(r["game"], r["ply"])] = r
known = {(c["game"], c["ply"]) for path in sys.argv[3].split(",") for c in json.load(open(path))}


def is_mate(v):
    return v is not None and abs(v) >= MATE - 5000


def simple_grab(board, move):
    if not board.is_capture(move) or board.is_en_passant(move):
        return False
    target, mover = board.piece_at(move.to_square), board.piece_at(move.from_square)
    return not board.attackers(not board.turn, move.to_square) or VALUE[target.piece_type] > VALUE[mover.piece_type]


def hanging(board, square):
    piece = board.piece_at(square)
    attackers = board.attackers(not board.turn, square)
    if not piece or not attackers or piece.piece_type == chess.KING:
        return False
    cheapest = min(VALUE[board.piece_at(sq).piece_type] or 99 for sq in attackers)
    return not board.attackers(board.turn, square) or cheapest < VALUE[piece.piece_type]


out = []
for (gi, ply), r in sorted(rows.items()):
    if "s1" not in r or r["s2"] is None or ply < 14 or (gi, ply) in known:
        continue
    board = chess.Board(r["fen"])
    if board.is_check():
        continue
    s1, s2 = r["s1"], r["s2"]
    prev_row = rows.get((gi, ply - 1), {})
    prev = -prev_row["s1"] if "s1" in prev_row else 0
    nxt = rows.get((gi, ply + 1), {})
    after = -nxt["s1"] if "s1" in nxt else None  # score after the move actually played
    kind = None
    if is_mate(s1) and s1 > 0 and not (is_mate(s2) and s2 > 0) and s1 >= MATE - 800:
        kind = "mate"
    elif s1 >= 200 and s2 <= s1 - 200 and s2 <= 100 and prev < 400:
        kind = "win"
    elif -150 <= s1 <= 150 and s2 <= -200 and s2 <= s1 - 200 and r["legal"] >= 4:
        kind = "save"
    if not kind:
        continue
    best = chess.Move.from_uci(r["best"])
    moves = list(games[gi].mainline_moves())
    last = moves[ply - 1] if ply else None
    if last and board.is_capture(best) and best.to_square == last.to_square:
        continue  # recapture
    if kind != "save" and simple_grab(board, best):
        continue  # a piece simply left hanging
    if kind == "save" and board.is_capture(best):
        continue  # defending by trading is too obvious
    if kind == "save" and hanging(board, best.from_square):
        continue  # moving a threatened piece away is too obvious
    me_white = games[gi].headers["White"] == ME
    me = (board.turn == chess.WHITE) == me_white
    out.append({"game": gi, "ply": ply, "fen": r["fen"], "kind": kind, "relaxed": True, "lost_game": True,
                "played": r["played"], "s1": s1, "s2": s2, "last": last.uci() if last else None,
                "me_to_move": me,
                # his decisive mistake: he had one move that held and played something that lost
                "turning": me and kind == "save" and r["played"] != r["best"] and after is not None and after <= -200})
json.dump(out, open(sys.argv[4], "w"), indent=1)
print(f"{len(out)} candidates from {len(L)} lost games; {sum(c['turning'] for c in out)} turning points; "
      f"{sum(not c['me_to_move'] for c in out)} with the opponent to move")
