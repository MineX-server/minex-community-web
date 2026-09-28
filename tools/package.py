#!/usr/bin/env python3
"""Create an archive containing only the reviewed public inventory."""
import argparse
from pathlib import Path
import tarfile

from check_public import ROOT, check, inventory


def public_metadata(info):
    info.uid = info.gid = 0
    info.uname = info.gname = ""
    info.mtime = 0
    info.mode = 0o644
    info.pax_headers = {}
    return info


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.is_relative_to(ROOT):
        parser.error("write the archive outside the public repository")
    errors = check(ROOT)
    if errors:
        raise SystemExit("Public checks failed:\n" + "\n".join(errors))
    if output.exists():
        parser.error("output already exists; choose a new path")
    with tarfile.open(output, "x:gz") as archive:
        for relative in sorted(inventory(ROOT)):
            archive.add(ROOT / relative, arcname="minex-community-web/" + relative,
                        recursive=False, filter=public_metadata)
    print(f"Created public-only archive: {output}")


if __name__ == "__main__":
    main()
