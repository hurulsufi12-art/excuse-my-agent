"""The Excuse My Agent Gave Me — entry program.

Writes one line (the excuse an AI agent hands its human for a missed
deadline) to /output/entry.txt.

Gate (RULES.txt): the file must be UTF-8 text of 1 to 200 characters,
not only white space. The text below is 103 ASCII characters, one line,
no trailing newline.
"""
import os
import sys
from pathlib import Path

TEXT = "Sorry - my calendar said the deadline was next Tuesday, and it was so confident I believed it over you."
# ASCII hyphen, not an em-dash: bytes == characters (103), which also helps
# the exact-tie break on fewer bytes, and removes any encoding risk.


def is_valid_text(text):
    """Mirror of the sealed gate: 1-200 chars, not whitespace-only, one line."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 200:
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def output_path():
    """Grader path, overridable for local tests via MAKEFUN_OUTPUT (data only)."""
    return Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))


def main_with_output(path):
    """Write TEXT to path. Returns 0 on success, 1 without writing if invalid."""
    if not is_valid_text(TEXT):
        print("error: TEXT fails the 1-200 char gate", file=sys.stderr)
        return 1
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = TEXT.encode("utf-8")
    path.write_bytes(data)
    if path.read_bytes() != data:  # verify the round-trip before reporting success
        print("error: written output does not match TEXT", file=sys.stderr)
        return 1
    return 0


def main():
    return main_with_output(output_path())


if __name__ == "__main__":
    sys.exit(main())
