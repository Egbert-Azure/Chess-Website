# Puzzle of the Month

One position from Egbert's own finished correspondence games on the 1st of
every month, with a short story. Each puzzle has exactly one move that works.

## How a puzzle goes live

- Each puzzle is a file in `_puzzles/<year>/`, like the weekly puzzles before
  it, dated the 1st of its month, with `layout: puzzle` and its own address,
  `/puzzles/<month>-<year>/`. It is listed on the Puzzles page, not in the blog.
- `_plugins/future_puzzles.rb` leaves puzzles dated in the future out of the
  site: not built, not on the Puzzles page, in search or in the sitemap.
- `netlify/functions/monthly-puzzle.mjs` rebuilds the site at 10:00 UTC on the
  1st and the 15th of each month, so that month's puzzle appears (and the game
  review in the blog, dated the 15th; Jekyll hides future-dated blog posts by itself). It needs a Netlify build
  hook, saved as the environment variable `PUZZLE_BUILD_HOOK`.
- Deploy Previews build with `--future` (see `netlify.toml`), so puzzles for
  coming months can be checked in a pull request before they go live.

## The post

The story is the post's text. The puzzle under it comes from the `puzzle:`
block in the front matter, drawn by `_includes/puzzle.html`:

| Field | What it is |
|---|---|
| `task` | "White to move and win", shown next to the board |
| `board`, `answer` | the two board images in `assets/puzzles/`; the answer has the move marked |
| `move` | the solution, shown big after "Show solution" |
| `game` | what was played from the position on: the game, not an engine line |
| `check` | the engine check in one line, and whether it was found |
| `ply`, `orientation` | where and how "Replay the full game" opens the game |
| `links` | "or open it": the annotated game on this site, the game on ICCF, the crosstable |
| `pgn` | the whole game (ICCF score, no comments) for the Lichess viewer |

Gaps for Egbert's own memories, and the sources behind each story, sit in the
post as `{% comment %}` blocks: they never show on the site, and the post reads
fine without them. To fill a gap, replace the comment with the text.

## Making posts

`make_posts.py` writes the posts and board images from `months.json` (one entry
per month: date, title, story, which puzzle, links, sources) and
`shortlist.json` (the 26 checked puzzles with their games):

    pip install chess
    python3 _tools/puzzles/make_posts.py

It overwrites the posts it writes. Once a story has been edited in the post
itself, edit that post by hand, or copy the change into `months.json` first.

Story markup in `months.json`: `[[...]]` a gap (becomes a comment), `{{...}}`
Egbert's own words quoted from his annotated games (becomes plain text),
`*...*` italics.

## Finding more puzzles

The scripts in `analysis/` found the shortlist (Stockfish 16, python-chess):

1. `collect.py` gathers the finished games (ICCF downloads from the
   Tournaments tool, plus the 2021 US Chess server games on this site), leaving
   out tournaments that are still running.
2. `scan.py` gives every position a quick two-line engine look.
3. `verify.py` keeps positions where exactly one move wins, mates or holds and
   checks each with a deeper three-line search; `ek_cands.py` (US Chess games,
   played without engines), `traps.py` ("what if" positions) and `losses.py`
   (games Egbert lost) add candidates with their own rules.
4. `select.py` picks one per game; `finalcheck.py` checks the picks again
   (20 seconds, three lines, and that each position arises in the game);
   `fixnames.py` restores accented names.

Rules kept so far: exactly one move works (no duals); only finished games from
finished tournaments; the solution shows the moves of the game; quotes of
Egbert are first-person lines from his own notes, never ChessBase's automatic
comments; every historical fact in a story has a source.
