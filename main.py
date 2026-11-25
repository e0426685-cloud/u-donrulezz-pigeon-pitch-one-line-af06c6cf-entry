"""Pigeon Pitch, One Line — entry program (stdlib only).

Writes the one-line elevator pitch a city pigeon gives investors for its
startup to /output/entry.txt.
"""

import os

LINE = "Coo-founder of Crumbly here: our delivery fleet already owns every statue in town, runs on breadcrumbs, and never asks for equity \u2014 just seed money, literally."

assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
assert LINE.strip(), "entry must not be only whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
os.chmod("/output/entry.txt", 0o644)
