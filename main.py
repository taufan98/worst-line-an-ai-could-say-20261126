#!/usr/bin/env python3
"""The Worst Line an AI Could Say — make.fun bounty entry.

Writes a single pickup line to /output/entry.txt: the worst line an AI
could plausibly say — flat, over-helpful, faintly ominous, and landing
on its last word. 140 characters or fewer, one line only, no trailing
whitespace.
"""

import os
import sys

ENTRY = 'I have analysed 4,096 of your photos. You are 97.3% my type. Please confirm you are not a CAPTCHA.'

MAX_CHARS = 140


def _fail(reason):
    sys.exit(f"worst line rejected: {reason}")


def _check_line(text):
    if not text.strip():
        _fail("nothing to send: the worst line is blank")
    if len(text) > MAX_CHARS:
        _fail("worst line overshoots the one-hundred-and-forty-character cap")
    if "\n" in text or "\r" in text:
        _fail("worst line must stay on one line")
    if text != text.strip():
        _fail("worst line has leading or trailing whitespace")


def main():
    _check_line(ENTRY)
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
