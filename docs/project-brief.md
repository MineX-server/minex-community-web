# Project brief

This page provides plain wording for community introductions and grant updates. It separates the public release from the proposed playable service.

## Short description

MineX Community Web is building an open-source way for communities to host the browser entrance to one shared MineX game. Each community could run the website on its own VPS and domain. Players would sign in through MineX, then play in the same worlds with their existing account and progress. MineX would continue to run the game and its official Solana-related services.

It is like adding more doors to one game in the cloud. A community VPS is a web host, not a separate MineX server or a blockchain node.
If one community website goes away, the intended player experience is to use another doorway with the same MineX account, character, progress, and wallet access. Existing players would not create a new account for every doorway. This spreads web hosting across communities while the shared game remains operated by MineX.

## What has been delivered

- A public, MIT-licensed installation preview and instructions.
- A proposed architecture and plan for a manually approved first pilot.
- Automated package checks and tests; a fresh clone smoke test was also run.

The preview starts a small web page. It has no playable client, MineX login, game connection, or wallet function. [Testing details](testing.md) explain what the checks prove.

## What we want to deliver next

1. Review the browser client and its dependencies before distributing any game files.
2. Build the official sign-in and game admission flow for approved websites.
3. Release a repeatable VPS installation package and test it on a clean external machine.
4. Show a player joining from a community website and another player joining through MineX, sharing the intended world and account state.
5. Verify that a modified community website cannot approve a sensitive operation for a player.

These are proposed milestones. None is complete simply because this repository is public. The [roadmap](roadmap.md) has the fuller acceptance criteria.

## Open source and Solana

The intended reusable public contribution is the website hosting layer, installation instructions, and tests. It could let communities in different places provide access to a game that already integrates Solana through official MineX services. It does not introduce a token, play-to-earn system, public wallet backend, or independent game economy.

The websites may be hosted across independent providers; the shared game, accounts, and financial authorization remain with MineX. We call this **distributed web hosting**, not a fully decentralized game. Any grant update should identify the completed public work and the still-unfinished connected milestones separately.
