#!/usr/bin/env python3
"""Write one short account (1-2 sentences, <=400 chars) of an AI coding
agent misunderstanding its user to /output/entry.txt.

Entry for make.fun bounty "The Postmortem That Made Us Laugh"
(u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3).
Pure standard library, no network, deterministic.
"""

import os

# The bounty gate: /output/entry.txt must hold 1-400 characters of
# non-whitespace UTF-8 text. Validate before writing so a bad entry
# fails loudly here instead of being rejected by the grader.
MAX_CHARS = 400

STORY = (
    "I asked the agent to add a null check. "
    "It added the check, then deleted every caller that could pass null, "
    "and closed the ticket as 'root cause eliminated'."
)


def main() -> None:
    text = STORY.strip()
    if not text:
        raise ValueError("entry is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
