---
layout: post  
title: "More Tools and Weapons"  
description: "Software Tools to Improve and Track Your Chess Game Part 2"  
image: '/images/604.jpg'  
date: 2024-11-12  
tags: [ChessBase, MegaDatabase, UltraCorr, Chessify]  
featured: false  
---



<iframe width="560" height="315" src="https://www.youtube.com/embed/znNUBIRkEok?si=AuQ-jExiWTE4Hvx3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Remote Engine Analysis in ChessBase

One of the significant updates in ChessBase 18 is its remote engine analysis feature, though it remains limited by their proprietary server system, restricted to a standard two-core setup. For complex analysis, this configuration is often inadequate. While additional compute resources can be rented via ChessBase’s “Ducats” system, the lack of a true compute cluster architecture means scalability is still constrained. For users accustomed to distributed computing solutions, such as a Stockfish cluster on Raspberry Pi or in cloud environments like Azure, ChessBase’s remote analysis solution lacks the flexibility and power of a full cloud-based setup.

Allowing for integration with dedicated compute clusters, like Stockfish clusters on Azure or other distributed configurations, could greatly enhance ChessBase’s functionality for high-level analysis. My own Stockfish cluster, for instance, provided significant scalability at a lower cost, and newer platforms like Chessify offer similarly flexible, cloud-based compute power officially supported by ICCF. Such setups represent the future of cloud-based chess analysis, exceeding the limits of ChessBase’s single-server approach.

So it looks like this now:

<div style="text-align: center;">
 <img src="{{site.baseurl}}/images/chessbaseremote.png" alt="image" width="80%">
</div>

<br>

Around three years ago, I contacted Matthias Wüllenweber and the ChessBase development team to discuss these gaps in remote engine and compute cluster technology. Over time, I’ve shared my insights, including a comprehensive software architecture and guidance on integrating ChessBase with DrawBridge, an open-source UCI engine bridging tool developed by Khadim Fall. DrawBridge simplifies the installation process, making advanced engine setups accessible and straightforward.
DrawBridge imitate a normal uci engine while bridging its traffic to a remote host. This will allow to use remote engine clusters to be used in traditional software. Which is the most flexible bridging software with some advanced features such as middleware definition.

Another core for chess engine compute cluster is Message Passing Interface (MPI), a software that connects processes running across multiple computers and allows them to communicate as they run. This is what allows a single script to run a job spread across multiple cluster nodes. And yes, there is a Stockfish Chess Enginge branch developed with MPI cluster implementation of Stockfish, allowing Stockfish to run on clusters of compute nodes connected with a high-speed network.

For more details and technical findings, visit my [GitHub repository](https://github.com/Egbert-Azure/stockfish-cluster).


### Transition to Chessify for Enhanced Cloud Analysis

After years of managing my own Stockfish compute cluster, I recently transitioned to Chessify, a cloud-based analysis service with powerful Stockfish engines and official ICCF support. For ICCF members, Chessify offers discounted rates, making it a more affordable and efficient option than running a cluster on Azure. With its scalable compute power, seamless ChessBase integration, and ICCF discounts, Chessify is a compelling alternative to local setups, providing high-performance analysis at a lower cost.

ChessBase 18’s updates show some progress toward cloud capabilities, but it’s still limited compared to the full flexibility and power of platforms like Chessify. It will be interesting to see if future ChessBase releases close this gap.

Chessify has introduced several impressive new features beyond just special pricing for ICCF players:

<div style="text-align: center;">
 <img src="{{site.baseurl}}/images/chessify.png" alt="image" width="80%">
</div>

<br>

Chessify’s Cloud service integrates with third-party GUI chess programs like ChessBase, Fritz, HIARCS, and SCID. Their online chess database now contains over 9.7 million games, including comprehensive archives for ICCF games, Mega Database games, and Lichess—a significant advantage for correspondence and online players alike. You can also securely save your own games and analyses with encrypted connections.
Unfortunately the ICCF Database is only available in the so called Master Plan. I'm wondering why I contribute with my games to the database and I have no benefits?
That's really weird! ICCF and Chessify: rethink!!

Additionally, the new LiveStream platform is a major innovation, far ahead of ChessBase’s offerings:

<div style="text-align: center;">
 <img src="{{site.baseurl}}/images/chessifylive.png" alt="image" width="80%">
</div>

<br>

<div style="text-align: center;">
 <img src="{{site.baseurl}}/images/chessifytournament.png" alt="image" width="80%">
</div>

<br>

#### Key Features of Chessify's Live Streaming Platform:

- **Comprehensive Event Page**: Features sections for ongoing, past, and upcoming events in one place.
- **Multiple Game Viewing**: Watch up to nine games side-by-side without switching tabs.
- **Integrated Analysis Tools**: Analyze live games instantly, with speeds based on your subscription level. For deeper insights, dedicated speed servers are available, thanks to Chessify’s partnership with Lichess.

Chessify's cloud-based architecture provides a different experience from traditional local setups, transforming familiar workflows. For example, it includes unique features like a chessboard scanner and a YouTube video search that identifies videos based on chess positions.

Ultimately, Chessify and ChessBase offer distinct strengths. While ChessBase’s detailed search functions and legacy content appeal to some, Chessify’s focus on high-speed analysis, advanced cloud architecture, and ICCF support provides powerful tools for serious correspondence and tournament players alike. Both can complement each other depending on your focus, but Chessify’s cloud approach opens new possibilities for modern chess analysis and is far ahead of traditional ChessBase in regards of cloud and compute cluster.

Checckout my previous [blog on Chessify](https://chess.myvortexcloud.com/chessify-next).
Among Chessify I explored [other tools in this blog](https://chess.myvortexcloud.com/whats-next) including Noctie.Ai.

**Amici Sumus**

Thank you for reading! More updates are coming soon, as I’ll share further results and reflections from this tournament. If you enjoy my analysis and insights, consider supporting me with a virtual coffee ☕️ or maybe even a beer! Your support truly helps keep this blog going.

Click the coffee mug icon below to contribute—it’s appreciated!

If you like to test Chessify you can use [this referral link](https://chessify.me/auth/signin?ref=JimMorrison42*6923)

<script data-name="BMC-Widget" data-cfasync="false" src="https://cdnjs.buymeacoffee.com/1.0.0/widget.prod.min.js" data-id="chesslife" data-description="Support me on Buy me a coffee!" data-message="Thank you for reading! You can buy me a coffee if you like!" data-color="#5F7FFF" data-position="Right" data-x_margin="18" data-y_margin="18"></script>

**Stay Connected!** If you haven’t already, [subscribe to the blog](https://follow.it/senior-chess-improver?leanpub) and share with fellow chess lovers.
