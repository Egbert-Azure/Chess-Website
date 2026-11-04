---
layout: post
title: "The Road to 2200: USCF Electronic Knights Tournament"
description: "The Electronic Knights is THE USCF tournament for correspondence chess players. Here is the latest update on my standing in Electronic Knights 2021 Final."
image: '/images/randy-fath-G1yhU1Ej-9A-unsplash.jpg'
date: 2024-06-16
tags: [USCF, tournaments, Electronic-Knights]
featured: false
---
<small>Photo by <a href="https://unsplash.com/@randyfath?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Randy Fath</a> on <a href="https://unsplash.com/photos/selective-focus-photography-of-chess-pieces-G1yhU1Ej-9A?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a></small>
  
# Introduction

Before sharing the latest updates on my progress in the Electronic Knights tournament, I want to share a fun story and a cherished memory involving the legendary chess player Rainer Schlenker. This memory is connected to the [Week 23 puzzle](https://chess.myvortexcloud.com/puzzles/2024-Week-23/), which featured one of his games.

Rainer Schlenker, a German International Master (IM), has significantly contributed to the chess world through his exceptional play and dedication to the game. Over the years, he has competed in numerous national and international tournaments, showcasing his strategic prowess. Beyond his playing career, Schlenker has also been an advocate for chess, engaging in both promotion and teaching.

The term "knight on the rim" is a nod to the adage "A knight on the rim is grim," yet history has shown that these edge knights can be game-changers. Notable examples include Bobby Fischer's surprising Nf6-h5 move in his 1972 World Championship match against Boris Spassky and Magnus Carlsen's occasional use of the "edge knight system" with moves like 1.e4 g6 2.d4 Nf6 3.e5 Nh5.

In German, a knight on the rim translates to *Randspringer*, which was also the title of Raomer Schlenker's self-published magazine.

Back in the day, publishing a magazine involved a typewriter and a lot of passion—a true testament to Schlenker's love for the game.

<div style="text-align: center;">
<img src="{{site.baseurl}}/images/randspringer.jpg" alt="Randspringer Magazine" width="40%">
</div>

Today, technology makes sharing our love for chess easier through platforms like this blog. While it still requires effort, the process is much more accessible. Now, let's get into the updates on my latest results in the Electronic Knights tournament.

# Electronic Knights - Finals

## Section 21ENf01

First of all, this shows how correspondence chess goes. The tournament started in 2021, and we are now—three years later—in the finals. That sets things in perspective. I have to say it was a great decision by USCF to move to the ICCF server with this engine-free format. It makes things much easier than with email. The start date was 1/19/2024, and the end date is 7/19/2026.

As of May 2024, I was on the top 100 player list and ranked as [nr. 73 Schroeer](https://www.uschess.org/component/option,com_top_players/Itemid,371?op=list&month=2405&f=usa&l=C:Top%20Correspondence%20Ratings.&h=Correspondence%20Players), Egbert Heinrich (30088451) with ELO 2099.

All details about ratings with calculation examples [are here](https://new.uschess.org/correspondence-chess/ratings) for those who want to learn more.

And now I finished the first two games. Enjoy!

## Game Analysis: Nohr, Matthew

I don't remember exactly, but this might be my fourth game against Mathew, whom I met first to discuss how to implement a chess engine compute cluster with ChessBase, but that's a different story.
Have a look at the annotated game. You will find my thoughts during the game, also added in annotations.

```pgn
[Event "USCF/2021 Electronic Knights Final/21ENf"]
[Site "ICCF"]
[Date "????.??.??"]
[Round "?"]
[White "Schroeer, Egbert"]
[Black "Nohr, Matthew"]
[Result "1-0"]
[ECO "A13"]
[WhiteElo "2137"]
[BlackElo "1800"]
[Annotator "Schroeer,Egbert"]
[PlyCount "107"]
[GameId "489181478346"]
[EventDate "2024.01.19"]
[EventType "corr"]

1. Nf3 Nf6 2. c4 {When Black starts to mimic White, opening my repertoire, the
answer is c4 to avoid drawish positions.} g6 {g6 is an option, I expected e6}
(2... e6 3. b3 d5 4. Bb2) 3. Nc3 Bg7 4. e4 {[%cal Gd2d4,Gf1e2,Ge1g1] In my game
versus David-Bordier outplayed me with e4. I played e4 against Detlef Zoll in
the Veterans World Cup Semi-Final with an advantage.} (4. e3 c5 5. Qb3 d6 6. d4
Qb6 7. Be2 Qxb3 8. axb3 Nc6 9. h3 Bf5 10. O-O h5 11. d5) (4. g3 O-O 5. Bg2) 4...
d6 5. d4 {[%cal Bd2d4,Bd4d5]} O-O 6. Be2 e5 7. O-O Nc6 {[%cal
Bb8c6,Bc6e7,Be7f5,Bf5h6,Bh6f7]} 8. d5 Ne7 9. b4 {pretty much common theory} Nh5
(9... a5 10. Ba3 axb4 11. Bxb4 b6 12. a4 Ne8 13. Qb3) 10. Re1 f5 11. a4 {E97:
King's Indian: Classical Main Line (6...e5 7 0-0 Nc6): 8 Be3 and 8 d5 Ne7, not 9
Ne1} a5 12. bxa5 Rxa5 13. exf5 {White is slightly better. let's see how this
goes} (13. Bd2) 13... Nxf5 (13... gxf5 14. Ra3 {[%cal Yf3e5]} Nf6) (13... Bxf5
14. Ra3 $10) 14. Bg5 Nf6 15. Bd3 (15. Nh4 $6 $10) 15... Nh6 $6 (15... h6 16. Bd2
(16. Bxf6 Bxf6 17. Be4 h5) 16... Ra8 17. a5 (17. c5 $5 e4 18. Nxe4 Nxe4 19.
Bxe4) 17... g5 18. h3) 16. Ne4 Nf7 17. Bd2 Ra8 (17... Ra6 18. Nfg5 Nxg5 19. Nxg5
{[%cal Yc4c5]} e4 20. Bxe4 Ng4 21. Nf3 $1 $16 {Repels Bd4}) 18. a5 {White has
more active pieces.} Bg4 $5 (18... Bf5 19. Qc2) 19. h3 {[%cal
Rf6e4,Rg4f3,Gd3e4,Gd1f3]} Nxe4 (19... Bxf3 20. Qxf3 Nxe4 21. Qxe4 Bh6 {Inhibits
h4.} 22. Bxh6 Nxh6 23. c5 Qf6 24. Ra2) 20. Bxe4 Bxf3 21. Qxf3 $16 {½-½ Pierzak,R
(2515)-Serazeev,A (2520) Israeli CC 2021 (ISR) corr ICCF ICCF to 2022} Bh6
(21... Qh4 $5 22. Re2 Bh6 23. Be1 {½-½ Lara Ruiz,J (2301)-Tanti,J (2319)
CAPEA50-Op-Sf 5 (ESP) corr ICCF 2022 ICCF to 2022}) 22. Bxh6 Nxh6 {strong white
Bishop} 23. Qe3 (23. Qb3 $5) (23. Qg3 $5) 23... Nf5 {There are 5 games actually
in UltraCorr 2024 with the same position and taking on f5. I think Nf7 would
have been better.} (23... Nf7 24. Reb1 b6 25. a6 (25. axb6 Rxa1 26. Rxa1 cxb6
27. Bd3 Qc7) 25... Ra7 26. Qe2 Kg7 27. Bd3 Qh4 28. Ra3 Qd4 29. Qc2 Nh6) 24. Bxf5
Rxf5 25. Reb1 (25. g4 $6 Rf4) (25. Qg3 $5) (25. c5 dxc5 26. Qxc5 e4 27. Rxe4
Qxd5 28. Qc2) 25... Rb8 {[%cal Gc4c5,Rd6c5,Ge3c5,Re5e4,Gc5e3,Rd8d5,Ga5a6]}
(25... b6 26. axb6 (26. a6 Ra7) 26... Rxa1 27. Rxa1 cxb6 28. Rb1 Rf4 29. Qxb6
Qxb6 30. Rxb6 Rxc4 31. Rxd6 Rd4) 26. c5 dxc5 27. Qxc5 e4 {[%cal
Rf5d5,Yc5b4,Gc5e3] I thought about the next move for a pretty long time and I
see ?e3 or b4 or c3 as options. I think ?d4 with ?xd5 is leading to an equal
position.} 28. Qe3 $36 {White has the initiative.} (28. Qd4 $6 {[%cal Yb1d1]}
Qxd5 $10) (28. Qb4 $5 Qxd5 29. a6) 28... Rxd5 (28... Qxd5 29. a6 $16 {No
sacrifices found (Beauty=2.4)}) (28... Qxd5 29. a6 $16) 29. Qxe4 Qd7 {I guess c6
was the better move. Now pinning the ? and forcing the ? to f6} (29... c6 30.
Qc4 {Threatens to win with Rb6.} Kh8 31. Qc3+ Kg8 32. Qb4 {Black must now
prevent a6.} Rb5 33. Qf4) 30. Qc4 b5 $6 {what if I move a6?} (30... Qf7 {[%cal
Yd5d1]} 31. Qh4 {Hoping for a6.} c6 $2 ({Better is} 31... Rf8 $14) 32. a6 $18
{a7 would now be deadly.} Qc7 33. a7 Ra8 34. Re1) 31. a6 {White now steadily
converts the win.} Ra8 (31... bxc4 $4 {31...Ra8 1.01} 32. Rxb8+ Kf7 {Strongly
threatening ...Rd1+.} 33. a7 {and ? is unstoppable} Qc6 (33... Rd1+ 34. Rxd1
Qxd1+ 35. Kh2 Qd6+ 36. g3 Qd5 37. a8=Q Qxa8 38. Rxa8) 34. a8=Q Qxa8 35. Rbxa8)
(31... bxc4 $2 32. Rxb8+ Kf7 33. a7 $18) 32. Qa2 {still attack ?a5 and pinning
?d5} (32. Qe4 c6 33. Re1) 32... Qf7 {[%csl Rd5][%cal Ga2b3,Rd5d2,Rf7b3,Gb1b5] If
he goes for ? exchange I will win a ?} (32... c6 33. Rb2 Qf7 34. Qa5 Rd7) 33.
Qb3 {invite to go ?d2} (33. a7 c6 $16) 33... Rf5 (33... c6 34. Qe3 Qc7 35. Rc1
Re5 36. Qb3+ Qf7 37. Qxf7+ (37. Qa3 Re2 38. Qc5) 37... Kxf7 38. Rxc6 {aiming for
Kf1.} b4 39. Rc7+ Re7 40. Rc4) (33... Rd2 $2 {33...Rf5 1.55} 34. Qxf7+ Kxf7 35.
Rxb5) 34. Qb2 {Inhibits Qxb3.} (34. Qxf7+ $2 {34.Qb2 2.30} Kxf7 $13) (34. Qb4
Rxf2 $2 (34... Qd5 35. Rc1 c6 36. Re1 Qc5 {Repels Re7} 37. Qd2 (37. Qb2 {Re2 is
the strong threat.} b4)) (34... Qd5 $14) 35. Qxb5 $18) (34. a7 Qxb3 35. Rxb3 c6
$10) 34... c6 {[%cal Gb1d1,Gb2a2,Ga2a5,Ga5b6]} (34... Qf6 35. Qa2+ Qf7 36. Qa5
Qd7 37. Rd1 $1 Qc6 {[%cal Yf5f2]} 38. Qa2+ Rf7 39. Rd4 $1) 35. Rd1 Qa7 {[%cal
Gd1d2,Gg1h2]} (35... Qf6 36. Qa2+ Qf7 37. Qa5 Qe7 {[%cal Yf5f2] Repels Rd8+} 38.
Qb6 {[%cal Yb6b7] And now Qb7! would win.} Qc5 $2 (38... Rc8 {is a better
chance.} 39. Rdc1 Rf6) 39. Rd8+ $18 Rxd8 40. Qxd8+ Rf8 41. Qc7 (41. Qd7 $2
{41.Qc7 4.74} Rxf2) 41... Qxf2+ 42. Kh2 Ra8 43. a7 Qf7 44. Qb8+ Qf8 45. Qb7) 36.
Rd2 Raf8 {[%cal Ga1d1,Rf5f7,Gb2b3] double ? and put pressure with mate? or ?b3+?
I think the ? is better on b3} 37. Qb3+ R5f7 38. Kh1 $1 Qc5 (38... Qe7 39. Rad1
Kg7 40. Rd6 Qa7 $2 (40... Kh6 41. f3 Qh4) 41. Qc3+ $18 Kg8 42. Qxc6) 39. Rd7
{White is clearly winning.} Qc4 (39... Qxf2 {39...Qf5 5.09} 40. Rxf7 Qxf7 41.
Qxf7+ Rxf7 42. a7) 40. Rxf7 ({Weaker is} 40. Qxc4 bxc4 41. Rd4 Ra7 $16) 40...
Qxf7 $18 {Endgame. KQR-KQR} 41. Qe3 {need to eliminate ?c6} Qc7 42. a7 {let the
pawn roll. I think it's better than Re1.} (42. Re1 Rf7 43. Qc5 Qa7 44. Qxc6 b4)
42... Ra8 43. Qc5 Kg7 (43... Qb7 44. f4) 44. Ra6 Qb7 45. Rxc6 {Intending Rc7+
and mate.} ({Inferior is} 45. Qxc6 Qxc6 (45... Rxa7 46. Qf6+ Kh6 47. Qh4+ Kg7
48. Qd4+ Kg8 49. Rxa7) 46. Rxc6 Rxa7 $10) 45... Rxa7 46. Qe5+ (46. Qd4+ $142 Kh6
47. Re6) 46... Kh6 (46... Kg8 $142 47. Re6 Ra8) 47. Qf4+ Kg7 {the only move,
otherwise mate in 2} 48. Qf6+ Kg8 49. Rd6 {[%cal Rd6d8]} Ra8 50. Qd4 $1 Qf7
(50... Rf8 51. Rd7 Qxd7 52. Qxd7) 51. Rd7 Qf8 52. Qh4 {[%csl Gd7][%cal Rh4h7]}
h6 {I even didn't thought about h6 vs h5} (52... h5 53. Qe4) 53. Qe4 Ra6 54.
Qd5+ {Weighted Error Value: White=0.17 (very precise) /Black=0.18 (very precise)
. Inaccurate: White=1 Black=5 OK: White=22 Black=14 Best: White=3 Black=7
Strong: White=1 ---} 1-0
```

<br>

## Game Analysis: Barclay, Dean

I have never played Dean, and it was an interesting experience. Under correspondence, I thought this was more like a "correspondence blitz."
My pawn majority at the end didn't bring me over a winning finish line, and I offered a draw when a threefold repetition by White would have been very likely.

My thoughts during the game are in the annotations, too.

```pgn
[Event "USCF/2021 Electronic Knights Final/21ENf01"]
[Site "ICCF"]
[Date "????.??.??"]
[Round "?"]
[White "Barclay, Dean"]
[Black "Schroeer, Egbert"]
[Result "1/2-1/2"]
[ECO "A16"]
[WhiteElo "1800"]
[BlackElo "2137"]
[Annotator "Schroeer,Egbert"]
[PlyCount "86"]
[GameId "489232844371"]
[EventDate "2024.01.19"]
[EventType "corr"]

1. c4 Nf6 2. g3 g6 3. Bg2 d5 {try something new} (3... Bg7 4. Nc3) 4. cxd5 Nxd5
5. Qb3 {Unexpected. I think ?c3 would have been stronger} (5. Nc3) 5... c6 6.
Nc3 Nb6 7. Nf3 Bg7 8. O-O {[%cal Yd2d4]} O-O 9. d4 $1 {White is slightly
better.} Be6 (9... Na6 10. Bf4) 10. Qc2 Na6 {[%cal Bb8a6,Ba6c7,Bc7e6,Be6d4] He
is playing extremely fast, like Blitz. Maybe he knows the line in and out, or
it's psychology.} 11. a3 Nc7 {[%cal Ya7a5] Move away from a "do nothing"
position and control d5} (11... Bg4 {[%cal Yg4f3]} 12. Rd1 (12. e3 Qd7 13. Ne4
Bf5) 12... Qc8 13. Ne5 Bh3) 12. Rd1 Qc8 13. e4 $5 {?g5 was the move} (13. Bg5
Re8 14. e4) 13... Bg4 14. Ne2 Ne6 (14... f5 15. e5 Nbd5) 15. h3 (15. h4 f5 16.
e5 f4 17. Nxf4 Nxf4 18. Bxf4 Nd5 19. Qb3 Rxf4 20. gxf4 Bh6 {Against Ng5}) 15...
Bxf3 16. Bxf3 c5 17. d5 Nd4 18. Nxd4 cxd4 19. Qe2 (19. Qxc8 Raxc8 $10 20. Bg5
Rfe8 21. Rac1 h6 22. Rxc8 Nxc8 23. Bd2 Nd6 24. Rc1 d3 25. b3 Rc8 26. Rxc8+ Nxc8
27. Kf1 Nd6 28. Ke1 b6 29. Bg2 Kf8 30. Be3 Bc3+ 31. Bd2 Bg7 $1 32. Be3 f5 33.
exf5 gxf5 $2 (33... Nxf5 $10 {and Black has nothing to worry.} 34. Bf4 Nd4) 34.
Bf1 $16) 19... e5 {Inhibits Bf4.} (19... Qc7 20. Bf4 Qc4 21. Rac1 Qxe2 22. Bxe2
Rac8 23. Bg5 $16) (19... Qc4 20. Bg5 e5 21. dxe6 Qxe6) 20. Bd2 $5 {[%cal
Bc1d2,Bd2b4,Bb4e7]} (20. dxe6 Qxe6 21. Bf4 Nc4 $10 {seems to me the most
promissing line for Black}) 20... Qc2 $5 {[%cal Yc2b3]} (20... Qd7 {[%cal
Yb6c8]} 21. h4 Nc8 22. h5 f5 23. hxg6 hxg6 $14) 21. a4 $1 Nc4 (21... Qb3 {[%cal
Yf8c8]} 22. Ra3 Qxb2) 22. Bb4 {[%csl Rc2,Rf8]} (22. Rac1 Qb3 $1 23. Rxc4 d3 $1)
22... Qxe2 23. Bxe2 Rfc8 {[%cal Bf8c8,Bc8c3,Bc3g3] Black is weak on the light
squares} 24. b3 a5 25. Be7 $5 {White is more active.} (25. Bxc4 axb4) 25... Nb6
26. d6 Bf8 27. Bb5 Rc3 28. f4 $5 {I considered this move as interesting. Now
it's on the board} (28. Rac1 Rxc1 (28... Nc8 29. Rxc3 dxc3 30. Bxf8 c2 $3 31.
Rc1 Kxf8 32. d7 Nd6 33. Rxc2 Ke7 {[%cal Ya8d8]} 34. Rc5 f6 {[%cal Ya8d8]} (34...
Nxb5 $2 {34...f6 1.92} 35. Rc8 $18) 35. f4 exf4 36. e5 $1 fxe5 37. Rxe5+ Kf8)
29. Rxc1 Nc8 $1 30. Bxf8 Kxf8 31. d7 Nd6 {[%cal Ya8d8]} 32. Rc5 f6 $1 $10) 28...
Rxg3+ {The position is equal.} (28... Rxb3 29. fxe5 Rc8 (29... Bxe7 $2 30. dxe7
Rxb5 31. axb5 $18) 30. Rac1 Rxg3+ (30... Bxe7 $2 31. dxe7 Rxg3+ 32. Kf2 $18) 31.
Kf2 $18) 29. Kf2 exf4 (29... Rxh3 30. fxe5 Rxb3 31. Rxd4 $16) 30. e5 $5 {can I
let the ? roll? ?xb3? or secure ?g7?} (30. Rac1 Nc8 31. Bxf8 Kxf8 32. Rxd4 Na7
$1 33. e5 Nxb5 34. axb5 g5) 30... Bg7 {Black needs to move the ? or go
immediately for ?f6} (30... Bg7 $5 31. Bf6 Bxf6 (31... Rxb3 32. Rxd4 Rb2+ 33.
Kf3 $10) 32. exf6 d3 $10 (32... Rxh3 33. Rxd4 Re3 34. Rc1 $14)) (30... Bg7 $5
31. Bf6 Rxh3 $10) 31. d7 {Really sharp! That's really forcing! I should have
enough compensation} (31. Bf6 Bxf6 32. exf6 d3 {this looks better}) 31... Nxd7
32. Bxd7 {This pair of bishops is nice.} Bxe5 {[%cal Yd4d3]} ({Much weaker is}
32... Rxb3 $6 33. Rab1 Re3 34. Rxd4 $16) 33. Bh4 {if ?xb3 I lose the pawn on b7
or exchange ?. This is a very tough position!} Re3 (33... Rc3 $5) 34. Kg2 Ra6
{[%cal Ya6d6]} 35. Bb5 Rb6 36. Bf2 $5 (36. Bd8 Rg3+ 37. Kf2 Rd6 38. Bc7 Re6 39.
Bxe5 Rxe5 40. Rxd4 {Threatens to win with Bc4.} Rxh3 41. Bc4 g5 42. Rg1 (42.
Re1) 42... Rf5) 36... Rxb3 {the only move I think} 37. Rac1 $5 (37. Bxd4 Bxd4
38. Rxd4 g5 {should be equal} 39. Rg1 h6 40. Kh2 {[%cal Yh3h4]} Rb2+ 41. Rg2
Rxg2+ 42. Kxg2 Kg7 43. Rd8 Kg6 44. Ra8 Kh5 45. Rxa5 Kh4 46. Bd7 Rd6 47. Bc8 Rd2+
48. Kf3 Ra2 49. Ra7 Ra3+) 37... Kg7 (37... Rb2 38. Rc5 Re6 39. Kf3 {[%cal
Yb5c4]} Kg7 40. h4 h6 41. Bc4 b6 42. Rc8 {[%cal Yf2d4]} Re7 43. Re1 {Strongly
threatening Bxd4.} Rd2 44. Re2 Rd1) 38. Rxd4 $5 {[%csl Ge5][%cal
Gb6b5,Ra4b5,Gf4f3,Rg2g1,Ge5d4] Interesting move! Now let's go wild and
unexpected} (38. Bxd4 Bxd4 39. Rxd4 Rg3+) 38... R6xb5 39. axb5 {Black must now
prevent Rd7.} f3+ 40. Kg1 Bxd4 41. Bxd4+ Kh6 42. b6 {Hoping for Rc7.} Rd3 43.
Rc4 {Kf2 is the strong threat.} (43. Be5 Rb3 {draw?} 44. Bd4 {And now Rc7 would
win.} Rd3 45. Bf2 {aiming for Rc7.} a4 46. Ra1 a3 47. Bc5 g5 48. Rxa3 Rxa3 49.
Bxa3 Kh5 50. Be7 Kh4 51. Kh2 f5 (51... f2 $5 52. Kg2 $7 f5 $16)) 43... f5
{Weighted Error Value: White=0.05 (flawless) /Black=0.03 (flawless) .
Inaccurate: White=1 Black=1 OK: White=18 Black=22 Best: --- Black=7 a threefold
repetion is very likely and so I offered a draw after long thought. My pawn
majority and the position doesn't gave me much advantage I think. Dean answered:
one of us could err in the future (e.g., 44 Kf2 f5?), but yes, I agree, a
threefold repetition is likely soon if we both are mindful. our moves so far
have certainly been just that! So I accept. Well played. Thanks for the
challenge. --Dean} 1/2-1/2
```

<br>
I am considering looking into it again, especially considering the calculated sidelines during the game.
<br>

## Game Analysis: Corkum, Tim

And then -update 06/17/2024- after posting the blog I finished this game against Tim Corkum.
I played Tim before and was able to secure a draw, but this one ended different - in favour for Tim; and as he always says **"sláinte"**

Tim Corkum is a Correspondence Chess Master (CCM) from Wisconsin. He has had significant achievements in the world of correspondence chess. He won the Electronic Knights title 3 times: 2011, 2016 and 2018. He was the co-champion of the 2022 US Chess Absolute Championship with John Walton. This is a testament to his skill and dedication to the game of chess.

```pgn
[Event "USCF/2021 Electronic Knights Final/21ENf01"]
[Site "ICCF"]
[Date "????.??.??"]
[Round "?"]
[White "Schroeer, Egbert"]
[Black "Corkum, Tim"]
[Result "0-1"]
[ECO "A15"]
[WhiteElo "2137"]
[BlackElo "2363"]
[Annotator "Schroeer,Egbert"]
[PlyCount "98"]
[GameId "489232715680"]
[EventDate "2024.01.19"]
[EventType "corr"]

1. Nf3 Nf6 2. c4 e6 3. b3 {sideline of my standard repertoire} g6 4. Bb2 Bg7 5.
g3 O-O (5... b6 6. Bg2 Bb7 7. O-O (7. Nc3 $5) (7. d4 $5 O-O 8. O-O d5 (8... Na6
9. e3) 9. Qc2) 7... O-O 8. Nc3 d6 9. Qc2 c5 10. d4 $10 {should be equal}) 6. Bg2
b6 7. d4 Bb7 8. e3 $5 {The position is equal.} (8. O-O d5 9. cxd5 exd5 10. Nc3)
8... d5 $5 (8... Qe7 9. O-O Ne4 10. Nc3) 9. Nc3 dxc4 10. bxc4 c5 (10... Nbd7 11.
O-O c5 12. Qe2) 11. Qe2 (11. d5 $2 {11.Rc1 0.00} exd5 $17) 11... Qe7 {[%cal
Ga1d1,Rf8d8,Ya1c1,Ge1g1] And theory ends already after 11. move. We are on our
own.} (11... cxd4 12. exd4) 12. Rc1 (12. O-O) (12. Rd1 Rd8 13. O-O Nc6 14. d5
exd5 15. Nxd5 Nxd5 16. cxd5 Nb4 17. Bxg7 Kxg7 18. e4 {Black must now prevent
Rfe1.} Nxd5 $1 19. Rxd5 Bxd5 (19... Rxd5 $5 20. Qb2+ Rd4 21. Nxd4 cxd4 $10)
(19... Rxd5 $5 20. Qb2+ Rd4 21. Nxd4 cxd4 $10) 20. Qb2+) 12... Ne4 {with this
move my strategy is gone. Castling should be the right move order. Exchange of ?
is probably not good due the fact the ? is coming in.} (12... Rd8 13. O-O Nc6
{more pressure on the d-?} 14. dxc5 Qxc5 15. Nd4 (15. Nb5 $5)) 13. O-O Nxc3 $1
{Didn't expect the exchange. I would have kept the ?} (13... Rd8 14. Rfd1 Nxc3
15. Bxc3 $10 Nd7 16. Qb2 cxd4 17. exd4 Rac8 18. d5 Bxc3 19. Rxc3 {Have a hard
time getting an attack. Black's blocking position is pretty strong.}) 14. Bxc3
Nd7 (14... Rd8 15. h4) 15. Rfd1 Rfd8 (15... Rfe8 16. a4 Rac8 17. d5 (17. Qa2)
17... exd5 {[%cal Yd5d4] And now ...d4! would win. aiming for ...d4! Threatens
to win with ...d4!} 18. Bxg7 Kxg7 19. cxd5 Red8 $2 (19... Rcd8 $10 {and Black
stays safe.}) (19... Rcd8 $10 {and Black is okay.}) ({Better is} 19... Rcd8 $10)
20. e4) 16. h4 {[%cal Gf3g5]} Rac8 {[%cal Gf3g5,Rb7f3,Gg1g2,Yh4h5,Yg6h5] I don't
feel comfortable and have a hard time calculating a plan.} (16... h6) 17. h5 Ba6
{[%cal Rc5d4,Gf3d4,Ra6c4,Ge2d2] that's the thread now. I think ?b2 is the best
move? or ?a3 to play later ?b4? However, a ? sacrifice with ?gxh5} (17... gxh5
18. Nh4 cxd4 {Hoping for ...Bxg2.} 19. exd4 Bxg2 20. Kxg2) 18. a3 {not a good
move I found out in the aftermath.} (18. d5 exd5 19. Bxg7 Kxg7 20. Rxd5 Bb7 $10)
(18. Qb2 Bxc4 19. dxc5 Bxc3 20. Rxc3 $10) 18... gxh5 19. Bb2 {[%cal
Gd4d5,Gb2g7,Rd7f6,Rd7f8,Rc5d4]} Nf8 20. d5 {[%cal Rg7b2,Re6d5,Rf8g6]} Ng6 21.
Bh3 (21. Bxg7 {the better move} Kxg7 22. Qb2+ Qf6 23. Qxf6+ $10) 21... Rb8 {I
believe Black has an advantage. Very solid position} 22. Bxg7 Kxg7 23. Qb2+ (23.
Nd2 $2 {23.Qb2+ -0.17 23.Qb2+ -0.20} Rxd5 {desaster}) 23... Qf6 24. Qxf6+ Kxf6
25. e4 exd5 (25... h4 26. Nxh4 Nxh4 27. gxh4 exd5 28. cxd5 {Black must now
prevent f4.} Rg8+ 29. Kh2) (25... Ne5 $2 {25...exd5 -0.18} 26. Nxe5 Kxe5 27. f4+
Kf6 (27... Kxe4 $2 {27...Kf6 1.52 27...Kf6 1.91} 28. Kf2 $1 $18) 28. d6 $14)
(25... Ne5 $2 {25...exd5 -0.46} 26. Nxe5 Kxe5 27. f4+ Kf6 (27... Kxe4 28. Kf2)
28. d6 $14) (25... Ne5 $6 26. Nxe5 Kxe5 27. f4+ Kf6 28. d6 $14) 26. exd5 h4 $1
27. d6 (27. gxh4 Re8 $15) 27... Rg8 $5 (27... hxg3 28. fxg3) 28. d7 (28. Kh2
hxg3+ 29. fxg3 Rge8 30. d7 Re2+) 28... hxg3 (28... Nf4 29. Kh2 hxg3+ 30. fxg3
Nxh3 31. Kxh3 Bb7 {[%cal Yb8f8,Yf6e7] Strongly threatening ...Rbf8!} 32. Rf1
{Threatens to win with Rce1. And now Rce1 would win. Rce1 would now be deadly.}
Rgd8 33. Nh4+ $2 (33. Rcd1 $10 {and White has nothing to worry.}) (33. Rcd1 $10
{and White stays safe.}) (33. Rcd1 $10) 33... Kg7 $19 {[%cal Yg7f8]} 34. Nf5+
Kf8 $1 35. Rf4 Rxd7 {Threatens to win with ...Rbd8.} 36. Rh4 {this is too slow})
29. Rd6+ (29. fxg3 {I think I'm screwed... all this isolated pawns. However,
fxg3 was the better move.} Nf4 30. Kh2 Nxh3 31. Kxh3) 29... Ke7 30. Rc6 $1 Nf4
31. Re1+ Kd8 (31... Kf8 $5 32. Bf5 $7 Bb7 $15 (32... Bxc4 $2 {32...Bb7 0.07} 33.
Rc8+ Kg7 34. Ree8 $18) (32... Bb7 $5 33. Ne5 Rg5 34. fxg3 (34. Bxh7 $2 Nh3+ 35.
Kh1 gxf2 $19) (34. Rc8+ $2 Rxc8 35. dxc8=B Bxc8 $19) 34... Rxf5 (34... Rxg3+ 35.
Kf2 $16) 35. gxf4 Rxe5 (35... Rxf4 $2 36. Rc7 $18) 36. Rc8+ Rxc8 37. dxc8=Q+
Bxc8 38. Rxe5 Ba6 $10)) 32. Bf5 Bb7 (32... Bxc4 $2 {32...Bb7 -0.86 32...Bb7
-0.08} 33. Rc8+) (32... Bb7 $5 33. Ne5 gxf2+ 34. Kxf2 Bxc6 35. Nxc6+ Kc7 36.
Nxb8 Rxb8 $17) ({Worse is} 32... Bxc4 33. Rc8+) 33. Ne5 {[%cal Re5f7]} Bxc6 34.
Nxc6+ Kc7 35. Nxb8 Rxb8 $19 {Endgame. KRB-KRN} ({Don't take} 35... gxf2+ 36.
Kxf2 {Intending Re8 and mate.} Rxb8 (36... Kxb8 $2 {36...Rxb8 -1.15 36...Rxb8
-0.10} 37. Re8+ Kb7 38. Rxg8 h6 39. d8=Q {[%csl Gf5,Gg8][%cal Rd8c8]} Ka6 40.
Qe8) 37. Re7 $1 $17) ({Don't take} 35... gxf2+ 36. Kxf2 {White wants to mate
with Re8.} Rxb8 (36... Kxb8 37. Re8+ Kb7 38. Rxg8 h6 39. d8=Q) 37. Re7 $17) 36.
Re8 $2 {Rxb8 would kill now. White does not recover from this. That was a
blunder and after this Black is on a winning path} (36. Re7 $1 $15 gxf2+ 37.
Kxf2 Rd8 38. Rxf7 Ng6 39. Ke1) (36. Re7 $1 $10 Ng6 37. d8=R+ Kxd8 38. Rxf7)
36... gxf2+ 37. Kxf2 {[%cal Ye8b8]} Rd8 {[%cal Yf4e6] Hoping for ...Ne6!} 38.
Re7 (38. Kf3 $2 {38.Re7 -2.63 38.Re7 -3.70 38.Re7 -3.75} Ne6 39. Bxh7 (39. Bxe6
$142 fxe6 40. Rxe6) 39... Ng5+ {doesn't work}) 38... Ng6 39. Rxf7 Ne5 $1 {[%csl
Rc4,Rd7,Rf7]} 40. Rxh7 Rf8 (40... Nxc4 {[%cal Yd8f8]} 41. Ke2 Nxa3 {That was it.
It's over}) ({Not} 40... Nxc4 {[%cal Yd8f8]} 41. a4 $19) ({Weaker is} 40... Nxd7
$2 {40...Rf8 -3.05 40...Nxc4 -4.33} 41. Re7 $10) ({Weaker is} 40... Nxd7 41. Re7
$10) ({Much less strong is} 40... Nxc4 41. a4 $19) ({Not} 40... Nxd7 41. Re7
$10) 41. Rh5 Nxc4 {[%cal Yc4d6]} 42. Ke2 Nxa3 43. Kd3 Nb5 44. Bg4 (44. Bh3 Nd6
45. Kc3) 44... Nd6 45. Be6 Nb7 (45... Rf3+ 46. Kc2) 46. Bf5 Rf6 47. Kc3 Nd8 48.
Kc4 a6 49. Kb3 Ne6 {Weighted Error Value: White=0.20 (precise) /Black=0.02
(flawless) . Inaccurate: White=5 Black=1 OK: White=15 Black=28 Best: White=2
Black=7 at this point and after some thoughts I resigned. No chance he will
blunder and no chance to turn the tide.} 0-1
```

<br>
As you can see, I never recovered from my move 36. That's how it goes in correspondence chess. Over the board you might have had a chance to draw, but not here. I have 3 games to go and ranked actually at 3rd place. Let's wait and see how it goes.

You can find my other game from [semi-final here](https://chess.myvortexcloud.com/tournaments/21ENs04-Corkum/)
<br>
<br>

**Amici Sumus**

See you next week, when I will share the 2024 Electronic Knights Preliminary results so far. If you enjoy my insights, consider supporting me with a virtual coffee! ☕️ Or a beer? Either way 😎 - Your support fuels me to continue sharing valuable content.

Click the coffee mug below at the end of the webpage, and please subscribe and share broadly.

> [Please subscribe](https://follow.it/senior-chess-improver?leanpub)
