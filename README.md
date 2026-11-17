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

## Puzzle of the Month

A puzzle from my own games goes live on the Puzzles page on the 1st of every month by itself. The puzzles are written ahead in `_puzzles/`, dated the 1st of their month, with `layout: puzzle`; `_plugins/future_puzzles.rb` keeps them out of the site until their date, and a scheduled Netlify function rebuilds the site on the 1st. How it works, how to fill in a story and how to find more puzzles: see `_tools/puzzles/README.md`.

## Newsletter

The site sends its own newsletter: one short email when a new post or a new Puzzle of the Month goes live. No outside newsletter service, no ads.

- **Sign-up:** `/newsletter/` (linked in the footer and at the end of the posts). Readers confirm with one click; every email has a one-click unsubscribe link, and mail apps get their own "Unsubscribe" button (List-Unsubscribe header). Unsubscribing deletes the address.
- **Where the addresses are:** in Netlify Blobs (store `newsletter`) in the Netlify account. Never in this repository.
- **Sending:** `netlify/functions/newsletter-send.mjs` runs every day at 16:00 UTC (8 AM in Redmond). It reads `/newsletter.json` (the newest live posts and puzzles), mails what is new to the confirmed readers through Resend, and remembers what it sent. The first run only remembers what is already on the site.
- **Code:** `netlify/lib/newsletter.mjs` (logic), `netlify/lib/runtime.mjs` (Netlify and Resend), `netlify/functions/newsletter-*.mjs` (subscribe, confirm, unsubscribe, send, admin).

**Netlify environment variables**

| Key | Value |
|---|---|
| `RESEND_API_KEY` | API key from resend.com (sending access is enough) |
| `NEWSLETTER_FROM` | `Senior Chess Improver <newsletter@news.myvortexcloud.com>` |
| `NEWSLETTER_ADMIN_KEY` | a long random string for the admin commands (`openssl rand -hex 24`) |
| `NEWSLETTER_REPLY_TO` | optional: an address readers' replies go to |

The sending domain `news.myvortexcloud.com` is verified in Resend with the DNS records Resend shows (added at Squarespace).

**Admin commands** (Terminal; replace KEY with the admin key):

```
# how many readers
curl -X POST -H "Authorization: Bearer KEY" "https://chess.myvortexcloud.com/api/newsletter-admin?action=count"
# all addresses
curl -X POST -H "Authorization: Bearer KEY" "https://chess.myvortexcloud.com/api/newsletter-admin?action=list"
# import a follow.it export, leaving out one address
curl -X POST -H "Authorization: Bearer KEY" --data-binary @Followers.csv "https://chess.myvortexcloud.com/api/newsletter-admin?action=import&exclude=someone@example.com"
# remove a reader
curl -X POST -H "Authorization: Bearer KEY" "https://chess.myvortexcloud.com/api/newsletter-admin?action=remove&email=someone@example.com"
# send the newest post or puzzle to one address, as a test
curl -X POST -H "Authorization: Bearer KEY" "https://chess.myvortexcloud.com/api/newsletter-admin?action=test&to=you@example.com"
# once: tell the imported follow.it readers about the move
curl -X POST -H "Authorization: Bearer KEY" "https://chess.myvortexcloud.com/api/newsletter-admin?action=moved-notice"
# announce now instead of waiting for the morning (add &dry=1 to only see what would go out)
curl -X POST -H "Authorization: Bearer KEY" "https://chess.myvortexcloud.com/api/newsletter-admin?action=send-now"
```
