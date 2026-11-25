"""Pigeon Pitch, One Line — entry program (stdlib only).

Writes the one-line elevator pitch a city pigeon gives investors for its
startup to /output/entry.txt.
"""

import os

MAX_LEN = 200
OUTPUT_PATH = "/output/entry.txt"

LINE = "Coo-founder of Crumbly here: our delivery fleet already owns every statue in town, runs on breadcrumbs, and never asks for equity \u2014 just seed money, literally."


def validate(line):
    """Return True only if the line is a valid one-line entry."""
    if not isinstance(line, str):
        return False
    if not 1 <= len(line) <= MAX_LEN:
        return False
    if "\n" in line or "\r" in line:
        return False
    return bool(line.strip())


def main():
    if not validate(LINE):
        raise SystemExit("invalid entry line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        if f.read() != LINE:
            raise SystemExit("written entry does not match the pitch")


if __name__ == "__main__":
    main()
