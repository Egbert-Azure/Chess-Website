"""Extra candidates from the Electronic Knights games, which are played without
engines: any position where exactly one move wins, also when the side to move
was already a little better, found or missed, by either player.
Usage: python3 -I ek_cands.py <games.pgn> <scan.jsonl> <out.json>"""
import json, sys
import chess, chess.pgn

ME = "Schroeer, Egbert"
VALUE = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0}
games = []
with open(sys.argv[1]) as f:
    while (g := chess.pgn.read_game(f)) is not None:
        games.append(g)
ek = {i for i, g in enumerate(games) if any(k in g.headers.get("SiteEvent", "") for k in ("Electronic Knights", "Palciauskas"))}  # US Chess: no engines
rows = {}
for line in open(sys.argv[2]):
    r = json.loads(line)
    if r["game"] in ek:
        rows[(r["game"], r["ply"])] = r


def simple_grab(board, move):
    if not board.is_capture(move) or board.is_en_passant(move):
        return False
    target, mover = board.piece_at(move.to_square), board.piece_at(move.from_square)
    return not board.attackers(not board.turn, move.to_square) or VALUE[target.piece_type] > VALUE[mover.piece_type]


out = []
for (gi, ply), r in sorted(rows.items()):
    if "s1" not in r or r["s2"] is None or ply < 14:
        continue
    board = chess.Board(r["fen"])
    if board.is_check():
        continue
    prev_row = rows.get((gi, ply - 1), {})
    prev = -prev_row["s1"] if "s1" in prev_row else 0
    if not (r["s1"] >= 200 and r["s2"] <= 100 and prev < 400):
        continue
    best = chess.Move.from_uci(r["best"])
    moves = list(games[gi].mainline_moves())
    last = moves[ply - 1] if ply else None
    if last and board.is_capture(best) and best.to_square == last.to_square:
        continue  # recapture
    if simple_grab(board, best):
        continue  # a piece simply left hanging
    me_white = games[gi].headers["White"] == ME
    out.append({"game": gi, "ply": ply, "fen": r["fen"], "kind": "win", "relaxed": True, "played": r["played"],
                "s1": r["s1"], "s2": r["s2"], "last": last.uci() if last else None,
                "me_to_move": (board.turn == chess.WHITE) == me_white})
json.dump(out, open(sys.argv[3], "w"), indent=1)
print(f"{len(out)} Electronic Knights candidates ({sum(c['played'] != rows[(c['game'], c['ply'])]['best'] for c in out)} missed in the game)")
