"""Pass 1: quick two-line engine scan of every position in every game.
Writes one JSON line per position: best and second-best score (side to move's
view), best move, the move actually played.
Usage: python3 -I scan.py <games.pgn> <out.jsonl> [nodes]"""
import json, sys
from multiprocessing import Pool
import chess, chess.engine, chess.pgn

PGN, OUT = sys.argv[1], sys.argv[2]
NODES = int(sys.argv[3]) if len(sys.argv) > 3 else 150_000
MATE = 100_000


def cp(score):
    """Score from the side to move's view as a number; mates as huge values."""
    s = score.relative
    if s.is_mate():
        m = s.mate()
        return MATE - abs(m) * 100 if m > 0 else -MATE + abs(m) * 100
    return s.score()


def work(args):
    idx, text = args
    import io
    game = chess.pgn.read_game(io.StringIO(text))
    eng = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")
    eng.configure({"Threads": 1, "Hash": 64})
    rows = []
    board = game.board()
    moves = list(game.mainline_moves())
    for ply, played in enumerate(moves):
        legal = board.legal_moves.count()
        row = {"game": idx, "ply": ply, "fen": board.fen(), "played": played.uci(), "legal": legal}
        if legal >= 2:
            infos = eng.analyse(board, chess.engine.Limit(nodes=NODES), multipv=2)
            row["best"] = infos[0]["pv"][0].uci()
            row["s1"] = cp(infos[0]["score"])
            row["s2"] = cp(infos[1]["score"]) if len(infos) > 1 else None
        rows.append(row)
        board.push(played)
    eng.quit()
    return rows


def games():
    with open(PGN) as f:
        idx = 0
        while (g := chess.pgn.read_game(f)) is not None:
            yield idx, str(g)
            idx += 1


if __name__ == "__main__":
    done = 0
    with open(OUT, "w") as out, Pool(2) as pool:
        for rows in pool.imap_unordered(work, games()):
            for r in rows:
                out.write(json.dumps(r) + "\n")
            out.flush()
            done += 1
            if done % 10 == 0:
                print(f"{done} games scanned", flush=True)
    print("scan finished", flush=True)
