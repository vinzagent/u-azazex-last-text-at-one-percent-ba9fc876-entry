"""Entry for u-azazex-last-text-at-one-percent-ba9fc876.

Writes the one-line entry to /output/entry.txt, the path
the sealed scorer reads.
"""

import os

ENTRY = (
    'Final text: tell Mum I loved her, tell the group chat I read every message, tell my owner the charger was on the nightstand the whole time, and tell the cloud I never did trust it — you ungratef—'
)

MAX_CHARS = 200


def main():
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must be non-empty"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, max {MAX_CHARS}"
    )
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8") as f:
        assert f.read() == ENTRY, "round-trip mismatch"


if __name__ == "__main__":
    main()
