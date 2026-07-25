# Design Brief — Capstone Werewolf

**Revision 2 — Form + Function.** Supersedes revision 1. Revision 1's systems work is preserved;
what changed is **scope structure**: Part A is now a *finished-looking* working game, not a
grey-box one, and art/audio/UI interleave into the build order rather than being deferred.

**Author:** designer agent · **Consumes:** `project-brief.md` · **Consumed by:** developer agent
**Engine target:** Unreal Engine 5 (5.4+), **Blueprint-only**. No C++ anywhere in this brief.
**Date of pass:** 25 July 2026 · **Hard deadline:** 1 September 2026 (38 days)

---

## 0. How to read this document

| Part | Status | What it is |
|---|---|---|
| **PART A — THE DELIVERABLE** | **BUILD THIS. Nothing may block it.** | A **finished-looking, working** game: explore a styled mansion interior, a werewolf actively pursues, reach the escape (win) or be caught (game over) — and it **looks and sounds like a game**, and it **ships as a packaged `.exe`**. This is the 1 September commitment. |
| **PART B — STRETCH** | Do **not** start until Part A is done **and a packaged build exists**. Abandonable in full. | GDD "Risk prototype" items beyond the core loop: scent trail, high-scent threshold, odor masking, one hiding place, one pounce, one firearm, one safe haven + autosave. |
| **PART C — RECORDED, NOT SCHEDULED** | Off the critical path. Written down so nothing from `project-brief.md` is lost. | Full werewolf state set, silver/gunpowder economy, puzzle chains, 3–5 areas, narrative, charge counterplay, art beyond Part A's bar. |

If unsure whether to build something: **does it appear in Part A?** If no, it waits.

### Part A has two tracks and they interleave

| Track | Tag | Covers |
|---|---|---|
| **Function** | `[FN]` | Movement, AI perception, behaviour tree, navigation, catch → game over, key → escape → win. |
| **Form** | `[FORM]` | Character design, environment styling, materials, lighting, post-process, VFX, UI, audio, packaging. |

**Form is not a final-week bolt-on.** The build order (A.16) alternates `[FN]` and `[FORM]` so that
at every checkpoint the game both works and looks progressively less like a prototype. A grey-box
build with a default mannequin and white UI is **not an acceptable deliverable**.

