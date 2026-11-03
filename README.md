# Senior Chess Improver

Source of [chess.myvortexcloud.com](https://chess.myvortexcloud.com), a Jekyll site deployed by Netlify.

## Preview locally

```bash
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000.

## Writing posts

Posts live in `_posts/` as `YYYY-MM-DD-Title-Of-Post.md`. The file name sets the address: `2026-04-06-Back-on-the-Board.md` becomes `/Back-on-the-Board`. Don't rename published posts, or links to them break.

Front matter:

```yaml
---
layout: post
title: "Back on the Board: A New Chapter"
description: "One or two sentences shown under the title and in the post list."
date: 2026-04-06
image: '/images/about-unsplash.jpg'
tags: [HIARCS, Electronic-Knights, ICCF, tools, tournaments]
---
```

Reuse existing tags where you can (see `/tags/`), spelled the same way, so posts on one topic stay together.

Image file names are case-sensitive on the server: `Night.jpg` and `night.jpg` are different files there, even though your Mac treats them as the same.

## Adding a game or a position

**A full game:** paste the PGN, for example exported from HIARCS Chess Explorer, into a code block marked `pgn`. Comments and variations are shown in the move list.

````markdown
```pgn
[Event "Electronic Knights 25EN03"]
[White "Gladis, Peter"]
[Black "Schroeer, Egbert"]
[Result "0-1"]

1. b4 e5 2. Bb2 ...
```
````

**A single position**, such as a puzzle, takes its FEN:

```html
<div class="board" data-fen="8/8/5Bp1/6P1/5k1K/4r3/8/8 b - - 0 1"></div>
```

Add `data-orientation="black"` to show either kind from Black's side.

The board is the [Lichess PGN Viewer](https://github.com/lichess-org/pgn-viewer), stored in `assets/lpv/` under the GPL v3. Because of that licence, keep this repository public.
