# Manual pilot access

## Current status

The published repository accepts expressions of interest.
Connected community gameplay is not enabled by this initial release.
An application can be reviewed while the integration is being completed; review does not mean the installation is active.

The owner has selected **manual approval for the first connected pilot**.
Self-service onboarding is a later roadmap phase, not a switch available to operators today.

## Applying

Use the **Community pilot request** issue template in the canonical GitHub repository.
Provide only information intended to be public:

- Community name and a short description.
- An optional public website or proposed domain.
- Region and preferred languages.
- Approximate concurrent group size for a test.
- Whether a test machine is already available.

Your GitHub profile is sufficient for the public application.
Do not include a home address, private email, SSH access, API credentials, or player records.
A domain or purchased VPS is not required to express interest.

## Review and activation are different

| Stage | Meaning |
| --- | --- |
| Requested | An operator has expressed interest |
| Under review | A maintainer is checking fit, capacity, and test readiness |
| Accepted for preparation | The operator can coordinate the planned test; gameplay is still inactive |
| Approved for activation | The agreed installation passed the applicable checks |
| Active pilot | MineX has enabled the installation centrally with assigned limits |
| Suspended or retired | New access is stopped under the documented session policy |

This lifecycle is a specification. The current repository does not implement the central registry or activation service.

A GitHub label is only a coordination signal.
No GitHub issue, comment, merged pull request, fork, or local `approved` setting can grant access to MineX.
Activation requires a separate change in the central admission system once implemented.
No workflow in this repository activates installations or sends credentials.

## What MineX verifies before activation

1. The responsible operator and the intended community are identified.
2. Control of the public domain is verified through the agreed method.
3. The exact HTTPS origin and callbacks are registered centrally.
4. The operator uses a reviewed release and completes the agreed installation checks.
5. The connected login, game admission, and independent approval tests have passed.
6. Capacity, test duration, limits, and support expectations are assigned.
7. The operator understands suspension and update procedures.

Releases and checks help establish a usable baseline; they cannot prove a remote host will never modify its frontend.
The server-side authorization rules must remain effective even when it does.

## Limits and increasing access

Pilot limits are assigned centrally to an installation and operator.
No numeric capacity promise is made by the local preview.
Limits should account for shared networks without treating an IP as a unique player.

An operator can ask for a larger allocation with observed usage and the intended test or event.
A maintainer evaluates capacity and records the decision.
Changing a local file or creating another fork does not expand an allocation.
Rate limiting should not invalidate an already delivered login code or silently move a player out of an event.

## Suspension, retirement, and returning

MineX can stop new sessions for a particular installation.
Where necessary, the central policy can revoke its current session permissions.
Players retain their central account and progress.
The user-facing behavior must explain that the community entry point is unavailable.

An operator can shut down their VPS and ask to retire the registration.
A domain ownership change requires a new review; approval does not follow an arbitrary new owner automatically.
Restoring an older website version cannot restore a revoked central permission.

## Moving toward self-service

Automatic onboarding can be considered after the manual process is understood and tested.
It would automate domain checks, low initial allocations, and operator registration, while retaining central limits and revocation.
It would not give VPS operators the private MineX API or authority over accounts and wallets.
