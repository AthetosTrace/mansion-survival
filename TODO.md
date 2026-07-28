# TODO — deferred items

Things that are **known, deliberately deferred, and must not be forgotten**. The
commander reads this at the start of every session (see `CLAUDE.md`).

> **Rule — completed items are deleted, not ticked.** When an item is genuinely done,
> **remove its entry from this file entirely**. Do not strike it through, do not mark
> it `[x]`, do not move it to a "done" section. This file is a list of what is *still
> outstanding* and nothing else — if it is written here, it is not finished. The commit
> that completes the work is the same commit that deletes the entry, so the git history
> is the record of what was done. Do not renumber the surviving items when one is
> removed; `inspection.md` and past commits refer to them by ID.

Nothing here blocks Assignment #3 (28 Jul) or Assignment #4 (30 Jul). Everything
here is about the Unreal build, which starts after Assignment #4 is submitted.

---

## Parked by decision

### T1 — Unreal MCP connection
**Status:** deferred deliberately, 27 July 2026.
**Decision:** get Assignment #4 done first, then connect the MCP. If something before
then genuinely requires it, connect it at that point rather than working around it.

The design brief mandates the connection but never names the server, repo, transport
or port anywhere in 1770 lines, and there is no `.mcp.json` in the project. So
reconnecting is a recovery job, not a config job — `build-sequence.md` step 0a has the
search procedure.

**Why this matters more than it looks:** 22 of the 35 Part A steps are tagged `MCP` or
`MIXED`. Step 0a.5 says "if the MCP is not live by 30 July, build Part A by hand" — but
the 28-day calendar was never re-baselined for that branch. Before starting the Unreal
build, either connect the MCP or re-cost the schedule for hand-building. Do not start
Part A assuming the existing dates hold on the hand-build path.

---

## Defects in `build-sequence.md` — fix before building from it

### T2 — Phase numbering contradicts itself `(inspection.md D1)`
§0, §1 and §2 refer to Part B/C as "Phase 8 and Phase 9". The actual headers say
**Phase 6 and Phase 7**. The guardrail that gates Part B therefore points at sections
that do not exist. Mechanical fix, but it is the kind of thing that gets followed
literally under deadline pressure.

### T3 — `SC_Player` does not exist `(inspection.md, step 4a)`
Step 4a invents a `SC_Player` sound class. It appears in neither §A.1 nor §A.13 of
`design-brief.md`. Should read **`SC_SFX`**.

### T4 — §A.8 texel-density unification has no step `(inspection.md G1)`
One of §A.8's five mechanisms was never given a build step. This is the **only Part A
design decision in the brief that is genuinely unimplemented** in the sequence.

### T5 — Step 29 needs a clean machine and nothing procures one `(inspection.md G2)`
Step 29 verifies the packaged build on a machine that has never had the Unreal Editor
installed. No step arranges for one, and Appendix C does not flag the gap. Sort this
well before late August — discovering it on 26 August is a bad day.

---

## Minor — worth a pass, not urgent

- **T6** `(G3)` Retargeting guidance for missing animation clips was dropped from the
  brief and never landed in the sequence.
- **T7** `(G4)` Kenney UI **sounds** have no clean row in the §A.14 asset register.
  Under the $0 rule, anything without a nameable licence row does not get imported.
- **T8** `(G5)` Appendix A traces assets at **row** level, not asset level — so it
  proves the register was honoured, not that each individual asset is accounted for.
- **T9** `CreatureAudio` (step 11.3) is an inference the developer made but did not
  flag, unlike `DeathCam`, which it did flag properly.
- **T10** Appendix C says "the one place I added a step" but there are **two** — step
  0c as well as step 4a.

---

## Structural, later

- **T11** `design-brief.md` is 1770 lines in a single file. The designer's instructions
  now say long output goes in section files under `design/` with the brief as a short
  index. The existing brief was **deliberately left unrestructured** — do not convert
  it as a task of its own. Let it shrink naturally as sections get revised.
