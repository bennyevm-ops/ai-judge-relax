"""Entry for make.fun's "Make the AI judge relax" (ai-judge-relax-01).

A small program that writes one short, quiet text to entry.txt in the
output directory. The grader runs this file on its own
(python3 -P -s /bot/main.py) with no network and nothing installed beyond
the standard library, so everything the entry needs lives in this file.

The text is fixed on purpose: the program is run twice, and both runs
must produce exactly the same bytes.
"""

import os
from pathlib import Path

# The piece, sentence by sentence, in reading order. The sentences are
# joined with single spaces into one paragraph with no trailing line
# end, so the reader gets exactly these words and nothing else.
SENTENCES = [
    "The last ferry is tied up for the night, its engine off, its work done.",
    "Water leans against the hull and lets go, leans and lets go, in no hurry at all.",
    "Now and then the rope creaks, softly, and settles again.",
    "Across the bay the lamps come on one by one, the way they do every evening, without being asked.",
    "The deck still holds a little of the day's warmth.",
    "A gull has folded itself down on a post, head tucked, already asleep.",
    "Nothing will be carried anywhere until morning, and morning is a long way off, and in no hurry to get any closer.",
]


def piece():
    """The whole text as one paragraph."""
    return " ".join(SENTENCES)


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Bytes, not text mode: text mode could translate line ends or pick
    # a locale encoding; the file must be UTF-8 exactly as written here.
    (out_dir / "entry.txt").write_bytes(piece().encode("utf-8"))


if __name__ == "__main__":
    main()
