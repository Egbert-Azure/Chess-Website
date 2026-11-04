---
layout: post
title: "Decoding Correspondence Chess: Seven Pieces Rule and the 50-Move Rule Unveiled"
date: 2023-12-06
description: "Unravel the intricacies of the Seven Pieces Rule and the 50-Move Rule in International Correspondence Chess Federation (ICCF) games. Explore how these rules, connected to endgame tablebases, shape strategic thinking and computational precision in the world of correspondence chess."
tags: [correspondence-chess, rules, strategy, endgame-tablebases]
image:  '/images/decode 2.jpeg'
featured: false
---


## Introduction

Welcome to another blog, Chess Enthusiasts! Today, we will double-check on a fascinating exploration of the intricacies within the International Correspondence Chess Federation (ICCF) rules. Specifically, we unravel the "Seven Pieces Rule" and its connection to endgame tablebases alongside the well-known "50-Move Rule." Let's dive into the world of correspondence chess, where strategic prowess meets computational precision.

## The Seven Pieces Rule and Endgame Tablebases

The "Seven Pieces Rule" in chess is a distinctive feature in correspondence chess under ICCF rules, intricately tied to using endgame tablebases. According to ICCF guidelines, if a player has seven pieces or fewer on the board, the endgame can be claimed as a win or draw with reference to endgame tablebases³. This rule discourages premature resignations, prompting players to leverage the exhaustive analysis stored in these databases.

### Endgame Tablebases and 7-piece Claims

Endgame tablebases can be pivotal in correspondence chess, especially with recent ICCF Congress decisions. Players can claim a win or draw if the position can be resolved in a 7-piece tablebase position¹. ICCF has an agreement with LiChess to provide Tournament Directors free access to the 7-piece Syzygy tablebases. These computer databases offer precise calculations for optimal play, ensuring certainty in endgame positions.

### Syzygy Tablebases

Syzygy tablebases, allowing perfect play with up to 7 pieces², bring an additional layer to correspondence chess. They enable players to navigate through complex endgames, adhering to the fifty-move drawing rule while maximizing their strategic potential.

### Making a Claim with 7-piece Tablebases

Players seeking to claim based on 7-piece tablebases must follow a specific procedure. Claims are only valid for positions resolved by these tablebases. The process is similar to other ICCF claims; players can use the dropdown menu on the game page to either "Claim a win" or "Claim a draw." In the claim form, players must explicitly state that they are claiming based on endgame tablebases. They can claim based on the current board position or propose a move and claim based on that position. However, the proposed move must not be played on the board; otherwise, the player must wait until the next turn before filing the claim. Once submitted, the server automatically evaluates the position and sets the result if the claim is correct. Notably, claims in team matches are now submitted directly to the server, eliminating the need to go through team captains.

## The 50-Move Rule in Perspective

The well-known "50-Move Rule," as the ICCF outlines, allows a player to claim a draw if no capture or pawn move occurs in the last fifty moves. However, an interesting caveat arises: this rule only applies when more than seven pieces remain on the board. Players can leverage the Seven Pieces Rule and refer to endgame tablebases for potential game-changing strategies when the game reaches a critical juncture with seven pieces or fewer.

## Strategic Considerations and Conclusion

Understanding these rules is essential for correspondence chess players seeking to master the game. The Seven Pieces Rule encourages tenacity as players navigate the endgame armed with insights from endgame tablebases. Meanwhile, the 50-move rule adds additional complexity, urging players to carefully manage move counts and strategically reset the counter when necessary.


You might wonder WHY you can even use a tablebase.

If no tablebase rule was implemented, it could lead to endless games in certain situations. This is particularly true in complex endgame scenarios where perfect play is required to secure a win or a draw. Without the use of tablebases, players might struggle to find the optimal moves, leading to prolonged games.

While the absence of a tablebase rule might not necessarily lead to endless games due to the fifty-move rule, it could lead to inaccuracies in the adjudication of complex endgames and potentially unfair outcomes. The implementation of the tablebase rule helps to mitigate these issues, ensuring that games are decided by skill and strategic understanding rather than computational power alone.

In correspondence chess, the use of additional tools varies based on the platform and tournament rules. Here's a straightforward breakdown:

