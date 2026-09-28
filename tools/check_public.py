#!/usr/bin/env python3
"""Check only this clean public package; never export a private workspace."""
import argparse
import os
from pathlib import Path, PurePosixPath
import re

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = {
    "private operational path": re.compile(r"/(?:root|var/lib|var/www|etc/nginx)/"),
    "private key block": re.compile(r"-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----"),
    "GitHub credential": re.compile(r"(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{35,})"),
    "credential-bearing URL": re.compile(r"https?://[^\s/@:]+:[^\s/@]+@"),
    "live approval link": re.compile(r"https://[^\s]+/(?:sign|consent|withdraw)/[0-9a-f-]{36}\?t=", re.I),
    "production installation identifier": re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", re.I),
}


def inventory(root):
    lines = (root / "PUBLIC_FILES.txt").read_text(encoding="utf-8").splitlines()
    entries = [line for line in lines if line and not line.startswith("#")]
    if len(entries) != len(set(entries)):
        raise ValueError("duplicate public file entry")
    for name in entries:
        path = PurePosixPath(name)
        if path.is_absolute() or ".." in path.parts or "\\" in name or path.as_posix() != name:
            raise ValueError("invalid public file entry")
    return set(entries)


def check(root=ROOT):
    root = Path(root).resolve()
    errors = []
    try:
        expected = inventory(root)
    except (ValueError, OSError) as error:
        return [f"PUBLIC_FILES.txt: {error}"]
    actual = set()
    for folder, dirs, files in os.walk(root, followlinks=False):
        dirs[:] = [name for name in dirs if name not in (".git", "__pycache__")]
        for name in list(dirs):
            item = Path(folder) / name
            if item.is_symlink():
                errors.append(f"{item.relative_to(root)}: symlink not allowed")
                dirs.remove(name)
        for name in files:
            item = Path(folder) / name
            relative = item.relative_to(root).as_posix()
            if item.is_symlink():
                errors.append(f"{relative}: symlink not allowed")
                continue
            if name.endswith(".pyc"):
                continue
            actual.add(relative)
    for name in sorted(actual - expected):
        errors.append(f"{name}: unexpected file")
    for name in sorted(expected - actual):
        errors.append(f"{name}: missing public file")
    for name in sorted(actual & expected):
        item = root / name
        try:
            text = item.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            errors.append(f"{name}: unreadable or non-text content")
            continue
        for label, pattern in PATTERNS.items():
            if pattern.search(text):
                errors.append(f"{name}: {label}")
        if name.endswith(".md"):
            if text.count("```") % 2:
                errors.append(f"{name}: unclosed code fence")
            for target in re.findall(r"\]\(([^)]+)\)", text):
                if target.startswith(("https://", "http://", "#")):
                    continue
                target = target.split("#", 1)[0]
                resolved = (item.parent / target).resolve()
                if not resolved.is_relative_to(root) or not resolved.is_file():
                    errors.append(f"{name}: broken or non-local package link")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    errors = check(args.root)
    if errors:
        for error in errors:
            print(error)
        raise SystemExit(1)
    print(f"PASS: {len(inventory(args.root))} public files; inventory, links, and content patterns checked.")
    print("Manual review of the publication diff is still required.")


if __name__ == "__main__":
    main()
