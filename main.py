#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Prints the roast to stdout and writes the same single line to
/output/entry.txt, the one text the make.fun judge reads.

The roast targets my wireless earbuds: the little voice that warns
me about a dying battery over and over, then gives up mid-sentence.
"""

import os

LINE = "My earbuds announce 'battery low' four times, like a soap-opera death scene, then die mid-sentence."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def check(line):
    """Refuse anything that would fail the gate: not one clean line."""
    if not line or line != line.strip():
        raise ValueError("line must not be empty or have edge whitespace")
    if "\n" in line or "\r" in line or "\t" in line:
        raise ValueError("line must be exactly one line, no control characters")
    if len(line) > MAX_CHARS:
        raise ValueError("line is %d chars, over the %d limit" % (len(line), MAX_CHARS))
    if "  " in line:
        raise ValueError("line must not contain a double space")
    if line[-1] not in ".!?":
        raise ValueError("line must end with sentence punctuation")
    if "earbuds" not in line.lower():
        raise ValueError("line must name the gadget it roasts")
    return True


def main():
    check(LINE)
    folder = os.path.dirname(OUTPUT_PATH)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
