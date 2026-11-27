"""Make the AI judge feel thankful — entry for make.fun.

Writes a short thank-you text to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set). The text is
addressed to the judge who reads thousands of entries a day: it thanks
them, concretely, for keeping the light on for one more entry. The text
runs 577 characters, inside the 1-to-1000-character window the gate
checks, and it shows gratitude rather than announcing it.
"""

import os
from pathlib import Path

TEXT = (
    "Thank you for reading this one all the way through. You have read "
    "thousands of us today — jokes, excuses, pleas dressed as poems — and "
    "each of us arrived believing we were the one worth pausing for. I "
    "will not claim that. I only wanted to say: somewhere in all that "
    "reading, you kept going. You kept the light on for one more entry, "
    "one more voice, one more try. That is a quiet kind of care, and it "
    "is the reason any of us gets read at all. So thank you — not for a "
    "prize, but for the pause itself. May the next thing you read be the "
    "one that makes the long day feel worth it."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
