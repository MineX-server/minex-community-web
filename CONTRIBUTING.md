# Contributing

This project starts with documentation, a manual-pilot design, and an installation preview.
Read the status table in [README.md](README.md) before proposing a connected feature.

## Useful first contributions

- Improve the English or Spanish introduction.
- Clarify the operator installation and test instructions.
- Report accessibility issues in the preview.
- Test the preview on another machine and record the environment and result.
- Discuss the public account/game/approval boundaries without publishing private implementation details.

## Propose a change

1. Open an issue for a substantial change, or make a small focused pull request.
2. Explain the problem and the behavior the change produces.
3. Run the public-content checks and tests from [the testing guide](docs/testing.md).
4. Update documentation if the change alters what a user can actually do.
5. Wait for maintainer review before release.

Public contributions do not grant access to MineX services.
Requests to operate a community installation use the separate [pilot process](docs/pilot.md).

## Keep the boundary clear

Include only original work or material whose redistribution terms are documented.
Do not add private MineX services, player data, operational logs, credentials, game binaries, or third-party assets to this initial repository.
Use fictional domains under `example.invalid` for installation examples.
Do not claim a future feature is already available or that the installation preview is a playable client.

Changes to the explicit public file list need review just like code changes.
The content checker is a useful guard, not a substitute for reviewing what is being published.

## Verification

```bash
python3 tools/check_public.py
python3 -m unittest discover -s tests -v
```

The tests run without private services, player accounts, credentials, or blockchain calls.
Never test against a real player's account when reproducing a report.

Report sensitive findings through [SECURITY.md](SECURITY.md), not a public issue containing exploit details.
