---
layout: post
title: "Enhancing Your Chess Journey with Chessify: A Comprehensive Review"
date: 2024-03-21
tags: [tools, technology, ChessBase, Chessify]
description:  "we delve into the latest innovations in chess technology and explore the enhancements Chessify brings to the table."
image:  '/images/shri-CG-JvqWqutM-unsplash.jpg'
featured: false
---

<div style="text-align: left; font-size: smaller;">
Photo by <a href="https://unsplash.com/@thefatdash?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">shri</a> on <a href="https://unsplash.com/photos/chess-pieces-on-chess-board-CG-JvqWqutM?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
</div>  

# Website Update

I made a significant change to my blog page which includes some new features including topic tags, featured blog posts with a beautiful and modern design which is also great on mobile devices. Additonally search is enabled now and makes it easier to find topics of interest. 

If there is still any hiccup, bear with me, or even better: drop me a note.

If you like it: drop me a note or comment

If you don't like it: yeah, you know what to do

## Introduction

Seeking constant improvement is intrinsic to the pursuit of chess mastery. In my previous blog post, "What's Next," I evaluated Chessify and other tools as potential aids in this journey, aiming to augment or replace certain functions of ChessBase with more efficient alternatives.

Now, breaking news surfaces: Chessify has seamlessly integrated the ICCF database, boasting over 2 million high-quality correspondence chess games. Even more enticing, for a limited time, they offer FREE access to all users! While this development promises affordability, especially when compared to maintaining a Stockfish cluster on platforms like Azure or personal hardware solutions, there's a caveat: existing subscribers must cancel their current subscription to take advantage of this offer, rather than seamlessly transitioning or receiving a discounted rate.



<div style="border: 1px solid white; padding: 10px">
     <blockquote style="font-size: 20px; font-style: italic; font-weight: 400;">
Hello Egbert,

Thank you for your kind words and congratulations!

Regarding your subscription and the ICCF discount, you can renew your subscription in November and take advantage of the ICCF special offer at that time. However, if you'd like to use the discount now, you'll need to upgrade your subscription from Amateur to Master.

We appreciate your support and for mentioning us on your blog page. 

Sincerely,
Chessify support team
   </blockquote>
</div>

As a user you can chose now between several databases: Megadatabase, which claims to be the competitor to ChessBase, ICCF, the newly added database and last the Lichess game database. Typical filter functions are available and for MegaDatabase you can exclude rapid and blitz as an example.

<div style="text-align:center;">
  <img src="{{site.baseurl}}/images/Chessify 2024-03-20 160443.png" alt="Chessify" style="width:80%;">
</div>

I proceeded to put Chessify through its paces, initiating several maneuvers and analyses. Firstly, I filtered games with my name:

<div style="text-align:center;">
  <img src="{{site.baseurl}}/images/Chessify 2024-03-20 163214.png" alt="Chessify" style="width:80%;">
</div>

Subsequently, I requested a thorough analysis with a depth of 30:

<div style="text-align:center;">
  <img src="{{site.baseurl}}/images/Chessify 2024-03-20 164423.png" alt="Chessify" style="width:80%;">
</div>

Initial impressions suggested parity with industry staples like ChessBase or Lichess, yet reality proved otherwise. Utilizing a recent challenging game from the 2024 Champions League, I instructed Chessify to analyze via the ChessBase plugin, employing *Fine* and *9s* parameters. The game, characterized by a tense climax resulting in a draw, exposed a significant discrepancy:

#### ChessBase Tactical Analysis

