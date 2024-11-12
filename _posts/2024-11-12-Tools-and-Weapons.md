---
layout: post  
title: "Tools and Weapons"  
description: "Software Tools to Improve and Track Your Chess Game"  
image: '/images/604.jpg'  
date: 2024-11-12  
tags: [ChessBase, MegaDatabase, UltraCorr, Chessify]  
featured: false  
---

Today, I’d like to share some updates and early findings on the chess tools I use to enhance and track my game.

On November 11, ChessBase released ChessBase 18 with several promising features despite unresolved issues from previous versions. With six open support tickets still pending a response, I debated the upgrade. However, with the 25% discount offer, I decided to go ahead, securing the new version for under $100, including a one-year premium membership.

### ChessBase 18: First Impressions

The setup process was a bit frustrating. Manual entry for the activation key—uncommon in modern software—was required, and closing certain applications like VPN and NVIDIA drivers turned out to be more complex than necessary. After a reboot, I was finally ready to explore. Another glitch is your premium membership. When you purchase the order promised you no longer need to add the one year perium membership key to your account, it will be automatically added. Unfortunately, it's not working, you need to add manually. Not a big deal, beut hey... ChessBase, who is doing your reviews?

#### New Design and Player Analysis

ChessBase describes this release as introducing “New dimensions in study and preparation,” and the player analysis tool reflects that direction. It allows users to analyze opponents’ playing styles, which can be particularly useful for correspondence players preparing for specific matchups. The interface has also been updated, and while it looks sleeker, I’ll need more time to assess its functionality fully.

I tested the player style analysis feature with my own games after merging the UltraCorr database into MegaDatabase, bringing my combined version up to 234 games. Below are some screenshots showcasing my personal style analysis report.

<div style="text-align: center;">
 <img src="{{site.baseurl}}/images/ESgames.png" alt="image" width="80%">
</div>

<br>

The analysis offers insights into various aspects of my style, which could be especially useful for identifying tendencies and refining my approach.

<div style="text-align: center;">
 <img src="{{site.baseurl}}/images/ESStyleReport.png" alt="image" width="80%">
</div>

<br>

#### Database Enhancements with MegaDatabase and UltraCorr

After weighing the value of upgrading from MegaDatabase 2023, I took the plunge with MegaDatabase 2025. Merging it with UltraCorr—a database widely regarded as the top resource for Correspondence Chess games—significantly enhances its value for serious players. UltraCorr includes ICCF games and top U.S. correspondence events like Electronic Knights. It’s frustrating, though, that ChessBase keeps Correspondence Chess games separate from the main database, perhaps to promote their costly Correspondence Database product. Adding blitz games in bulk further dilutes the analytical utility, as blitz and correspondence games differ significantly in quality and approach. 

Once I merged UltraCorr, ChessBase flagged around 850 duplicate games, which I refined using filters for “Top Games” and beauty evaluations. Re-reviewing my tournament games has been a practical way to reinforce lessons from past games and inspire new strategies.

For those interested in the new ChessBase 18 features, here’s a quick overview video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/w3CJ_s-vdZI?si=YDmiEYRswO483pWa" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<br>

### Remote Engine Analysis in ChessBase

One of the significant updates in ChessBase 18 is its remote engine analysis feature, though it remains limited by their proprietary server system, restricted to a standard two-core setup. For complex analysis, this configuration is often inadequate. While additional compute resources can be rented via ChessBase’s “Ducats” system, the lack of a true compute cluster architecture means scalability is still constrained. For users accustomed to distributed computing solutions, such as a Stockfish cluster on Raspberry Pi or in cloud environments like Azure, ChessBase’s remote analysis solution lacks the flexibility and power of a full cloud-based setup.

Allowing for integration with dedicated compute clusters, like Stockfish clusters on Azure or other distributed configurations, could greatly enhance ChessBase’s functionality for high-level analysis. My own Stockfish cluster, for instance, provided significant scalability at a lower cost, and newer platforms like Chessify offer similarly flexible, cloud-based compute power officially supported by ICCF. Such setups represent the future of cloud-based chess analysis, exceeding the limits of ChessBase’s single-server approach.

Around three years ago, I contacted Matthias Wüllenweber and the ChessBase development team to discuss these gaps in remote engine and compute cluster technology. Over time, I’ve shared my insights, including a comprehensive software architecture and guidance on integrating ChessBase with DrawBridge, an open-source UCI engine bridging tool developed by Khadim Fall. DrawBridge simplifies the installation process, making advanced engine setups accessible and straightforward.

For more details and technical findings, visit my [GitHub repository](https://github.com/Egbert-Azure/stockfish-cluster).

<div style="text-align: center;">
 <img src="{{site.baseurl}}/images/chessbaseremote.png" alt="image" width="80%">
</div>

<br>

### Transition to Chessify for Enhanced Cloud Analysis

After years of managing my own Stockfish compute cluster, I recently transitioned to Chessify, a cloud-based analysis service with powerful Stockfish engines and official ICCF support. For ICCF members, Chessify offers discounted rates, making it a more affordable and efficient option than running a cluster on Azure. With its scalable compute power, seamless ChessBase integration, and ICCF discounts, Chessify is a compelling alternative to local setups, providing high-performance analysis at a lower cost.

ChessBase 18’s updates show some progress toward cloud capabilities, but it’s still limited compared to the full flexibility and power of platforms like Chessify. It will be interesting to see if future ChessBase releases close this gap.

Chessify has introduced several impressive new features beyond just special pricing for ICCF players:

<div style="text-align: center;">
 <img src="{{site.baseurl}}/images/chessify.png" alt="image" width="80%">
</div>

<br>

Chessify’s Cloud service integrates with third-party GUI chess programs like ChessBase, Fritz, HIARCS, and SCID. Their online chess database now contains over 9.7 million games, including comprehensive archives for ICCF games, Mega Database games, and Lichess—a significant advantage for correspondence and online players alike. You can also securely save your own games and analyses with encrypted connections.

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

**Amici Sumus**

Thank you for reading! More updates are coming soon, as I’ll share further results and reflections from this tournament. If you enjoy my analysis and insights, consider supporting me with a virtual coffee ☕️ or maybe even a beer! Your support truly helps keep this blog going.

Click the coffee mug icon below to contribute—it’s appreciated!

<script data-name="BMC-Widget" data-cfasync="false" src="https://cdnjs.buymeacoffee.com/1.0.0/widget.prod.min.js" data-id="chesslife" data-description="Support me on Buy me a coffee!" data-message="Thank you for reading! You can buy me a coffee if you like!" data-color="#5F7FFF" data-position="Right" data-x_margin="18" data-y_margin="18"></script>

**Stay Connected!** If you haven’t already, [subscribe to the blog](https://follow.it/senior-chess-improver?leanpub) and share with fellow chess lovers.
