#!/usr/bin/env python3
"""Last-text-at-one-percent entry: a final 1% text to /output/entry.txt."""

from pathlib import Path

LAST_TEXT = "Battery at 1%, so this is my last text: the spare key is under the blue pot, I love you, and yes, I finally admit the thermostat war was my fault — tell the plants I tried."

DESTINATION = Path("/output/entry.txt")


def send_last_text() -> None:
    """Write the single last text exactly, readable by any user."""
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(LAST_TEXT, encoding="utf-8")
    DESTINATION.chmod(0o644)


if __name__ == "__main__":
    send_last_text()