```pgn
[Event "CL/2024/C2"]
[Site "ICCF"]
[Date "2024.02.25"]
[Round "?"]
[White "Schroeer, Egbert"]
[Black "Maioriello, Graziano"]
[Result "1/2-1/2"]
[ECO "A13"]
[WhiteElo "2137"]
[BlackElo "2272"]
[PlyCount "111"]
[EventDate "2024.??.??"]
[WhiteTeam "FSB Thuringia I"]
[BlackTeam "I Gladiatori"]

1. Nf3 d5 2. e3 e6 {[%cal Be7e6,Be6d5,Bd5d4]} 3. c4 Nf6 4. b3 c5 5. Bb2 Nc6 6.
cxd5 exd5 7. Nc3 d4 {The position is equal.} 8. Na4 Be7 9. Bb5 Bd7 $1 {[%cal
Bc8d7,Bd7c6,Bc6e4,Be4g2]} 10. O-O O-O {[%cal Yc6e5]} 11. Re1 Re8 12. Bxc6 Bxc6
13. exd4 cxd4 14. Nxd4 Be4 $1 15. Rc1 {[%cal Yd4e6]} Bb4 16. Nc5 Bxg2 {A strong
pair of Bishops.} 17. Rxe8+ Nxe8 18. Qg4 {Prevents Qg5.} Rc8 19. Nd3 Rxc1+ 20.
Bxc1 h5 21. Qxg2 {[%cal Yc1b2]} Qxd4 22. Qxb7 Bf8 23. Qf3 {[%cal Yc1b2]} Qa1 $1
24. a4 Qb1 25. Qd5 a5 26. Qc4 Nd6 27. Qd5 {[%csl Ra5,Rh5][%cal Yg1g2]} g6 28.
Kg2 {[%cal Yc1a3]} Nf5 29. Qc4 {Inhibits Nh4+.} Nd6 30. Qd5 {[%cal Yc1a3]
Strongly threatening Ba3!} Nf5 31. Ne5 Nh4+ 32. Kg3 (32. Kh3 $5 Qf5+ $7 33. Kxh4
Qxf2+ 34. Kh3 Qf1+ 35. Kg3 $10) 32... Qf5 {[%cal Yf8h6]} 33. d4 {[%cal Yc1d2]}
g5 34. Bd2 {[%cal Yf2f3]} (34. Qxa5 $2 Qe4 35. f3 Qxd4 36. Bxg5 Qg1+ 37. Kf4
Qc1+ (37... Qxh2+ $2 38. Ke4 $19) 38. Ke4 Qxg5 $19) 34... Kg7 $1 35. f3 (35.
Qxa5 $2 Bd6 (35... Nf3 36. Kg2 $10) 36. f4 Qe4 $19) 35... Bb4 36. Bxb4 axb4 $10
{Endgame. KQN-KQN} ({Don't blunder} 36... Qf4+ $2 37. Kf2 $18) 37. Qe4 {Black
must now prevent Nc6. Active counter play!} (37. a5 $5 Qf4+ $7 {Deflection} 38.
Kf2 Qxh2+ 39. Kf1 Qh1+ (39... Qg2+ 40. Ke1 $10) 40. Ke2 Qg2+ 41. Ke1 Qg1+ 42.
Ke2 Qg2+ 43. Ke1 Qg1+ 44. Ke2 Qg2+ $10) 37... Qc8 38. Nc4 Ng6 $1 {Repels Qe5+}
39. Qd5 {[%cal Yd5f7]} h4+ $1 40. Kf2 {[%cal Yd5f7] Qxf7+! is the strong
threat.} Qc7 41. Qd6 Qc8 42. Qd5 {[%cal Yd5f7]} Qc7 43. Qd6 (43. Nd6 $5 Qc2+ $7
44. Ke3 Qc3+ 45. Kf2 Qd2+ 46. Kf1 $10) 43... Qc8 44. d5 Qf5 $1 45. Qxb4 {aiming
for Qd2.} Qh3 46. Qd6 Nf4 47. Qe5+ Kg6 {Hoping for ...Nd3+.} 48. Qe4+ Kg7 49. d6
{Ke1 would now be deadly.} Qxh2+ 50. Ke1 $1 {Threatens to win with d7.} Qh1+ 51.
Kd2 h3 52. Qe5+ ({But not} 52. d7 Qg2+ 53. Kc3 Ne6 $14) 52... Kg6 53. Qe4+ Kg7
54. d7 Qg2+ 55. Kc3 {Dancing on a razor blade.} Ne6 56. Qe5+ {An interesting
draw. An exciting game. Weighted Error Value: White=0.00 (flawless) /Black=0.00
(flawless) . OK: White=30 Black=30 Best: White=4 Black=6 Strong: White=1
Black=6} 1/2-1/2
```

Subsequently, using the standard PGN from the ICCF website, I subjected it to Chessify's full game analysis, configured with a depth of 20, which is the standard preset on the the website.

#### Chessify Full Game Analysis

