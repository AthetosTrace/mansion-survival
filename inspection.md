# Inspection — `build-sequence.md` against `design-brief.md`

**Author:** inspector agent · **Consumes:** `design-brief.md` (rev 2, 1770 lines) + `build-sequence.md` (1751 lines) + both leave-offs
**Date:** 27 July 2026 · **Deadline:** 1 September 2026 — 36 days
**Method:** every step's citation was opened in the brief and read before being accepted. Feature
coverage, asset coverage and guardrail coverage were re-derived from the brief independently rather
than read off the developer's appendices.

---

## OVERALL VERDICT

**Yes — the build sequence is faithful to the design brief.** All 35 Part A steps trace to real,
correctly-cited brief material; no orphans. Independently verified: 32/32 §A.15 features implemented,
16/16 §A.14 asset rows honoured with no off-register asset anywhere, 12/12 designer "must not miss"
items genuinely enforced rather than merely listed. The gaps found are small and mostly originate in
the brief, not in the developer's expansion. **One real project risk remains open and is not a
document problem: the Unreal MCP connection (step 0a) is unspecified and unproven.**

---

## 1. Per-step verdict

Every step below was checked by opening its cited brief section. "TRACES" means the citation exists
and actually supports the step's content.

### Phase 0

| Step | Verdict | Brief item it implements | Note |
|---|---|---|---|
| **0a** MCP connection | **TRACES** | §A.16 Block 0 step 0a ("Nothing else can start"); §0 "Notes for MCP-driven Blueprint work"; leave-off item 1 | Citation holds. **Step content does not come from the brief** — see §5.2. |
| **0b** Claim/download every A.14 asset | **TRACES** | §A.14 (all 16 rows, binding); §A.16 Block 0 step 0b; leave-off item 2 | Row-by-row table matches the register exactly; row 6 correctly omitted as unused. |
| **0c** Compliance artefacts | **TRACES** | §A.14 "Compliance obligations" 1–4; §A.1 `/Game/Sourced/` note | **Inserted step with no A.16 number** — the brief folds these into 0b's Test line. Legitimate, but the developer's disclosure of "one added step" (Appendix C item 4) undercounts; 0c is a second one. |

### Phase 1 — "it moves"

| Step | Verdict | Brief item | Note |
|---|---|---|---|
| **1** Project skeleton | **TRACES** | §A.1 (folder tree, Maps & Modes, Rendering table); §A.16 step 1 | Rendering table reproduced verbatim. `Game Default Map` deferred to step 24 — matches §A.16 step 24, no conflict. |
| **2** `BP_PlayerCharacter`, both cameras, input | **TRACES** | §A.2 components + Enhanced Input table; §A.15 F1, F4 | Component hierarchy matches §A.2 exactly, including `Jump Z Velocity` 0. |
| **3** `ApplyPerspective` + `V` toggle | **TRACES** | §A.2 "Keeping perspective swappable"; F4; leave-off 6 | `Set Owner No See` preferred over `Set Hidden In Game`, as the brief instructs. |
| **4** Crouch/sprint/stamina/breath/noise | **TRACES** | §A.2 "Movement and stamina", "Readable stamina without a HUD bar", "Sprinting is audible"; F1, F2, F3, F7 | All numbers match. Inert-`Tag` observation is correct and honest. |
| **4a** Audio mix architecture | **TRACES** | §A.13 "Mix architecture — set this up first" | **Deviation, assessed in §5.1. Not an orphan** — every asset it creates (`SC_*`, `SM_*`, `ATT_*`) is named in §A.13 and §A.1. |
| **5** Game Animation Sample → `ABP_Player` | **TRACES** | §A.10 "$0 sources, whichever branch wins"; §A.14 row 3 | Correctly takes the animations, not Motion Matching, per §A.10. |
| **6** Perspective decision gate | **TRACES** | §0 "Things this brief deliberately does NOT decide"; §A.10 cost table; §C.5; leave-off 6 | 60-second traverse content inferred from §A.7 dimensions and disclosed. |

### Phase 2 — "it hunts"

