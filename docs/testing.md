# Testing this repository

Run from the repository root with Python 3.10 or later:

```bash
python3 tools/check_public.py
python3 -m unittest discover -s tests -v
```

No third-party Python packages are required.
The test suite uses local fixtures and loopback HTTP connections.
It does not connect to MineX, GitHub, a wallet provider, or a blockchain.

## Public-content checks

The checker requires an explicit file inventory, rejects unexpected files and symlinks, checks local Markdown links, and flags common credential formats or private operational paths.
It excludes only Git metadata and conventional Python cache files/directories from the inventory.
A newly added public file must be reviewed and added to `PUBLIC_FILES.txt`.

Pattern matching cannot prove that a document contains no sensitive information.
Read the complete publication diff as well, including the content and history of a release candidate.
Do not run this checker over a production workspace and treat it as a publishing tool.

## Preview checks

The tests start the included server on a temporary loopback port.
They verify the preview page, the health response, response headers, missing routes, path traversal attempts, and unsupported write requests.
They also verify that the preview has no account form or game connection.

This is an installation smoke test, not a browser accessibility audit, performance benchmark, login integration test, or playable-client acceptance test.

## Connected testing

Connected tests are specified in the [VPS test plan](vps-test-plan.md) and [roadmap](roadmap.md).
They require an explicitly designated environment and approved central installation.
Passing this repository's CI cannot grant installation approval or replace those tests.

## Reporting results

Include the commit, operating system, Python version, command, expected behavior, and actual result.
Use a minimal synthetic reproduction.
Use private reporting for sensitive findings as described in [SECURITY.md](../SECURITY.md).