```pgn
[Event "CL/2024/C2"]
[Site "?"]
[Date "2024.02.25"]
[Round "?"]
[White "Schroeer, Egbert"]
[Black "Maioriello, Graziano"]
[Result "*"]
[ECO "A13"]
[WhiteElo "2137"]
[BlackElo "2272"]
[PlyCount "111"]
[EventDate "2024.??.??"]
[SourceTitle "ICCF"]
[WhiteTeam "FSB Thuringia I"]
[BlackTeam "I Gladiatori"]

1. Nf3 {%eval} d5 {%eval} 2. e3 {%eval} e6 {%eval} 3. c4 {%eval} Nf6 {%eval} 4.
b3 {%eval} c5 {%eval} 5. Bb2 {%eval} Nc6 {%eval} 6. cxd5 {%eval} exd5 {%eval} 7.
Nc3 {%eval} d4 {%eval} 8. Na4 {%eval} Be7 {%eval} 9. Bb5 {%eval} Bd7 {%eval} 10.
O-O {%eval} O-O {%eval} 11. Re1 {%eval} Re8 {%eval} 12. Bxc6 {%eval} Bxc6
{%eval} 13. exd4 {%eval} cxd4 {%eval} 14. Nxd4 {%eval} Be4 {%eval} 15. Rc1
{%eval} Bb4 {%eval} 16. Nc5 {%eval} Bxg2 {%eval} 17. Rxe8+ {%eval} Nxe8 {%eval}
18. Qg4 {%eval} Rc8 {%eval} 19. Nd3 {%eval} Rxc1+ {%eval} 20. Bxc1 {%eval} h5
{%eval} 21. Qxg2 {%eval} Qxd4 {%eval} 22. Qxb7 {%eval} Bf8 {%eval} 23. Qf3
{%eval} Qa1 {%eval} 24. a4 {%eval} Qb1 {%eval} 25. Qd5 {%eval} a5 {%eval} 26.
Qc4 {%eval} Nd6 {%eval} 27. Qd5 {%eval} g6 {%eval} 28. Kg2 {%eval} Nf5 {%eval}
29. Qc4 {%eval} Nd6 {%eval} 30. Qd5 {%eval} Nf5 {%eval} 31. Ne5 {%eval} Nh4+
{%eval} 32. Kg3 {%eval} Qf5 {%eval} 33. d4 {%eval} g5 $6 {Inaccuracy %eval}
(33... Qf6 {was best}) 34. Bd2 $6 {Inaccuracy %eval} (34. Bd2 {was best}) 34...
Kg7 {%eval} 35. f3 {%eval} Bb4 {%eval} 36. Bxb4 {%eval} axb4 {%eval} 37. Qe4
{%eval} Qc8 {%eval} 38. Nc4 {%eval} Ng6 {%eval} 39. Qd5 {%eval} h4+ {%eval} 40.
Kf2 {%eval} Qc7 {%eval} 41. Qd6 {%eval} Qc8 {%eval} 42. Qd5 {%eval} Qc7 {%eval}
43. Qd6 {%eval} Qc8 {%eval} 44. d5 {%eval} Qf5 {%eval} 45. Qxb4 {%eval} Qh3
{%eval} 46. Qd6 {%eval} Nf4 {%eval} 47. Qe5+ {%eval} Kg6 {%eval} 48. Qe4+
{%eval} Kg7 {%eval} 49. d6 {%eval} Qxh2+ {%eval} 50. Ke1 {%eval} Qh1+ {%eval}
51. Kd2 {%eval} h3 {%eval} 52. Qe5+ {%eval} Kg6 {%eval} 53. Qe4+ {%eval} Kg7
{%eval} 54. d7 {%eval} Qg2+ {%eval} 55. Kc3 {%eval} Ne6 {%eval} 56. Qe5+ {%eval}
*
```

The disparity is stark! Chessify flagged move 33. ..g5?! as a Black inaccuracy, favoring White with a 1.01-point advantage, only to later suggest the erroneous move 34. Bd2!? for White, erroneously indicating a minor advantage. That this was the only correct move was overlooked and really weird, Chessify suggested then the alternative 34. Bd2, which is exactly the move I made.

In contrast, Lichess failed to identify any flaws:

<iframe width="600" height="371" src="https://lichess.org/study/embed/PmMDa3wy/GfOBTEdT" frameborder=0></iframe>

## Chessify Mobile App

Finally, exploring the Chessify Mobile App proved frustrating. Despite its potential, the app operates independently of the Chessify platform, akin to the disjointed structure observed with the ChessBase app. This segmentation introduces an additional revenue stream, diverging from user expectations. Why should loyal subscribers incur extra expenses merely to access the app on mobile devices?


<div style="border: 1px solid white; padding: 10px;">
     <blockquote style="font-size: 20px; font-style: italic; font-weight: 400;">
Actually, our mobile app and website are separate products, so you need different accounts, as well as different subscriptions for them.

If you have any further questions or need assistance, please don't hesitate to reach out.

Sincerely,
Chessify support team
        </blockquote>
</div>

# Conculsion

In the ever-evolving landscape of chess technology, Chessify emerges as a promising contender. Its integration of the ICCF database heralds a new era of accessibility and analysis. However, discrepancies in analysis accuracy and the disjointed nature of its mobile app underscore areas for improvement. As enthusiasts, we eagerly anticipate advancements that align with the seamless, intuitive experience we crave in our pursuit of chess excellence.

**Amici Sumus**


> [Please subscribe](https://follow.it/senior-chess-improver?leanpub) 

