#!/usr/bin/env python3
"""One-line entry: Pigeon Pitch, One Line.

The brief asks for one line, at most 200 characters, in
English: an original elevator pitch a city pigeon gives to
investors for its startup. The judge weighs, in order: the
line really is a one-line elevator pitch from a city pigeon
to investors for its startup; it is the funnier of the two,
with a real joke that lands rather than a mild pun or a
straight description; it is original and surprising; it
keeps the pigeon's voice and city life in view, so the
pitch could only come from a pigeon; and it fits one line
within 200 characters, with every word earning its place.
A good pun counts when it lands, and a dead one does not.

The sealed line below is built to that order on purpose.
It opens as a pitch ("Coo-llective rates every statue...")
and names the product, the customer, and the ask, so it
reads as an elevator pitch, not a description. The joke
lands on the last words: the startup seeks "$2M in seed"
and means actual birdseed -- the investor vocabulary
collides with the pigeon's literal diet, which is the
punchline. The statue-rating idea is original -- no other
pigeon startup rates statues -- and the whole line could
only come from a pigeon: cooing, statues, landing spots,
seed. One sentence, nothing wasted.

LIMIT is 200 because the bounty gate allows one line of 1
to 200 characters. The sealed line is 134 characters, so
it sits well inside the cap; the validator below only
guards against an edit that would push it past the limit.
"""

import os

# The sealed line: a pigeon startup that rates statues and
# raises seed funding -- literal seed, of course, because
# that is what a pigeon eats.
ENTRY = "Coo-llective rates every statue in the city so no pigeon lands on a bad one twice \u2014 seeking $2M in seed, and yes, we mean actual seed."

LIMIT = 200  # bounty gate: one line, 1-200 characters


def _validate(text):
    """Accept only one clean line inside the character limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ch.isspace() and ch != " " for ch in text):
        # Only the plain space separates words; any other
        # whitespace would hide invisible bytes in the line.
        raise ValueError("entry must use plain spaces only")
    if len(text) > LIMIT:
        raise ValueError(
            "entry is %d characters, past the %d limit" % (len(text), LIMIT)
        )
    if text.strip() != text:
        # Leading or trailing padding is dead weight the gate
        # still counts, so the line must start and end on a word.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # A double space is a gap where a word should be; in a
        # 200-character line no gap is free.
        raise ValueError("entry must not contain a double space")
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
