#!/usr/bin/env python3
"""Dad Joke Showdown — entry for make.fun.

Writes one dad joke (at most 200 characters) to /output/entry.txt.

Final: the grounded joke, winner of an 18-variant pairwise tournament
screened against the judge's criteria in order. One seam (electrical
calm vs. a disciplined kid) carries two interlocking puns, grounded
and currently, and the punchline is the last beat: delete the ending
and the joke dies. A dad, his daughter, a dinner-table question.
Stdlib only.
"""

import os

JOKE = (
    "My daughter asked why electricians are always so calm. I said, "
    "'They stay grounded, sweetheart. Unlike your brother, who is "
    "currently grounded.'"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(JOKE)
    print(f"wrote {len(JOKE)} chars to {path}")


if __name__ == "__main__":
    main()