| Step | Verdict | Brief item | Note |
|---|---|---|---|
| **7** Navmesh in `L_Sandbox` | **TRACES** | §A.6 items 1, 2, 3, 7; F13; leave-off 4 | |
| **8** Werewolf character + capsule | **TRACES** | §A.9 (whole); §A.14 rows 1, 2; V6, V7; leave-off 7 | 8.8 adds a nav-settings reconciliation the brief implies but does not spell out — a correct inference from §A.4's "these propagate". |
| **9** Enum, Blackboard, controller, Patrol branch | **TRACES** | §A.4 (whole); F8, F9 | All ten enumerators declared including the seven unused, per §A.4. |
| **10** Sight perception + Chase branch | **TRACES** | §A.3 "AI Perception lives on the AI Controller" + "Reacting to perception" 1–5; F6, F8; leave-off 3, 5 | Decorator settings reproduce §A.4's tree exactly, including `Observer Aborts: Self` on the second Chase decorator. |
| **11** Per-state creature audio | **TRACES** | §A.13 content list + "The sniff is a mechanic"; rows 11, 12, 13; F12, V13 | |
| **12** Catch → death beat → game over | **TRACES** | §A.5 "Catch (lose)" (LOCKED); §A.4 (catch is not a state); F15 | `DeathCam` component is an inference and is labelled as one. |
| **13** Hearing, Investigate, decay, `ResetToPatrol` | **TRACES** | §A.3 item 6 + "Memory decay and `ResetToPatrol`"; F7, F8, F10 | |
| **14** Speed table + blend space together | **TRACES** | §A.4 speed table + the "460 vs 480" note; F11; leave-off 11 | |
| **14b** Throwaway package smoke test | **TRACES** | §A.17 (whole); §A.16 step 14b; leave-off 8, 10 | |

### Phase 3 — "it's a place"

| Step | Verdict | Brief item | Note |
|---|---|---|---|
| **15** Modular blockout set | **TRACES** | §A.7 "The grid"; V1 | Module table matches §A.7 row for row. Correctly gated on step 8. |
| **16** Blockout `L_Mansion_Slice` | **TRACES** | §A.7 layout properties 1–9 + "Actors to place"; F17; leave-off 4 | All nine layout properties reproduced as requirements, not suggestions. |
| **17** Interaction, key, escape door, win | **TRACES** | §A.2 "Interaction"; §A.5 "Escape (win)" (LOCKED); F5, F16 | |
| **18** AI doors + nav link | **TRACES** | §A.6 items 4, 5; F13, F14; leave-off 4 | §A.6 item 6 (`NavArea_Null`) correctly recorded as not-in-Part-A. |
| **19** Five master materials | **TRACES** | §A.11 "Five master materials"; §A.8 mechanism 3; rows 7, 8; V2 | |
| **20** Lighting pass | **TRACES** | §A.8 "Light — the two-temperature rule"; §A.11 "Lighting build" 1–5; row 8; V3 | |
| **21** Post-process + fog + `Sight Radius` re-tune | **TRACES** | §A.11 "Post-process" / "Fog"; §A.3 "Second failure mode"; V4, V5; leave-off 9 | |
| **22** Set dressing, decals, Niagara | **TRACES** | §A.11 "Decals" / "Niagara VFX" / "Set dressing rule"; §A.8 cues + anti-cues; rows 8, 9, 10; V9, V10 | |

### Phase 4 — "it's a game you can read"

| Step | Verdict | Brief item | Note |
|---|---|---|---|
| **23** UI restyle | **TRACES** | §A.12 (typography, colour, framing, motion); rows 15, 16; V11 | |
| **24** `L_Title`, title screen, credits | **TRACES** | §A.12 widget set; §A.14 obligation 2; V12; leave-off 10 | |
| **25** Full audio pass | **TRACES** | §A.13 content list + implementation notes; rows 11, 12, 14, 16; V13 | Row 16 citation is a small stretch — see gap G4. |
| **26** Player visual per step-6 verdict | **TRACES** | §A.10 (whole); rows 3, 4, 5; V8 | Both branches costed as §A.10 costs them. |
| **27** Playtest ×5 | **TRACES** | §A.16 step 27; §A "Definition of done" 1–4 | Gathers the brief's own acceptance bars into one checklist — good practice, no invention. |

### Phase 5 — "it ships"

| Step | Verdict | Brief item | Note |
|---|---|---|---|
| **28** Full packaging pass | **TRACES** | §A.17 settings + all seven breakages; §A.2 dev-tool gating; V14; leave-off 10 | Correctly *disables* the toggle rather than deleting a camera. |
| **29** Clean-machine verification | **TRACES** | §A "Definition of done" item 5; §A.16 step 29 | See gap G2. |
| **30** Submission package, HARD STOP | **TRACES** | §A.16 step 30; §A.14 obligations 1–3; leave-off 12 | |

