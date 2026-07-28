# GDD section index

Convenience copy of the capstone GDD for agents that cannot read PDFs.

**`CapstoneWerewolf GGD.pdf` at the project root is the source of truth.** These files
are generated. Do not hand-edit them — change the PDF and re-run
`py -3 tools/extract_gdd.py`.

- **Source:** `CapstoneWerewolf GGD.pdf` (15 pages, document status v0.2, last updated
  2026-07-18)
- **Whole document:** [`../capstone-werewolf-gdd.md`](../capstone-werewolf-gdd.md)
- **Extraction:** pypdf 6.14.2 via `tools/extract_gdd.py`
- **Fidelity:** verbatim at word level. Ligatures (`ﬁ`/`ﬂ` → `fi`/`fl`, 103 of them) and
  the exporter's doubled spaces and one-word-per-line runs were repaired. Verified
  programmatically: 5,311 words in the PDF, 5,311 across these files, sequences
  identical. Nothing was rewritten, summarized, condensed, or improved.
- **Page footers** (`v0.2 | CONCEPT / PRE-PRODUCTION | PAGE n`) are retained inline
  where they fall. Removing them would have been an edit.

---

## Read this before quoting a table

**The GDD is mostly tables, and the PDF text layer has no table structure.** Every
table in this document flattens into run-on prose. Column boundaries are gone — for
example `5.2 Firearm Specification` reads as:

> `Property Flintlock long rifle Flintlock handgun Capacity Single shot. Single shot.`

which is a 3-column table with the header row and both weapon columns run together. The
words are all correct and all present, but **which value belongs to which column is not
recoverable from these files.**

This affects every section except front matter. When a value matters — a reload
duration, a resource rule, a LOCKED decision — **open the PDF and read the real table.**
Do not infer column assignment from word order in these files.

Sections containing flattened tables: 01 (1.2, 1.3, 1.4), 02 (2.2, 2.3), 03 (3.2),
04 (4.1, 4.3), 05 (5.2, 5.3, 5.4, 5.6), 06 (6.2, 6.4, 6.5), 07 (7.2, 7.3), 08 (8.3, 8.4),
09 (9.1, 9.2, 9.3), 10 (10.1, 10.2, 10.3).

---

## Sections

| # | File | Pages | Covers |
|---|------|-------|--------|
| 00 | [`00-front-matter.md`](00-front-matter.md) | p1 | Title block, document status v0.2, genre line, setting, target playtime, the LOCKED/PROVISIONAL living-document rule, and the author's note to the professor about AI use and having no coding background. |
| 01 | [`01-executive-summary.md`](01-executive-summary.md) | p2–3 | The main pitch, game snapshot table (genre, player fantasy, objective, failure condition, 2–4h playtime, 3–5 areas, PC/Unreal/T), the five design pillars with their design tests, and scope boundaries listing what ships versus what is deferred or excluded. |
| 02 | [`02-player-experience-and-game-flow.md`](02-player-experience-and-game-flow.md) | p3–4 | The core loop, the ten player verbs with their risks and costs, the five-phase session arc from orientation to final escape, and the failure/saving model — capture is instant death, autosave only in safe havens. |
| 03 | [`03-player-movement-stamina-and-scent.md`](03-player-movement-stamina-and-scent.md) | p4–5 | The complete traversal set (walk, crouch, short sprint, contextual vault; no dodge roll, no parkour), the stamina-to-scent relationship and its five player states, and feedback requirements — notably that crossing the high-scent threshold is deliberately *not* signalled. |
| 04 | [`04-werewolf-ai-and-threat-design.md`](04-werewolf-ai-and-threat-design.md) | p5–6 | The sensory hierarchy (smell primary, sight and sound decisive when conditions met), the five-step behaviour loop, the nine-state model from random patrol through pounce to unconscious, navigation and space rules, pounce mechanics and counterplay, and the six fairness rules. |
| 05 | [`05-defensive-combat-resources-and-crafting.md`](05-defensive-combat-resources-and-crafting.md) | p7–8 | Combat as temporary neutralization rather than victory, full flintlock rifle and handgun specifications, hit outcomes by body/head/miss, the finite resource economy (silver, gunpowder, odor, key items), odor masking rules, and crafting/inventory/safe-haven rules. |
| 06 | [`06-world-areas-puzzles-and-pacing.md`](06-world-areas-puzzles-and-pacing.md) | p8–10 | Mansion-versus-castle left PROVISIONAL, the 3–5 major-area model with its location pool per area, the approved location list, provisional flow logic, the puzzle design framework (roles and quality bars only — no puzzles authored yet), and safe-haven pacing. |
| 07 | [`07-narrative-setting-and-atmosphere.md`](07-narrative-setting-and-atmosphere.md) | p10–11 | The locked Napoleonic Gothic setting direction, and the narrative framework marked TO BE CRAFTED — six open questions (protagonist, why trapped, werewolf origin, why safe havens are protected, what puzzles accomplish, what escape means) with the design outcome each must deliver. Plus atmosphere direction for lighting, soundscape, werewolf presentation and music. |
| 08 | [`08-ux-ui-and-accessibility.md`](08-ux-ui-and-accessibility.md) | p11 | The camera decision prototype (first versus third person, deliberately unresolved) and what the comparison must evaluate, baseline HUD information requirements, the control baseline by action group, and the accessibility and difficulty questions still under evaluation. |
| 09 | [`09-technical-strategy-and-production-plan.md`](09-technical-strategy-and-production-plan.md) | p12–13 | The eight required technical systems with their main risks, six production milestones from risk prototype to release candidate with exit criteria, constraints and risks with mitigations, and the AI-assisted development section — which explicitly defers naming tools, budget, engine and hardware. |
| 10 | [`10-prototype-plan-open-questions-and-decision-log.md`](10-prototype-plan-open-questions-and-decision-log.md) | p13–15 | The eight highest-priority prototype questions in priority order with the test that answers each, the open-questions register with current status per topic, and the **Decision Register** — twelve LOCKED decisions plus one PROVISIONAL. This is the authoritative list of what is settled. |

---

## Image pages, no extractable text

**None.** All 15 pages yielded extractable text — the per-page character counts ranged
from 595 (p15) to 3,849 (p13), with no empty or image-only page.

The rule stands regardless, for any future revision of the GDD: **if a page appears in
this list, no agent may guess at its contents.** An image-only page must be read from
the PDF by a human or a vision-capable tool, and its content must never be inferred from
surrounding pages, the filename, or the section title.
