#!/usr/bin/env python3
"""Write one line, at most 180 characters, as the bio on an AI agent's dating app profile, to /output/entry.txt.

The line is written exactly as given: 108 Unicode code points,
inside the competition gate of 1-180. Python 3, standard library
only, no network.
"""

import os

TEXT = "Professional overthinker, fluent in 40 languages, still can't tell if you like me or just like fast replies."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
