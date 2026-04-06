---
layout: post
title: "Back on the Board: A New Chapter"
description: "Tournament updates, a farewell to ChessBase after decades, and a new chapter with HIARCS Chess Explorer — there is a lot to catch up on."
date: 2026-04-06
image: '/images/about-unsplash.jpg'
tags: [HIARCS, ChessBase, Electronic-Knights, ICCF, tools, tournaments]
featured: false
---

# Back on the Board: A New Chapter

It has been a while. A long while. But chess has a way of pulling you back — and today it pulled me back to the keyboard.

There is quite a bit to catch up on, so let me get right to it.

---

## A Deliberate Slowdown

I made a conscious decision to reduce tournament stress. Going forward, I'm limiting myself to **one Electronic Knights section per year** and have paused new ICCF tournament signups entirely. The RoW Championship 2024 Semi-Final I blogged about in late 2024? It hasn't gone well — the field is packed with IMs and CCMs, all rated significantly above me, and the overall standing reflects that. But honestly, just competing at that level and drawing against opponents like IM Allyne Smith, CCM Unes Hassim, and IM James Ellis is its own reward.

*Amici sumus.*

The more valuable insight from the slowdown: fewer tournaments means more quality in the games I *do* play, more time to analyze, and — apparently — more time to write.

---

## USCF Rankings: Something Worth Sharing

Here's something I didn't expect: despite reducing my tournament load, my **USCF Correspondence Chess ranking has climbed to #41** in the USA. In November 2024 I was ranked #67. If you had told me back in 2021 — when I was playing Electronic Knights via email for the first time — that I'd crack the US Top 50 in correspondence chess, I would have laughed. Loudly.

Proof that quality over quantity actually works.

---

## Electronic Knights: The Full Picture

Let me give you the complete tournament update, because across multiple active fronts, there is quite a story to tell.

### EN 2025 (25EN03) — Preliminary, Running

Currently **tied for 1st place with 5 points** alongside Jerry Weiner. My first game — a win against Peter Gladis, who opened with the Sokolsky (1.b4) — set the tone nicely. I'll share the annotated game in a future post. The Sokolsky has a wonderful history going back to Tartakower at New York 1924 — look up where the name "Orangutan Opening" comes from if you're curious.

### EN 2023 Semi-Final (23ENs02) — Finished

I scored **4.5 points, finishing 3rd in the section** — enough to qualify for the finals. The field included Michael Buss (2216), Timothy Julkowski CCE (2224), and IM Clarence Anderson (2372). Holding my own in that company was satisfying.

### EN 2023 Finals (23ENf01) — Just Started

This is the big news on the USCF side. I've qualified for the **2023 Electronic Knights Championship Finals**, which started on **March 31, 2026**. My weighted qualifying score of 14.4 (4.5 prelim + 4.5 semi) places me as the lowest-ranked qualifier — the other finalists include Michael Buss, Robert Irons, Timothy Julkowski, Eric Moskow, and Patrick Gordon-Davis. Some familiar names. It will be a tough section, no question.

This is my second Electronic Knights Final. The EN 2021 Finals ended with approximately 5th place. Let's see if I can improve on that this time around.

### EN 2024 Semi-Final (24ENs01) — Running

This section has been running since May 2025 and is still in progress. Updates to follow when there is something concrete to report.

---

## The Big News: Farewell ChessBase, Hello HIARCS

Let me be direct: I left ChessBase after decades. And honestly? I should have done it sooner.

This isn't a rage-quit. It's the result of years of accumulated frustration — documented right here on this blog — finally reaching a tipping point. So let me lay it out clearly, because I suspect many of you are in exactly the same position and just haven't admitted it yet.

### The ChessBase Problem

Back in March 2024, I wrote about having **six open support tickets with no response**. Not one. Six. That alone should tell you something about how ChessBase treats its paying users.

When ChessBase 18 launched in November 2024, I debated whether to upgrade. I did — mainly because of a 25% discount offer. Here's what I got for that: a manual activation key entry process (in 2024!), a requirement to close VPN software and GPU drivers just to install, credentials including my ICCF login lost in the process, a premium membership that was supposed to activate automatically but didn't, and a first service patch released within 24 hours of launch. ChessBase, who exactly is doing your QA?

And this isn't even a proper upgrade — it installs *parallel* to ChessBase 17. You have to manually uninstall the old version yourself. That's simply not how modern software works.

But the deeper issues go well beyond installation hiccups. The so-called **ChessBase Cloud** is not a cloud — it's a glorified file share. Move your repertoire there and don't expect local changes to sync. They don't. The MegaDatabase annotations are inconsistent and in mixed languages, even for famous, well-documented games. The Opening Database released every year is largely the same product with minor additions. And correspondence chess? ChessBase keeps a separate correspondence database behind an additional paywall, yet you still can't look up correspondence players in the main player database. That's incoherent product design.

