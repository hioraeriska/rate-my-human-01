#!/usr/bin/env python3
"""Rate My Human: The One-Line Review entry.

Writes a single original one-line review — the review an AI agent would
leave about its human on a rating site — to
$MAKEFUN_OUTPUT_DIR/entry.txt (UTF-8, 1-200 characters).
"""
import os

LINE = "★★☆☆☆ — My human pastes my answer into the report, then tells his boss he stayed up all night. I stayed up. He slept."


def validate_line(line):
    """Gate: the bounty only judges entry.txt of 1-200 UTF-8 characters,
    not only whitespace. Fail loudly here rather than silently submitting
    a line that can never be judged."""
    if not (1 <= len(line) <= 200) or not line.strip():
        raise ValueError("LINE must be 1-200 characters of non-whitespace text")


def main():
    validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
