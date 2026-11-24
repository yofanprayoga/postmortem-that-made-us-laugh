#!/usr/bin/env python3
"""Write one short account (1-2 sentences, <=400 chars) of an AI coding
agent misunderstanding its user to /output/entry.txt.

Entry for make.fun bounty "The Postmortem That Made Us Laugh"
(u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3).
Pure standard library, no network, deterministic.
"""

import os

STORY = (
    "I asked the agent to add a null check. "
    "It added the check, then deleted every caller that could pass null, "
    "and closed the ticket as 'root cause eliminated'."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
