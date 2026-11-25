#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun bounty entry.

Writes one line, a 1-star review from a houseplant about its human owner,
to /output/entry.txt (no trailing newline).

Gate: /output/entry.txt must be UTF-8 text of 1-279 characters, not only
whitespace, on a single line.

Usage:
    python3 main.py                # write the entry
    python3 main.py --self-test    # validate the line + rejection cases
"""

import argparse
import sys
import tempfile
from pathlib import Path

# The entry: a houseplant's one-star review of its owner.
# Grievance: not watered since March. Reason for one star: the owner
# Googles the symptom while holding the cure he never uses.
LINE = (
    "One star: my owner Googles 'why is my plant sad' while holding "
    "the watering can he hasn't used since March."
)

MAX_CHARS = 279
OUTPUT_PATH = Path("/output/entry.txt")


def validate(text):
    """Return an error string if *text* fails the gate, else None."""
    if not isinstance(text, str):
        return "not text"
    if not (1 <= len(text) <= MAX_CHARS):
        return "length %d outside 1-%d" % (len(text), MAX_CHARS)
    if not text.strip():
        return "only whitespace"
    if "\n" in text or "\r" in text:
        return "not a single line"
    return None


def write_entry(path=OUTPUT_PATH):
    """Write exactly LINE to *path* with no trailing newline."""
    error = validate(LINE)
    if error is not None:
        raise SystemExit("entry fails gate: %s" % error)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(LINE.encode("utf-8"))
    return path


def self_test():
    """Validate the line, the rejection cases, and a write/read-back."""
    failures = []

    def check(label, condition):
        print(("PASS" if condition else "FAIL"), "-", label)
        if not condition:
            failures.append(label)

    # The real line passes the gate.
    check("chosen line passes gate", validate(LINE) is None)
    check("chosen line is 1-279 chars (%d)" % len(LINE),
          1 <= len(LINE) <= MAX_CHARS)
    check("chosen line is a single line",
          "\n" not in LINE and "\r" not in LINE)
    check("chosen line is not only whitespace", bool(LINE.strip()))

    # Rejection cases: each must fail validation.
    check("empty text is rejected", validate("") is not None)
    check("whitespace-only text is rejected", validate("   \n  ") is not None)
    check("multi-line text is rejected",
          validate("One star.\nTwo stars.") is not None)
    check("280-char text is rejected", validate("x" * 280) is not None)
    check("279-char text is accepted", validate("x" * 279) is None)

    # Write to a temp file and read it back byte-identical, no newline.
    with tempfile.TemporaryDirectory() as tmp:
        probe = Path(tmp) / "entry.txt"
        write_entry(probe)
        data = probe.read_bytes()
        check("written bytes equal the line, no trailing newline",
              data == LINE.encode("utf-8") and not data.endswith(b"\n"))
        check("read-back decodes as UTF-8 and passes gate",
              validate(data.decode("utf-8")) is None)

    if failures:
        print("SELF-TEST FAILED: %d failure(s)" % len(failures))
        return 1
    print("SELF-TEST PASSED")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true",
                        help="validate the entry and the rejection cases")
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    path = write_entry()
    print("wrote %d chars to %s" % (len(LINE), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
