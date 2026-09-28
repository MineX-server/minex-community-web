# VPS test plan

Start without buying a machine. The included preview is enough to check the first installation step locally.
An external VPS is useful later to test a clean environment, independent networking, a public domain, and the connected flow.

## Phase A: local preview

Requirements: Python 3.10 or later, a terminal, and a browser.
No game client, account service, credentials, database, or blockchain connection is used.

From the repository folder:

```bash
python3 tools/check_public.py
python3 -m unittest discover -s tests -v
python3 tools/preview.py --port 8787
```

Open `http://127.0.0.1:8787`.
The server binds to loopback only and serves an explicit small set of routes.
It does not serve the repository directory or accept sign-in data.
Stop it with `Ctrl+C` when finished.

Record the OS, Python version, test outcome, and whether the page renders correctly.
Do not describe this result as a successful MineX game connection.

## Phase B: clean external machine

Use an existing spare Linux VPS if one is available.
For the preview alone, 1 vCPU, 1 GB RAM, and 10 GB disk are an initial test baseline, not a capacity estimate for the future client distribution or MineX servers.
The external test does not require a blockchain node, game server, wallet backend, or player database.
Choose a machine that can be recreated without affecting another service.
Provider pricing and availability should be compared when a machine is actually needed; this plan makes no purchase or cost commitment.

Access preparation:

1. Use an SSH account created for this test and an SSH public key.
2. Arrange access through a private channel; never put access credentials in a GitHub issue.
3. Transfer only this public repository to the machine.
4. Install or verify Python 3.10 or later through the OS package manager.
5. Run the same checks and preview command as in Phase A.

For this preview, keep the service on loopback and use an SSH tunnel from your computer:

```bash
ssh -L 8787:127.0.0.1:8787 operator@YOUR_TEST_VPS
```

With the preview running on the VPS, open `http://127.0.0.1:8787` on your computer.
`YOUR_TEST_VPS` is a placeholder, not a deployed endpoint.
This validates access through SSH, not public HTTPS or community admission.

## Phase C: public HTTPS rehearsal

This is a later deployment step, not performed automatically by the preview.

- Use an operator-controlled test subdomain.
- Terminate HTTPS with a reviewed web server configuration.
- Keep the application listener private behind the web server.
- Verify DNS, certificate renewal, headers, caching, and a restart of the machine.
- Confirm that no private files or application credentials are being served.
- Test a controlled shutdown and restore of the website.

A simple installation preview should still collect no account credentials and should make its non-playable status clear.
Do not present a future login button as functional before the official handoff exists.

## Phase D: approved connected pilot

This phase waits for the central account/admission implementation, independent approvals, and reviewed playable artifacts.

| Test | Required observation |
| --- | --- |
| Fresh installation | The public package and operator instructions are sufficient |
| Official sign-in | Account input occurs on the official origin |
| Community admission | Only the centrally activated installation gains the scoped access |
| Two entry points | A community player and an existing MineX player share the intended world |
| Existing identity | The player retains the same account and character |
| Sensitive operation | It cannot execute from frontend-declared approval alone |
| Network change | A changed IP does not create another identity |
| Event timeout | The user is not silently sent into a different game mode |
| Installation suspension | New access stops according to central policy |
| Version rollback | Website rollback preserves central state and revocations |
| Quota reached | A clear error appears without disrupting unrelated active players |

Start with an agreed small group and duration.
Keep capacity observations separate from guesses about how many players a VPS can handle.
The host serves client files; game-server capacity remains a separate central concern.

## Teardown

Stop the preview or test service and close any SSH tunnels.
Retire the central registration if one was created for a connected test.
Remove the test SSH access when it is no longer needed.
Delete the VPS only when its owner confirms it has no other purpose.
Keep a sanitized test summary with versions and results, excluding credentials and player records.
