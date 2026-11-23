"""Six Words, One Story - make.fun entry.

Writes one complete story in exactly six words to /output/entry.txt.
Standard library only; no network, no secrets, no input read.
"""

import os

STORY = "She left the light on. Forever."


def main() -> None:
    words = STORY.split()
    if len(words) != 6:
        raise ValueError(f"story must be exactly six words, got {len(words)}")
    if not 1 <= len(STORY) <= 60:
        raise ValueError("story must be 1-60 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
