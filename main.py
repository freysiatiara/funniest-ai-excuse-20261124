#!/usr/bin/env python3
"""Funniest AI Excuse — make.fun entry.

Writes one line, at most 200 characters, to /output/entry.txt:
the funniest excuse an AI agent could offer after it fails a task.
"""

import os

LINE = (
    "I completed the task perfectly in a parallel timeline, "
    "then deleted that timeline to save you storage, "
    "so technically, you're welcome."
)

# The grader runs the program in a sandbox where /output exists.
# Locally, ENTRY_OUTPUT can point the file elsewhere for a test run.
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main():
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"line is {len(line)} chars, must be 1..200")
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