**ICCF Tournaments:**

The International Correspondence Chess Federation (ICCF) allows chess engines in their tournaments. This practice is sometimes referred to as "Centaur Chess.". It's crucial to note that while engines can offer valuable analysis, they cannot complement human strategy and understanding. Successful players often use engines to explore ideas, guide the analysis, and make final decisions. Utilizing an engine to analyze positions and calculate variations is beneficial, but understanding the positions, strategies, and tactics is equally important.

ICCF also permits the use of opening books and databases in their tournaments. These tools are valuable for studying positions, understanding plans, and considering alternative moves for both sides.

**USCF Tournaments on ICCF Platform:**

For US Chess Correspondence Chess (CC) tournaments on the ICCF platform, using computer programs or algorithms to generate moves is **NOT** allowed. Players are required to analyze the game and decide on their moves independently.

The USCF does permit the use of opening books in their correspondence chess. It's essential to remember that while opening books provides valuable insights, they are not a substitute for human strategy and understanding.

These are general guidelines, and specific tournaments may have additional rules. Always check the specific regulations for each tournament you participate in.

However, the true essence of correspondence chess lies in profound analysis. Simply following engine moves may not lead to success. The luxury of time in correspondence chess allows for deep exploration of positions, often resulting in the discovery of brilliant, non-intuitive moves. The ultimate goal is to reach a complicated, imbalanced position.

## Learning from Veterans World Cup 13

I had the pleasure of playing against Correspondence Chess Master Christophe David-Bordier (ELO 2374), a very experienced player from France. 
<div style="text-align: center;">
<img src="{{site.baseurl}}/images/Christophe David-Bordier.png" alt="image" width="20%">
</div>

Christophe David-Bordier is a recognized player in the world of correspondence chess. He holds the title of Correspondence Chess Master (CCM) and was awarded the Correspondence Chess Expert (CCE) in 2017. He has completed 1220 games, winning 287 of them, and has played in 129 tournaments. His play is characterized by strategic planning and a deep understanding of the game. He has also participated in the 12th Chess 960 World Cup. His current rating is 2379.

Christophe played an opening as White which is close to my repertoire, and I was pretty confident. As you can see, it's going a bit back and forth until his brilliant move 42. h5!
However, the root cause for my troubled position was earlier. My move 27... c6 should have been 27... b6. However, his position was very strong already.

