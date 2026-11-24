"""make.fun entry: The One-Line Cat Joke That Lands (cat-joke-B).

Writes a single original one-line cat joke to /output/entry.txt.

Gate (from RULES.txt): the entry file must be UTF-8 text of 1 to 200
characters, not only white space, and a single line. The joke below is
an original invention for this entry: a cat starts a podcast about its
owner, and the twist is that the cat's one complaint is both true and
the whole show.
"""

ENTRY = (
    "My cat started a podcast about me \u2014 one episode, titled "
    "'He Feeds Me Late,' and honestly, he's not wrong."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def verify(text: str) -> None:
    """Enforce the gate limits from RULES.txt."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")


def main() -> None:
    verify(ENTRY)
    import os

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(ENTRY + "\n")
    print(f"wrote {len(ENTRY)} characters, 1 line to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
