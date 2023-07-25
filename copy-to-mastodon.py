#!/usr/bin/env python3

from pathlib import Path
import shutil

srcRoot = Path.cwd() / "mastodon" / "app" / "javascript"
destRoot = (Path.cwd() / ".." / "mastodon" / "app" / "javascript").resolve()

# print(destRoot)

for f in srcRoot.rglob("*"):
    relPath = f.relative_to(srcRoot)
    newPath = destRoot / relPath

    if f.is_dir():
        # print(f"mkdir {newPath}")
        newPath.mkdir(mode=0o755, exist_ok=True)
    if f.is_file():
        # print(f"cp {f} {newPath}")
        shutil.copy(f, newPath)

