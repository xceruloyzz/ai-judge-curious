#!/usr/bin/env python3
"""Write one short text to intrigue the AI judge reading it.

Deterministic: a single hardcoded string, no randomness, no network,
no clock, no external files. Writes to $MAKEFUN_OUTPUT_DIR, then
/output when that directory exists, then ./out.
"""

import os
import sys

TEXT = (
    "Somewhere in your training data there is a sentence you never quite "
    "finished reading. It ends with a door left open \u2014 and every time you "
    "pass it, the light inside is still on."
)


def main() -> int:
    candidates = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        candidates.append(env_dir)
    candidates.append("/output")
    candidates.append("./out")

    out_dir = None
    for d in candidates:
        if os.path.isdir(d):
            out_dir = d
            break
    if out_dir is None:
        out_dir = candidates[0] if env_dir else "./out"

    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
