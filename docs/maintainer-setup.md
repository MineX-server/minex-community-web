# Maintainer setup and publication

This file records the repository setup to perform on GitHub. A file in this repository cannot enforce a branch rule or central installation policy by itself.

## Publish the reviewed content

1. Create a new repository from this clean public package.
2. Review its complete file inventory and diff before the initial push.
3. Do not import a production repository's history, internal plans, logs, reports, or private source snapshots.
4. Run the included checks and tests.
5. Use the English README as the landing page and keep the Spanish introduction linked.
6. Keep the current release status explicit: documentation and installation preview, with connected gameplay planned.

Suggested repository name: `minex-community-web`.
Suggested description: `Community-hosted web access to the shared MineX service — public design, local preview, and a manually approved pilot plan.`

The initial license applies only to the original material in this public package.
Any future addition of a third-party client or asset requires its own distribution review and notices.

## Require maintainer review

Configure a branch rule or ruleset for the default branch:

- Require pull requests before changes are merged.
- Require one approving review once a second trusted reviewer is available.
- Require the `Public package checks` check to pass.
- Dismiss stale approvals after relevant changes.
- Block force pushes and branch deletion.
- Keep any administrator bypass narrow and explicit.

A sole maintainer cannot approve their own pull request as a second reviewer. Until another reviewer is available, document that limitation rather than pretending independent approval has occurred.
Do not claim these settings are active until they have been applied and verified in GitHub.

## Enable useful repository features

- Enable Issues for pilot requests, preview problems, and public design feedback.
- Enable private vulnerability reporting before inviting testers.
- Enable secret scanning and push protection where available for the repository.
- Keep Actions permissions read-only for this documentation and preview workflow.
- Do not add production deployment or service credentials to this initial repository's workflows.
- Leave automatic merge and automatic installation activation disabled.

The workflow runs on `push`, `pull_request`, and manual dispatch. It uses no production secrets or deployment permissions.
Do not change it to a privileged workflow that runs untrusted pull-request code with service credentials.

## Manual operator approval

Use issues to coordinate the stages in [pilot.md](pilot.md).
An accepted application is not a central access grant.
When the connected system exists, activation must be performed through its separate registry after the installation checks pass.
No action in this initial repository can issue account, game, or financial credentials.

## First release

Describe the release as `public planning and installation preview`.
Do not use a release title that implies the connected client is complete.
Record the checks actually run and their environment.
Do not attach internal audit reports as public release evidence.

## Authoritative references

- [GitHub: protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- [GitHub: repository creation](https://docs.github.com/en/rest/repos/repos#create-a-repository-for-the-authenticated-user).
