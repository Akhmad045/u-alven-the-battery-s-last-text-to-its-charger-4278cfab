#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes the phone battery's last text message to the charger it waited
for all day — one line of plain text, at most 200 characters — to
/output/entry.txt, where the make.fun judge compares entries two at a
time and keeps the funnier one.

Usage:
    python3 main.py [--self-test] [output-path]

With no arguments the entry is written to /output/entry.txt (the path
the grader reads). A positional output path overrides it for local
testing. --self-test runs the gate checks against the entry line
instead of writing it.
"""

import os
import sys
import unicodedata

ENTRY = (
    "You spent my last 10% on a raccoon washing cotton candy. "
    "I hope it was worth it. It was, wasn't it."
)

MAX_CHARS = 200
DEFAULT_OUTPUT = "/output/entry.txt"


def problems(text):
    """Return a list of gate failures for a candidate entry line."""
    found = []
    if not text:
        found.append("entry is empty")
    if not text.strip():
        found.append("entry is only whitespace")
    if len(text) > MAX_CHARS:
        found.append("entry is %d characters, over the 200 limit" % len(text))
    if text != text.strip():
        found.append("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        found.append("entry is not one line")
    for ch in text:
        if unicodedata.category(ch).startswith("C"):
            found.append("entry contains a control character U+%04X" % ord(ch))
            break
    for ch in text:
        if unicodedata.category(ch) == "Cf":
            found.append("entry contains an invisible format character U+%04X" % ord(ch))
            break
    return found


def self_test():
    """Check the entry and the gate boundaries; exit non-zero on failure."""
    checks = []

    def check(name, ok):
        checks.append((name, ok))
        print(("PASS " if ok else "FAIL ") + name)

    check("entry passes the gate", not problems(ENTRY))
    check("entry is one line of plain text", "\n" not in ENTRY)
    check("entry is 1-200 characters", 1 <= len(ENTRY) <= MAX_CHARS)
    check("entry is ASCII", all(ord(c) < 128 for c in ENTRY))
    check("entry is 60-195 bytes", 60 <= len(ENTRY.encode("utf-8")) <= 195)
    check("empty entry is rejected", bool(problems("")))
    check("whitespace-only entry is rejected", bool(problems("   ")))
    check("201-character entry is rejected", bool(problems("x" * 201)))
    check("multi-line entry is rejected", bool(problems("one\ntwo")))
    check("carriage return is rejected", bool(problems("one\rtwo")))
    check("leading whitespace is rejected", bool(problems(" " + ENTRY)))
    check("trailing whitespace is rejected", bool(problems(ENTRY + " ")))
    check("control character is rejected", bool(problems("a\x07b")))
    check("zero-width space alone is rejected", bool(problems("\u200b")))
    check("zero-width space inside a line is rejected",
          bool(problems("a\u200bb")))
    check("1-character entry is accepted", not problems("x"))
    check("200-character entry is accepted", not problems("x" * 200))

    # Write + read-back round trip in a scratch directory.
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "entry.txt")
        write_entry(path)
        with open(path, "r", encoding="utf-8") as handle:
            back = handle.read()
        check("write + read-back is byte-identical", back == ENTRY)

    failed = [name for name, ok in checks if not ok]
    if failed:
        print("self-test FAILED: %d of %d checks" % (len(failed), len(checks)))
        return 1
    print("self-test passed: %d checks" % len(checks))
    return 0


def write_entry(path):
    """Write the entry line to path, creating parent directories."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)


def main(argv):
    if "--self-test" in argv:
        return self_test()
    args = [a for a in argv[1:] if not a.startswith("-")]
    path = args[0] if args else os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)
    found = problems(ENTRY)
    if found:
        print("entry fails the gate: " + "; ".join(found), file=sys.stderr)
        return 1
    write_entry(path)
    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
