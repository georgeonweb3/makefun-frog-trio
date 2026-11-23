"""Sleeve Notes for the Frog Trio — make.fun entry.

Writes an album title plus a short back-cover blurb (at most 400
characters in total) for a jazz trio made entirely of frogs to
/output/entry.txt. Deterministic, no network, no randomness.
"""

import os

ENTRY = (
    "Pondwater Swing\n"
    "Three frogs hold the late set at the Lily Pad Club: Marlowe on tenor "
    "sax, croaking low over the reeds; Bea on upright bass, plucking the "
    "waterline; and Tad on brushes, keeping time on an upturned tin can. "
    "Recorded live at midnight, reeds humming, crowd hushed — small, "
    "swinging, and entirely serious about the blues."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