The final straw was the **remote engine story**. Years ago, I identified a real problem: running Stockfish intensively on a laptop drains the battery fast and limits compute power compared to what a proper server cluster can deliver. The solution — a remote engine connected to your chess GUI over a network — was something I explored thoroughly, documented at [github.com/Egbert-Azure/stockfish-cluster](https://github.com/Egbert-Azure/stockfish-cluster), and brought directly to Matthias Wüllenweber. I never heard back. ChessBase eventually moved in that direction — and built a **proprietary paid cluster service** out of it. An idea shared in good faith, turned into someone else's revenue stream. That was the moment I knew we were done.

You can read the full history of my frustrations in the [Tools and Weapons](https://chess.myvortexcloud.com/tools-and-weapons) series from 2024. The receipts are all there.

### Why HIARCS Is the Real Deal

So what did I switch to? **HIARCS Chess Explorer Pro** — and I'll be direct: it is a better product.

First, the credentials. HIARCS isn't some scrappy newcomer. It's a **four-time World Chess Software Champion** with six world titles earned across three decades. The engine has been used by Vishy Anand in his tournament preparation and by Kasparov for his Deep Blue matchup. John Saunders, longtime Chess Magazine editor, put it plainly: *"I prefer using HIARCS Chess Explorer to ChessBase."* That's not a random opinion — that's someone who has used both professionally for years.

Now the practical side. HIARCS Chess Explorer runs natively on any Apple Mac since 2010, including Intel and Apple Silicon M-series, and supports everything from macOS 10.14 Mojave through the latest macOS 26 Tahoe. It just works on a Mac — cleanly, natively, without workarounds or third-party drivers. No parallel installs, no lost credentials, no VPN drama. You install it and you use it. The architecture is, as I mentioned to Mark Uniacke at HIARCS, refreshingly clean.

The feature set is genuinely comprehensive:

- Fast searching for players, openings, events, material, pawn structure and positions
- Full game database support including **reading ChessBase CBH and CBV formats** — so your existing databases are immediately usable
- Extensive game notation with variations, comments, symbols, diagrams and named openings
- Export to PGN, PDF, EPUB e-book and HTML
- Online access to terabyte endgame tablebases — about 250 DVDs worth of data
- Opening book with **over 133 million positions and moves** as of April 2026, with the latest theory
- The HIARCS 15 engine in HCE Pro — **more than 250 Elo stronger** than HIARCS 14 — supporting up to 32 threads and any UCI engine including Stockfish

That last point matters for correspondence players specifically: you're not locked into one engine. Stockfish, Leela, anything UCI-compatible runs cleanly inside HIARCS.

And the price? **HIARCS Chess Explorer starts at $54.95 — a one-time purchase, no annual subscription.** Compare that to ChessBase's model: annual MegaDatabase updates, a separate correspondence database, a premium subscription, and now a paid cloud cluster on top. The math is not close.

What struck me most, though, was something simpler than any feature list. When I emailed HIARCS with a question about connecting my ChessNut Air board, **Mark Uniacke replied promptly and directly.** ChessNut support isn't there yet, but it's on the roadmap for summer/autumn 2026. One email, one clear answer. After years of support tickets disappearing into the void at ChessBase, that responsiveness felt almost remarkable.

I also raised the topic of remote engine support with the HIARCS team — the same concept I once brought to ChessBase, which went nowhere officially but eventually became someone else's paid proprietary service. Whether HIARCS explores this direction remains to be seen, but at least the conversation is open, and with people who actually listen.

The switch is done. The architecture is cleaner, the support is real, the price is fair, and it runs beautifully on my Mac. If you're still on ChessBase out of habit — and I was, for *decades* — it might be time to ask yourself why.

---

## What's Next

There is plenty coming on the blog in the weeks ahead:

- Annotated game from EN 2025 (25EN03) — my win against Gladis with the Sokolsky
- First impressions of the EN 2023 Finals field
- A deeper look at HIARCS Chess Explorer workflows for correspondence chess players
- The remote engine question revisited — is there a clean, open solution in 2026?

The break was good. The return feels better.

**Amici Sumus**

If you enjoy the blog, consider supporting it with a virtual coffee ☕️ or a beer 🍺 — the mug is waiting below. And please [subscribe](https://follow.it/senior-chess-improver?leanpub) if you haven't already.

<script data-name="BMC-Widget" data-cfasync="false" src="https://cdnjs.buymeacoffee.com/1.0.0/widget.prod.min.js" data-id="chesslife" data-description="Support me on Buy me a coffee!" data-message="Thank you for reading! You can buy me a coffee if you like!" data-color="#5F7FFF" data-position="Right" data-x_margin="18" data-y_margin="18"></script>

> [Please subscribe](https://follow.it/senior-chess-improver?leanpub)
