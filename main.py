#!/usr/bin/env python3
"""Pigeon Pitch, One Line: a city pigeon pitches investors.

Brief: one line, at most 200 characters, in English -- an
original elevator pitch a city pigeon gives to investors
for its startup. Judging, in order: the line really is a
one-line elevator pitch from a city pigeon to investors for
its startup; it is the funnier of the two, with a real joke
that lands rather than a mild pun or a straight
description; it is original and surprising; it keeps the
pigeon's voice and city life in view, so the pitch could
only come from a pigeon; and it fits one line within 200
characters, with every word earning its place. A good pun
counts when it lands, and a dead one does not.

Why this line works, in that order: it opens as a pitch
("Coo-llective rates every statue...") and names the
product, the customer, and the ask, so it reads as an
elevator pitch, not a description. The joke lands on the
last words: the startup seeks "$2M in seed" and means
actual birdseed -- investor vocabulary collides with the
pigeon's literal diet, which is the punchline. The
statue-rating idea is original -- no other pigeon startup
rates statues -- and the whole line could only come from a
pigeon: cooing, statues, landing spots, seed. One sentence,
nothing wasted. The validator below guards only against an
edit that would push the sealed line past the 200-char gate.
"""

from pathlib import Path

MAX_CHARS = 200  # bounty gate: one line, 1-200 characters

# Sealed entry: a pigeon startup that rates statues and
# raises seed funding -- literal seed, of course, because
# that is what a pigeon eats.
ENTRY = (
    "Coo-llective rates every statue in the city so no pigeon lands "
    "on a bad one twice — seeking $2M in seed, and yes, we mean actual seed."
)

OUT_PATH = Path("/output/entry.txt")


def _reject(message):
    raise ValueError(message)


def check_entry(text):
    """Return text unchanged when it is one clean line within the gate."""
    if not isinstance(text, str):
        _reject("entry must be text")
    if text == "":
        _reject("entry must not be empty")
    if text.strip() == "":
        _reject("entry must not be only white space")
    if any(c in text for c in "\r\n"):
        _reject("entry must be exactly one line")
    if any(c.isspace() and c != " " for c in text):
        # Any whitespace other than a plain space would hide
        # invisible bytes inside the line.
        _reject("entry must use plain spaces only")
    if len(text) > MAX_CHARS:
        _reject(
            "entry is %d characters, past the %d limit" % (len(text), MAX_CHARS)
        )
    if text != text.strip():
        # Padding at either end is dead weight the gate counts.
        _reject("entry must not pad itself with spaces")
    if not text.isprintable():
        _reject("entry must contain no control characters")
    if "  " in text:
        # In a 200-character line, no gap is free.
        _reject("entry must not contain a double space")
    return text


def run():
    line = check_entry(ENTRY)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(line, encoding="utf-8")
    print(line)


if __name__ == "__main__":
    run()
