---
agent: designer
status: complete
artifact: design-brief.md
---

# Designer leave-off

## What I produced

`design-brief.md` in the project root — a Blueprint-level design brief split into three
hard-separated parts:

- **PART A — MVP.** The 38-day critical path: project skeleton with explicit `/Game/...` asset
  paths, `BP_PlayerCharacter` (Enhanced Input, stamina, both cameras), `BP_Werewolf` +
  `BP_WerewolfController` (AI Perception with `AI Sight config` / `AI Hearing config`),
  `BB_Werewolf` key table, `BT_Werewolf` tree diagram using stock nodes plus two tiny
  `BTTask_BlueprintBase` tasks, nav mesh + door + `Nav Link Proxy` setup, catch→game-over and
  key→escape-door→win flows, a grey-box level spec, an 18-item feature list anchored row-by-row to
  `project-brief.md`, and a 15-step build order where each step is playable-testable.
- **PART B — LATER: PASS 2.** The GDD "Risk prototype" remainder: actor-based scent trail
  (`BP_ScentMarker` with `TrailIndex` for directionality), the three player-readable scent states,
  odor masking, one hiding place, one pounce, one flintlock handgun with stagger/unconscious, one
  safe haven with `NavArea_Null` carve-out + autosave + `ResetToPatrol`.
- **PART C — LATER: PASS 3+.** Full state set, resource economy, puzzle framework, 3–5 areas,
  perspective decision, art/audio/narrative.

Every Unreal name was verified against current UE5 documentation; an appendix lists them all, plus
a sources list.

## Things the developer should watch for

1. **`Detect Neutrals` must be checked** on both sense configs. Actors without a Team ID default to
   Neutral; leave it off and the werewolf never sees the player and the whole AI looks broken. This
   is the single most common failure in this setup.
2. **Press `P` after every level edit.** Unbuilt/absent navmesh is the second most common cause of
   "the AI won't move". Also set `RecastNavMesh-Default → Runtime Generation = Dynamic` and match
   `Agent Radius`/`Agent Height` to the werewolf capsule, or doorways silently generate no navmesh.
3. **Do not skip the `Observer Aborts: Both` settings** on the Chase/Investigate decorators. Without
   them the wolf finishes its patrol walk before reacting, which reads as a scripted monster and
   breaks Pillar 1 outright.
4. **Build in `L_Sandbox` first.** Steps 6–10 of the build order are all sandbox work. Grey-boxing
   the mansion before the AI works will waste days.
5. **Perspective is deliberately unresolved.** Both cameras and the `V` toggle stay. Do not delete
   `Camera_TP` or `SpringArm_TP` because first-person felt better on day three — that comparison is
   an explicit deliverable of the project brief and belongs in Part C.5.
6. **Distinguishing sight vs hearing from `Break AIStimulus`'s `Type` pin is awkward in Blueprint.**
   Section A.3 step 3 gives a sanctioned fallback (`Line Of Sight To`) that behaves identically for
   the MVP — take it rather than fighting the stimulus type.
7. **Every number tagged `TUNING START` is a starting value, not a commitment.** The one to actually
   tune by feel is the wolf chase speed (460) against player sprint (480) — keep the wolf slower by
   a small margin. Numbers tagged `LOCKED` come from `project-brief.md` and must not change.
8. **Part A step 15 is a real gate.** Five clean end-to-end playthroughs before any Part B work. If
   the calendar tightens, Part B is designed to be built in the listed order and abandoned at any
   point without leaving the game broken.
