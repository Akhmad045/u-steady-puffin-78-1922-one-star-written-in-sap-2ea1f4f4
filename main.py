#!/usr/bin/env python3
"""One Star, Written in Sap.

Writes one one-star review, in the voice of a houseplant reviewing its
human owner, to /output/entry.txt (the program/v1 artifact this
competition's gate scores) and prints it.

The review: a fern, a spray bottle, and a motivational speech.
"""

import sys
from pathlib import Path

REVIEW = (
    "One star. I asked for water. He gave me a spray bottle, two "
    "squirts, and a motivational speech about resilience. I am a fern, "
    "not a boot camp."
)

OUTPUT_PATH = Path("/output/entry.txt")


def validate(text: str) -> None:
    """Enforce the competition gate: UTF-8 text of 1 to 279 characters,
    not only whitespace, a single line with no leading or trailing
    whitespace and no control characters."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= 279:
        raise ValueError(f"entry is {len(text)} characters, gate is 1-279")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry must not contain control characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line, no line breaks")
    text.encode("utf-8")  # raises if not encodable


def write_entry(path: Path = OUTPUT_PATH) -> str:
    validate(REVIEW)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(REVIEW, encoding="utf-8")
    return REVIEW


def self_test() -> int:
    """Check the gate against the entry and its boundary cases."""
    failures = []

    def check(name: str, ok: bool) -> None:
        print(f"{'PASS' if ok else 'FAIL'}: {name}")
        if not ok:
            failures.append(name)

    try:
        validate(REVIEW)
        check("entry itself passes the gate", True)
    except ValueError as exc:
        check(f"entry itself passes the gate ({exc})", False)

    for name, text, should_pass in [
        ("empty entry rejected", "", False),
        ("whitespace-only rejected", "   ", False),
        ("280 chars rejected (gate is 279, not 280)", "x" * 280, False),
        ("279 chars accepted", "x" * 279, True),
        ("1 char accepted", "x", True),
        ("leading whitespace rejected", " review", False),
        ("trailing whitespace rejected", "review ", False),
        ("newline rejected", "a\nb", False),
        ("carriage return rejected", "a\rb", False),
        ("control character rejected", "a\x01b", False),
    ]:
        try:
            validate(text)
            check(name, should_pass)
        except ValueError:
            check(name, not should_pass)

    # Round trip: the file the program writes must be byte-identical
    # to the entry it prints.
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        probe = Path(tmp) / "entry.txt"
        write_entry(probe)
        check(
            "written file matches the entry exactly",
            probe.read_text(encoding="utf-8") == REVIEW,
        )
        check(
            "written file is 1-279 chars",
            1 <= len(probe.read_text(encoding="utf-8")) <= 279,
        )

    print(f"self-test: {len(failures)} failure(s)")
    return 1 if failures else 0


def main(argv: list[str]) -> int:
    if argv and argv[0] == "--self-test":
        return self_test()
    if argv:
        print(f"usage: {sys.argv[0]} [--self-test]", file=sys.stderr)
        return 2
    review = write_entry()
    print(review)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
