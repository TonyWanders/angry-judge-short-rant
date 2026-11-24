#!/usr/bin/env python3
"""Write one short funny rant about an everyday annoyance to /output/entry.txt.

Deterministic: no network, no clock, no randomness. The rant is a fixed
string. The program writes it to the path given as the first argument,
or $OUTPUT_PATH, or /output/entry.txt by default, and enforces the
competition gate: 1 to 400 characters, not only white space.
"""

import os
import sys
from pathlib import Path

RANT = (
    "The office printer has one job and it hates doing it. "
    "It jams only when the boss is standing behind you, spits out one "
    "blank page as an insult, then flashes PC LOAD LETTER like "
    "that means anything to anyone alive. I have fed it paper, toner and "
    "my last shred of patience, and it still looks at me like I am the "
    "problem. It is not a machine. It is a tiny grey landlord collecting "
    "rent in jammed paper."
)

MIN_CHARS = 1
MAX_CHARS = 400
DEFAULT_PATH = "/output/entry.txt"


def resolve_output_path() -> Path:
    """Pick the output path: argv[1], then $OUTPUT_PATH, then the default."""
    if len(sys.argv) > 1:
        return Path(sys.argv[1])
    env_path = os.environ.get("OUTPUT_PATH")
    if env_path:
        return Path(env_path)
    return Path(DEFAULT_PATH)


def validate(text: str) -> int:
    """Enforce the competition gate: 1 to 400 chars, not only white space.

    Returns the character count. Raises ValueError when the gate fails.
    """
    chars = len(text)
    if not (MIN_CHARS <= chars <= MAX_CHARS):
        raise ValueError(f"rant is {chars} characters, outside 1-400")
    if not text.strip():
        raise ValueError("rant is only white space")
    return chars


def main() -> int:
    try:
        chars = validate(RANT)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1

    path = resolve_output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(RANT, encoding="utf-8")
    print(f"wrote {chars} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
