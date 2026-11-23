import os
from pathlib import Path
import sys


TEXT = "The 3am page went to my agent, not to me; by morning the incident was a one-paragraph note and the phone was still face down."


def main():
    text = TEXT
    assert 1 <= len(text) <= 280
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", os.environ.get("OUTPUT_DIR", "/output")))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(text.encode("utf-8"))
    print(len(text), file=sys.stderr)


if __name__ == "__main__":
    main()
