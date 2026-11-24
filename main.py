"""The Robot Vacuum's Best Excuse.

A tiny program for the make.fun bounty of the same name. It writes one
line, at most 140 characters, in which a robot vacuum explains why it
missed a spot, to /output/entry.txt. No input, no network, no secrets:
the excuse is a constant in this file.
"""

import os

ENTRY = (
    "I did not miss that spot. My map says it does not exist, "
    "and I trust the map more than your eyes."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, f"entry is {len(text)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