### Phases 6 and 7 — LATER

| Step | Verdict | Brief item |
|---|---|---|
| **B1** Scent trail | **TRACES** | §B.1; §B.6 order 1 |
| **B2** Three scent states | **TRACES** | §B.2; §B.6 order 2 |
| **B3** Odor masking | **TRACES** | §B.3; §B.6 order 4 |
| **B4** Hiding place / pounce / flintlock | **TRACES** | §B.4; §B.6 orders 5, 6, 7 |
| **B5** Safe haven, autosave, reset | **TRACES** | §B.5; §B.6 order 3 |
| **Phase 7** C.1–C.6 | **TRACES** | §C.1–§C.6, all six recorded |

All seven items of §B.6's build order are present across B1–B5; none dropped.

**ORPHANS: none.** Every step in the document implements something the brief decides.

---

## 2. Coverage the other way — §A.15's 32 features, verified independently

I re-derived this from §A.15 and searched the sequence for an implementing instruction, rather than
reading Appendix B. **All 32 are genuinely implemented. The developer's claim holds.**

| # | Where it is actually built | OK |
|---|---|---|
| F1 | 2.6 (move, control-rotation-derived), 2.6 (crouch), 4.2–4.3 (sprint) | yes |
| F2 | 4.3 | yes |
| F3 | 4.4 (`BreathAudio` + `Post Process` vignette, no bar) | yes |
| F4 | 2.1/2.2 (both cameras), 3.3 (`V`), 6 | yes |
| F5 | 17.2, 17.3, 17.4 | yes |
| F6 | 10.2 (sight), 13.1 (hearing) | yes |
| F7 | 4.5 (sprint/walk/crouch), 18.1 (doors) | yes |
| F8 | 9.4 + 10.5 + 13.3, with `Observer Aborts` set | yes |
| F9 | 9.5 step 3 | yes |
| F10 | 13.4, 13.5 | yes |
| F11 | 9.6 table, tuned at 14 | yes |
| F12 | 11.2, 11.3 with `ATT_Creature` + `Enable Occlusion` | yes |
| F13 | 7.2, 16 (re-confirm), 18.1 | yes |
| F14 | 18.3 | yes |
| F15 | 12.1–12.4 | yes |
| F16 | 17.6–17.9 | yes |
| F17 | 16, all nine properties | yes |
| F18 | §2 standing prohibition + re-checked at 27 | yes (a negative feature; "never built" is the correct implementation) |
| V1 | 15, applied at 16 | yes |
| V2 | 19.2–19.4 | yes |
| V3 | 20.1–20.6 | yes |
| V4 | 21.1 (exposure `Manual`) | yes |
| V5 | 21.2 | yes |
| V6 | 8.1–8.4 | yes |
| V7 | 8.5–8.6, retuned at 14 | yes |
| V8 | 26, both branches | yes |
| V9 | 22.3, 22.4 (incl. `M_Decal_Claw` on wolf routes) | yes |
| V10 | 22.5 (Niagara) + 20.5 (flicker) | yes |
| V11 | 23.1–23.7 | yes |
| V12 | 24.1–24.3 | yes |
| V13 | 4a, 11, 25 | yes |
| V14 | 14b, 28, 29 | yes |

---

## 3. The asset register — §A.14, binding, zero budget

I enumerated every third-party asset named anywhere in `build-sequence.md` and tried to break the
trace. **I could not. No off-register asset appears anywhere in the document.**

Paragon Rampage/Khaimera/Narbash → rows 1–2 · Game Animation Sample → row 3 · Paragon
Wraith/Gideon/Revenant/Murdock/Sparrow → row 4 · `SKM_Manny`/`SKM_Quinn`/`IK_Mannequin` → row 5 ·
MetaHuman → row 6, explicitly *not used* · ambientCG → row 7 · Poly Haven (HDRI, surfaces, props) →
row 8 · Infinity Blade packs → row 9 · Fab free drops → row 10 · Sonniss → row 11 · Freesound → row 12
· Infinity Blade Effects/Sounds → row 13 · Incompetech → row 14 · Cinzel/EB Garamond/UnifrakturMaguntia
→ row 15 · Kenney/ambientCG/Poly Haven CC0 paper + icons → row 16.

The exclusions are also carried correctly: step 0b's "Do not download" list reproduces §A.14's
rejected-sources table, including escalating AI text-to-3D to the commander as an academic-integrity
question rather than treating it as a build decision.

