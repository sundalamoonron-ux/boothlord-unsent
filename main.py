#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — writes one two-part micro-confession
to /output/entry.txt.

Winner of the pairwise tournament (see candidates.md and judge_results.md):
C7, 6 wins 0 losses. Three R1 games were real verdicts from z-ai/glm-5.3-flash
(the house judge model); the rest was a manual audit after the CanTrustAI
balance hit 402, applying the house brief's criterion order by hand.

Why C7 wins: the reason it stayed in drafts is "too late" in the most final
sense — he is gone, so the message literally cannot be sent any more — and
the detail (calling his number just to hear it ring once) is specific,
honest, and only makes sense addressed to Dad. No dependencies, no network.
"""

import os

ENTRY = (
    "To: Dad\n"
    "i kept your voicemails and i still call your number just to hear it ring once before it goes quiet"
)


def validate(entry: str) -> bool:
    """Gate: /output/entry.txt must be UTF-8 text of 1 to 260 characters,
    not only whitespace; exactly two parts (a To: line and one message line
    of at most 200 characters, written exactly as typed)."""
    if not isinstance(entry, str):
        return False
    if not 1 <= len(entry) <= 260:
        return False
    if not entry.strip():
        return False
    lines = entry.split("\n")
    if len(lines) != 2:
        return False
    if not lines[0].startswith("To: ") or not lines[0][4:].strip():
        return False
    if not 1 <= len(lines[1]) <= 200 or not lines[1].strip():
        return False
    entry.encode("utf-8")  # raises if not valid UTF-8-encodable
    return True


def main() -> None:
    if not validate(ENTRY):
        raise ValueError(f"entry violates gate: {len(ENTRY)} chars")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Re-read and re-validate exactly what landed on disk.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY or not validate(written):
        raise ValueError("written entry failed re-validation")
    print(f"wrote {path} ({len(written)} chars)")


if __name__ == "__main__":
    main()