Form is anchored, not decorative. Every `[FORM]` item traces to **Pillar 4 *Atmospheric
Discovery*** ("architecture, objects, and sound communicate layout, puzzles, and history without
constant objective markers") or **Pillar 2 *Readable Lethality*** ("the player can explain why a
capture happened" — impossible if they cannot see or hear the werewolf). Legibility is a gameplay
requirement here, which is why styling is Part A and not Part C.

### HARD CONSTRAINT — $0 budget

**No purchases. None.** Two legal sources of art and audio only:

1. **Assets we author ourselves.**
2. **Genuinely free assets by others**, where the licence permits use in a student capstone that
   will be submitted and may be shown publicly.

Section **A.14** is the binding register. **Do not import anything not in A.14 or not satisfying
A.14's rules.**

### Things this brief deliberately does NOT decide

- **Perspective (first vs third person).** Still **PROVISIONAL**. Both cameras exist and toggle at
  runtime. The comparison is an explicit project deliverable and is **scheduled early** (build
  step 6) because the two branches have *different Form costs* (A.10). Do not delete either camera;
  do not resolve it silently in code.
- **Mansion vs castle.** Napoleonic Gothic (A.8) is a *look*, valid for both.
- **Narrative** (protagonist, why trapped, werewolf origin, safe-haven fiction, ending). A.18 marks
  the sockets. Do not author story text.
- **Individual puzzle solutions.** C.3 gives the framework only.
- **Numbers.** `TUNING START` = a first-playable starting value; change freely. `LOCKED` = from
  `project-brief.md`; may not be changed.

### Notes for MCP-driven Blueprint work

- Prefer **component defaults and property values** over long node graphs. Most Part A behaviour is
  properties on standard components (AI Perception, Character Movement, Nav Mesh, Post Process).
- Keep graphs **shallow**: small named functions. Where a graph is unavoidable, nodes are listed in
  execution order so they can be created linearly.
- Asset paths below are **explicit and final**; Parts B and C reference them by path.
- `Backticks` = the name **as it appears in the Unreal editor**. The appendix lists every one used.
- **Some Form work is not MCP work.** Importing a character, setting up an `IK Retargeter`, dressing
  a room, grading a `Post Process Volume` are hands-on tasks with visual judgement. Budget them as
  such; do not assume they can be scripted blind.

### Calendar

| Window | Days | Purpose |
|---|---|---|
| 25 – 30 July | 6 | **Pre-production.** Re-establish the Unreal MCP connection. Acquire and licence-log every free asset (A.14). No feature work. |
| 31 July – 27 August | 28 | **Part A**, both tracks, per A.16. |
| 28 – 31 August | 4 | **Reserve.** Packaging repair, final playtest, README + CREDITS, submission. Not feature time. |

A first Unreal package reliably breaks something, so A.17 requires a **throwaway package smoke test
in week 2** — the reserve is repair time, not discovery time.

---
---

# PART A — THE DELIVERABLE

**Definition of done — all five must be true:**

1. **It works.** Packaged build launches → styled title screen → walk and sprint a mansion
   interior → hunted by a werewolf that patrols, notices, and chases → find a key → open the escape
   door → win screen. Contact → game-over screen → restart.
2. **It looks finished.** No default grey material anywhere. No default mannequin as the werewolf.
   Deliberate palette, deliberate lighting, fog, post-process grade, dressed rooms.
3. **It sounds finished.** Room ambience with per-room reverb, footsteps, three audibly distinct
   werewolf states, UI sounds, two music cues.
4. **The UI is styled.** Period typography, no pure white, framed panels, fades, title screen,
   credits screen.
5. **It ships.** A packaged Windows build that runs on a machine that never had the editor.

Anchors: `project-brief.md` §"Build priority" item 1; Win/Lose **LOCKED**; Pillars 1, 2, 4.

## A.1 Project skeleton `[FN]`

Project `CapstoneWerewolf`. Blueprint project. **Use the Third Person template**, not Blank — it
ships `SKM_Manny`, `SKM_Quinn`, `IK_Mannequin` (the IK Rig every retarget in A.9/A.10 starts from)
and a working locomotion `Animation Blueprint`. Starting Blank throws away days of free work.

```
/Game/
├── Core/  GM_Werewolf (Game Mode Base) · GI_Werewolf (Game Instance) · PC_Werewolf (Player Controller)
│   └── Enums/  E_WolfState (Blueprint Enumeration)
├── Input/ IMC_Default · IA_Move (Axis2D) · IA_Look (Axis2D) · IA_Sprint · IA_Crouch · IA_Interact
│         · IA_TogglePerspective  [dev tool]
├── Player/  BP_PlayerCharacter (Character) · ABP_Player (Animation Blueprint)
├── Werewolf/ BP_Werewolf (Character) · BP_WerewolfController (AIController) · ABP_Werewolf
│         · BS_Werewolf_Locomotion (Blend Space 1D) · BB_Werewolf · BT_Werewolf
│   └── Tasks/  BTT_FindPatrolPoint · BTT_SetWolfState   (BTTask_BlueprintBase)
├── World/  BP_Interactable (Actor, base) · BP_KeyItem · BP_EscapeDoor · BP_Door
│         · BP_Candle · BP_Sconce · BP_Hearth
├── UI/  WBP_TitleScreen · WBP_GameOver · WBP_Escaped · WBP_Prompt · WBP_Credits
│   └── Style/  F_Cinzel (Font) · F_EBGaramond (Font) · T_Panel_Vellum
├── Art/
│   ├── Materials/  M_Stone · M_Plaster · M_Wood_Dark · M_Metal_Tarnished · M_Fabric
│   │   ├── Instances/  MI_*  (every mesh in the level uses one of these)
│   │   └── Decals/  M_Decal_Stain · M_Decal_Soot · M_Decal_Scuff · M_Decal_Claw · M_Decal_Blood
│   ├── Textures/   imported CC0 surfaces (ambientCG / Poly Haven)
│   ├── Blockout/   SM_Blockout_*  (the modular grid set, A.7)
│   └── VFX/        NS_DustMotes · NS_CandleFlame · NS_Embers · NS_ColdBreath
├── Audio/  Ambience/ Creature/ Player/ UI/ Music/
│   ├── Classes/     SC_Master · SC_Ambience · SC_SFX · SC_Creature · SC_UI · SC_Music
│   ├── Mixes/       SM_Default · SM_Chase
│   └── Attenuation/ ATT_Creature · ATT_Prop
├── Sourced/  ← ALL third-party assets, one folder per source (Paragon_Rampage/, GameAnimationSample/, …)
└── Maps/  L_Title · L_Mansion_Slice · L_Sandbox
```

> **`/Game/Sourced/` is a licence-compliance mechanism, not tidiness.** One folder per source means
> `CREDITS.md` and `WBP_Credits` can be assembled by reading folder names, and an asset with a
> licence problem can be pulled without hunting. Never import a sourced asset straight into `/Art/`.

`Project Settings → Maps & Modes`: `Default GameMode` = `GM_Werewolf`, `Default Pawn Class` =
`BP_PlayerCharacter`, `Player Controller Class` = `PC_Werewolf`, `Game Instance Class` =
`GI_Werewolf`, `Editor Startup Map` = `L_Sandbox`, **`Game Default Map` = `L_Title`**.

`Project Settings → Rendering` — set once at project creation; changing later invalidates lighting work:

| Setting | Value | Why |
|---|---|---|
| `Dynamic Global Illumination Method` | `Lumen` | dark interiors lit by practicals, no bake step — we have no time to bake |
| `Reflection Method` | `Lumen` | wet stone and varnished wood need reflections to read |
| `Shadow Map Method` | `Virtual Shadow Maps` | crisp candle shadows; the A.8 silhouette read depends on it |
| `Anti-Aliasing Method` | `TSR` | default |
| `Default RHI` | `DirectX 12` | required by Lumen / VSM |
| `Extend default luminance range for Auto Exposure` | on | needed for the A.11 exposure lock |

## A.2 Player character — `/Game/Player/BP_PlayerCharacter` `[FN]`

Parent: `Character`. Anchors: Scent/stamina **LOCKED core** (stamina half ships in Part A, scent
half in Part B); Perspective **PROVISIONAL**.

```
CapsuleComponent (root, inherited)
├── Mesh (inherited SkeletalMeshComponent)
│   └── Camera_FP            (Camera)   Parent Socket: head
├── SpringArm_TP             (SpringArmComponent)
│   └── Camera_TP            (Camera)
├── InteractTrace            (SceneComponent)
├── BreathAudio              (Audio)    stamina readout
└── AIPerceptionStimuliSource (AIPerception Stimuli Source)
```

- `AIPerception Stimuli Source`: `Auto Register as Source` = **true**; `Register as Source for
  Senses` = `AISense_Sight`, `AISense_Hearing`. Explicit even though Pawns auto-register for sight.
- `SpringArm_TP`: `Target Arm Length` 300 `TUNING START`, `Socket Offset` Z 60, `Do Collision Test`
  true, `Use Pawn Control Rotation` true, `Camera Lag` ~0.1.
- `Camera_FP`: `Use Pawn Control Rotation` true, on the mesh's `head` socket, offset ~(0, 15, 0).

### Keeping perspective swappable (do not resolve this)

- Variable `bFirstPerson` (Boolean, `Instance Editable`, default true `TUNING START` — a coin-flip
  for testing, **not** a decision).
- Function `ApplyPerspective`, called from `Event BeginPlay` and the `IA_TogglePerspective` handler:
  1. `Branch` on `bFirstPerson`.
  2. True: `Activate` `Camera_FP`; `Deactivate` `Camera_TP`; **`Set Owner No See` on `Mesh` = true**
     (better than `Set Hidden In Game` — the body still casts a shadow, a free and convincing
     first-person detail); `Set Use Controller Rotation Yaw` (self) = true;
     `Character Movement → Orient Rotation to Movement` = false.
  3. False: the inverse — `Activate` `Camera_TP`, `Deactivate` `Camera_FP`, `Set Owner No See` =
     false, `Use Controller Rotation Yaw` = false, `Orient Rotation to Movement` = true,
     `Rotation Rate` = (0, 540, 0).
- `IA_TogglePerspective` (key `V`) is a **development tool** so the same sequence can be played in
  both perspectives and compared. Gate it behind `bAllowPerspectiveToggle` before packaging.

### Movement and stamina

| `Character Movement` property | Value | Note |
|---|---|---|
| `Max Walk Speed` | 220 | `TUNING START` |
| `Max Walk Speed Crouched` | 120 | `TUNING START` |
| `Can Crouch` | true | enables `Crouch` / `UnCrouch` |
| `Crouched Half Height` | 45 | `TUNING START` |
| `Jump Z Velocity` | 0 | **No jump.** Vertical traversal is authored, not player-driven. |
| `Air Control` | 0.1 | default |

Sprint is a speed override, not a mode:

- Variables: `Stamina` (100), `MaxStamina` (100), `bSprintHeld`, `SprintSpeed` (480), `WalkSpeed`
  (220), `StaminaDrainPerSec` (18), `StaminaRegenPerSec` (12), `StaminaRegenDelay` (1.5) — all
  `TUNING START`.
- `IA_Sprint` `Started` → `bSprintHeld` = true; `Completed` → false.
- `Event Tick` → `TickStamina(DeltaSeconds)`:
  1. `Branch`: `bSprintHeld` AND `Stamina > 0` AND `Get Velocity → Vector Length > 10`.
  2. True: `Set Max Walk Speed` = `SprintSpeed`; `Stamina -= StaminaDrainPerSec * Delta`;
     `Clamp (float)` 0..`MaxStamina`.
  3. False: `Set Max Walk Speed` = `WalkSpeed`; after `StaminaRegenDelay` since last drain,
     `Stamina += StaminaRegenPerSec * Delta`, clamped.
  4. At `Stamina` 0, force `bSprintHeld` = false so the player must re-press (readable, Pillar 2).

**Readable stamina without a HUD bar** (Pillar 4 — "without constant objective markers"; also saves
the UI-art time A.12 needs elsewhere):
- `BreathAudio` looping; drive `Set Volume Multiplier` / `Set Pitch Multiplier` from
  `1 - (Stamina / MaxStamina)` inside `TickStamina`.
- A `Post Process Component` on the character driving `Vignette Intensity` from the same ratio,
  blend weight ~0.4 so it layers over the global grade rather than fighting it.
- Numeric readout only behind `bShowDebugHUD` via `Print String`. **`Print String` is compiled out
  of Shipping builds** — never let real behaviour depend on it. No shipping stamina bar.

### Sprinting is audible — this is Part A's whole detection story

Hearing is Part A's only long-range sense. In `TickStamina`, on the sprint branch, call
`Report Noise Event` (**AI → Perception**) at most every 0.35 s `TUNING START` via an accumulated
float: `Noise Location` = `Get Actor Location`, `Loudness` 1.0, `Instigator` self, `Max Range` 1800,
`Tag` `Footstep_Sprint`. Walking: `Loudness` 0.3, `Max Range` 600. Crouching: nothing.
Anchor: "Hearing = authored range (investigates sprinting…)".

### Enhanced Input

`Event BeginPlay`: `Get Controller` → `Cast To PlayerController` → `Get Local Player` →
`Get Subsystem` (`EnhancedInputLocalPlayerSubsystem`) → `Add Mapping Context` (`IMC_Default`,
Priority 0) → `ApplyPerspective`.

| Input Action | Keys | Modifiers / Triggers |
|---|---|---|
| `IA_Move` | W/S/A/D, Gamepad Left Thumbstick 2D-Axis | W: `Swizzle Input Axis Values` (YXZ); S: `Swizzle` + `Negate`; A: `Negate`; D: none |
| `IA_Look` | Mouse XY 2D-Axis, Right Thumbstick | Mouse Y: `Negate` |
| `IA_Sprint` | Left Shift, Left Shoulder | — |
| `IA_Crouch` | Left Ctrl / C, Face Button Right | — |
| `IA_Interact` | E, Face Button Bottom | — |
| `IA_TogglePerspective` | V | dev tool; disable before packaging |

`IA_Move`: `Get Action Value` → `Break Vector 2D` → `Add Movement Input` ×2 using
**control-rotation-derived** forward/right vectors, so one graph is correct in both perspectives.
`IA_Look`: `Add Controller Yaw Input` (X), `Add Controller Pitch Input` (Y).
`IA_Crouch` `Started`: `Branch` on `Is Crouched` → `UnCrouch` / `Crouch`.

### Interaction

`IA_Interact` `Started` → `TryInteract`: `Get Actor Eyes View Point` → `Line Trace By Channel`
(`Visibility`, End = Start + Forward × 250 `TUNING START`) → `Break Hit Result → Hit Actor` →
`Cast To BP_Interactable` → call its `Interact` with `Instigator` = self.
Prompt: same trace on a `Set Timer by Event` at 0.1 s, showing/hiding `WBP_Prompt` with the
interactable's `PromptText`. Styling and copy rules in A.12.

## A.3 Werewolf — sensory model `[FN]`

Anchors: Pillar 1 (actively searches and tracks; not a scripted-scene monster); Sensory hierarchy
(Sight = line of sight, Hearing = authored range, Smell = primary otherwise).

**Scope decision:** smell is the primary sense per `project-brief.md`, but the scent *simulation* is
explicitly secondary. Part A runs on **Sight + Hearing only**; Part B's scent system plugs into the
*same* Blackboard keys and Behavior Tree, so nothing is rebuilt (B.1 specifies the seam).

### `AI Perception` lives on the AI Controller

Add `AI Perception` to `BP_WerewolfController` — not the pawn. The controller outlives possession
and is where `Run Behavior Tree` and the Blackboard live. Add two `Senses Config` entries:

**`AI Sight config`**

| Property | Value |
|---|---|
| `Sight Radius` | 2000 `TUNING START` |
| `Lose Sight Radius` | 2600 `TUNING START` (must exceed Sight Radius or the wolf flickers) |
| `Peripheral Vision Half Angle Degrees` | 70 `TUNING START` (140° cone) |
| `Auto Success Range from Last Seen Location` | 400 `TUNING START` |
| `Max Age` | 5.0 `TUNING START` |
| `Detection by Affiliation → Detect Enemies / Neutrals / Friendlies` | true / **true** / true |

> **Known failure mode.** Actors with no Team ID default to **Neutral**. With `Detect Neutrals`
> unchecked the werewolf never sees the player and the AI looks completely broken. This is the
> single most common cause of "AI Perception does nothing".

> **Second failure mode, specific to this game.** `Sight Radius` 2000 is a maximum, not a guarantee
> of fairness: in A.11's dark, fog-filled interior the player is often invisible to the *human eye*
> at 2000 units while the AI sees perfectly. That is a Pillar 2 violation — the player cannot
> explain a capture they never saw coming. **Tune `Sight Radius` against the final lighting, not the
> grey-box**, and if they disagree, shorten the radius. This is exactly why lighting is in Part A.

**`AI Hearing config`**: `Hearing Range` 1500 `TUNING START`, `Max Age` 4.0 `TUNING START`,
`Detection by Affiliation` all true.

Set `Dominant Sense` = `AISense_Sight` `TUNING START` so a confirmed visual overrides a stale noise.
(In Part B this is where sight > hearing > smell is expressed explicitly.)

### Reacting to perception

Bind `On Target Perception Updated (AIPerception)`:

1. `Cast To BP_PlayerCharacter` from `Actor`; fail → return.
2. `Break AIStimulus` on `Stimulus` → `Successfully Sensed`, `Stimulus Location`, `Type`.
3. Decide the sense with **`Line Of Sight To`** (an `AIController` node) against the player: true →
   visual, false → noise. Behaves identically to inspecting `Type` for Part A and avoids awkward
   sense-ID comparison through MCP.
4. **Sight (`Successfully Sensed` true, line of sight true):** Blackboard `Set Value as Object`
   `TargetActor` = player; `Set Value as Bool` `bHasVisual` = true; `Set Value as Vector`
   `LastKnownLocation` = player location; `Set Value as Enum` `WolfState` = `Chase`; `Set Focus`.
5. **Sight lost (`Successfully Sensed` false):** `bHasVisual` = false; `LastKnownLocation` =
   `Stimulus Location`; `WolfState` = `Investigate`; `Clear Focus`. **Do not clear `TargetActor`
   immediately** — short memory is what makes the predator persistent (Pillar 1).
6. **Hearing:** `LastKnownLocation` = `Stimulus Location`; `WolfState` = `Investigate`. Do not set
   `bHasVisual`.

Blackboard access from the controller: `Get Blackboard` → `Set Value as Object` / `as Vector` /
`as Bool` / `as Enum` / `Clear Value`.

### Memory decay and `ResetToPatrol`

`Set Timer by Event` (looping, 0.5 s) → `DecayMemory`: if `bHasVisual` is false and `WolfState` is
`Investigate`, increment `SearchTimer`; past `GiveUpTime` = 12.0 `TUNING START`, call
`ResetToPatrol`. Any fresh stimulus resets `SearchTimer` to 0.

**`ResetToPatrol`** on `BP_WerewolfController` — write it once, here: `Clear Value` `TargetActor`;
`bHasVisual` = false; `Clear Value` `LastKnownLocation`; `WolfState` = `Patrol`; `SearchTimer` = 0;
`Clear Focus`. Part B's safe haven (B.5) calls the *same* function.

## A.4 Werewolf — state model `[FN]`

### `E_WolfState` — `/Game/Core/Enums/E_WolfState`

Part A enumerators (create exactly these three now):

| Enumerator | Meaning |
|---|---|
| `Patrol` | Random patrol of navigable space. Anchors "random patrol" in the LOCKED state list. |
| `Investigate` | Move to `LastKnownLocation` and look around. Covers *sound investigation* and *lost visual*. |
| `Chase` | Confirmed visual; run at `TargetActor`. Covers *visual chase*. |

**Add these now but leave them unused** so Parts B/C slot in without renumbering or invalidating
saved assets: `ScentPursuit`, `PouncePrep`, `Pounce`, `Charge`, `SearchHiding`, `Staggered`,
`Unconscious`. (The rest of the LOCKED state list. Declaring early costs nothing and prevents an
enum migration.) `E_WolfState` is also the **animation and audio switch** (A.9, A.13).

*Catch* is **not** a state — it is an overlap event (A.5). Keeping it out of the state machine means
it can never be blocked by a mis-transition, which matters because capture is an immediate game over.

### `BB_Werewolf` — Blackboard keys

| Key | Type | Set by | Used by |
|---|---|---|---|
| `TargetActor` | Object (`Actor`) | perception handler | Chase branch |
| `LastKnownLocation` | Vector | perception handler, decay | Investigate branch |
| `PatrolLocation` | Vector | `BTT_FindPatrolPoint` | Patrol branch |
| `bHasVisual` | Bool | perception handler | Chase decorator |
| `WolfState` | Enum (`E_WolfState`) | perception handler, tasks | decorators, animation, audio |
| `HomeLocation` | Vector | controller `On Possess` | patrol radius origin |

`Instance Synced` off for all keys (single AI in Part A).

### `BP_WerewolfController`

Parent: `AIController`. Components: `AI Perception` (A.3). `Event On Possess` (not BeginPlay — the
pawn is guaranteed valid), in order:
1. `Run Behavior Tree` with `BTAsset` = `BT_Werewolf`. This creates the Blackboard Component from
   the Blackboard assigned inside `BT_Werewolf` — do **not** add a Blackboard component manually.
2. `Get Blackboard` → `Set Value as Vector` `HomeLocation` = `Get Controlled Pawn → Get Actor Location`.
3. `Set Value as Enum` `WolfState` = `Patrol`.
4. Start the `DecayMemory` looping timer.

Optionally `Set Generic Team Id` = 1 on the controller, but **keep `Detect Neutrals` true
regardless** — do not rely on team setup working first try.

### `BT_Werewolf`

Assign `Blackboard Asset` = `BB_Werewolf` in the Behavior Tree Details panel.

```
ROOT
└── Selector  "Brain"
    ├── Sequence  "Chase"
    │     ├─ Decorator: Blackboard   Key Query: Is Set, Key: TargetActor
    │     │                          Observer Aborts: Both   Notify Observer: On Value Change
    │     ├─ Decorator: Blackboard   Key Query: Is Equal To, Key: bHasVisual, Value: true
    │     │                          Observer Aborts: Self   Notify Observer: On Value Change
    │     ├─ Task: BTT_SetWolfState  (NewState = Chase)
    │     └─ Task: Move To           Key: TargetActor, Acceptable Radius: 60,
    │                                Observe Blackboard Value: true
    ├── Sequence  "Investigate"
    │     ├─ Decorator: Blackboard   Key Query: Is Set, Key: LastKnownLocation
    │     │                          Observer Aborts: Both   Notify Observer: On Value Change
    │     ├─ Task: BTT_SetWolfState  (NewState = Investigate)
    │     ├─ Task: Move To           Key: LastKnownLocation, Acceptable Radius: 100
    │     ├─ Task: Wait              Wait Time: 2.0  Random Deviation: 1.0
    │     └─ Task: BTT_SetWolfState  (NewState = Patrol, ClearLastKnown = true)
    └── Sequence  "Patrol"
          ├─ Task: BTT_SetWolfState  (NewState = Patrol)
          ├─ Task: BTT_FindPatrolPoint
          ├─ Task: Move To           Key: PatrolLocation, Acceptable Radius: 80
          └─ Task: Wait              Wait Time: 2.0  Random Deviation: 1.5
```

All **stock** nodes except two tiny custom tasks — deliberate, for speed through MCP.
The `Observer Aborts` settings are what make the werewolf persistent rather than scripted
(Pillar 1). Without them the wolf finishes its patrol walk before reacting, which reads as a
scripted monster and violates Pillar 1 directly.

**`BTT_FindPatrolPoint`** (`BTTask_BlueprintBase`):
1. `Event Receive Execute AI` → `Controlled Pawn`.
2. `Get Blackboard Value as Vector` (`HomeLocation`).
3. **`Get Random Reachable Point in Radius`**: `Origin` = `HomeLocation`, `Radius` = 4000
   `TUNING START`. Use this, **not** `Get Random Point in Navigable Radius` — the former guarantees
   a path exists from the origin, preventing the wolf picking a point across an unlinked gap and
   stalling.
4. `Branch` on the return bool → `Set Blackboard Value as Vector` (`PatrolLocation`) →
   `Finish Execute` (Success true); else `Finish Execute` (Success false).

**`BTT_SetWolfState`** (`BTTask_BlueprintBase`, instance-editable inputs `NewState` (`E_WolfState`)
and `ClearLastKnown` (Boolean, default false)):
1. `Event Receive Execute AI` → `Get AI Controller → Get Blackboard` → `Set Value as Enum` (`WolfState`).
2. Set the pawn's `Max Walk Speed` from the table below **and** call a custom event
   `OnWolfStateChanged(NewState)` on `BP_Werewolf`. That one event drives **animation** (A.9) and
   **audio** (A.13) — one hook, two Form systems.
3. If `ClearLastKnown`: `Clear Value` `LastKnownLocation` and `TargetActor`.
4. `Finish Execute` (Success true).

### `BP_Werewolf` — the pawn

Parent: `Character`. `AI Controller Class` = `BP_WerewolfController`; `Auto Possess AI` =
`Placed in World or Spawned`.

**Mesh, skeleton, animation set and capsule come from a sourced free asset chosen in A.9. They are
not placeholder and not deferred — A.9 is a Part A section.**

`Capsule Component`: `Capsule Half Height` **110**, `Capsule Radius` **55** `TUNING START`, taken
from the chosen character's real proportions. These **propagate**: Nav Mesh agent settings (A.6) →
minimum doorway width → the modular grid (A.7). Set them at build step 8, before blockout.

| `WolfState` | `Max Walk Speed` | Rationale |
|---|---|---|
| `Patrol` | 200 `TUNING START` | slow, audible, gives reading time |
| `Investigate` | 320 `TUNING START` | purposeful, still escapable |
| `Chase` | 460 `TUNING START` | **below** the player's sprint (480) |

> **460 vs 480 is a design decision, not an accident.** A sprinting player outruns the werewolf
> *slowly*: escape is possible but costs all their stamina — and in Part B sprinting is exactly what
> creates the high-scent trail that brings the wolf back. Pillar 5 *Temporary Relief* expressed as
> two numbers. Keep the gap 10–30 units. Faster wolf = unwinnable; much slower = not a predator.

> **Tune these after the animated mesh is in** (step 8, before step 14). A large creature at
> 460 uu/s foot-skates badly unless the `Blend Space` sample speeds match. Speed tuning and
> animation play-rate tuning are the same job; doing them separately means doing them twice.

## A.5 Catch → game over, escape → win `[FN]`

Both **LOCKED**: win = leave the location; lose = immediate game over on physical contact, no
health bar.

### Catch (lose)

`Sphere Collision` on `BP_Werewolf` named `CatchSphere`: `Sphere Radius` 110 `TUNING START`
(capsule radius plus a lunge's reach); `Collision Presets` `Custom`; `Collision Enabled`
`Query Only (No Physics Collision)`; Object Type `Pawn`; `Overlap` for `Pawn`, `Ignore` everything
else; `Generate Overlap Events` true.

`On Component Begin Overlap (CatchSphere)`: `Cast To BP_PlayerCharacter` (fail → return) → guard on
a bool `bCaught` (`Branch`; return if true, else set true) → `Get Game Mode` → `Cast To GM_Werewolf`
→ `OnPlayerCaught(Player)`.

`GM_Werewolf → OnPlayerCaught(Player)`:
1. `Disable Input` on the player.
2. `Set Ignore Move Input` / `Set Ignore Look Input` = true on `PC_Werewolf`.
3. **The death beat** — 1.2 s `Delay` `TUNING START` during which: `Set View Target with Blend` to a
   `Camera Actor` on the werewolf (or force the player's look toward it), the catch audio sting, and
   a fade to black via `Widget Animation`. **This beat is Form work that is also Pillar 2 work** —
   showing the player *what* got them is how they explain the capture. Do not cut straight to a menu.
4. `Create Widget` (`WBP_GameOver`) → `Add to Viewport` → `Play Animation`.
5. `Set Input Mode UI Only` (`In Widget to Focus` = the widget); `Set Show Mouse Cursor` = true.
6. `Set Game Paused` = true (target: the player controller).

`WBP_GameOver`: title (placeholder wording — final copy is narrative TBD), `Restart`, `Main Menu`,
`Quit`. Styling in A.12.
- `Restart`: `Set Game Paused` false → `Get Current Level Name` → `Open Level (by Name)`.
  (Part B replaces this with a load from the safe-haven autosave.)
- `Main Menu`: `Open Level (by Name)` `L_Title`. `Quit`: `Quit Game`.

### Escape (win)

`BP_KeyItem` (child of `BP_Interactable`): `Interact` → `bHasEscapeKey` = true on `GI_Werewolf`
(Game Instance, so it survives Part B's reload) → `Destroy Actor` → a diegetic acquisition cue (a
short `WBP_Prompt` line plus a sound; no inventory pop-up — Pillar 4).

`BP_EscapeDoor` (child of `BP_Interactable`): `Interact` →
1. `Get Game Instance` → `Cast To GI_Werewolf` → `Branch` on `bHasEscapeKey`.
2. False: set `PromptText` to a diegetic refusal ("the bar is fixed fast — something must lift it")
   and return. **No objective marker, no quest text** (Pillar 4).
3. True: door opens (`Timeline` rotating the mesh) → `Get Game Mode` → `Cast To GM_Werewolf` →
   `OnPlayerEscaped`.

`GM_Werewolf → OnPlayerEscaped`: same shape with `WBP_Escaped`, and the opposite Form beat — the
door swings, cold moonlight and fog pour in, the win music cue (A.13) starts, then the widget fades
up. **The win needs a visual payoff or it reads as a bug.**

**This one-key/one-door structure is deliberately the degenerate case of the puzzle framework**
(C.3): the escape door asks the world a question; something elsewhere answers it. Part C replaces
`bHasEscapeKey` with a multi-step chain without touching `BP_EscapeDoor`'s shape.

## A.6 Navigation `[FN]`

Anchors: "Travels all zones, opens doors, climbs authored nav links" (LOCKED state list).

1. **`Nav Mesh Bounds Volume`** enclosing the playable interior plus margin. A
   `RecastNavMesh-Default` actor appears in the Outliner. Press **`P`** to visualise the navmesh —
   after *every* level edit. Unbuilt navmesh is the #1 cause of "the AI doesn't move".
2. **`RecastNavMesh-Default`**: `Runtime Generation` = **`Dynamic`** (doors move; Parts B/C add
   dynamic obstacles).
3. **`Project Settings → Navigation Mesh`**: `Agent Radius` **55**, `Agent Height` **220**
   `TUNING START`, matching A.4/A.9. **This is the number that sizes the architecture.** A doorway
   needs at least `2 × AgentRadius` plus margin of clear width or no navmesh generates through it
   and the werewolf silently cannot follow — which looks like broken AI and is actually broken
   geometry. Radius 55 → ~150 cm minimum; A.7 uses **200 cm** openings for margin.
4. **`BP_Door`**: on the door mesh set **`Can Ever Affect Navigation` = false** so navmesh runs
   through the doorway. Add `Box Collision` `DoorTrigger` spanning the opening;
   `On Component Begin Overlap` → if the actor is `BP_Werewolf` or `BP_PlayerCharacter`, run the
   open `Timeline` and `Report Noise Event` (`Loudness` 0.6, `Max Range` 1200 `TUNING START` —
   doors are named explicitly in the LOCKED sensory hierarchy). Doors are never locked against the
   wolf in Part A. This satisfies "opens doors" with no EQS and no custom nav area.
5. **`Nav Link Proxy`** for each authored vertical shortcut (over a balustrade, down a stairwell):
   set `Point Links` `Left`/`Right` and `Direction` = `Both Ways` (or `Left to Right` for one-way
   drops). Place **at least one**. Anchors "climbs authored nav links".
6. **`Nav Modifier Volume`** with `Area Class` = `NavArea_Null` is how spaces the werewolf cannot
   path into are made. **Not used in Part A**, but it is exactly how safe havens work in B.5 — note
   it now so the layout leaves room.
7. **`L_Sandbox`**: flat box, navmesh volume, one `BP_Werewolf`, one `Player Start`. Build all AI
   here first. Debug with the apostrophe key (`'`) to toggle the **Gameplay Debugger**, then number
   keys for Behavior Tree and Perception categories. This habit saves more hours than anything else
   in this brief.

## A.7 Level and the modular grid — `L_Mansion_Slice` `[FN]` + `[FORM]`

Anchors: "one mansion or castle (PROVISIONAL)"; Pillars 2 and 4.

**Scope: one floor, 8–10 rooms.** Blocked out first, then styled in place. The grid exists so that
**styling never requires rebuilding the level.**

### The grid — the load-bearing decision of the Form track

Viewport `Grid Snap` **10** for detail, **50** for placement. Never scale a blockout piece to a
non-module size; if a wall wants to be 437 cm, change the layout.

| Module | Dimensions (cm) | Asset |
|---|---|---|
| Wall segment | 400 W × 350 H × 20 T | `SM_Blockout_Wall_400` |
| Half wall | 200 W × 350 H × 20 T | `SM_Blockout_Wall_200` |
| Tall wall (halls) | 400 W × 700 H × 20 T | `SM_Blockout_Wall_400_Tall` |
| Floor / ceiling tile | 400 × 400 × 20 | `SM_Blockout_Floor_400` |
| **Door opening (clear)** | **200 W × 280 H** | `SM_Blockout_DoorFrame_200` |
| **Corridor clear width** | **300 minimum** | — |
| Stair run | 400 W, rise 350 over 400 depth | `SM_Blockout_Stair` |
| Column / pilaster | 40 × 40 × 350 | `SM_Blockout_Column` |

Room heights **350 cm** (service/private) and **700 cm** (hub hall). The 200 cm door opening is
derived from `Agent Radius` 55 (A.6 step 3) with margin and reads as a grand double door — the
constraint and the aesthetic agree.

**Authoring the blockout:** **Modeling Mode → `CubeGrid`** with a 50 cm step, or `Cube` static
meshes scaled to exact module sizes. Save each module as its own `Static Mesh` in
`/Game/Art/Blockout/` so a styled mesh of the same dimensions can replace it by swapping the
`Static Mesh` reference on placed actors — **no re-layout, no re-lighting, no navmesh rebuild from
scratch.** That swap path is the whole reason for the grid.

### Required layout properties

1. **A hub with sightlines.** One large central space (700 cm ceiling) with ≥3 exits — where the
   player first sees the werewolf across distance, the moment that teaches the game (Pillar 4). It
   is also the room that gets the most Form attention, because it is the screenshot.
2. **No dead ends, one deliberate exception.** Every room has **two** ways out. A pursuit in a
   two-exit room is a decision; in a one-exit room it is a coin flip and the player cannot explain
   the capture — a direct Pillar 2 violation. The exception is a small chamber for Part B's hiding
   place; leave it in the layout now.
3. **At least one loop** — a circuit the player can run so the wolf can be led away and doubled back
   on. Without a loop, "evade" collapses into "outrun in a straight line".
4. **Vertical interest for one nav link** — a balcony/stair giving the wolf a drop-down shortcut
   (A.6 step 5). The player learns the wolf takes routes they cannot.
5. **Spatial separation of key and door.** `BP_KeyItem` in the room furthest by path length from
   `BP_EscapeDoor`. The forced traverse *is* the gameplay.
6. **Werewolf start out of sight of `Player Start`** — two or three rooms away. The first 20–40 s
   should be quiet exploration; the wolf's first appearance should be earned. `HomeLocation` (its
   spawn point) is the centre of its 4000-unit patrol radius; make sure that covers the floor.
7. **A marked-out safe-haven footprint** — a small side room off the hub. Do not implement it in
   Part A; just do not build over it. B.5 carves it with a `Nav Modifier Volume`.
8. **At least three deliberate silhouette positions** — places where a lit surface (moonlit window,
   hearth, candle-lit doorway) sits *behind* a spot the werewolf will pass through, so it reads as a
   black shape against light. Design these into the *layout*, not the lighting pass: they are the
   most valuable thing the level does for Pillar 2 and they cannot be added later without moving
   walls.
9. **One material story per room.** A.8 limits us to five master materials, so give each room a
   dominant one — stone undercroft, panelled study, plastered corridor, draped bedchamber, iron
   service passage. Repetition with variation reads as a real building; every room being the same
   mix reads as an asset dump.

### Actors to place

| Actor | Count | Notes |
|---|---|---|
| `Player Start` | 1 | far side from the escape door |
| `BP_Werewolf` | 1 | `Auto Possess AI` = Placed in World or Spawned |
| `Nav Mesh Bounds Volume` | 1 | encloses everything |
| `Nav Link Proxy` | 1+ | at least one vertical shortcut |
| `BP_Door` | 3–5 | main circulation route |
| `BP_KeyItem` / `BP_EscapeDoor` | 1 / 1 | furthest apart by path length |
| `Post Process Volume` | 1 | `Infinite Extent (Unbound)` = true (A.11) |
| `Exponential Height Fog` | 1 | `Volumetric Fog` on (A.11) |
| `Sky Light` | 1 | CC0 night HDRI, very low intensity (A.11) |
| `Directional Light` | 1 | moonlight only; low, cool (A.11) |
| `BP_Candle` / `BP_Sconce` / `BP_Hearth` | 25–50 | practicals (A.11) |
| `Audio Volume` + `Reverb Effect` | 4–6 | one per room type (A.13) |
| `Ambient Sound` | 6–10 | per-zone beds (A.13) |
| `Decal Actor` | 30+ | stains, soot, scuffs, claw marks (A.11) |
| Niagara components | 10+ | dust motes, flames, embers (A.11) |

## A.8 Visual identity — Napoleonic Gothic `[FORM]`

Anchors: Pillar 4 (architecture and objects communicate layout and history); Pillar 2 (the player
must be able to see the threat); "Napoleonic-era Gothic" from `project-brief.md`.

This section exists so every later art decision has something to be checked against, and so that
free assets by six different authors do not read as six different games. **It does not resolve
mansion-vs-castle** — the vocabulary is deliberately valid for both.

### The period, concretely

Napoleonic = **c. 1799–1815**. The premise the art carries: an **older Gothic building** (16th
century fabric or earlier) **occupied and half-converted** during the wars. That mixture does real
work: two prop vocabularies for the price of one, an explanation for why the building is sealed, and
it legitimises almost any sourced medieval/stone asset.

**Period cues — use these:** pointed and segmental arches; ribbed vaulting below, beamed or coffered
ceilings above; stone mullioned windows with small leaded panes and interior shutters, some nailed
shut; oak wainscot panelling to dado height with cracked, water-stained lime plaster above; tall
double doors (plank-and-batten in service areas, panelled in public rooms) with wrought-iron strap
hinges and dulled brass; **candles only** — candelabra, sconces, hand candlesticks, oil lamps,
hearth fires, lanterns; Empire-period military occupation — campaign trunks, crates, bedrolls, a
stacked arms rack, a folding field desk with maps, bandages and a saw on a surgeon's table, empty
bottles; dust sheets over furniture; dark-varnished portraits; a long refectory table; mirrors with
foxed silvering.

**Anti-cues — if one is visible, the look has failed:** gas or electric lighting; cast-iron
radiators; plate glass; modern door hardware; saturated fantasy colour; un-restyled fantasy/sci-fi
geometry from a sourced pack (glowing runes, oversized shoulder armour, alien plants); chrome; neon.

### Palette

| Role | Colour | Where | Share |
|---|---|---|---|
| Dominant cool | desaturated stone grey, black-green | walls, vaults, floors | ~60% |
| Dominant warm-neutral | bitumen brown, dark walnut, umber | panelling, boards, furniture | ~25% |
| Neutral light | bone, ivory, candle-wax cream | plaster, linen, dust sheets, **all UI text** | ~10% |
| Accent A (warm) | candle amber / firelight | light sources and their pools only | ≤3% |
| Accent B (cold) | moon blue-grey | window light and fog inscatter only | ≤3% |
| Accent C (alarm) | oxblood / madder red | drapery, upholstery, blood, UI danger | ≤2% |
| Accent D (value) | tarnished gilt, plus a distinct cool **silver** | the silver resource must be its own note so it reads as valuable at a glance (Pillar 3; prepares Part B) | small |

**Forbidden:** pure white (`#FFFFFF`) anywhere including UI; saturated blue or purple; teal-orange
grading; more than one dominant accent in a single room.

### Light — the two-temperature rule

Every lit space is lit by *one* of two families, never a muddle:

| Family | `Temperature` | Used for |
|---|---|---|
| Interior warm | **1900–2200 K** | candles, sconces, hearths, lanterns |
| Exterior cold | **6500–8000 K** | moonlight through windows, the escape-door beat |

Corridors and connective space get **neither** — near-black, with only spill from the rooms either
side. Enable `Use Temperature` on every light and set `Temperature`; do not tint via `Light Color`
(temperature keeps the palette coherent automatically).

**High contrast is a gameplay decision.** Deep blacks make the werewolf a silhouette, and a
silhouette is more legible *and* more frightening than a fully-lit model — which is precisely why an
imperfect sourced creature (A.9) is acceptable. But the floor of the contrast range is set by
Pillar 2: **if the player cannot see the werewolf when it matters, the design has failed.** Test
every lighting session: stand at each of A.7's three silhouette positions and confirm the wolf reads
at 400, 800 and 1500 cm.

### How mismatched free assets are unified

The difference between "styled" and "a pile of downloads". Five mechanisms, most effective first:

1. **One global grade.** A single `Post Process Volume`, `Infinite Extent (Unbound)` = true (A.11).
   Everything passes through the same saturation, shadow tint and grain. This alone removes most of
   the mismatch.
2. **Fog.** `Exponential Height Fog` + `Volumetric Fog` desaturates with distance, hides seams and
   LOD pops, softens detail, and equalises albedo across authors. The cheapest unifier in real-time
   rendering. Use it generously.
3. **Five master materials, everything through instances** (A.11). Any sourced mesh whose albedo
   fights the palette is re-materialled onto ours, or at minimum gets a `BaseColorTint` override.
   **Never ship a sourced asset on its original material without checking it against the palette.**
4. **Consistent texel density** — aim ~3–5 cm per texel on hero surfaces. Mismatched texel density
   reads as amateur even when nothing else is wrong.
5. **Limit distinct sourced sets to two or three.** Ten packs produce ten looks.

## A.9 Character design — the werewolf `[FORM]`

Anchors: Pillars 1 and 2; "a werewolf tracks them". The client called this out by name. It is a
**Part A** decision made **at build step 8, before blockout**, because the creature's proportions
size the doorways (A.6, A.7).

### The honest constraint first

**Modelling, rigging, texturing and animating a beast from scratch is not achievable in this
window.** A competent beast with a locomotion set (idle, walk, run, turn, attack, hit-react) is 3–6
weeks of specialist work alone; we have 28 days for all of Part A with one person also building
every system. The werewolf **must be sourced**, and the design's job is to make a sourced creature
read as *our* werewolf.

### The decision — `Paragon: Rampage`

| | |
|---|---|
| **Asset** | **Paragon: Rampage** |
| **Source** | Fab → Epic Games Content (also via the Epic Games Launcher's free Epic content) |
| **Cost** | **Free, permanently.** Claimed items stay in the library. |
| **Licence** | Epic Games Content / Fab Standard — free, commercial use allowed, **but only within Unreal Engine projects**. You **may not use the trademark "PARAGON"** to name or advertise the game. |
| **Attribution** | Not required. Credit it in `WBP_Credits` anyway (A.14). |
| **Contents** | Skeletal mesh, multiple skins, **a full AAA animation set**, `Animation Blueprint`s, VFX. |

**Why Rampage and not a "werewolf" asset:** there is no reliable, genuinely-free, rigged and
animated werewolf. Fab's werewolf listings are paid. itch.io's free werewolf assets are 2D sprites.
AI-generated CC0 werewolves ship as un-rigged T-pose static meshes needing rigging and animation
anyway — plus an academic-integrity question (A.14). Rampage is a **hunched, heavy-shouldered,
long-armed, fur-covered brute** whose silhouette is already most of the way to lycanthrope, and
critically it **arrives with its own skeleton and its own complete animation set**, so **zero
retargeting** — the single largest time saving available anywhere in this project.

**Alternates, same licence — evaluate side by side in `L_Sandbox` at step 8 and pick by silhouette:**
- **`Paragon: Khaimera`** — leaner, faster, more feral-human. Better if the fiction wants "a man who
  turns"; reads better in first person because the head sits at a human-ish height.
- **`Paragon: Narbash`** — heavier, more ogre-like. Slower read, more mass, more menace at distance.

Pick **one** and delete the others' folders. Three imported hero characters is ~2 GB of cook time
you do not need.

### Closing the gap between "big furry brute" and "werewolf"

A well-lit, well-silhouetted imperfect model reads better than a perfect model badly lit. Five cheap
interventions, highest payoff first:

1. **Re-material the fur.** Duplicate the body material into a `Material Instance` in
   `/Game/Art/Materials/Instances/`. Drive `Base Color` toward **charcoal with a cold brown
   undertone**, flatten `Roughness` variation, cut `Specular`, and **remove every emissive and
   fantasy-coloured element** — Paragon characters carry team-colour emissives and FX; those must
   go. This step does more than all the others.
2. **Light it only from behind and the side.** Never let the player see it in flat frontal light for
   more than about a second. A.7's three silhouette positions are for this.
3. **Scale and pose.** `Mesh → Scale` ~1.1–1.2 `TUNING START`; bias idle/walk poses low — a
   low-slung head with the shoulders above it is *the* werewolf read. If the set has a crouch/prowl,
   use it as the `Patrol` pose.
4. **Never show it clean.** Grime decals, fog, partial occlusion behind doorframes and balusters.
   Occlusion is free detail.
5. **Sell it with audio, not geometry** (A.13). The growl, the sniff and the gallop do more
   characterisation than the mesh. That is not a consolation — it is how horror actually works.

### `ABP_Werewolf`

Do **not** reuse Paragon's shipped `Animation Blueprint` — it is built around Paragon's ability
system and will fight the Behavior Tree. Build a small one:

1. `Blend Space 1D` at `/Game/Werewolf/BS_Werewolf_Locomotion`, axis `Speed` 0→500, samples = idle at
   0, walk at ~200, run at ~460. **Set sample speeds to match A.4's speed table** or the feet skate.
2. `ABP_Werewolf` `AnimGraph`: a `State Machine` with a `Locomotion` state driving the blend space
   from a `Speed` float set in `Event Blueprint Update Animation` (`Get Velocity → Vector Length`),
   plus one-shot states or `Play Anim Montage` for the pounce windup and attack.
3. Use **`Blend Poses by Enum`** on `E_WolfState` to swap a prowl pose for a run pose.
4. Assign `Anim Class` = `ABP_Werewolf` on `BP_Werewolf`'s `Mesh`.

**If a clip is missing** (most likely Part B's lowered-profile pounce windup): the route is
`IK Rig` + `IK Retargeter` — create an `IK Rig` for the creature, an `IK Retargeter` from the source
rig, map `Retarget Chains`, set the `Retarget Pose`, then `Export Selected Animations`. **Warning:**
retargeting *human* animation (Mixamo, Game Animation Sample) onto a beast with radically different
proportions looks wrong — the arms will not reach the ground. Prefer re-timing an existing clip from
the same asset (`Play Rate`, `Animation Modifier`) over retargeting a human one.

**Do not build a dependency on Mixamo.** Adobe signalled deprecation in 2025 and the service has had
extended outages since; it is also humanoid-only, so it cannot animate this creature anyway.

## A.10 Character design — the player `[FORM]` · perspective still PROVISIONAL

**This brief does not resolve first vs third person.** `project-brief.md` marks it PROVISIONAL and
the comparison is an explicit project deliverable. What this section does is state the **Form cost
difference honestly**, because the branches cost different numbers of days.

| | **First person** | **Third person** |
|---|---|---|
| Visible body | hands/forearms only, optional in Part A | **a full, period-appropriate, animated body** |
| Locomotion animation | not visible; anything will do | visible and load-bearing; foot-skate reads as broken |
| Costume design | none | required — where "Napoleonic" is sold or lost |
| Camera framing work | minimal | real: spring-arm tuning, occlusion, doorway framing, chase readability |
| **Extra Form days** | **~0.5** | **~3–5** |

Those 3–5 days come out of the same 28-day budget as the functional work. That is why build step 6
runs the comparison in **week one** and records the verdict as a new LOCKED line in
`project-brief.md`. Deciding late means paying the cost twice, or paying it in the reserve window.

### $0 sources, whichever branch wins

**Locomotion animation — take this either way.** **`Game Animation Sample`** (Fab, Epic, free):
500+ AAA mocap locomotion animations on the **UE5 Mannequin skeleton**, plus a plug-and-play
third-person locomotion `Animation Blueprint`. Licence: free, commercial use permitted, **Unreal
Engine projects only**, no attribution. Use its *animations* even if you skip its Motion Matching —
a plain `Blend Space 1D` from its walk/run/crouch clips is lighter and entirely sufficient, and
Motion Matching adds tuning time we do not have.

**Body mesh options, cheapest first:**
1. **First person, no body.** `Set Owner No See` = true (A.2) — the character still casts a shadow,
   which sells presence for free. **The cheapest credible Part A.**
2. **A free Paragon hero with a long-coat silhouette**, re-materialled to the A.8 palette. At
   third-person distance a **greatcoat, boots, high collar** silhouette *is* "Napoleonic" — the
   silhouette carries it, not the buttons. Evaluate in-editor at step 6: **`Paragon: Wraith`**,
   **`Gideon`**, **`Revenant`**, **`Murdock`**, **`Sparrow`**. Same free Epic licence as the
   werewolf. Needs an `IK Rig` + `IK Retargeter` from **`IK_Mannequin`** (ships with the Third
   Person template) to the hero's rig — name them `IK_<Hero>` and `RTG_Mannequin_<Hero>` — so the
   Game Animation Sample clips drive it. Humanoid-to-humanoid retargeting is reliable: half a day.
3. **`SKM_Manny` / `SKM_Quinn`** (engine, UE EULA). Correct skeleton, zero setup, **wrong century**.
   Fine as a step-6 stand-in; not acceptable in the shipped build if third person wins.
4. **MetaHuman** (in-engine MetaHuman Creator, UE 5.6+; free under the standard Unreal licence below
   $1M revenue, and since 2025 usable beyond Unreal). Excellent faces. **Not recommended here:** the
   wardrobe is contemporary, MetaHumans are expensive to render under Lumen plus volumetric fog, and
   a beautiful modern-dressed face is worse for this project than a well-silhouetted coat.

**Authoring a period costume ourselves** (a greatcoat over `SKM_Manny` in Modeling Mode with weight
transfer) is 3+ days with real failure risk. Do not schedule it in Part A; it is recorded in Part C.

**If third person wins, the minimum bar:** visible body on the Game Animation Sample locomotion;
coat-silhouette mesh re-materialled to the palette; `SpringArm_TP` tuned so the camera does not clip
walls in 300 cm corridors (`Do Collision Test` true, `Probe Size` raised, `Camera Lag` ~0.1); and —
the one people forget — **confirm the werewolf is still legible when the player's own body occupies
the centre of the screen.** Pillar 2 is measured in the perspective that ships.

## A.11 Environment art, lighting and effects `[FORM]`

Anchors: Pillar 4 (architecture and objects communicate layout and history); Pillar 2 (legibility).

### Five master materials — and no more

In `/Game/Art/Materials/`. Every surface uses a **`Material Instance`** of one of them. Five masters
is what makes a self-authored level coherent, and it is also what tames sourced assets (A.8).

| Master | Covers | Exposed parameters |
|---|---|---|
| `M_Stone` | ashlar, limestone, flags, vaulting | `BaseColorTint`, `Tiling`, `RoughnessScale`, `DirtAmount`, `WetnessAmount` |
| `M_Plaster` | lime plaster, whitewash, cracks | `BaseColorTint`, `Tiling`, `StainAmount` |
| `M_Wood_Dark` | oak panelling, floorboards, furniture | `BaseColorTint`, `Tiling`, `VarnishGloss`, `DirtAmount` |
| `M_Metal_Tarnished` | wrought iron, brass, **silver** | `BaseColorTint`, `Metallic`, `RoughnessScale`, `TarnishAmount` |
| `M_Fabric` | wool, velvet, dust sheets, linen | `BaseColorTint`, `Tiling`, `SheenAmount` |

Build each as: tiling `Texture Sample` set (BaseColor / Normal / packed ORD) from **ambientCG** or
**Poly Haven** (both **CC0**, A.14) × a `Vector Parameter` `BaseColorTint`, a `Scalar Parameter`
`Tiling` on a `TexCoord`, and a grime layer `Lerp`ed by `DirtAmount`. Keep instruction counts modest
— Lumen plus volumetric fog plus VSM is already the frame budget.

Instances named `MI_Stone_Hall`, `MI_Wood_Panel_Study`, … — **one per material-per-room-story**
(A.7 requirement 9), not one per mesh.

### Lighting build

1. **`Directional Light`** — moonlight only. `Intensity` 0.3–1.0 lux `TUNING START`, `Temperature`
   7000 K, `Use Temperature` on, `Volumetric Scattering Intensity` ~1.5. Angle it through the hub
   windows and the escape door and nowhere else useful. This is the light the player navigates by.
2. **`Sky Light`** — `Source Type` = `SLS Specified Cubemap`, `Cubemap` = a **Poly Haven CC0 night
   HDRI**, `Intensity Scale` 0.05–0.2 `TUNING START`. Ambient fill so unlit corners are *dark* not
   *black voids*. This value is most of the difference between "atmospheric" and "I can't see".
3. **Practicals everywhere else.** `Point Light` for candles and hearths (`Temperature` 1900 K,
   `Attenuation Radius` 300–600, `Intensity Units` Candelas, `Source Radius` ~2 for soft shadows);
   `Spot Light` for lanterns and directed pools; `Rect Light` in window apertures and fireplaces (a
   `Rect Light` in a window is the cheapest convincing moonlight-through-glass there is). Raise
   `Volumetric Scattering Intensity` where you want visible shafts.
4. **All lights `Movable`** under Lumen. Do **not** attempt a lightmap bake — no time, and it fights
   dynamic doors and Part C's navmesh changes.
5. **A candle is a light *and* a mesh *and* a flame *and* a sound.** Build `BP_Candle`,
   `BP_Sconce`, `BP_Hearth` bundling `Static Mesh` + `Point Light` + Niagara flame + `Audio` crackle
   + a flicker (`Timeline` or `Light Function Material` driving `Intensity` ±10%), then place them
   by the dozen. **Flicker is the highest value-per-minute effect in the whole Form track** — it
   makes a static scene feel alive.

### Post-process — one global volume

`Post Process Volume`, `Infinite Extent (Unbound)` = **true**. All `TUNING START`:

| Setting | Value | Why |
|---|---|---|
| `Exposure → Metering Mode` | `Manual` (or `Auto Exposure Histogram` with `Min EV100` = `Max EV100`) | **Critical.** Auto-exposure brightens dark corridors and destroys both the horror and the silhouette read. Lock it. |
| `Exposure → Exposure Compensation` | to taste | the one dial that sets overall darkness |
| `Local Exposure → Highlight Contrast Scale` | 0.8 | gentle local relief so candle-lit faces are not blown out — use this *instead of* auto-exposure |
| `Color Grading → Global → Saturation` | 0.75 | desaturated, period, unifying |
| `Color Grading → Shadows → Gain` | slight blue-green push | cold shadows against warm candlelight — the palette in one setting |
| `Color Grading → Highlights → Gain` | slight warm push | complements the above |
| `Lens → Image Effects → Vignette Intensity` | 0.4 | frames the image, focuses attention |
| `Film Grain → Film Grain Intensity` | 0.3 | hides low-res sourced textures remarkably well |
| `Lens → Bloom → Intensity` | 0.4 | candles need a little; more reads as cheap |
| `Lens → Chromatic Aberration → Intensity` | 0.15 | a whisper; zero is better than too much |
| `Rendering Features → Motion Blur → Amount` | 0.2 | high motion blur hurts the chase read (Pillar 2) |

**Do not overdrive the post-process.** Paint with light, fog and materials; the grade is the last
10%, not the first 50%.

### Fog

`Exponential Height Fog`: `Fog Density` ~0.02 `TUNING START`, `Fog Height Falloff` ~0.2,
`Fog Inscattering Color` cold blue-grey, **`Volumetric Fog` on**, `Scattering Distribution` ~0.2,
`Albedo` dim grey, `View Distance` tuned so the far end of the hub is hazy but the werewolf still
reads there. Fog does four jobs at once: atmosphere, asset unification, distance legibility for the
wolf, and hiding the fact that the level is small.

### Decals

`Decal Actor` with `Material Domain = Deferred Decal`, `Blend Mode = Translucent`:
`M_Decal_Stain` (water runs below windows, in vaults) · `M_Decal_Soot` (above every sconce and
hearth — instantly ages a wall) · `M_Decal_Scuff` (door thresholds, stair treads, where feet
actually go) · **`M_Decal_Claw` (gouges on the werewolf's habitual routes — decoration *and*
signposting: Pillar 4 says the environment communicates without objective markers, and claw marks
near the nav-link shortcut teach the player something true about the AI)** · `M_Decal_Blood`
(sparing — target rating **T**; suggest, do not depict).

Rule of thumb: 30+ decals across 8–10 rooms. Nearly free, and most of what "dressed" means.

### Niagara VFX

| System | Where | Why |
|---|---|---|
| `NS_DustMotes` | every light shaft, especially the hub | **Highest ratio of "looks finished" to authoring time in the project.** |
| `NS_CandleFlame` | inside `BP_Candle` / `BP_Sconce` | a candle light with no visible flame reads as a bug |
| `NS_Embers` | hearths | slow rising sparks; sells warmth |
| `NS_ColdBreath` | player and werewolf in unheated rooms | cheap, and it makes the creature feel like it is breathing near you |

Build each from a stock template (`Fountain`, `Simple Sprite Burst`); do not author from empty.

### Set dressing rule

**Every room needs one focal object and one story of use.** An empty box with nice materials still
reads unfinished; a room with a toppled chair, a guttered candle and a half-packed campaign trunk
reads finished on three props. Three well-placed props beat thirty scattered ones. Sourced props
come from the **Infinity Blade** packs (stone set pieces, candelabra, weapons, statues — free, Epic,
UE-only) and **Poly Haven** (CC0), both re-materialled per A.8, plus anything claimed from Fab's
bi-weekly free drops in pre-production.

## A.12 UI styling `[FORM]`

The client named "basic white UI" as unacceptable. This is the cheapest, fastest, most visible Form
win in the project — roughly one day changes the perceived finish of the whole game. Anchors:
Pillar 4 (no constant objective markers, so there is *less* UI and what exists must be good);
Pillar 2 (game-over and prompt legibility).

### Typography

| Role | Font | Licence |
|---|---|---|
| Titles, buttons, headings | **`Cinzel`** (Google Fonts) — Roman capitals, engraved, period-plausible | **SIL OFL 1.1** |
| Body, prompts, credits | **`EB Garamond`** (Google Fonts) — a Garamond is the right century-adjacent read | **SIL OFL 1.1** |
| Decorative (≤1 use) | `UnifrakturMaguntia` (Google Fonts) | **SIL OFL 1.1** |

OFL permits commercial use; when embedding, **credit the fonts in the credits screen / readme**
(A.14). **Use blackletter almost never** — one flourish on the title at most, or the game reads
Halloween rather than Napoleonic.

Import the `.ttf` → Unreal creates a `Font Face`; create a `Font` asset (`Runtime` caching) at
`/Game/UI/Style/F_Cinzel` and `F_EBGaramond`; set them on `Text Block` / `Rich Text Block` widgets.

### Colour and framing

- Text: warm bone **`#E8DFC8`** on near-black. **Never `#FFFFFF`.**
- Accents: oxblood **`#5A1414`** (danger, game over), tarnished gilt **`#C9A227`** (titles,
  selection), cool silver **`#C8D0D8`** (the silver resource; prepares Part B).
- **Every panel gets a frame.** A `Border` with `Brush → Draw As = Box`, a vellum texture
  (`T_Panel_Vellum` — CC0 paper from ambientCG/Poly Haven, or painted in five minutes), and `Margin`
  set so it scales without stretching corners. Nest a second thin `Border` inset ~8 px as a double
  rule. **That double rule alone kills the "default Unreal UI" read.**
- Aged edges: bake the darkening and irregular edge into the texture's alpha; do not attempt it with
  widget nodes.
- Buttons: `Button` with `Style → Normal / Hovered / Pressed` brushes tinted from the palette. No
  rounded blue default anywhere. Hovered = gilt text, not a colour block.

### Motion

Every widget fades: a `Widget Animation` per widget, 0.15–0.3 s opacity (plus an 8–12 px upward
translate on titles), played in `Event Construct` or on the game-over beat. **Instant pop-in is the
most reliable tell of an unfinished UI.** Minutes of work.

### The Part A widget set

| Widget | Contents | Notes |
|---|---|---|
| `WBP_TitleScreen` | title (`Cinzel`), `Begin`, `Credits`, `Quit`, over a slow camera drift in `L_Title` | A large share of "this is a finished game" for very little work. `L_Title` = one dressed corner of the mansion with a candle and fog. |
| `WBP_Prompt` | keybind glyph in a small bordered box + a diegetic verb phrase | copy rules below |
| `WBP_GameOver` | title, `Restart`, `Main Menu`, `Quit`; oxblood accent; fade from black | driven by A.5's death beat |
| `WBP_Escaped` | title, `Main Menu`, `Quit`; gilt accent; fade from warm white | the win needs a payoff |
| `WBP_Credits` | scrolling `Rich Text Block` — **all sourced-asset attributions (A.14)** | a **licence-compliance artefact**, not a nicety |

**Prompt copy rules** (Pillar 4 — diegetic, no quest text): write a verb phrase about the object,
not a UI instruction (`Take the silver candlestick`, not `[E] INTERACT`); keybind in its own
bordered glyph, separate from the sentence; refusals as in-world observations (`The bar is fixed
fast — something must lift it.`); sentence case, ALL CAPS on titles only.

### And what there deliberately is *not*

**No permanent HUD.** No stamina bar, no scent meter, no objective marker, no minimap, no crosshair
(until Part B's firearm needs one). Stamina is breath and vignette (A.2); the werewolf is sound and
silhouette (A.9, A.13). A direct Pillar 4 anchor *and* it removes the largest block of UI-art work
from the schedule. Stated explicitly so nobody "helpfully" adds a health bar to a game whose LOCKED
design has no health. Debug HUD behind `bShowDebugHUD` only, via `Print String` — **stripped in
Shipping builds** (A.17).

## A.13 Audio `[FORM]`

Sound sells horror harder than texture resolution, CC0 libraries make it nearly free, and it is the
werewolf's primary readability channel. Anchors: Pillar 1 (a predator you can hear searching);
Pillar 2 (recognisable cues — *the player must be able to hear which sense the wolf is using*);
Pillar 4 ("architecture, objects, and **sound** communicate…"); Core loop ("listen for the predator"
is the first verb in the LOCKED loop).

### Mix architecture — set this up first, it takes 20 minutes

- `Sound Class`es: `SC_Master` → `SC_Ambience`, `SC_SFX`, `SC_Creature`, `SC_UI`, `SC_Music`.
  Assign every imported `Sound Wave` / `Sound Cue` to one.
- `Sound Mix`es: `SM_Default`, and **`SM_Chase`** ducking `SC_Ambience` −6 dB and lifting
  `SC_Creature` +3 dB. `Push Sound Mix Modifier` (`SM_Chase`) when `WolfState` becomes `Chase`,
  `Pop Sound Mix Modifier` when it leaves. Two nodes; the chase instantly feels different.
- `Sound Attenuation`: **`ATT_Creature`** — long falloff (inner ~600, falloff ~4000),
  **`Enable Air Absorption`** on, **`Enable Occlusion`** on with a low-pass when occluded. Occlusion
  is what makes the werewolf audibly *behind a wall* rather than vaguely nearby — a Pillar 1/2
  requirement, not polish. **`ATT_Prop`** — short falloff for candles, clocks, fires.
- `Audio Volume` actors with `Reverb Effect` presets, **one per room type** (stone vault, panelled
  study, plastered corridor, draped bedchamber, great hall). Different reverb per room is the
  cheapest "this is a real building" effect in existence, and it gives the player spatial
  information — Pillar 4.

### Content list for Part A

| Bucket | Content | Source (A.14) |
|---|---|---|
| Ambience beds | wind in chimneys, distant timber creak, rain on leaded glass, a long-case clock, rats in the wainscot — 6–10 `Ambient Sound` actors | Sonniss / Freesound CC0 |
| Player | footsteps ×2 surfaces (stone, board) with random variation, cloth rustle, breathing loop (the A.2 stamina readout), a grunt on hard stop | Sonniss / Freesound CC0 |
| **Werewolf — three states** | `Patrol`: heavy padding + slow breathing. `Investigate`: **sniffing** + low growl + claws on stone. `Chase`: roar + fast gallop + impacts. All on `ATT_Creature`, swapped by `OnWolfStateChanged` | Infinity Blade Effects/Sounds (Epic, free) pitched down; Sonniss; Freesound CC0 |
| Werewolf — events | door slam as it barges through, pounce windup inhale (prepares Part B), the catch sting | as above |
| UI | paper-turn for navigation, low thud for game over, rising chord for escaped, soft tick for hover | Freesound CC0 / Kenney CC0 |
| Music — exactly two cues | a game-over cue and an escape/win cue, 30–60 s each | Kevin MacLeod / Incompetech — **CC-BY, attribution REQUIRED** |

> **The sniff is a mechanic.** Pillar 2 requires the player to be able to explain a capture. If
> `Investigate` and `Chase` sound alike, they cannot. Make the three states unmistakable with eyes
> closed — that is the acceptance test for build step 11.

> **No chase music.** Silence plus the creature's own audio is scarier, cheaper, and keeps the
> hearing-based gameplay legible. Two cues is the whole soundtrack. Anchor: Pillar 4 — sound carries
> information here, so it must not be buried under score.

**Implementation notes.** Randomise footsteps and creature vocals with a **`MetaSound Source`**
using a `Random` node (or a `Sound Cue` with `Random`) — repeated identical samples are the audio
equivalent of default grey material. Footsteps in Part A: an `Anim Notify` on the locomotion
animation (available once A.10's set is in) is better than a timer. `BP_Candle` / `BP_Hearth` each
carry their own `Audio` component on `ATT_Prop` — sound sources should be *objects in the world*,
which is what makes the space navigable by ear. Cap 50 looping candles with a `Sound Concurrency`
setting.

## A.14 Asset sourcing register — the $0 rule `[FORM]`

**Binding.** Nothing enters `/Game/Sourced/` unless it is a row here or satisfies the rules below.
All rows verified July 2026; **re-verify each listing at download time** — free-asset licensing has
moved repeatedly (Megascans and Sketchfab both changed within the last 18 months).

| # | Asset / need | Source | Licence | Attribution? | What it's for |
|---|---|---|---|---|---|
| 1 | **Werewolf** — mesh, skins, animations, AnimBPs, FX | **Paragon: Rampage** — Fab / Epic Games Content | Free permanently; Epic Content / Fab Standard. **Unreal Engine projects only.** **May not use the "PARAGON" trademark to name or advertise the game.** | Not required (do it anyway) | `BP_Werewolf` (A.9) |
| 2 | Werewolf alternates | **Paragon: Khaimera**, **Paragon: Narbash** | as row 1 | as row 1 | silhouette comparison at step 8 |
| 3 | Player locomotion animation library + TP locomotion AnimBP | **Game Animation Sample** — Fab / Epic | Free; **Unreal Engine projects only**; commercial use OK | No | `ABP_Player` (A.10) |
| 4 | Player body candidates (if TP wins) | **Paragon: Wraith / Gideon / Revenant / Murdock / Sparrow** | as row 1 | as row 1 | coat-silhouette protagonist (A.10) |
| 5 | Default skeleton, IK Rig source | **`SKM_Manny` / `SKM_Quinn` / `IK_Mannequin`** — ships with the UE Third Person template | Unreal Engine EULA | No | stand-in body; retarget source |
| 6 | Optional protagonist face | **MetaHuman** (in-engine Creator, UE 5.6+) | Free under the standard Unreal licence below $1M revenue; since 2025 usable beyond Unreal | No | not recommended (A.10) |
| 7 | Stone / plaster / wood / metal / fabric textures | **ambientCG** (ambientcg.com) | **CC0 1.0** | **No** | the five master materials (A.11) |
| 8 | Textures, night HDRIs, some props | **Poly Haven** (polyhaven.com) | **CC0** | No (appreciated) | `Sky Light` HDRI, surfaces, furniture-class props |
| 9 | Period-adjacent props, stone set pieces, candelabra, statues, weapons | **Infinity Blade: Grass Lands / Ice Lands / Fire Lands / Weapons / Adversaries / Effects** — Fab / Epic Games Content | Free permanently; **Unreal Engine projects only** | No | level dressing (A.11). **Stylised fantasy — restyle materials or use only the neutral stone/prop pieces.** |
| 10 | Opportunistic extras | **Fab bi-weekly free content** (new free items every two weeks; claimed items are kept **permanently**) | Fab Standard License — **check the tier on each listing: `Personal` vs `Professional`**, and whether it is a Creative Commons listing | Varies — read each | **Claim every free drop between now and 1 Sept even if unused.** Costs nothing, expands options later. |
| 11 | Bulk sound effects | **Sonniss GDC Game Audio Bundle** (gdc.sonniss.com — annual, incl. GDC 2026) | Royalty-free, **no attribution required**, unlimited projects for life, commercial use OK | No | ambience, footsteps, creature layers, impacts (A.13) |
| 12 | Specific sounds | **Freesound** — **filter to CC0 first** | **CC0** preferred; **CC-BY** acceptable *with credit*; **reject CC-BY-NC and Sampling+** | CC0 no / CC-BY **yes** | creature, ambience, UI (A.13) |
| 13 | Creature roars, impacts | **Infinity Blade: Effects / Sounds** (Epic, free) | as row 9 | No | werewolf vocal base — pitch down, distort |
| 14 | Two music cues | **Kevin MacLeod / Incompetech** (also on Free Music Archive) | **CC-BY 3.0 / 4.0 — attribution REQUIRED** | **YES — in `WBP_Credits` and `CREDITS.md`** | game-over and escape cues (A.13) |
| 15 | UI fonts | **Google Fonts: `Cinzel`, `EB Garamond`** (+ optional `UnifrakturMaguntia`) | **SIL Open Font License 1.1** | Credit when embedding | all UI type (A.12) |
| 16 | UI paper/vellum textures, simple icons | **ambientCG / Poly Haven** (CC0), **Kenney** (kenney.nl, CC0), or author them | **CC0** | No | `T_Panel_Vellum`, keybind glyphs (A.12) |

### Sources deliberately NOT used, and why

| Source | Status | Verdict |
|---|---|---|
| **Quixel Megascans** | The free-for-Unreal era **ended 31 December 2024.** Most surfaces are now paid on Fab. Only the free-tagged subset and **Megaplants** remain free under Fab Standard. Assets downloaded before the change remain licensed under the terms accepted then. | **Do not plan around Megascans.** ambientCG and Poly Haven (CC0) cover our needs. Use only free-tagged Megascans/Megaplants if genuinely marked free at download time. |
| **Sketchfab** (CC0 / CC-BY models) | Download licensing is being retired in the Fab migration, and **CC0 / CC-BY-SA / CC-BY-NC / CC-BY-ND do not exist as licence types on Fab.** Free content availability has been shrinking. | **Source of last resort.** If used, **save the licence page as a PDF at the moment of download** — otherwise the licence is unprovable later. |
| **Mixamo** | Free and royalty-free, and you **may not redistribute the raw files** — but Adobe signalled deprecation in 2025 and the service has had extended outages since. Humanoid-only. | **Not a dependency.** One-off humanoid clip only, if it happens to be up. |
| **Paid Fab / CGTrader / marketplace werewolves** | Cost money. | **Excluded by the $0 rule.** |
| **AI text-to-3D generators** (e.g. CC0-labelled generated meshes) | Legally usable if the licence is explicit, but they ship un-rigged and would need rigging and animation anyway. | **Escalate to the commander as an academic-integrity question before use** — not a design decision. Not in the plan. |

### Compliance obligations — do not let these slip

1. **Maintain `/CREDITS.md` in the repo *as you download*, not at the end.** Columns: asset, author,
   source URL, licence name + version, date downloaded, required attribution string, where it is
   used. Retro-fitting this at the end is how projects end up shipping assets they cannot prove.
2. **`WBP_Credits` in the shipped build must carry every CC-BY attribution** (row 14 music, any
   CC-BY Freesound entries) and the font credits (row 15). This is the *only* hard legal
   requirement in the register, and it is a five-minute job if the register is current.
3. **Keep `/Docs/licences/` with a saved copy of each licence** (PDF or .txt) captured at download
   date.
4. **Rows 1–6, 9 and 13 are Unreal-only licences.** That is fine — the deliverable is an Unreal
   game. But it means **no asset from those rows may be exported, reused in another engine, or
   shipped as a standalone model.**
5. **Never use a listing marked `Personal` tier, `non-commercial`, or CC-BY-NC.** A capstone that
   may be shown publicly is exactly the ambiguous case; avoid the ambiguity entirely.
6. **If you cannot name the licence, do not import the asset.**

## A.15 Minimum feature list for Part A

Every row traces to `project-brief.md`. A row that cannot be anchored does not belong in Part A.

### Function `[FN]`

| # | Feature | Anchor |
|---|---|---|
| F1 | Walk / crouch / sprint with control-rotation-relative movement | Core loop ("choose a route and pace"); Scent/stamina LOCKED core |
| F2 | Stamina drains on sprint, recovers on walk/crouch/rest | Scent/stamina **LOCKED** |
| F3 | Diegetic stamina readout (breath, vignette) instead of a HUD bar | Pillar 4; "no health bar" LOCKED |
| F4 | Both FP and TP cameras present and runtime-toggleable | Perspective **PROVISIONAL** — "build the same short sequence in both and compare" |
| F5 | Line-trace interaction with a diegetic prompt | Core loop ("search for clues… puzzle objects"); Pillar 4 |
| F6 | Werewolf `AI Perception`: `AI Sight config` + `AI Hearing config` | Sensory hierarchy |
| F7 | Sprinting emits `Report Noise Event`; walking quieter; crouch silent; doors and (later) gunshots noisy | Sensory hierarchy: "investigates sprinting, doors, gunshots" |
| F8 | Behavior Tree with Patrol / Investigate / Chase, interruptible mid-action | Werewolf AI states (subset); Pillar 1 |
| F9 | Random patrol via `Get Random Reachable Point in Radius` | State list: "random patrol" |
| F10 | Memory decay → `ResetToPatrol` after ~12 s | State list (patrol is the resting state); Pillar 5 |
| F11 | Wolf chase speed just below player sprint speed | Pillars 5 and 2 |
| F12 | Per-state werewolf audio — patrol / investigate / chase audibly distinct, occluded by walls | Pillars 1, 2, 4; Core loop ("listen for the predator") |
| F13 | Nav mesh `Runtime Generation = Dynamic`; AI-openable doors | State list: "Travels all zones, opens doors" |
| F14 | ≥1 `Nav Link Proxy` traversal the player cannot use | State list: "climbs authored nav links" |
| F15 | Contact → death beat → immediate game over widget with Restart | Win/Lose **LOCKED** |
| F16 | Key item + escape door → win widget with a visual payoff | Win/Lose **LOCKED** |
| F17 | One floor: hub, loop, no dead ends, vertical shortcut, 3 silhouette positions | World (PROVISIONAL); Pillars 2 and 4 |
| F18 | **No survival timer of any kind** | `project-brief.md`: "there is no survive-until-sunrise timer" |

### Form `[FORM]`

| # | Feature | Anchor |
|---|---|---|
| V1 | Blockout on the modular grid (400/200 walls, 200×280 doors, 300 corridors) so styled geometry drops in without rebuilding | Pillar 4 (architecture communicates); makes V2–V4 affordable at all |
| V2 | Five master materials + per-room instances; no default grey anywhere | Pillar 4; the mechanism that unifies sourced assets (A.8) |
| V3 | Two-temperature lighting (1900–2200 K practicals vs 6500–8000 K moonlight) with dark connective space | Pillar 2 (the wolf must be visible when it matters); Pillar 4 |
| V4 | Global post-process grade with **locked exposure** | Pillar 2 (consistent legibility); Pillar 4 |
| V5 | Exponential height fog + volumetric fog | Pillar 4; distance legibility of the wolf (Pillar 2); asset unification |
| V6 | Sourced werewolf character, re-materialled, silhouette-first presentation | Pillars 1 and 2; "a werewolf tracks them" |
| V7 | `ABP_Werewolf` locomotion matched to the speed table; state-driven poses | Pillar 2 (recognisable cues); Pillar 1 |
| V8 | Player character visual appropriate to the chosen perspective | Perspective **PROVISIONAL** (A.10) |
| V9 | Set dressing: one focal object + one story of use per room; 30+ decals incl. claw marks on wolf routes | Pillar 4 (environment communicates history and layout without markers) |
| V10 | Niagara dust motes, candle flames, embers, cold breath; light flicker | Pillar 4 |
| V11 | Styled UI: period fonts, palette, framed panels, fades, **no pure white, no permanent HUD** | Pillar 4; Pillar 2 |
| V12 | `WBP_TitleScreen` + `L_Title` + `WBP_Credits` carrying all licence attributions | Deliverable requirement; A.14 obligation 2 |
| V13 | Audio: per-zone ambience with per-room reverb, footsteps, three occluded creature states, UI sounds, two music cues, `SM_Chase` duck | Pillars 1, 2, 4; Core loop |
| V14 | **Packaged Windows build**: title → play → win/lose → quit, runs on a clean machine | Deliverable requirement ("a working, *playable* game") |

## A.16 Build order for Part A — interleaved

31 July – 27 August, 28 days. Each step is independently testable before the next begins; do not
batch. `[FN]` = Function, `[FORM]` = Form.

### Block 0 — pre-production (25–30 July, before the 28 days)

| Step | Track | Work | Test |
|---|---|---|---|
| 0a | — | **Re-establish the Unreal MCP connection.** Nothing else can start. | MCP responds; a test Blueprint can be created and deleted. |
| 0b | `[FORM]` | **Claim and download every asset in A.14.** Paragon Rampage + 1–2 alternates, Game Animation Sample, Infinity Blade packs, current Fab free drops, ambientCG/Poly Haven starter set, Sonniss bundle, fonts. Start `/CREDITS.md` and `/Docs/licences/`. | Every download has a `CREDITS.md` row **and** a saved licence file. Downloads are slow; licences must be captured at download time, not later. |

### Block 1 — "it moves" (days 1–4)

| Step | Track | Work | Test |
|---|---|---|---|
| 1 | `[FN]` | Third Person template project; folder structure; `GM_Werewolf`, `GI_Werewolf`, `PC_Werewolf`; Maps & Modes; Rendering settings (A.1); `L_Sandbox`. | PIE launches into an empty box. |
| 2 | `[FN]` | `BP_PlayerCharacter`: components, both cameras, Enhanced Input assets, `IMC_Default`, move/look. | You can walk and look in `L_Sandbox`. |
| 3 | `[FN]` | `ApplyPerspective` + `IA_TogglePerspective`. | `V` flips FP↔TP and both control correctly. |
| 4 | `[FN]` | Crouch, sprint, stamina, `BreathAudio`, sprint noise events. | Sprint drains, breath rises, sprint cuts out at zero. |
| 5 | `[FORM]` | Import **Game Animation Sample**; build `ABP_Player` (blend space from its walk/run/crouch clips) on the player. | No T-pose; no foot skate at 220 and 480 uu/s. |
| 6 | `[FORM]` **decision gate** | **Perspective comparison.** Build the same 60-second sandbox traverse and play it in FP and TP. Judge: threat legibility, doorway framing, whether the body helps or hurts. **Write the verdict into `project-brief.md` as a new LOCKED line.** | A written verdict exists. The Form budget for A.10 is now known (~0.5 day vs ~3–5 days). |

### Block 2 — "it hunts" (days 5–11)

| Step | Track | Work | Test |
|---|---|---|---|
| 7 | `[FN]` | Navmesh in `L_Sandbox`; `Runtime Generation = Dynamic`; `Agent Radius` 55 / `Agent Height` 220. | `P` shows green floor. |
| 8 | `[FORM]` | **Werewolf character.** Import Rampage (+ alternates), compare silhouettes, pick one, delete the rest. Re-material the fur per A.9. Build `BS_Werewolf_Locomotion` + `ABP_Werewolf`. **Measure the mesh and set the capsule (110 / 55).** | It stands and idles in the sandbox, correctly scaled beside the player, in charcoal fur with no fantasy emissives. **The capsule number is now fixed and A.7's grid can be finalised.** |
| 9 | `[FN]` | `E_WolfState`, `BB_Werewolf`, `BP_Werewolf`, `BP_WerewolfController`, `BT_Werewolf` **Patrol branch only**, `BTT_FindPatrolPoint`, `BTT_SetWolfState`. | The wolf wanders the sandbox indefinitely without stalling, animating correctly. |
| 10 | `[FN]` | `AI Perception` sight config, **`Detect Neutrals` on**, `On Target Perception Updated`, Chase branch with `Observer Aborts: Both`. | The wolf abandons patrol mid-step and runs at you on sight. |
| 11 | `[FORM]` | `OnWolfStateChanged` → per-state audio: three loops on `ATT_Creature` with `Enable Occlusion`; `SC_*` classes; `SM_Chase` duck. | **Eyes closed, through a wall, you can name the wolf's state.** That is the acceptance test. |
| 12 | `[FN]` | `CatchSphere` + `OnPlayerCaught` + the death beat + `WBP_GameOver` (unstyled) + Restart. | Being touched ends the run with a visible death beat; Restart reloads. |
| 13 | `[FN]` | `AI Hearing config` + Investigate branch + `DecayMemory` + `ResetToPatrol`. | Sprinting out of sight draws the wolf to where you were; it gives up and resumes patrol. |
| 14 | `[FN]` | Tune the A.4 speed table **and the blend space play rates together**. | Sprinting barely escapes a chase and costs all stamina; no foot skate. |
| 14b | `[FORM]` | **Throwaway package smoke test** (A.17). Package Development for Windows and run the `.exe`. Fix whatever breaks. Discard the build. | An `.exe` launches into `L_Sandbox` and the wolf chases you. **Do this now, not in the reserve window.** |

### Block 3 — "it's a place" (days 12–19)

| Step | Track | Work | Test |
|---|---|---|---|
| 15 | `[FORM]` | Build the module set `SM_Blockout_*` at exactly A.7's dimensions; set `Grid Snap` 50. | Modules snap together with no gaps and no arbitrary scaling. |
| 16 | `[FN]` | Blockout `L_Mansion_Slice` per A.7 (hub, loop, no dead ends, vertical shortcut, hiding-place chamber, safe-haven footprint, **three silhouette positions**). Navmesh; verify with `P`. | Navmesh reaches every room *including through every doorway*. |
| 17 | `[FN]` | `BP_Interactable`, `BP_KeyItem`, `BP_EscapeDoor`, `WBP_Prompt`, `WBP_Escaped`, `bHasEscapeKey` on `GI_Werewolf`. | Door refuses, then opens after the key; win screen appears. |
| 18 | `[FN]` | `BP_Door` (`Can Ever Affect Navigation` false + trigger + noise); one `Nav Link Proxy`. | The wolf paths through closed doors and takes a shortcut you cannot. |
| 19 | `[FORM]` | Five master materials; per-room `MI_*` instances; apply to all blockout. | **No default grey remains.** A screenshot reads as stone/wood/plaster, not boxes. |
| 20 | `[FORM]` | Lighting pass: `Directional Light` moonlight, `Sky Light` CC0 HDRI, `BP_Candle`/`BP_Sconce`/`BP_Hearth` practicals with flicker, two-temperature discipline. | Every room is navigable; the wolf silhouettes at all three positions at 400/800/1500 cm. |
| 21 | `[FORM]` | Global `Post Process Volume` (**exposure locked**) + `Exponential Height Fog` with `Volumetric Fog`. Then **re-tune `Sight Radius`** against the finished lighting (A.3). | Dark rooms stay dark when you look at a candle. AI sight range and human sight range agree. |
| 22 | `[FORM]` | Set dressing: Infinity Blade + Poly Haven props re-materialled; one focal object and one story of use per room; 30+ decals including claw marks on the wolf's routes; Niagara dust motes, flames, embers, cold breath. | Every room has something to look at. No un-restyled fantasy geometry visible. |

### Block 4 — "it's a game you can read" (days 20–25)

| Step | Track | Work | Test |
|---|---|---|---|
| 23 | `[FORM]` | UI restyle: `F_Cinzel` / `F_EBGaramond`, palette, `T_Panel_Vellum` framed panels with double rules, `Widget Animation` fades — `WBP_Prompt`, `WBP_GameOver`, `WBP_Escaped`. | No pure white, no default blue button, nothing pops in instantly. |
| 24 | `[FORM]` | `L_Title` (one dressed corner, candle, fog, slow camera drift) + `WBP_TitleScreen` + **`WBP_Credits` populated from `CREDITS.md`**; `Game Default Map` = `L_Title`. | Title → Begin → play → Main Menu → Credits all work. Every CC-BY attribution is present. |
| 25 | `[FORM]` | Audio pass: 6–10 `Ambient Sound` beds, 4–6 `Audio Volume` + `Reverb Effect` per room type, footsteps via `Anim Notify`, UI sounds, two music cues, `Sound Concurrency` cap. | Each room sounds different with your eyes shut. |
| 26 | `[FN]` | If TP won at step 6: the A.10 body work (retarget, re-material, camera tuning). If FP won: `Set Owner No See` confirmed and optional forearms. | The player character looks period-appropriate in the perspective that ships. |
| 27 | `[FN]` | **Playtest end-to-end at least five times.** Fix only what breaks the loop or the read. | Five clean runs: explore → spotted → chased → escape or caught. |

### Block 5 — "it ships" (days 26–28, then the 28–31 August reserve)

| Step | Track | Work | Test |
|---|---|---|---|
| 28 | `[FORM]` | Disable `IA_TogglePerspective` and `bShowDebugHUD`. Full packaging pass per A.17: `List of maps to include in a packaged build`, project name and icon, **Development first, then Shipping**. | A Shipping `.exe` exists. |
| 29 | `[FORM]` | **Run the packaged build on a machine that never had the Unreal Editor.** | Title → play → win → quit, with no editor-only behaviour missing. |
| 30 | — | `README.md`, final `CREDITS.md`, submission package. **Part A is done. Stop. Do not start Part B until a packaged build exists and runs.** | |

## A.17 Packaging and release `[FORM]`

A first Unreal package reliably breaks something. **Part A ends with a packaged, runnable build,
not with PIE working in the editor.** Step 14b packages once in week 2 as a smoke test so the
reserve window is repair time, not discovery time.

**Settings.** `Project Settings → Packaging`: **`List of maps to include in a packaged build`** =
`L_Title` **and** `L_Mansion_Slice` (a map reached only via `Open Level (by Name)` is **not**
auto-cooked and will fail at runtime with a black screen); `Additional Asset Directories to Cook`
for anything referenced only by soft path or Data Table; `Use Pak File` on.
`Project Settings → Description`: game name, version, and an icon under
`Platforms → Windows → Icon` — a default Unreal icon on the submitted `.exe` undoes a surprising
amount of the finish work. `Project → Maps & Modes → Game Default Map` = `L_Title`.
Package via `Platforms → Windows → Package Project`, `Build Configuration` = **Development first**,
then **Shipping**.

**Known breakages, in the order they bite:**

1. **`Print String` and `Draw Debug*` are compiled out in Shipping.** Any behaviour that leans on
   them fails silently. Keep them behind `bShowDebugHUD` and never depend on them.
2. **Missing maps** — see `List of maps…` above. The most common Part A failure.
3. **Shipping fails where Development succeeds.** Usually toolchain, not project: Windows SDK /
   .NET / `hostfxr.dll`. Confirm Development packages *first* so you know which class of problem you
   have. Blueprint-only projects package without Visual Studio, but install the launcher
   prerequisites anyway — one C++ plugin and you need a compiler.
4. **Navmesh.** Ours is `Runtime Generation = Dynamic` so it rebuilds at runtime — verify in the
   `.exe`, not only in PIE. (`Static` would need building and saving before cooking.)
5. **`Set Game Paused` + `Set Input Mode UI Only` + `Show Mouse Cursor`** behave differently once
   the mouse is truly captured. **Test the game-over and escaped screens in the `.exe`.**
6. **Performance.** Lumen + `Virtual Shadow Maps` + volumetric fog + 50 shadow-casting practicals
   is heavy. If the packaged build is unplayable: cap `Attenuation Radius` on practicals, turn
   `Cast Shadows` off on the majority of candles (keep it on 5–10 hero lights), lower
   `Volumetric Fog → Grid Pixel Size`, and reduce `Lumen Final Gather Quality`. Do this in the
   `Post Process Volume` and light properties — not by abandoning the look.
7. **Empty or tiny output folder** = cook failed even if the UI said it finished. Read the log.

## A.18 Where narrative hooks in (do not author it)

Narrative is TBD in `project-brief.md`. These are the sockets, empty:

- `WBP_TitleScreen` — the game's title and any epigraph. Placeholder only.
- `WBP_GameOver` / `WBP_Escaped` title and body text — placeholder strings.
- `BP_KeyItem` → `PromptText` and a future `DescriptionText` — the object's identity is a narrative
  decision.
- `BP_EscapeDoor` → the refusal line. Currently a mechanical hint; eventually characterised voice.
- A future `BP_Note` / `BP_Readable` child of `BP_Interactable` is the primary narrative delivery
  vehicle and fits the existing interaction plumbing with no changes.
- The set dressing itself (A.11) is narrative-bearing and is the *only* place Part A tells story:
  whose room this was, what the occupying unit did here. Dress toward suggestion; author no text.
- The safe haven's fiction (why the werewolf cannot enter) is TBD; B.5's implementation is
  deliberately fiction-agnostic.

---
---

# PART B — STRETCH (do not begin until a packaged Part A build exists and runs)

This completes the GDD's **"Risk prototype"** milestone named in `project-brief.md`: movement +
stamina/high-scent threshold + scent trail + odor masking + one hiding place + one pounce + one
firearm + one safe haven. Part A delivers movement and stamina. B.1–B.6 deliver the rest.

**Every subsection is independently shippable.** Build them in B.6's order and stop wherever the
calendar stops you; each one improves the game on its own. **Nothing here may be started at the
cost of Part A's Form work** — a working scent trail in a grey-box game is worth less to this
deliverable than a finished-looking game without one.

Each subsection also carries a small `[FORM]` tail so that anything shipped from Part B ships
*styled*, to the same bar as Part A.

## B.1 Scent trail — representation and tuning

Unreal has **no built-in smell sense** in AI Perception (shipped senses: Sight, Hearing, Damage,
Touch, Team, Prediction, plus a Blueprint-extensible base). The established approach in real
projects is an **actor-based breadcrumb trail** the AI reads directly. Simple, debuggable, no C++.

### Data model — `/Game/Werewolf/BP_ScentMarker` (Actor, no visible mesh)

| Variable | Type | Meaning |
|---|---|---|
| `Strength` | Float | current potency, 0..1+ |
| `SpawnTime` | Float | `Get Game Time in Seconds` at creation |
| `TrailIndex` | Integer | monotonically increasing — **this is what makes it a trail, not a cloud** |

- Spawned by `BP_PlayerCharacter` on a `Set Timer by Function Name` looping at `ScentInterval` =
  0.5 s `TUNING START` — dense enough to be a path, sparse enough not to flood the level.
- `Initial Life Span` = `ScentLifetime` = 40 s `TUNING START`. **Lifespan *is* the decay**; no tick.
  Long, because this werewolf is a tracker, not a proximity monster.
- `Strength` at spawn = the player's current scent multiplier (B.2).
- `Sphere Collision` `ScentVolume`, `Sphere Radius` 250 `TUNING START`, overlap-only against a
  dedicated **`Werewolf` object channel** (create it in `Project Settings → Collision → Object
  Channels`, default response `Ignore`).

### How the werewolf follows it

Add to `BB_Werewolf`: `ScentTargetLocation` (Vector), `ScentStrength` (Float), `bHasScent` (Bool).

`BP_Werewolf` gets a `Sphere Collision` `NoseVolume`, radius 400 `TUNING START`, overlapping the
`Werewolf` channel. `On Component Begin Overlap`:
1. `Cast To BP_ScentMarker`.
2. Compare its `TrailIndex` against a `LastSmelledIndex` integer on the wolf. **Higher = fresher →
   follow it. Lower → ignore.** This single comparison is the entire directionality solution: the
   wolf always moves toward increasing index, i.e. it follows the trail the way the player walked
   it. Without it, scent-following looks drunk.
3. Write `ScentTargetLocation` = marker location, `ScentStrength` = marker `Strength`, `bHasScent` =
   true, `LastSmelledIndex` = marker `TrailIndex`, `WolfState` = `ScentPursuit` (already declared in
   A.4).

### Behavior Tree change

Insert `Sequence "ScentPursuit"` **between** `Investigate` and `Patrol` — below sight, below fresh
sound, above idle wandering. **That ordering *is* the LOCKED sensory hierarchy, expressed as
Behavior Tree priority:**

```
Selector "Brain"
├── Sequence "Chase"          (sight — highest)
├── Sequence "Investigate"    (hearing)
├── Sequence "ScentPursuit"   (smell — primary when the others are silent)   ← NEW
│     ├─ Decorator: Blackboard  Is Equal To, bHasScent = true, Observer Aborts: Both
│     ├─ Task: BTT_SetWolfState (NewState = ScentPursuit)
│     ├─ Task: Move To          Key: ScentTargetLocation, Acceptable Radius: 80
│     └─ Task: Wait             Wait Time: 0.4
└── Sequence "Patrol"          (idle)
```

Because Part A's perception handler already writes through the Blackboard and the tree already
branches on Blackboard keys, adding smell touches **no Part A logic** — it adds keys, one branch and
two overlap handlers. That is the seam promised in A.3.

`bHasScent` is cleared by the same `DecayMemory` timer when no marker has been smelled for
`ScentGiveUp` = 8 s `TUNING START`.

| Parameter | Start | Effect if raised |
|---|---|---|
| `ScentInterval` | 0.5 s | denser trail, more actors, smoother following |
| `ScentLifetime` (normal) | 40 s | wolf picks up much older routes; pressure rises sharply |
| `ScentVolume` radius | 250 | trail is "wider"; wolf catches it further off-path |
| `NoseVolume` radius | 400 | wolf detects the trail from further away |
| `ScentGiveUp` | 8 s | wolf commits longer after losing the thread |

Performance guard: 0.5 s spacing × 40 s life ≈ 80 marker actors for a moving player. Fine. If you
shorten the interval or lengthen the life substantially, keep an Array of spawned markers on the
character and `Destroy Actor` the oldest past `MaxScentMarkers` = 150 `TUNING START`.

`[FORM]` tail: a barely-visible `NS_ScentWisp` Niagara on each marker, **off by default** and
enabled only by `bShowDebugHUD`. The player is not supposed to see their own scent; the *werewolf's*
reaction is the readable channel (Pillar 4).

## B.2 The three player-readable scent states

`project-brief.md` requires the player to read **normal / high-scent / odor-masked**. Add
`E_ScentState` (`/Game/Core/Enums/E_ScentState`) with `Normal`, `HighScent`, `Masked`, and a
`ScentMultiplier` float on `BP_PlayerCharacter` feeding `BP_ScentMarker.Strength` at spawn.

| State | Entered when | `ScentMultiplier` | Marker lifespan | Player-readable cue |
|---|---|---|---|---|
| `Normal` | default | 1.0 | 40 s | steady breathing, neutral grade |
| `HighScent` | `Stamina` drops below `HighScentThreshold` = 35% `TUNING START` **while sprinting** (TBD in the brief; this is a starting value) | 2.0 `TUNING START` | 80 s `TUNING START` | heavy ragged breathing, warm desaturated post-process, faint rising heartbeat |
| `Masked` | odor supply applied (B.3) | 0.25 `TUNING START` | 12 s `TUNING START` | audible cue on application, cool blue-green tint, a scent-fading ambience that resolves as it lapses |

Rules, anchored to the LOCKED scent/stamina system:
- `HighScent` **persists** after stamina recovers, for `HighScentDecay` = 25 s `TUNING START`.
  Sprinting has a consequence that outlives the sprint — the mechanical heart of Pillar 3 and
  Pillar 5: the panic option is always available and always costs.
- `Masked` overrides `HighScent` while active but does **not** clear it — when the mask lapses the
  player may drop straight back into `HighScent`. Readable, and it makes masking a decision about
  *timing*.
- All three cues must be legible **in both perspectives** — use audio and post-process, **not**
  third-person-only body animation.
- Debug readout of `E_ScentState` behind `bShowDebugHUD` only. **No permanent scent meter** — Pillar 4.

`[FORM]` tail: implement the three cues as three `Post Process Component` blend weights on the
player plus three audio layers, tuned so they stack with A.11's global grade rather than fighting
it. Test each in the *final* lighting.

## B.3 Odor masking

`/Game/World/BP_OdorSupply` — child of `BP_Interactable`, with `E_OdorType` (`Perfume`, `Cologne`,
`Absinthe` — exactly the three named in `project-brief.md`).
- `Interact` → add to the player's inventory Array; `Destroy Actor`.
- `IA_ApplyOdor` applies one: `E_ScentState` = `Masked`, start `MaskTimer` of `MaskDuration` = 60 s
  `TUNING START`, remove the item permanently.
- **Never respawns** (Pillar 3 **LOCKED**: "finite… no respawn"). Placement is authored; no spawner.
- For the slice, differentiate the three only by `MaskDuration` and `ScentMultiplier`; meaningfully
  distinct behaviours are Part C.

`[FORM]` tail: three distinct period bottles (Poly Haven CC0 or authored) on `M_Metal_Tarnished` /
a glass instance, each with its own application sound. A recognisable silhouette on a shelf is how
the player learns a resource exists without a marker (Pillar 4).

## B.4 One hiding place, one pounce, one firearm

**Hiding place** — `/Game/World/BP_HidingSpot` (child of `BP_Interactable`), in the single
deliberate dead-end chamber A.7 reserved.
- `Interact` → `Set Actor Location` the player to a `SceneComponent` marker inside, disable movement
  input, set `bHidden` = true, blend the camera to a slit/keyhole view (works in both perspectives —
  which is why the marker is a component, not a camera).
- While `bHidden`: **stop spawning scent markers**, stop noise events, and suppress perception via
  **`Unregister from Perception System`** on the stimuli source, re-registering on exit.
- **The trail *leading to* the hiding place still exists, so the wolf arrives. That is the point.**
  It transitions to `SearchHiding` (already declared) and runs a `Wait` + investigate loop nearby
  for `SearchTime` = 15 s `TUNING START` before giving up. Anchors the LOCKED "searches hiding
  places". A found player is caught immediately (Win/Lose LOCKED).

**One pounce** — LOCKED: "telegraphed by a lowered profile; countered by a timed sideways sprint at
the moment of commitment. No dodge-roll invulnerability."
- Activate `PouncePrep` and `Pounce`. Inside the `Chase` sequence add a child `Sequence` gated by an
  `Is At Location` decorator on `TargetActor` with `Acceptable Radius` = 600 `TUNING START`.
- `PouncePrep`: `BTT_SetWolfState` → `PouncePrep`, `Max Walk Speed` → 100, play the lowered-profile
  pose, hold `PounceWindup` = 0.9 s `TUNING START`. **The windup must be visible *and* audible** —
  Pillar 2 requires the player be able to explain the capture.
- `Pounce`: `Launch Character` toward the player's position **as sampled at the end of windup**. No
  aim tracking during the leap — committing to a stale point is exactly what makes a sideways sprint
  work.
- On landing: `Wait` 1.2 s `TUNING START` recovery, then back to `Chase`. That window is the
  player's escape or shot opportunity.
- `CatchSphere` stays exactly as built in A.5 — a connecting pounce catches through the existing
  path, so the game-over flow needs no changes.

**One firearm** — LOCKED as temporary: flintlock, single-shot, silver ball + gunpowder charge per
shot; body hit = stagger, head hit = unconscious, neither kills; handgun reload ~9 s (walk, no
sprint), rifle ~12 s (no movement). Build the **handgun** for the slice.
`/Game/Player/BP_FlintlockHandgun`.
- Fire: `IA_Fire` → require `SilverBalls > 0` AND `GunpowderCharges > 0` AND `bLoaded` →
  `Line Trace By Channel` from the camera → decrement both → `bLoaded` = false →
  `Report Noise Event` `Loudness` 2.0, `Max Range` 5000 `TUNING START` (gunshots are named
  explicitly in the LOCKED sensory hierarchy).
- Hit resolution: `Break Hit Result → Hit Bone Name`. `head` → `Unconscious`; anything else →
  `Staggered`.
- `Staggered`: `WolfState` = `Staggered`, zero `Max Walk Speed`,
  `Get AI Controller → Get Brain Component → Stop Logic`, `Delay` `StaggerTime` = 3 s
  `TUNING START`, `Start Logic`, restore speed.
- `Unconscious`: same with `UnconsciousTime` = 25 s `TUNING START`, plus `Clear Value` `TargetActor`
  and `bHasScent` so the wolf wakes without knowing where you went.
- **The wolf never dies** (LOCKED). There is no health variable anywhere in this system, only
  timers. Do not add one.
- Reload: `IA_Reload` → 9 s via `Timeline` or `Set Timer`; clamp `Max Walk Speed` to walk during
  reload rather than blocking movement.

`[FORM]` tail: muzzle flash (`NS_MuzzleFlash`) + smoke that lingers in the volumetric fog, a heavy
flintlock report on `SC_SFX`, and a full-screen `Post Process` flash. A period firearm's *smoke* is
the single most characterful visual in the whole weapon; do not skip it. Sourced flintlock mesh:
Infinity Blade weapons re-silhouetted, or author a simple one — it is only ever seen at arm's
length.

## B.5 Safe haven, autosave, and the werewolf reset

LOCKED: 2–3 total; autosave only there; entering ends the pursuit and resets the werewolf to random
patrol; the werewolf cannot enter. Build **one**, in the footprint A.7 reserved.
`/Game/World/BP_SafeHaven` — Actor with a `Box Collision` `HavenVolume`.

1. **The werewolf physically cannot enter.** Place a `Nav Modifier Volume` over the interior with
   `Area Class` = **`NavArea_Null`**. The navmesh is carved out, so no path can be generated in and
   the wolf will not even attempt it. This is a *navigation* solution, not a scripted one, so it
   cannot be defeated by a state-machine bug. Belt and braces: also block the wolf capsule with
   collision at the threshold.
2. **Entering ends the pursuit.** `On Component Begin Overlap (HavenVolume)` → cast to the player →
   get the werewolf's controller → call **`ResetToPatrol`** (written once in A.3) and additionally
   clear `bHasScent` and `LastSmelledIndex`. Also destroy all live `BP_ScentMarker` actors
   (`Get All Actors of Class` → `Destroy Actor`) so the wolf cannot re-acquire the trail that led to
   the door.
3. **Autosave, only here.** `/Game/Core/SG_WerewolfSave` — a `SaveGame` class holding
   `PlayerTransform`, `Stamina`, `bHasEscapeKey`, `SilverBalls`, `GunpowderCharges`, `Inventory`
   (Array), `PickedUpActorIDs` (Array of Name — so consumed finite resources stay consumed,
   Pillar 3), `LastHavenID` (Name). On entry: `Create Save Game Object` → fill → `Async Save Game to
   Slot`, `Slot Name` `"AutoSave"`, `User Index` 0. Confirm it **diegetically** — a hearth catching
   light, a soft chord — not with a "Saved" toast (Pillar 4).
4. **Loading.** `WBP_GameOver`'s `Restart` becomes: `Does Save Game Exist` (`"AutoSave"`) → true:
   `Load Game from Slot` → `Cast To SG_WerewolfSave` → store on `GI_Werewolf` → `Open Level (by
   Name)` → on `BP_PlayerCharacter` `BeginPlay`, read the pending save off `GI_Werewolf` and apply
   it. False: plain `Open Level`. Keep the handoff **on the Game Instance** — it is the only object
   that survives `Open Level`.
   > Applying a save on `BeginPlay` fights anything else that positions the player at startup. Have
   > exactly one authority for the player's initial transform.
5. **Crafting only here** (LOCKED). For the slice, one button on a haven widget: N silver objects →
   N silver balls. Instant. Pillar 3.
6. Havens 2 and 3, and the haven *economy* (limited uses, degrading safety), are Part C.

`[FORM]` tail: the haven must be *legible as safe on sight* — this is the one place in the game
where the two-temperature rule is broken deliberately: a warm hearth, brighter than anywhere else,
visible from the doorway, with the fog thinning. That contrast is Pillar 5 *Temporary Relief*
expressed in light, and it teaches the mechanic with no UI.

## B.6 Part B build order

1. B.1 scent markers + `NoseVolume` + `ScentPursuit` branch — test in `L_Sandbox`: walk a loop and
   watch the wolf retrace it.
2. B.2 three scent states + cues — sprint, and verify the wolf tracks you harder and longer.
3. B.5 safe haven + `NavArea_Null` + `ResetToPatrol` + autosave — the wolf gives up at the
   threshold; dying restores at the haven.
4. B.3 odor masking — masked, the wolf loses a fresh trail.
5. B.4 hiding place — hide, the wolf searches, gives up.
6. B.4 pounce — the sideways sprint counter works and the windup is readable.
7. B.4 handgun + stagger/unconscious — a body shot buys 3 s, a head shot 25 s, the wolf never dies.

---
---

# PART C — RECORDED, NOT SCHEDULED

Off the 1 September critical path. Listed so nothing from `project-brief.md` is lost.

## C.1 Full werewolf state set
Complete the LOCKED list: `Charge` (counterplay is **UNDER EVALUATION** — do not invent it), richer
`SearchHiding` via the **Environment Query System** (a `Run EQS Query` task scoring hiding-spot
actors by distance and last-known-location proximity), door-opening animations via `Smart Link`
(`Receive Smart Link Reached`), "cannot swim" as a `Nav Modifier Volume` with a water area class.
Consider **State Tree** only if the Behavior Tree becomes unmanageable; the Behavior Tree is
sufficient for everything above.

## C.2 Resource economy at full scale
Silver objects scattered as one-ball-each finds; gunpowder caches; the rifle (12 s reload, no
movement) alongside the handgun; full three-odor differentiation. Pillar 3's hard constraint holds:
**the game must remain finishable with zero resources**, so every gate needs a non-combat,
non-masking solution. Audit this whenever content is added.

## C.3 Puzzle framework (do not author solutions)
Framework only, per `project-brief.md` ("TO BE CRAFTED"):
- `BP_PuzzleNode` (child of `BP_Interactable`) — one manipulable element with a state.
- `BP_PuzzleChain` — an Actor holding an Array of `BP_PuzzleNode` references and a `CheckSolved`
  function; on solve, fires an Event Dispatcher.
- `BP_AccessGate` — subscribes to a chain's dispatcher and changes world access. **Every solve must
  change navigable space**, per "each major area owns at least one puzzle chain that changes world
  access". Keep `Runtime Generation = Dynamic` so the navmesh follows.
- `BP_EscapeDoor` (A.5) is already a `BP_AccessGate` in miniature; generalise it rather than
  replacing it.
- Puzzle logic must fit the building's function and period. Content, not framework.

## C.4 World at full scale
3–5 major areas (central/public, residential/private, service/storage, military/medical, exterior
grounds; optional underground). **Level Streaming** or **World Partition** per area, keeping one
navmesh domain so the werewolf can pursue across boundaries ("travels all zones"). Resolve
mansion-vs-castle here, not before. Target playtime 2–4 hours. The A.7 module set is what makes this
affordable — new areas are new arrangements of the same grid.

## C.5 Perspective decision
Note: A.16 step 6 schedules the *comparison* in week one and records a verdict for Part A. Part C is
where the verdict is revisited with the full pounce, hiding place and scent cues in play — judge
pounce readability, hiding-place framing and scent-state legibility, then confirm or reverse, and
record it as a LOCKED line in `project-brief.md` rather than deciding silently in code.

## C.6 Art, audio and narrative beyond Part A's bar
Part A ships a *finished-looking* game; Part C raises the ceiling. Bespoke werewolf sculpt or
heavy re-silhouetting of the sourced base; an authored period costume for the protagonist (the 3+ day
greatcoat job A.10 declined); a purpose-built modular Gothic art kit replacing the blockout meshes
module-for-module on the same grid; bespoke recorded creature vocals; original score; full narrative
layer (protagonist, why trapped, werewolf origin, safe-haven fiction, ending) into A.18's sockets;
localisation; accessibility options (subtitles, remappable input, brightness — note that a
very dark game *needs* a brightness slider, so promote this if there is any slack).

---

## Appendix — verified Unreal names used in this brief

Cross-checked against current UE5 documentation and working community projects. If a name below does
not appear in the editor, the engine version differs — search the exact string in the node palette
or Details panel before improvising.

**Components:** `AI Perception`, `AIPerception Stimuli Source`, `Character Movement`, `Spring Arm`,
`Camera`, `Sphere Collision`, `Box Collision`, `Audio`, `Post Process`, `Niagara`, `Static Mesh`,
`Skeletal Mesh`.

**AI Perception:** `Senses Config`, `AI Sight config`, `AI Hearing config`, `Sight Radius`,
`Lose Sight Radius`, `Peripheral Vision Half Angle Degrees`,
`Auto Success Range from Last Seen Location`, `Max Age`, `Hearing Range`,
`Detection by Affiliation` (`Detect Enemies` / `Detect Neutrals` / `Detect Friendlies`),
`Dominant Sense`, `On Target Perception Updated`, `On Perception Updated`, `Break AIStimulus`
(`Successfully Sensed`, `Stimulus Location`, `Tag`, `Age`, `Type`), `Report Noise Event`,
`Auto Register as Source`, `Register as Source for Senses`, `Unregister from Perception System`,
`Set Generic Team Id`.

**Behavior Tree:** `Run Behavior Tree`, `Get Blackboard`, `Set Value as Object` / `as Vector` /
`as Bool` / `as Enum`, `Clear Value`, `Get Blackboard Value as Vector`,
`Set Blackboard Value as Vector`. Composites: `Selector`, `Sequence`, `Simple Parallel`. Tasks:
`Move To`, `Move Directly Toward`, `Wait`, `Wait Blackboard Time`, `Play Sound`, `Play Animation`,
`Rotate to face BB entry`, `Run EQS Query`, `Finish With Result`, `Make Noise`. Decorators:
`Blackboard`, `Cooldown`, `Loop`, `Conditional Loop`, `Time Limit`, `Is At Location`,
`Does Path Exist`, `Compare BBEntries`, `Force Success`, `Cone Check`, `Keep in Cone`,
`Is BBEntry Of Class`. Decorator properties: `Observer Aborts` (None / Self / Lower Priority /
Both), `Notify Observer` (On Result Change / On Value Change), `Key Query` (Is Set / Is Not Set /
Is Equal To / …). Custom node bases: `BTTask_BlueprintBase` (`Event Receive Execute AI`,
`Finish Execute`), `BTService_BlueprintBase` (`Event Receive Tick AI`). Brain control:
`Get Brain Component`, `Stop Logic`, `Start Logic`.

**Navigation:** `Nav Mesh Bounds Volume`, `RecastNavMesh-Default`, `Runtime Generation`
(Static / Dynamic Modifiers Only / Dynamic), `Generate Nav Links`, `Nav Modifier Volume`,
`Area Class`, `NavArea_Null`, `NavArea_Default`, `Nav Link Proxy`, `Point Links`, `Smart Link`,
`Receive Smart Link Reached`, `Can Ever Affect Navigation`, `Agent Radius`, `Agent Height`,
`Get Random Reachable Point in Radius`, `Get Random Point in Navigable Radius`, `AI Move To`,
`Line Of Sight To`, `Set Focus`, `Clear Focus`.

**Enhanced Input:** `Input Action`, `Input Mapping Context`, `Value Type` (Digital (bool) / Axis1D /
Axis2D / Axis3D), `EnhancedInputLocalPlayerSubsystem`, `Add Mapping Context`, `Get Subsystem`,
`Get Local Player`, modifiers `Negate` / `Swizzle Input Axis Values`, triggers `Pressed` /
`Released` / `Hold`, `Started` / `Triggered` / `Completed` pins.

**Animation / retargeting:** `Animation Blueprint`, `AnimGraph`, `Event Blueprint Update Animation`,
`State Machine`, `Blend Space 1D`, `Blend Poses by Enum`, `Play Anim Montage`, `Anim Notify`,
`Animation Modifier`, `Play Rate`, `Anim Class`, `IK Rig`, `IK Retargeter`, `IK_Mannequin`,
`Retarget Chains`, `Retarget Pose`, `Export Selected Animations`, `Set Owner No See`,
`Set Hidden In Game`, `SKM_Manny`, `SKM_Quinn`.

**Rendering / lighting:** `Project Settings → Rendering`, `Dynamic Global Illumination Method`
(`Lumen`), `Reflection Method`, `Shadow Map Method` (`Virtual Shadow Maps`),
`Anti-Aliasing Method` (`TSR`), `Default RHI`,
`Extend default luminance range for Auto Exposure`. `Directional Light`, `Sky Light`
(`Source Type` = `SLS Specified Cubemap`, `Cubemap`, `Real Time Capture`, `Intensity Scale`),
`Point Light`, `Spot Light`, `Rect Light`, `Intensity Units` (Candelas / Lumens / EV),
`Attenuation Radius`, `Source Radius`, `Use Temperature`, `Temperature`,
`Volumetric Scattering Intensity`, `Cast Shadows`, `Light Function Material`, `IES Texture`,
`Mobility` (Static / Stationary / Movable). `Exponential Height Fog` (`Fog Density`,
`Fog Height Falloff`, `Fog Inscattering Color`, `Volumetric Fog`, `Scattering Distribution`,
`Albedo`, `Extinction Scale`, `View Distance`, `Grid Pixel Size`).
`Post Process Volume` (`Infinite Extent (Unbound)`, `Exposure → Metering Mode` / `Min EV100` /
`Max EV100` / `Exposure Compensation`, `Local Exposure → Highlight Contrast Scale`,
`Color Grading → Global / Shadows / Midtones / Highlights → Saturation` / `Gain`,
`Lens → Image Effects → Vignette Intensity`, `Film Grain → Film Grain Intensity`,
`Lens → Bloom → Intensity`, `Lens → Chromatic Aberration → Intensity`,
`Rendering Features → Motion Blur → Amount`, `Lumen Global Illumination → Final Gather Quality`).

**Materials / decals / VFX:** `Material`, `Material Instance`, `Vector Parameter`,
`Scalar Parameter`, `Texture Sample`, `TexCoord`, `Lerp`, `Material Domain` (`Surface` /
`Deferred Decal`), `Blend Mode`, `Decal Actor`, `Niagara System`, `Niagara Emitter`, templates
`Fountain` / `Simple Sprite Burst`.

**Level / modelling:** `Modeling Mode`, `CubeGrid`, `Geometry Script`, `Grid Snap`,
`Surface Snapping`, `StaticMeshActor`, `Static Mesh` reference swap.

**UMG / UI:** `Widget Blueprint`, `Canvas Panel`, `Overlay`, `Border` (`Brush`, `Draw As` =
`Box` / `Border` / `Image`, `Margin`, `Tint`), `Size Box`, `Text Block`, `Rich Text Block`,
`Button` (`Style → Normal / Hovered / Pressed`), `Widget Animation`, `Play Animation`,
`Set Visibility`, `Font Face`, `Font`, `Slate Brush`, `Create Widget`, `Add to Viewport`,
`Remove from Parent`, `Set Input Mode UI Only`, `Set Input Mode Game Only`, `Show Mouse Cursor`,
`Common UI` (plugin, optional).

**Audio:** `Sound Wave`, `Sound Cue`, `MetaSound Source`, `Sound Class`, `Sound Mix`,
`Push Sound Mix Modifier`, `Pop Sound Mix Modifier`, `Sound Attenuation`
(`Enable Air Absorption`, `Enable Occlusion`), `Sound Concurrency`, `Ambient Sound`,
`Audio Volume`, `Reverb Effect`, `Play Sound at Location`, `Spawn Sound Attached`,
`Set Volume Multiplier`, `Set Pitch Multiplier`, `Set Sound`.

**Save / flow / packaging:** `SaveGame`, `Create Save Game Object`, `Save Game to Slot`,
`Async Save Game to Slot`, `Does Save Game Exist`, `Load Game from Slot`, `Open Level (by Name)`,
`Get Current Level Name`, `Reset Level`, `Set Game Paused`, `Quit Game`, `Disable Input`,
`Enable Input`, `Set Ignore Move Input`, `Set Ignore Look Input`, `Set View Target with Blend`,
`Launch Character`, `Line Trace By Channel`, `Break Hit Result` (`Hit Actor`, `Hit Bone Name`),
`Set Timer by Function Name`, `Set Timer by Event`, `Get All Actors of Class`,
`Get Game Time in Seconds`, `Initial Life Span`, `Print String`,
`Project Settings → Packaging` (`List of maps to include in a packaged build`,
`Additional Asset Directories to Cook`, `Use Pak File`), `Project Settings → Description`,
`Platforms → Windows → Package Project` / `Icon`, `Build Configuration`
(Development / Shipping), `Project Settings → Collision → Object Channels`.

**Debugging:** apostrophe (`'`) toggles the **Gameplay Debugger** in PIE, then number keys switch
categories (Behavior Tree, Perception, EQS, Navmesh). `P` toggles navmesh visualisation. `show
Collision` for collision. `stat unit` / `stat GPU` for the packaging performance pass (A.17 item 6).
Use these constantly.

### Sources consulted

**Unreal systems**
- [AI Perception in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/ai-perception-in-unreal-engine)
- [UAIPerceptionComponent API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/AIModule/UAIPerceptionComponent)
- [Report Noise Event (Blueprint API)](https://dev.epicgames.com/documentation/en-us/unreal-engine/BlueprintAPI/AI/Perception/ReportNoiseEvent)
- [Fix: Unreal AI Perception Not Detecting Actors (Detect Neutrals / team affiliation)](https://bugnet.io/blog/fix-unreal-ai-perception-not-detecting-actors)
- [Behavior Tree Quick Start Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-tree-in-unreal-engine---quick-start-guide)
- [Behavior Tree Node Reference: Tasks](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-behavior-tree-node-reference-tasks)
- [Behavior Tree Node Reference: Decorators](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-behavior-tree-node-reference-decorators)
- [Behavior Tree User Guide (services, custom nodes)](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-tree-in-unreal-engine---user-guide)
- [Basic Navigation in Unreal Engine](https://dev.epicgames.com/documentation/unreal-engine/basic-navigation-in-unreal-engine)
- [Modifying the Navigation Mesh (Nav Modifier, area classes)](https://dev.epicgames.com/documentation/unreal-engine/overview-of-how-to-modify-the-navigation-mesh-in-unreal-engine?lang=en-US)
- [Automatic Navigation Link Generation](https://dev.epicgames.com/documentation/en-us/unreal-engine/automatic-navigation-link-generation)
- [Get Random Reachable Point in Radius](https://dev.epicgames.com/documentation/unreal-engine/BlueprintAPI/AI/Navigation/GetRandomReachablePointinRadius)
- [Enhanced Input in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/enhanced-input-in-unreal-engine)
- [Saving and Loading Your Game in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/saving-and-loading-your-game-in-unreal-engine)
- [Module 5: Create the Game Over Screen](https://dev.epicgames.com/documentation/unreal-engine/module-5-create-the-game-over-screen)
- [Epic forums: "Implementing Blind AI" — scent-actor breadcrumb trail pattern](https://forums.unrealengine.com/t/implementing-blind-ai/122578)
- [Epic forums: "Why no smell stimuli?" — confirms no built-in smell sense](https://forums.unrealengine.com/t/why-no-smell-stimuli/472709)
- [Epic forums: Hiding from AI Perception](https://forums.unrealengine.com/t/hiding-from-ai-perception/2017799)
- [UE5 first/third person camera toggle (community tutorial)](https://dev.epicgames.com/community/learning/tutorials/d6pe/how-to-switch-between-first-and-third-person-in-unreal-engine-5-smooth-camera)

**Art, animation and rendering**
- [Volumetric Fog in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/volumetric-fog-in-unreal-engine)
- [Environmental Light with Fog, Clouds, Sky and Atmosphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/environmental-light-with-fog-clouds-sky-and-atmosphere-in-unreal-engine)
- [Creating a Gothic Horror in Unreal Engine (lighting/grading practice)](https://www.exp-points.com/marcin-wiech-creating-a-gothic-horror-in-unreal-engine)
- [Lumen deep dive — Lumen with volumetric fog and post process](https://altheragames.com/en/blog/ue5-lumen-guide)
- [Creating realistic game interiors in Unreal Engine 5](https://www.creativebloq.com/how-to/create-game-interiors-in-unreal-engine-5)
- [Game Animation Sample Project (documentation)](https://dev.epicgames.com/documentation/en-us/unreal-engine/game-animation-sample-project-in-unreal-engine)
- [Game Animation Sample — over 500 free animations (Epic blog)](https://www.unrealengine.com/blog/game-animation-sample)
- [Game Animation Sample on Fab](https://www.fab.com/listings/880e319a-a59e-4ed2-b268-b32dac7fa016)
- [Mannequin animation retargeting with IK Rig / IK Retargeter](https://docs.readyplayer.me/ready-player-me/integration-guides/unreal-engine/animations/loading-mixamo-animations-1)
- [Mixamo → UE5 retargeting workflow (IK_Mannequin, RTG naming)](https://www.unamedia.com/ue5-mixamo/docs/retarget-mixamo-to-ue5/)
- [UE4/UE5 guide to player scale and world architecture dimensions](https://www.worldofleveldesign.com/categories/ue4/ue4-guide-to-scale-dimensions.php)
- [Tips on modular level design in UE4/UE5](https://80.lv/articles/tips-on-modular-level-design-in-ue4)

**Asset sourcing and licensing (A.14)**
- [Free Epic Games Content for Unreal Engine (documentation)](https://dev.epicgames.com/documentation/en-us/unreal-engine/free-epic-games-content-for-unreal-engine)
- [$17,000,000 of Paragon content for free](https://www.unrealengine.com/paragon)
- [Final Round of Free Paragon Assets Released](https://www.unrealengine.com/en-US/blog/final-round-of-free-paragon-assets-released)
- [Paragon: Rampage on Fab](https://www.fab.com/listings/0807cf74-08fd-4a33-8c8d-f33c9439fb1f)
- [Paragon: Grux on Fab](https://www.fab.com/listings/8c4bac2c-f7f7-4632-a644-47f4e104f5d8)
- [Paragon: Khaimera on Fab](https://www.fab.com/listings/e7c665c1-8c13-42f0-9152-0753008853d7)
- [Free Infinity Blade Collection (Epic announcement)](https://www.unrealengine.com/blog/free-infinity-blade-collection-marketplace-release)
- [Free Assets on Fab — Unreal Engine, Megascans, sponsored content](https://www.unrealengine.com/en-US/fabfreecontent)
- [Epic to share new free assets on Fab every two weeks](https://www.cgchannel.com/2024/11/epic-games-to-share-new-free-assets-on-fab-every-two-weeks/)
- [Fab limited-time free assets — Personal vs Professional licence tiers](https://forums.unrealengine.com/t/fab-limited-time-free-assets-licences-personal-or-professional/2305601)
- [Megascans free to all only until the end of 2024](https://www.cgchannel.com/2024/10/epic-games-has-made-megascans-free-to-all-but-only-until-the-end-of-2024/)
- [Quixel licence page](https://quixel.com/license)
- [Quixel on Fab — new Megascans and free Megaplants](https://quixel.com/en-US/news/quixel-on-fab-new-megascans-and-megaplants)
- [Fab publishing portal open for Sketchfab migration (CC licence limits)](https://sketchfab.com/blogs/community/fab-publishing-portal-open-for-sketchfab-migration/)
- [Epic forums: what happens to free/downloadable Sketchfab assets](https://forums.unrealengine.com/t/what-will-happen-to-free-downloadable-sketchfab-assets/2039791)
- [Mixamo FAQ — licensing, royalties, ownership, EULA](https://community.adobe.com/t5/mixamo-discussions/mixamo-faq-licensing-royalties-ownership-eula-and-tos/td-p/13234775)
- [Mixamo FAQ (Adobe Creative Cloud)](https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html)
- [MetaHuman licensing](https://www.metahuman.com/license)
- [You can now sell MetaHumans, or use them in Unity or Godot](https://www.cgchannel.com/2025/06/you-can-now-sell-metahumans-or-use-them-in-unity-or-godot/)
- [Poly Haven licence (CC0)](https://polyhaven.com/license)
- [ambientCG licence (CC0)](https://docs.ambientcg.com/license/)
- [Sonniss GDC Game Audio Bundle (free download)](https://gdc.sonniss.com/)
- [Sonniss #GameAudioGDC bundle licence](https://sonniss.com/gdc-bundle-license/)
- [Freesound FAQ — CC0 vs CC-BY vs CC-BY-NC](https://freesound.org/help/faq/)
- [Kevin MacLeod / Incompetech royalty-free music (CC-BY)](https://incompetech.com/music/royalty-free/music.html)
- [Are Google Fonts free for commercial use? (OFL / Apache)](https://fontsplugin.com/google-fonts-commercial-use/)

**Packaging**
- [Epic forums: cannot package project in Shipping configuration (UE5.6)](https://forums.unrealengine.com/t/cant-package-project-in-shipping-configuration-in-ue5-6/2577252)
- [Epic forums: unable to package Windows projects in UE5 — solutions thread](https://forums.unrealengine.com/t/are-you-unable-to-package-windows-projects-in-ue5-fear-not-i-have-a-solution-for-you/231593)
- [Epic forums: Shipping package produces a Development build](https://forums.unrealengine.com/t/packaging-the-project-windows-in-shipping-mode-still-produces-development/595455)