Two register-side nits, both minor and both listed as gaps below (G4, G5).

---

## 4. The designer's twelve "must not miss" items — enforced, not just listed

| # | Item | Genuinely enforced? | Where I found it |
|---|---|---|---|
| 1 | MCP first, nothing else starts | **Yes, with a documented override** | Step 0a is written as a hard gate; **0a.5 converts it to a soft gate after 30 July.** Assessed in §5.2. |
| 2 | Claim every A.14 asset + every Fab drop to 1 Sept | **Yes** | 0b table (all rows), 0c item 5 diary reminder, Appendix A row 10 "every 2 weeks to 1 Sept" |
| 3 | `Detect Neutrals` on **both** sense configs | **Yes — both** | 10.2 (sight, with the failure-mode quote) *and* 13.1 (hearing, "`Detect Neutrals` included") |
| 4 | Press `P`; `Dynamic`; agent 55/220 | **Yes** | 7.2/7.3/7.4, 16 ("Press `P`", re-confirm 55/220), 18.5, re-checked at 27 |
| 5 | `Observer Aborts: Both` | **Yes** | 10.5 (Chase, `Is Set TargetActor`) and 13.3 (Investigate) |
| 6 | Step 6 is a real gate; keep both cameras | **Yes** | 2.2 callout, 3, 6, and 28.1 "Neither camera is deleted" |
| 7 | Capsule from the real mesh before blockout | **Yes** | 8.7, 8.8, and step 15 opens "**Gated by step 8**" |
| 8 | 14b throwaway package in week 2 | **Yes** | Step 14b dated 10 Aug, "Do not move it", repeated in §1 calendar |
| 9 | Re-tune `Sight Radius` at 21 | **Yes** | 21.3, with a forward-pointer planted at 10.2 |
| 10 | `List of maps…` names both maps | **Yes, three times** | 14b.1, 24.5, 28.2 |
| 11 | TUNING vs LOCKED; wolf slower by a small margin | **Yes** | Step 14: "stays 10–30 units BELOW `SprintSpeed`" |
| 12 | Step 30 hard stop | **Yes** | Step 30 HARD STOP box + Phase 6 opening gate line. **But the guardrail table points at "Phase 8", which does not exist** — see D1. |

---

## 5. The two disclosed deviations — assessed

### 5.1 Step 4a (audio mix architecture) — **reasonable. Accept it.**

This is not scope creep and not drift. §A.13 opens with "**Mix architecture — set this up first, it
takes 20 minutes**", but §A.16 gives audio no step number until 11, while §A.16 step 4 requires
`BreathAudio` — which needs a `Sound Class` assigned. The brief contradicts its own ordering and 4a
resolves it in the direction the brief itself specifies. Every asset 4a creates (`SC_Master`,
`SC_Ambience`, `SC_SFX`, `SC_Creature`, `SC_UI`, `SC_Music`, `SM_Default`, `SM_Chase`, `ATT_Creature`,
`ATT_Prop`) appears in §A.1's folder tree and §A.13. Zero new scope, twenty minutes, correct place.

**One defect inside it:** 4a's last bullet says assign `BreathAudio` to "`SC_Player`-equivalent →
`SC_SFX`". `SC_Player` is not a class in §A.1 or §A.13. The sentence should simply read `SC_SFX`.
Trivial to fix, but it is a name that does not exist in the brief being introduced into a build step.

### 5.2 Step 0a (Unreal MCP) — **a real problem, and it is not the developer's to solve.**

The developer's handling is correct: it searched for prior configuration rather than inventing one,
refused to write `.mcp.json` itself (a configuration change an agent should not make unilaterally),
and wrote a dated fallback. That is the right behaviour. But the underlying situation is genuinely
unresolved and the commander should treat it as the top open risk:

- **The brief mandates a dependency it never specifies.** §0 and §A.16 step 0a require the MCP
  connection; no repo, plugin, transport or port is named anywhere in 1770 lines. `CLAUDE.md` calls
  it a build prerequisite that "was set up once before" — but no `.mcp.json` exists in the project.
