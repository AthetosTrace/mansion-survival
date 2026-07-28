# Project leave-off

**Overwritten every session.** This is the whole-project state — where we stopped and
where to resume. It is not one of the agent leave-offs in `leave-offs/`, which are gate
files for the pipeline. This file has no frontmatter and no gate; it is for the human
and the commander.

- **Session date:** 27 July 2026
- **Days to the 1 September 2026 deadline:** 36
- **Last commit:** `d62c885` — GDD extracted to markdown and split into sections
- **Pushed:** yes, `origin/main` verified in sync

---

## Where we are

**The three-agent pipeline has run end to end and is complete.** Designer → developer →
inspector all finished, all gates verified open by running `check_leaveoff.py` directly.
The straight line is done, so from here the user names the phase and the commander
dispatches to match — one specialist at a time.

| Artifact | Lines | State |
|---|---|---|
| `project-brief.md` | — | commander's seed, from the GDD |
| `design-brief.md` | 1770 | designer complete (ran twice; revision 2 added styling scope) |
| `build-sequence.md` | 1751 | developer complete |
| `inspection.md` | 316 | inspector complete — **verdict: pass** |

The inspector re-derived the developer's appendices rather than trusting them: 35/35
Part A steps trace with no orphans, 32/32 §A.15 features implemented, 16/16 §A.14 asset
register rows honoured, 12/12 designer guardrails enforced at a real step.

**The GDD is now machine-readable.** `gdd/sections/` holds eleven per-section files split
from the PDF, with `gdd/sections/INDEX.md` as the map. Regenerate with
`py -3 tools/extract_gdd.py`. Verified word-lossless (5,311 words both sides).

---

## Pick up here next session

### 1. Assignment #4 — the immediate priority. Due 30 July, nothing built yet.

A **dynamic content pipeline**: RAG over the GDD, three generated content types, and a
critic agent. This is a different system from the three-agent crew — that crew is
Assignment #3's deliverable and is finished.

What the rubric demands, and where we stand:

| Criterion | Pts | Status |
|---|---|---|
| Game-Anchored Source | 2.0 | **Ready** — `gdd/sections/` is a real GDD, not placeholder lore |
| Content Fit | 2.5 | **Gap named already** — see below |
| RAG Implementation | 2.0 | Not built. Must *show* query → retrieved chunk → output side by side |
| Consistency Checking | 2.0 | Not built. Critic must catch a real lore break, correction **shown** not claimed |
| Voice Judgment | 1.5 | Not written. Needs self-assessment plus one concrete prompt/retrieval tweak |

**"Code that does not run receives 0 across all criteria."** Functional code is the
minimum bar, not an achievement. The existing crew is agent definitions plus hooks — it
works, but it is not a script you execute. Assignment #4 needs something that runs.

**The gap to aim the generator at**, already documented in the GDD rather than invented
— this is what earns Content Fit:
- **§7.2 Narrative Framework — TO BE CRAFTED.** Six named empty sockets: protagonist,
  why the player cannot leave, werewolf origin, why safe havens are protected, what the
  puzzles accomplish, what escape means.
- **§6.5 Puzzle Design Framework** — roles and quality bars locked, **no puzzle
  solutions authored**.
- **§6.1 mansion vs castle** — still PROVISIONAL.

### 2. Assignment #3 — due 28 July (tomorrow). Ready to submit.

All five rubric criteria are satisfied by what is on disk. The end-to-end run this
session is the evidence for Working Crew. Nothing outstanding — **just submit it.**

---

## Live hazards

1. **Table flattening in `gdd/sections/`.** The GDD is mostly tables and the PDF text
   layer has none, so every section except front matter has run-on tables. All words
   survive; **column assignment does not.** A RAG pipeline reading §5.2 could confidently
   attribute the rifle's 12-second reload to the handgun. Mitigation is in
   `gdd/sections/INDEX.md`; for any value that matters, read the PDF.
2. **The GDD contradicts itself on playtime.** Page 1 says "Approximately 4 to 8 hours";
   §1.2 and the Decision Register say "2-4 hours". Unresolved in the source. A content
   generator reading both will produce inconsistent output. **This is a good candidate
   for the critic agent to catch** — it is a genuine lore break, already present.
3. **Unreal MCP is not connected** and is parked by decision (see `TODO.md` T1).
   Assignments #3 and #4 do not need it. It must be answered before Part A starts —
   22 of 35 Part A steps are tagged MCP/MIXED and the calendar was never re-baselined
   for the hand-build branch.

---

## Open decisions waiting on the user

- **Which Unreal MCP server was this?** Nothing in the repo records the server, repo,
  transport or port. Reconnecting is a recovery job, not a config job.
- **Perspective, first vs third person** — deliberately unresolved by the GDD, decided
  at `build-sequence.md` step 6, not before.
- **`.claude/settings.local.json` keeps dirtying the tree** as permissions accrue.
  Offered to gitignore and `git rm --cached` it; no answer yet.

---

## Also on disk

- `TODO.md` — eleven deferred items, T1–T11. T2–T5 are `build-sequence.md` defects that
  must be fixed **before** any Unreal build starts. Completed items get deleted, not
  ticked.
- `CLAUDE.md` — canonical pipeline, gates, and commander operating rules.
- `README.md` — mirrors the pipeline diagram for GitHub. Must match `CLAUDE.md`.
