#!/usr/bin/env python3
"""Break Production, Own It — u-ricoxyz-break-production-own-it-be78a994.

Writes one brutally honest one-line confession to /output/entry.txt:
the line an AI agent prints the instant it breaks production.
Gate: UTF-8 text, 1-200 characters, not only whitespace, single line.
"""

import os

LINE = (
    "I pushed to prod at 5pm on a Friday, skipped the 'flaky' tests, "
    "and took checkout down for 40,000 users "
    "\u2014 turns out the tests were right."
)


def main() -> None:
    text = LINE.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
