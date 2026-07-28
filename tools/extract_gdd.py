"""
Extract the capstone GDD from PDF to markdown, then split it into one file per
top-level section.

The PDF is the source of truth (see CLAUDE.md). The files this produces are a
convenience copy for agents that cannot read PDFs. Re-run this script to
regenerate them; do not hand-edit the output.

    py -3 tools/extract_gdd.py

Requires pypdf (installed). Deliberately does NOT use pdftoppm/poppler, which
are not available on this machine.

TEXT FIDELITY
-------------
The Google Docs PDF export damages the text layer in three cosmetic ways. This
script repairs exactly those three and nothing else. No word is added, removed,
reordered, or reworded.

  1. NFKC normalization  - the export writes 'fi'/'fl' as single ligature
     glyphs (U+FB01 / U+FB02), 103 times. Left alone, a search for "confirmed"
     or "first" silently misses every occurrence.
  2. Whitespace collapse - every space in the export is doubled, and long
     sentences are shredded into one-word-per-line vertical runs. All
     whitespace runs collapse to a single space. Verified word-lossless:
     the word sequence before and after is identical (5311 words).
  3. Line structure      - bullets and numbered subheadings are put back onto
     their own lines so the markdown is readable and chunks sensibly.

Page footers ("v0.2 | CONCEPT / PRE-PRODUCTION | PAGE n") are RETAINED inline
where they fall. Stripping them would be an edit.

KNOWN LIMITATION
----------------
Tables (GDD sections 5.6 and 10.3) have no structure in the PDF text layer and
flatten into run-on prose. That is pypdf's extraction, not a choice made here,
and it is not recoverable from the text layer. Consult the PDF for those.
"""

import re
import sys
import unicodedata
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "CapstoneWerewolf GGD.pdf"
OUT_DIR = ROOT / "gdd"
SECTIONS_DIR = OUT_DIR / "sections"
FULL_MD = OUT_DIR / "capstone-werewolf-gdd.md"

# The ten top-level section headings, read off the document rather than guessed.
# Order here is document order and drives the NN- file prefix.
TOP_LEVEL = [
    "1. Executive Summary",
    "2. Player Experience and Game Flow",
    "3. Player Movement, Stamina and Scent",
    "4. Werewolf AI and Threat Design",
    "5. Defensive Combat, Resources and Crafting",
    "6. World, Areas, Puzzles and Pacing",
    "7. Narrative, Setting and Atmosphere",
    "8. UX, UI and Accessibility",
    "9. Technical Strategy and Production Plan",
    "10. Prototype Plan, Open Questions and Decision Log",
]

BANNER = (
    "<!-- GENERATED FILE - do not hand-edit.\n"
    "     Source of truth is 'CapstoneWerewolf GGD.pdf' at the project root.\n"
    "     Regenerate with: py -3 tools/extract_gdd.py\n"
    "     Text is verbatim: whitespace and ligatures repaired, no word changed. -->\n"
)


def normalize(text: str) -> str:
    """Repair the three export artifacts. Changes no words."""
    text = unicodedata.normalize("NFKC", text)   # 1. ligatures
    text = text.replace(" ", " ")
    text = re.sub(r"[ \t\r\n]+", " ", text)      # 2. all whitespace -> one space
    return text.strip()


def add_line_structure(text: str) -> str:
    """3. Put bullets and numbered subheadings back on their own lines."""
    text = re.sub(r"\s*●\s*", "\n- ", text)
    # subheadings like "5.6 Crafting, ..." start a fresh block
    text = re.sub(r"\s(\d{1,2}\.\d{1,2})\s+(?=[A-Z])", r"\n\n\1 ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def kebab(title: str) -> str:
    body = title.split(".", 1)[1] if "." in title else title
    slug = unicodedata.normalize("NFKC", body).lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def main() -> int:
    if not SRC.exists():
        print(f"ERROR: source PDF not found: {SRC}", file=sys.stderr)
        return 1

    reader = PdfReader(str(SRC))
    n_pages = len(reader.pages)

    # Normalize page by page, tracking where each page starts in the joined text
    # so section -> page-range can be reported accurately.
    page_texts, image_pages = [], []
    for i, page in enumerate(reader.pages, start=1):
        raw = page.extract_text() or ""
        if not raw.strip():
            image_pages.append(i)
            page_texts.append("")
            continue
        page_texts.append(normalize(raw))

    offsets, cursor, parts = [], 0, []
    for t in page_texts:
        offsets.append(cursor)
        parts.append(t)
        cursor += len(t) + 1  # +1 for the joining space
    full = " ".join(parts)

    def page_of(pos: int) -> int:
        p = 1
        for i, off in enumerate(offsets, start=1):
            if off <= pos:
                p = i
            else:
                break
        return p

    # Locate each known top-level heading. Fail loudly rather than guessing.
    marks = []
    for title in TOP_LEVEL:
        idx = full.find(title)
        if idx == -1:
            print(f"ERROR: heading not found in extracted text: {title!r}", file=sys.stderr)
            return 2
        marks.append((idx, title))
    marks.sort()

    positions = [m[0] for m in marks]
    if positions != sorted(positions) or len(set(positions)) != len(positions):
        print("ERROR: headings out of document order or duplicated.", file=sys.stderr)
        return 3

    OUT_DIR.mkdir(exist_ok=True)
    SECTIONS_DIR.mkdir(exist_ok=True)

    # Whole-document markdown
    FULL_MD.write_text(BANNER + "\n" + add_line_structure(full) + "\n", encoding="utf-8")

    written = []

    # Front matter: everything before section 1
    front = full[: marks[0][0]].strip()
    if front:
        path = SECTIONS_DIR / "00-front-matter.md"
        body = add_line_structure(front)
        path.write_text(f"{BANNER}\n# Front Matter\n\n{body}\n", encoding="utf-8")
        written.append((path.name, 1, page_of(max(0, marks[0][0] - 1)), len(front)))

    # One file per top-level section
    for n, (start, title) in enumerate(marks, start=1):
        end = marks[n][0] if n < len(marks) else len(full)
        chunk = full[start:end].strip()
        body = add_line_structure(chunk)
        # promote the heading line to a markdown H1
        if body.startswith(title):
            body = "# " + body[: len(title)] + body[len(title):]
        path = SECTIONS_DIR / f"{n:02d}-{kebab(title)}.md"
        path.write_text(f"{BANNER}\n{body}\n", encoding="utf-8")
        written.append((path.name, page_of(start), page_of(max(start, end - 1)), len(chunk)))

    # Report for the human writing INDEX.md
    print(f"source        : {SRC.name}")
    print(f"pages         : {n_pages}")
    print(f"image pages   : {image_pages if image_pages else 'none - every page yielded text'}")
    print(f"full markdown : {FULL_MD.relative_to(ROOT).as_posix()}  ({len(full)} chars)")
    print()
    print(f"{'file':<52} {'pages':<10} chars")
    print("-" * 74)
    for name, p1, p2, size in written:
        rng = f"p{p1}" if p1 == p2 else f"p{p1}-{p2}"
        print(f"{name:<52} {rng:<10} {size}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
