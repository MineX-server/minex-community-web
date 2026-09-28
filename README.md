# MineX Community Web

**Building open-source community websites for one shared MineX game.**

[Español](README.es.md) · [Project brief](docs/project-brief.md) · [Roadmap](docs/roadmap.md)

The idea is simple: a community runs a MineX website on its own VPS or domain. Players open that website, sign in through MineX, and join the same MineX worlds as everyone else. Their account, character, and progress stay with MineX.

Think of each VPS as another **doorway** to the same game in the cloud. It hosts the website; it does not run a new MineX world or a blockchain node.

> **What works today:** this repository has an open-source installation preview, documentation, and tests. You can run the preview on a computer or VPS. **It cannot launch the game yet.** The playable client and connection to MineX are future work, and the first connected installations will need manual approval.

## How it should work

1. A community installs the future web package on its VPS.
2. A player visits that community's website.
3. The player signs in on an official MineX page.
4. The browser joins the shared MineX game. The player sees the same worlds and other players.

MineX runs the shared game, accounts, and sensitive services. A community website can welcome players, but it cannot approve account or wallet actions for them.

## Try what exists now

You need Git and Python 3.10 or later. This starts a **preview page**, not the game:

```bash
git clone https://github.com/MineX-server/minex-community-web.git
cd minex-community-web
python3 tools/preview.py --port 8787
```

Open <http://127.0.0.1:8787> on that computer. Stop the preview with `Ctrl+C`.

To check the package:

```bash
python3 tools/check_public.py
python3 -m unittest discover -s tests -v
```

For an SSH tunnel to a VPS, follow the [VPS test plan](docs/vps-test-plan.md). The preview does not ask for a MineX password, wallet, or API key.

## What comes next

| Now | Goal |
| --- | --- |
| Public preview, tests, and installation plan | A reviewed, playable browser package |
| Community interest requests | Approved VPS installations connected to MineX |
| Shared game operated by MineX | Players joining it from many community websites |

The [roadmap](docs/roadmap.md) lists the work and tests needed before we can say “install it and play.” You can [request a place in the first pilot](docs/pilot.md); an issue does not activate a server by itself.

## Why open source and Solana?

The goal is to make the **website hosting layer** reusable, so communities in different places can help people reach the same MineX game. MineX already has a Solana integration in its official services; this repository does not publish a wallet implementation, private API, or financial approval system. This is not a token or play-to-earn proposal.

Hosting can be spread across independent VPS providers. The worlds and account authority remain with MineX, so we describe this as **distributed web hosting**, not a fully decentralized game. The [project brief](docs/project-brief.md) separates the public work already done from the next milestones.

## Contribute and learn more

Start with [CONTRIBUTING.md](CONTRIBUTING.md). See [architecture](docs/architecture.md), [testing](docs/testing.md), and [security reporting](SECURITY.md) for details. Never post passwords, OTPs, SSH keys, or wallet recovery information in an issue.

The original files in this repository use the [MIT License](LICENSE). The license does not grant rights to MineX branding, private services, or third-party game code and assets. Any future playable client needs its own dependency and distribution review.
