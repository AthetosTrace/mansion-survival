---
agent: developer
status: complete
artifact: build-sequence.md
---

# Developer leave-off

## What I produced

`build-sequence.md` — an ordered, executable Unreal build sequence for **Part A**, expanded from
`design-brief.md` §A.16's numbered build order so that every step carries a real editor path
(`Content Browser > Add > …`, `Project Settings > …`, `Place Actors > …`), the exact Blueprint node
names involved (`Report Noise Event`, `On Target Perception Updated`, `Break AIStimulus`,
`Line Of Sight To`, `Get Random Reachable Point in Radius`, `Set Timer by Event`,
`Set View Target with Blend`, `Push Sound Mix Modifier`, and so on), what the step produces, and the
brief section it implements.

Structure: **Phase 0** gate and pre-production (0a MCP, 0b the A.14 asset claim, 0c compliance
artefacts) → **Phase 1** "it moves" (steps 1–6, ending at the perspective decision gate) →
**Phase 2** "it hunts" (7–14b, including the week-2 throwaway package) → **Phase 3** "it's a place"
(15–22) → **Phase 4** "it's a game you can read" (23–27) → **Phase 5** "it ships" (28–30, hard stop)
→ **Phase 6** Part B and **Phase 7** Part C, both explicitly **LATER** and gated on step 30, written
at node level so the scent trail, odor masking, hiding place, pounce, flintlock/silver, safe haven +
autosave and the puzzle framework are all recorded rather than lost.

Constraints honoured: A.16's `[FN]`/`[FORM]` interleave is preserved step by step (art is never
deferred to the end); every step is tagged `MCP` / `HAND` / `MIXED` because §0 warns some Form work
cannot be scripted blind; both cameras survive to step 6 and step 28 only *disables* the toggle;
Appendix A traces every referenced asset to one of §A.14's 16 rows; Appendix B traces all 32 §A.15
features to steps; §2 maps the designer's twelve "must not miss" items to enforcing steps.

## Schedule note the inspector should check

The brief's calendar assumed a **25 July** start. Today is **27 July — 36 days left**, so
pre-production is compressed to four days (27–30 July) while Block 1 still starts 31 July. The
deadline-critical ordering decision is **step 14b, the throwaway package on 10 August** — it converts
the 28–31 August reserve from discovery time into repair time. It must not be moved.

## Gaps I flagged rather than researched around (Appendix C of the artifact)

1. **The brief never names the Unreal MCP server** — no repo, plugin, transport or port. There is
   currently no `.mcp.json` in the project and no MCP tools available, so **step 0a is written as a
   recovery search plus a hard fallback (0a.5: build by hand if it is not live by 30 July)**. This is
   the largest unknown and it gates every other step. Note that 0a.3 requires the *user* to create
   `.mcp.json`; that is a configuration change I did not make.
2. §A.5's death-beat `Camera Actor` has no stated home — I specify a `DeathCam` `Camera` component on
   `BP_Werewolf` and label it an inference.
3. `Report Noise Event` tags are specified in §A.2 but never read in Part A; noted as inert.
4. The audio mix architecture (§A.13 "set this up first") has no A.16 step number even though step
   4's `BreathAudio` needs a `Sound Class` — **inserted as step 4a**, an ordering fix with no new
   scope. This is the one place I added a numbered step the brief did not have.
5. Step 6's "60-second traverse" content is unspecified; I defined it from §A.7's own dimensions.
6. `HighScentThreshold` is flagged TBD by the brief itself (§B.2) — LATER anyway.
7. Engine floor is ambiguous (§0 says 5.4+, §A.14 row 6 implies 5.6+ for MetaHuman, which is unused).
8. Pre-production is two days shorter than the brief assumed.
