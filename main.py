"""Write the one-line planet rename to /output/entry.txt and verify it."""

ENTRY = "Rename Mercury 'The Intern' \u2014 closest to the boss, finishes a whole year in 88 days, and still gets no credit."

OUTPUT_PATHS = ["/output/entry.txt", "./output/entry.txt"]


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"

    written_path = None
    last_error = None
    for path in OUTPUT_PATHS:
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(ENTRY)
            written_path = path
            break
        except OSError as exc:  # e.g. /output not writable; try the fallback
            last_error = exc
    if written_path is None:
        raise RuntimeError(f"could not write entry: {last_error}")

    with open(written_path, "r", encoding="utf-8") as f:
        read_back = f.read()
    assert read_back == ENTRY, "round-trip mismatch"

    print(ENTRY)
    print(f"characters: {len(ENTRY)}")
    print(f"wrote: {written_path}")


if __name__ == "__main__":
    main()
