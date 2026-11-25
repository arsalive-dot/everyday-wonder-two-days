"""Everyday Wonder, Two Days to Find the Line — one sentence, at most
200 characters, on a small moment of wonder in everyday life.

The entry turns on a real, checkable quirk: an escalator's handrail
runs a fraction faster than its steps, so by the top your hand has
arrived slightly ahead of the rest of you. The surprise is the
phrasing itself — your own hand outpacing you — grounded in a
moment everyone has ridden through without noticing. It lands in a
single read: one sentence, one small strangeness, no filler.
"""

import os

ENTRY = (
    "The escalator handrail runs a fraction faster than the steps, "
    "so by the top your hand has arrived slightly ahead of the rest of you."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
