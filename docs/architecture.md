# Architecture and trust boundaries

This is the target architecture for a future connected release.
The current package only runs a local installation preview.

## Shared service, community hosting

The community hosts a website and, once distribution is approved, the game client artifacts.
The browser connects to the shared MineX game service.
World simulation, account records, character state, and permissions stay central.
The VPS does not receive an independent game server or a copy of the account database.

The browser should connect directly to the published central game endpoint.
A community VPS does not need to relay every game packet merely because it serves the frontend.
Any future relay requires an explicit transport design and does not gain authority to identify players or approve operations.

## Separate three permissions

| Permission | Authority | What the community receives |
| --- | --- | --- |
| Account access | Official MineX account service | A limited result from the approved sign-in flow |
| Game connection | Central admission service | A short-lived permission scoped to the installation and game session |
| Sensitive operation approval | Official authorization service and applicable wallet authorization | A minimal status result |

The exact public protocol and endpoints will be documented with the implementation.
This document does not advertise a callable community API that already exists.

## Player journey

The player starts on a community website and enters account credentials only on an official account origin.
After sign-in, the browser returns through a registered callback for that community.
The callback and installation identity are checked centrally.
The browser receives limited game access, not an official account session that the community can reuse elsewhere.

A sensitive action opens an official approval page in a separate top-level browser context.
That page shows the operation details obtained from MineX.
The execution service must verify authorization for the exact operation before producing effects.
An installation credential, game session, IP address, or copied public request identifier is insufficient.

## Assume the frontend can be replaced

The operator can change HTML, scripts, styles, and client files.
They can see data delivered to their application and can display misleading interfaces.
Client minification, obfuscation, a manifest hash supplied by that client, and an approved domain do not make the operator trustworthy.

The protocol must limit the authority exposed to that application.
Private wallet implementation and service credentials are never part of the distribution.
The official approval remains independent of the community's visible confirmation button.
Account and approval pages remain necessary even if the official playable website is retired.

## Admission and operation

During the pilot, MineX reviews each operator and installation before activation.
Registered domains and installation identities are managed by the central service.
Any central credential is restricted to its stated installation capability; it does not grant general account creation or financial API access.
Limits are applied centrally and may combine installation, operator, destination, and global budgets.
Changing local configuration does not increase those limits.

Suspension can prevent new connections and, according to the selected policy, end active sessions.
Suspending an installation does not delete players' accounts or alter ownership of their wallets.
Closing a website cannot erase copies of an openly distributed package.

## Event continuity

An event session must not silently move to another game mode after a timeout.
The player should see a clear reconnect or exit choice that preserves the intended event destination.
Failures of account or approval services should not create a misleading successful game connection.

## Distribution boundary

Only original documentation, the preview, and tools are licensed in this initial release.
Playable client artifacts, dependencies, attribution, and redistribution conditions need a separate inventory before packaging.
Public code can be reused under its license; access to MineX remains a separate service decision.
