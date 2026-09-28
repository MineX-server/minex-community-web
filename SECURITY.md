# Security reporting and scope

The supported content in this initial release is the documentation, local preview, and repository tools.
The connected community client and central admission integration are not released here.

## Report privately

Use **Security → Report a vulnerability** on the canonical GitHub repository when private vulnerability reporting is enabled.
If that option is unavailable, open a minimal issue asking a maintainer to arrange a private reporting channel. Do not include the finding or sensitive material in that public issue.

Do not post credentials, account records, live approval links, wallet recovery material, or operational logs containing user data.
Use synthetic data when describing reproduction steps privately.

## Authorization boundaries

Publishing this repository does not authorize testing the production MineX service, another operator's VPS, or other players' accounts.
Use the included local preview and an explicitly agreed test environment.
Requests for connected pilot testing are coordinated through [the pilot process](docs/pilot.md).

The project is designed around a frontend that its operator can modify.
Sensitive operations must be authorized by official services; IP claims and local frontend checks do not establish player consent.
No claim of a complete security audit or zero-risk operation is made by this preview release.

## Maintainer setup

Enable GitHub private vulnerability reporting before inviting public testers.
Keep private incident evidence outside the public repository and its Git history.
Publish a coordinated, sanitized advisory when an issue is ready for disclosure.
