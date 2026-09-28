# Roadmap

The project is being prepared in stages. This document does not promise dates.
Items marked as available are present in this repository; connected features need separate implementation and evidence.

| Stage | Deliverable | Exit evidence | Status |
| --- | --- | --- | --- |
| 0. Public foundation | README, architecture, manual-pilot process, preview and checks | Public clean clone, local tests, and GitHub Actions pass | Published and verified |
| 1. Distribution contract | Inventory of client artifacts, dependencies, versions and public scope | Reviewed package contains only distributable components | Planned |
| 2. Account and admission | Official sign-in handoff and installation-scoped game access | Correct account joins; unauthorized and revoked installations are rejected | Planned |
| 3. Independent approvals | Official review and authorization for all sensitive operations reachable from the game | Modified frontend cannot authorize an operation by itself | Required before a connected community pilot |
| 4. VPS package | Repeatable installation and HTTPS setup for the agreed artifacts | Fresh external machine reproduces installation from public instructions | Planned |
| 5. Small manual pilot | One approved operator and a small agreed test group | Players share a MineX world; events and reconnects remain clear | Planned |
| 6. More communities | Measured capacity, updates, and support workflow | Several installations operate within central allocations | Planned |
| 7. Optional self-service | Automated low-limit registration and domain verification | Abuse, suspension, and quota tests pass | Future decision |
| 8. Optional hosting transition | Community-hosted play with official account and approval pages retained | No hidden dependency on the official playable website | Future decision |

## First implementation priorities

- Specify the account, game-admission, and sensitive-approval boundaries together.
- Keep public request identifiers separate from authorization credentials.
- Define an installation lifecycle whose authority is held centrally.
- Verify that the frontend cannot select a different account or approve its own sensitive request.
- Review game commands and plugin entry points as well as visible web buttons.
- Document artifact distribution before describing the project as a ready-to-install playable client.

## Evidence before scale

A working website preview is not a gameplay acceptance test.
A successful login is not proof of correct event placement.
A blocked browser request is not proof that a direct server request is authorized correctly.
An approved operator is not proof that their future frontend remains unchanged.

Each stage needs evidence for the boundary it introduces.
Use synthetic accounts and a designated test environment for connected checks.
Financial testing needs its own explicitly agreed scope and budget; it is not part of this preview.

## Change and rollback

Keep releases immutable and record the version used by each pilot installation.
Test a candidate with a limited group before broad updates.
A frontend rollback must not revert account data, financial state, revocations, or allocation history.
If an optional sensitive feature is unavailable, make that state clear without silently changing the user's game mode.

## What this roadmap does not commit

It does not commit to publishing private server software, wallet internals, game assets, or every part of the current MineX workspace.
It does not guarantee compatibility with arbitrary client forks.
It does not designate this documentation package as completion of a separate funding or delivery agreement.
It does not promise that a community frontend cannot be copied or modified.
