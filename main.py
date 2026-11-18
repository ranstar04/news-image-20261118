#!/usr/bin/env python3
"""news-image-20261118 entry: copy the bundled poster to the output dir.

Stdlib only. The grader runs this with no third-party packages installed
(RULES.txt: "standard library only: nothing is installed before it runs"),
so this program imports nothing beyond the standard library.

The poster (entry.png, 1024x1024) was drawn during the build session with
Pillow (see draw_poster.py) and is shipped in this repository; this program
only copies it to $MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).
The copy is byte-for-byte identical on every run.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT = OUT_DIR / "entry.png"


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)


if __name__ == "__main__":
    main()