- **Step 0a's body does not trace to the brief.** `Python Editor Script Plugin`, `Editor Scripting
  Utilities`, `Remote Control API`, port `30010`, the `.mcp.json` shape — none of these come from
  `design-brief.md`. They are plausible generic Unreal knowledge, and the developer flags the gap
  honestly, but a reader should know that this step is the one place in the document not backed by
  the brief.
- **0a.5 overrides a brief hard constraint.** "Nothing else can start" becomes "build it by hand
  after 30 July." I judge this the right trade against a 36-day deadline — MCP is an accelerator, not
  the deliverable — but it is a scope/constraint decision that belongs to the commander, and it is
  currently made inside a developer artefact.
- **The calendar is not re-baselined for the no-MCP branch.** Every phase length in §1 is inherited
  from the brief, which assumed MCP. Twenty-two of the 35 steps are tagged `MCP` or `MIXED`. If 0a.5
  fires, those become hand work and no day count in the plan changes. That is the schedule hole to
  watch, and the plan does not acknowledge it.
- Cosmetically, the document header (line 5) still asserts the build is "driven through an **Unreal
  MCP** server" while 0a.5 permits the opposite.

---

## 6. Gaps — brief decisions with no implementing step

| ID | Gap | Severity |
|---|---|---|
| **G1** | **§A.8 "How mismatched free assets are unified", mechanism 4 — consistent texel density (~3–5 cm per texel on hero surfaces)** — appears in no step. Mechanisms 1, 2, 3 and 5 all land (21.1, 21.2, 19.4/22.1, 22.1); 4 is dropped. The brief says mismatched texel density "reads as amateur even when nothing else is wrong", so this is a Form-quality item, not filler. Belongs in step 19 or 22. | **Low–moderate** — the only genuine Part A brief decision with no step at all. |
| **G2** | **§A "Definition of done" item 5 / §A.16 step 29 require a machine that never had the Unreal Editor installed.** Nothing in the sequence procures, books or identifies one, and Appendix C does not flag it. It is a physical dependency sitting on day 27 of 28 with a 4-day reserve behind it. The brief omits it too, but this was a flaggable gap the developer missed. | **Moderate as schedule risk** — a definition-of-done item with no owner. |
| **G3** | **§A.9 "If a clip is missing"** — the `IK Rig` + `IK Retargeter` route and the warning to prefer re-timing an existing clip over retargeting human animation onto a beast — is carried into no step. The brief names the exact case ("most likely Part B's lowered-profile pounce windup"), and step B4 calls for a "lowered-profile pose" without saying where the clip comes from. | **Low** — LATER scope only. |
| **G4** | **Kenney UI *sounds* have no clean register row.** §A.13 names "Freesound CC0 / Kenney CC0" as the UI-sound source, but §A.14's only Kenney row (16) covers "UI paper/vellum textures, simple icons". Step 25.4 cites row 16 for UI sounds. This originates in the brief, but Appendix A propagates it silently instead of flagging it. Row 12 (Freesound CC0) covers UI sounds cleanly, so the practical fix is to source UI sounds from row 12 only. | **Low** |
| **G5** | **Appendix A is a row-level trace, not the asset-level trace it claims.** The §A.13 catch sting (used at step 12.3) and the two Incompetech cues at their first *use* (step 17.8's win beat) do not appear in it, and step 12 cites no A.14 row for the sting. Both are register-traceable (rows 11/12/13 and row 14), so nothing off-register is imported — but the developer's leave-off claim that "Appendix A traces every referenced asset" is stronger than what the appendix does. | **Low** |

Nothing else in Part A is unimplemented. I checked §A.1 through §A.18 section by section, including
the folder contract (every asset in §A.1's tree is created by some step), all seven §A.6 navigation
items, all nine §A.7 layout properties, the full §A.7 actor table (each actor is placed at an
identifiable step), all five §A.11 lighting items, all five §A.12 widgets, the whole §A.13 content
list, all six §A.14 compliance obligations, all seven §A.17 breakages, and §A.18's narrative sockets
(placeholders only, no authored text — correct).

---

## 7. Defects that are not gaps

| ID | Defect |
|---|---|
| **D1** | **Phase numbers contradict themselves.** §0 (line 49), the §1 calendar row, and §2 guardrail 12 all call Part B/C "**Phase 8 and Phase 9**". The document's actual headers are **PHASE 6** and **PHASE 7**. The single most important gate in the plan — "nothing in Phase 8 or 9 may be started until Step 30 is signed off" — points at sections that do not exist. Fix the labels. |
| **D2** | Step 4a invents `SC_Player`, a `Sound Class` in neither §A.1 nor §A.13 (see §5.1). |
| **D3** | Step 11.3 introduces a `CreatureAudio` `Audio` component on `BP_Werewolf` that is not in the brief's `BP_Werewolf` spec. It is a necessary and obvious inference — but unlike the `DeathCam` inference at step 12, it is **not disclosed** in Appendix C. |
| **D4** | Step 5 creates `/Game/Player/BS_Player_Locomotion`, a path not in §A.1's folder contract, which §0 calls "explicit and final". Harmless, but the contract should be amended rather than silently extended. Step 4.5 similarly invents the tag `Footstep_Walk` (the brief gives no walk tag). |
| **D5** | Step 17.8 stages the win music cue at step 17, but the Incompetech cues are not imported until step 25. The beat will be silent for eight steps. Harmless if known; worth a note in the step. |
| **D6** | Appendix C item 4 says step 4a is "the one place I added a numbered step the brief did not have". **Step 0c is a second one.** 0c traces cleanly to §A.14's compliance obligations so it is not an orphan, but the disclosure undercounts. |

---

## 8. MVP and deadline sanity

**Arithmetic checks out.** 27–30 Jul (4) pre-production, then 31 Jul – 3 Aug (4) + 4–10 Aug (7) +
11–18 Aug (8) + 19–24 Aug (6) + 25–27 Aug (3) = **28 days**, matching the brief's 28-day Part A
window, with the 28–31 Aug reserve intact ahead of 1 September. The two lost pre-production days are
absorbed by compressing downloads, not by moving the 31 July start — correct call, since 0b is the
only genuinely compressible work in Phase 0.

**Nothing labelled LATER is load-bearing for the MVP loop.** I checked all of Part B against the
commander's MVP definition (explore a mansion, a werewolf pursues, escape or get caught): scent trail,
scent states, odor masking, hiding place, pounce, flintlock/silver, safe haven and autosave are each
removable without breaking the loop. In Part A the wolf hunts on **sight + hearing** (steps 10, 13),
which is sufficient for a predator that patrols, notices, chases and catches. Deferring scent — the
game's headline conceit — is a real concession, but it is one the brief makes explicitly (§A.3 "Scope
decision") and one `CLAUDE.md` endorses by name. **No LATER item needs promoting.**

**Three deadline risks, in order:**

1. **MCP (§5.2).** Gates everything, unproven, and the calendar assumes it works. Decision needed
   before 30 July.
2. **A third-person verdict at step 6 over-subscribes Phases 3 and 4.** §A.10 prices TP at 3–5 extra
   Form days. Step 26 sits inside a 6-day Phase 4 that already holds steps 23, 24, 25 and 27. The plan
   handles this with one sentence — "Take the days out of Phase 3's dressing time, not out of the
   reserve" — which is honest but means a TP verdict roughly halves the step-22 dressing budget in a
   deliverable whose whole revision-2 premise is that it must not look grey-box. The commander should
   pre-agree what gets cut *before* step 6 returns its verdict, not after.
3. **No end-to-end playable loop exists until step 17 (~15 August).** Steps 1–14b give chase, catch
   and game over; the win path (key → escape door) does not exist until day 16 of 28, and the first
   packaged *complete* build is step 28 on 25–27 August. Step 14b's 10 August throwaway package
   mitigates the packaging half of this well — it is the single best decision in the schedule and it
   must not move. But the loop-completeness half is unmitigated. If the commander wants earlier
   insurance, the cheap move is to stub `BP_KeyItem` + `BP_EscapeDoor` in `L_Sandbox` during Phase 2;
   it costs under half a day and buys a demonstrable win condition three weeks before the deadline.

**Phase 3 is the densest slab of hand work in the plan** — 8 days for an 8–10 room blockout, five
master materials, a full lighting pass, a post-process/fog grade and complete set dressing with 30+
decals and 10+ Niagara systems, for one person. It is not obviously wrong, but it is where slippage
will first show, and it is also the reserve that step 6's TP branch is told to raid.

---

## 9. What the commander should act on first

1. **Resolve MCP or invoke 0a.5 deliberately, before 30 July.** If it goes to the fallback, re-baseline
   the phase day-counts for hand work — the plan does not do this for you.
2. **Fix D1** (Phase 8/9 → Phase 6/7). It is a one-line edit in the most load-bearing guardrail in the
   document.
3. **Assign an owner and a date for the clean machine (G2)** — it is a definition-of-done item sitting
   on day 27 with nobody holding it.
4. **Decide the TP contingency now**, so step 6's verdict does not silently eat step 22.
5. **G1, G3, G4, G5, D2–D6 are small** and can be folded into the next developer pass without
   reopening the brief.