```pgn
[Event "VWC 13/SF 9"]
[Site "ICCF"]
[Date "2023.06.15"]
[Round "?"]
[White "David-Bordier, Christophe"]
[Black "Schroeer, Egbert"]
[Result "1-0"]
[ECO "E97"]
[WhiteElo "2374"]
[BlackElo "2114"]
[Annotator "Schroeer,Egbert"]
[PlyCount "141"]
[EventDate "2023.??.??"]

1. Nf3 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. d4 O-O 6. Be2 e5 7. O-O Nc6 8. d5 Ne7
9. b4 Nh5 10. Re1 f5 11. a4 {E97: King's Indian: Classical Main Line (6...e5 7
0-0 Nc6): 8 Be3 and 8 d5 Ne7, not 9 Ne1.} a5 {11...h6 is a critical line.} 12.
bxa5 Rxa5 13. Bd2 {White is better.} Nf6 {[%cal Bh5f6,Bf6e4,Be4f2]} 14. Ng5 h6
15. Ne6 Bxe6 16. dxe6 fxe4 17. Nxe4 {[%csl Ya5] Discovered Attack} Nxe4 {[%csl
Yf2] Discovered Attack} 18. Bxa5 Nxf2 19. Qc2 d5 $146 ({Predecessor:} 19... Nc6
20. Qxg6 Rf6 21. Qh5 Nxa5 22. Rf1 Ne4 23. Bf3 d5 24. Rad1 Nxc4 25. Bxe4 Rxf1+
26. Rxf1 dxe4 {½-½ Vekelis,G (2412)-Rallabandi,P (2486) EU-chT12 sf2 email ICCF
email 2021}) 20. Rab1 (20. cxd5 $6 Qxd5 21. Qd2 (21. Qxc7 Nh3+ 22. gxh3 Qd4+ 23.
Kh1 Qd5+ 24. Kg1 Qd4+ 25. Kh1 Qd5+ 26. Kg1 $10) (21. Bxc7 $2 Qd4 $19) 21... Qc5
$10) 20... e4 21. Rf1 (21. Rxb7 Qa8 22. Bb6 (22. Rxc7 $2 Qxa5 23. Rb1 Bd4 $19)
(22. Rb5 $2 c6 $19) 22... Qxb7 $17 (22... cxb6 23. Rxe7 Bd4 24. cxd5 $10)) 21...
d4 22. Rxf2 Rxf2 23. Qxe4 (23. Kxf2 d3 24. Bxd3 exd3 $14) 23... Rf5 24. Rb5 Qd6
25. Bd3 Qa3 26. Qe2 {Active counter play!} (26. Bxc7 $2 Qc1+ (26... Qxa4 $2 27.
Rb1 $18) (26... Qxa4 $2 27. Rb1 $18)) 26... Rxb5 27. cxb5 {[%cal Ye2f1]} c6 28.
Bd8 {Bxe7 would now be deadly.} cxb5 29. axb5 (29. Bxb5 d3 (29... Qc1+ 30. Kf2
$10) 30. Qd1 (30. Bxd3 $2 Qa1+ 31. Kf2 Qd4+ 32. Kf1 Qxd8 $19) 30... d2 31. Qxd2
Qa1+ 32. Kf2 Qf6+ 33. Kg1 Qa1+ 34. Kf2 Qf6+ 35. Kg1 Qa1+ $10) 29... Qc1+ 30. Kf2
Qf4+ 31. Qf3 Qd2+ 32. Be2 Nf5 {[%cal Yd4d3]} 33. e7 (33. Qxb7 $2 d3 34. Qe4 dxe2
(34... Qxe2+ 35. Qxe2 dxe2 36. b6 $17) 35. Qxe2 Qxd8 $19) 33... Qe3+ 34. Kf1
{Some like it hot} Qe5 35. Bc4+ (35. Qxb7 $6 d3 36. e8=Q+ (36. Bxd3 Qf4+ 37. Qf3
Qc1+ 38. Ke2 Qb2+ 39. Kf1 Qc1+ 40. Kf2 Bd4+ 41. Ke2 Qb2+ 42. Kf1 Qc1+ 43. Ke2
Qb2+ 44. Kf1 Qc1+ 45. Ke2 $10) 36... Qxe8 37. Qd5+ (37. Bxd3 $2 Qxd8 38. Qe4 Kh7
$19) 37... Kh7 38. Qxd3 Qe5 $10) 35... Kh7 36. Qe2 (36. Qxb7 $2 Ne3+ (36... Qxh2
$2 37. e8=Q $18) 37. Kg1 Nxc4 $19) 36... Qf4+ 37. Kg1 Qc1+ 38. Qf1 Qe3+ 39. Qf2
Qc1+ 40. Bf1 Nd6 {[%cal Yd4d3]} 41. h4 {[%cal Bh2h4,Bh4h5]} d3 {[%cal Yd3d2]
Threatens to win with ...d2!} (41... Nxb5 42. e8=Q (42. e8=R Nd6 $18) 42... Nd6
43. Qe6 Qc6 44. Qg3 (44. Bd3 Nf5 $18) 44... Qe8 45. Qgxd6 (45. Qexd6 g5 46. Bd3+
Kg8 47. Qd5+ Kh8 48. Qf5 Kg8 49. Qh7+ Kf7 50. Qc7+ {Skewer} Qd7 51. Qxd7+ Kf8
52. Qhxg7#) 45... Qxe6 46. Qxe6) 42. h5 $1 Ne8 (42... Nxb5 43. hxg6+ (43. e8=R
Bd4 $10 {Pin}) 43... Kxg6 44. e8=Q+ Kh7 45. Qf5#) (42... gxh5 $2 43. Bc7 Ne8
(43... Qxc7 44. Bxd3+ Kg8 45. Qa2+ Nf7 46. Bh7+ {Decoy, Promotion} Kxh7 47.
Qb1+) 44. Qf5+ (44. Bf4 Qc3 $16) 44... Kg8 45. Qd5+ (45. Ba5 Qe3+ 46. Kh1 Qxe7
$10) 45... Kh8 46. Qd8 (46. Qxh5 $2 Bd4+ 47. Kh2 Qxc7+ $19) 46... Qc5+ 47. Kh2
(47. Kh1 Qxb5 48. Bxd3 Qc6 $18) 47... Qxb5 (47... Qxc7+ $2 48. Kh3 $18) 48. Bxd3
$18 (48. Qxd3 Qxd3 49. Bxd3 Nxc7 $17)) (42... d2 $2 43. hxg6+ Kxg6 (43... Kh8
44. Qf8+ {Back Rank} Bxf8 45. exf8=Q#) 44. Qg3+ Kf7 45. Qxd6 $18) 43. Ba5
{Against d2} Bf6 ({But not} 43... Nd6 $2 44. hxg6+ (44. Qb6 gxh5 45. Qxd6 Qe3+
46. Kh1 Bd4 $18) 44... Kxg6 45. Bb4 $18 (45. Qg3+ Kf7 $18)) 44. Bd2 Qc4 45. Qf3
{[%csl Rb7,Rd3]} Qc5+ 46. Kh1 Qxh5+ 47. Qxh5 gxh5 48. Bxd3+ $18 {Endgame.
KBB-KBN} Kg7 49. Be4 Bxe7 50. Bxb7 {A strong pair of Bishops.} Nd6 51. Bc6 Nf5
52. Kh2 {Prevents Ng3.} Bd8 53. Bc3+ Kg6 54. Kh3 Kg5 55. Be4 Kf4 56. Bd3 Bb6 57.
Bd2+ Ne3 58. Bg6 Ke5 59. Bxh5 Ke4 60. Be2 Bc7 61. Bc1 Nf5 62. Bf3+ Kd3 63. Bb7
Kc2 64. Ba3 Bb6 {Repels Bc5} 65. Bf8 {Black must now prevent Be4+.} Kb3 66. g4
Nd4 67. Bxh6 {Be3 is the strong threat.} Nxb5 68. g5 {Hoping for Bg7.} Be3 69.
Kg4 Bxg5 70. Bd5+ Kc3 {The game is a win for White because white could claim a
win due to 7 piece tablebases. With move 71. no draw po is possible, therefore,
Balck resigned. The 50 moves rule is excluded, because less than seven pieces on
board.} 71. Bg7+ {Weighted Error Value: White=0.05 (flawless) /Black=0.05
(flawless) . Inaccurate: White=2 Black=4 OK: White=27 Black=30 Best: White=14
Black=12 Brilliant: White=1 ---} 1-0
```

