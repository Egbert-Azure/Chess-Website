"""Write the Puzzle of the Month posts and their board images.

Reads months.json (one entry per month: date, slug, title, story, which puzzle,
links) and shortlist.json (the checked puzzles with their games), and writes
  _puzzles/<year>/<date>-<slug>.md      the puzzle, dated the 1st of its month,
      at /puzzles/<slug>/ (on the Puzzles page, not in the blog)
  assets/puzzles/<year>-<month>-board.svg and -answer.svg   the two boards

A puzzle dated in the future stays out of the site until the first build after
its date (_plugins/future_puzzles.rb); netlify/functions/monthly-puzzle.mjs
starts that build on the 1st of each month.

Story markup in months.json:
  [[...]]  a gap for Egbert to fill; written into the post as a Liquid comment,
           so it never shows on the site, and the post reads fine without it
  {{...}}  Egbert's own words from his annotated games; written as plain text
  *...*    italics (Markdown)

Run from the repository root:  python3 _tools/puzzles/make_posts.py
Needs python-chess (pip install chess). Existing posts are overwritten, so
edit stories in the posts themselves only after the last run, or in months.json.
"""
import json, re
from pathlib import Path

import chess, chess.svg

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
ME = "Schroeer, Egbert"
COLORS = {"square light": "#f0d9b5", "square dark": "#b58863", "margin": "#3a2a1c", "coord": "#f0d9b5",
          "square light lastmove": "#e6cf8a", "square dark lastmove": "#c9a45f"}


def board_svg(fen, last=None, arrow=None):
    board = chess.Board(fen)
    arrows = [chess.svg.Arrow(arrow.from_square, arrow.to_square, color="#2f6f3ecc")] if arrow else []
    return chess.svg.board(board, orientation=board.turn, lastmove=last, arrows=arrows, size=360,
                           coordinates=True, colors=COLORS)


def score(v):
    if abs(v) >= 95_000:
        n = (100_000 - abs(v)) // 100
        return f"mate in {n}" if v > 0 else f"mated in {n}"
    return f"{v / 100:+.1f}"


def task(p):
    if p["kind"] == "mate":
        return f"{p['to_move']} to move and mate in {(100_000 - p['deep1']) // 100}"
    if p["kind"] == "save":
        return f"{p['to_move']} to move: find the only move that holds"
    return f"{p['to_move']} to move and win"


def numbered(p):
    dots = "." if p["to_move"] == "White" else "..."
    return f"{p['move_no']}{dots} {p['solution_san']}"


def game_line(p, plies=6):
    """What was played from the puzzle position on: the game, not an engine line."""
    import io
    import chess.pgn
    game = chess.pgn.read_game(io.StringIO(p["pgn"]))
    moves = list(game.mainline_moves())
    board = game.board()
    for move in moves[:p["ply"]]:
        board.push(move)
    text = board.variation_san(moves[p["ply"]:p["ply"] + plies])
    if p["ply"] + plies >= len(moves):
        return text + " " + p["result"].replace("1/2-1/2", "½–½")
    return text + " …"


def check(p):
    me_white = p["white"] == ME
    if p["me_to_move"]:
        found = "I found it in the game." if p["found"] else f"I missed it and played {p['played_san']}."
    else:
        found = "My opponent found it." if p["found"] else f"My opponent missed it and played {p['played_san']}."
    if p["result"] == "1/2-1/2":
        result = "The game was drawn."
    else:
        result = "I won the game." if (p["result"] == "1-0") == me_white else "I lost the game."
    return f"With this move: {score(p['deep1'])}. Next best move: {score(p['deep2'])}. {found} {result}"


def story(paragraphs):
    out = []
    for text in paragraphs:
        text = re.sub(r"\[\[(.+?)\]\]", r"{% comment %}\1{% endcomment %}", text)
        text = re.sub(r"\{\{(.+?)\}\}", r"\1", text)
        out.append(text.strip())
    return "\n\n".join(out)


def q(value):
    return json.dumps(value, ensure_ascii=False)  # a JSON string is a valid YAML double-quoted string


def main():
    months = json.loads((HERE / "months.json").read_text(encoding="utf-8"))
    shortlist = {p["no"]: p for p in json.loads((HERE / "shortlist.json").read_text(encoding="utf-8"))}
    (ROOT / "assets/puzzles").mkdir(parents=True, exist_ok=True)
    for m in months:
        p = shortlist[m["puzzle"]]
        year, month, _ = m["date"].split("-")
        stem = f"{year}-{month}"
        last = chess.Move.from_uci(p["last"]) if p.get("last") else None
        solution = chess.Move.from_uci(p["solution"])
        (ROOT / f"assets/puzzles/{stem}-board.svg").write_text(board_svg(p["fen"], last), encoding="utf-8")
        (ROOT / f"assets/puzzles/{stem}-answer.svg").write_text(board_svg(p["fen"], last, solution), encoding="utf-8")

        links = list(m.get("links", []))
        pgn = "\n".join("    " + line if line else "" for line in p["pgn"].splitlines())
        front = [
            "---",
            "layout: puzzle",
            f"title: {q(m['title'])}",
            f"description: {q('Puzzle of the Month, ' + m['month'] + ': ' + task(p) + '.')}",
            f"date: {m['date']}",
            f"permalink: /puzzles/{m['slug']}/",
            "puzzle:",
            f"  task: {q(task(p))}",
            f"  board: {q(f'/assets/puzzles/{stem}-board.svg')}",
            f"  answer: {q(f'/assets/puzzles/{stem}-answer.svg')}",
            f"  move: {q(numbered(p))}",
            f"  game: {q(game_line(p))}",
            f"  check: {q(check(p))}",
            f"  ply: {p['ply']}",
            f"  orientation: {q(p['to_move'].lower())}",
        ]
        if links:
            front.append("  links:")
            for text, url in links:
                front += [f"    - text: {q(text)}", f"      url: {q(url)}"]
        front += ["  pgn: |", pgn, "---", ""]
        body = story(m["story"])
        sources = "\n".join(f"  {text}: {url}" for text, url in m.get("sources", []))
        note = ("{% comment %}\nSources for this story (not shown on the site):\n" + sources + "\n{% endcomment %}\n") if sources else ""
        path = ROOT / f"_puzzles/{year}/{m['date']}-{m['slug']}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(front) + body + "\n\n" + note, encoding="utf-8")
        print("wrote", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