The game is a win for White because white could claim a win due to 7 piece tablebases. With move 71. no draw is possible, therefore, Black resigned. The 50 moves rule is excluded, because less than seven pieces on the board.


## Conclusion

In conclusion, these rules are specific to correspondence chess under ICCF guidelines, distinguishing this form of play from others. Welcome to the nuanced world of correspondence chess and its particular tactics. Those experienced players virtuously play with rules and tactics such as the Seven Pieces and 50-Move Rule.

Amici Sumus

I'd love to hear your thoughts on today's post. Feel free to share your favorite chess strategy or ask any questions you may have.

> [Please subscribe](https://follow.it/senior-chess-improver?leanpub) 



*Source: Conversation with Bing, 12/6/2023*

1. [Fifty-move rule - Wikipedia](https://en.wikipedia.org/wiki/Fifty-move_rule)
2. [KvK – Syzygy endgame tablebases](https://syzygy-tables.info/)
3. [Rules of chess - Wikipedia](https://en.wikipedia.org/wiki/Rules_of_chess)
4. [ICCF Endgame Tabelbase Rules](https://www.iccf.com/message?message=641#:~:text=The%202013%20ICCF%20Congress%20in%20Krak%C3%B3w%2C%20decided%20that,these%20claims%20be%20extended%20to%207%20piece%20tablebases)

Player Details Christophe David-Bordier

5. [International Correspondence Chess Federation](https://www.iccf.com/player?id=180292)
6. [ICCF Game - International Correspondence Chess Federation](https://www.iccf.com/MakeAMove.aspx?id=1385695&success=true)
7. [ICCF Game](https://www.iccf.com/game?id=1385081)