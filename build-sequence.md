# Build Sequence — Capstone Werewolf

**Author:** developer agent · **Consumes:** `design-brief.md` (revision 2) + `leave-offs/designer.md`
**Produces:** the ordered, executable build order for **Part A — the deliverable**
**Engine:** Unreal Engine 5 (5.4+), **Blueprint-only**, driven through an **Unreal MCP** server
**Written:** 27 July 2026 · **Hard deadline:** 1 September 2026 — **36 days**

---

## 0. How to read this document

This is an **ordered build sequence**. Execute top to bottom. Every step is written so a person
sitting in the Unreal editor (or an MCP client driving it) can do the step without re-reading the
design brief — but every step also **cites the design-brief section it implements**, so nothing here
is invented.

### Step header format

> **Step N — `[TRACK]` Title** · *`MCP` / `HAND` / `MIXED`* · **Implements:** `design-brief` §refs

- **Editor path** — the menu action or Content Browser path.
- **Do** — the concrete work, with `Blueprint node names` and property names exactly as they appear
  in the editor (the design brief's Appendix is the authority for every backticked name).
- **Produces** — the asset(s) or behaviour that exists afterwards.
- **Test** — the brief's acceptance test for that step (A.16 supplies most of these).

### Tracks (preserved from the brief, not flattened)

| Tag | Meaning |
|---|---|
| `[FN]` | **Function.** Movement, AI perception, behaviour tree, navigation, catch → game over, key → escape → win. (`design-brief` §"Part A has two tracks") |
| `[FORM]` | **Form.** Character, environment, materials, lighting, post-process, VFX, UI, audio, packaging. |

`[FN]` and `[FORM]` **alternate on purpose**. `design-brief` §0 states *"Form is not a final-week
bolt-on… A grey-box build with a default mannequin and white UI is not an acceptable deliverable."*
The ordering below is A.16's interleave, expanded — **do not batch all the art to the end.**

### Execution mode tags

| Tag | Meaning |
|---|---|
| `MCP` | Scriptable through the Unreal MCP server — asset creation, component adds, property sets, node graphs. |
| `HAND` | **Not MCP work.** Visual-judgement tasks: importing a character, `IK Retargeter` setup, dressing a room, grading a `Post Process Volume`. `design-brief` §0 "Notes for MCP-driven Blueprint work" says explicitly to budget these as hands-on and not assume they can be scripted blind. |
| `MIXED` | Skeleton via MCP, judgement pass by hand. |

### MVP-first rule (commander's binding constraint, and `design-brief` §0)

**Part A only, in this order.** Parts B and C appear at the end of this document as
**Phase 8 and Phase 9, both labelled LATER**, with real node-level detail so they are not lost —
but **nothing in Phase 8 or 9 may be started until Step 30 is signed off** (`design-brief` §0
Part B row: *"Do not start until Part A is done and a packaged build exists"*; leave-off item 12).

---

## 1. Calendar — reconciled against today

`design-brief` §0 "Calendar" assumed a **25 July** start. **Today is 27 July** — two days of the
six-day pre-production window are already gone. Pre-production is therefore **compressed to four
days (27–30 July)** and Block 1 must still start on **31 July**. The 28-day Part A window and the
4-day reserve are unchanged.

| Phase | Steps | Window | Days | Deliverable at the end |
|---|---|---|---|---|
| **Phase 0 — gate & pre-production** | 0a, 0b, 0c | **27 – 30 Jul** | 4 (was 6) | MCP responds; every A.14 asset downloaded and licence-logged |
| **Phase 1 — "it moves"** | 1 – 6 | 31 Jul – 3 Aug | 4 | Walk/sprint/crouch in a sandbox; **perspective decided at step 6** |
| **Phase 2 — "it hunts"** | 7 – 14b | 4 – 10 Aug | 7 | Werewolf patrols, sees, hears, chases, catches; **throwaway `.exe` at 14b** |
| **Phase 3 — "it's a place"** | 15 – 22 | 11 – 18 Aug | 8 | Styled, lit, dressed, navigable mansion slice with key + escape door |
| **Phase 4 — "it's a game you can read"** | 23 – 27 | 19 – 24 Aug | 6 | Styled UI, title screen, credits, full audio pass, five clean playtests |
| **Phase 5 — "it ships"** | 28 – 30 | 25 – 27 Aug | 3 | **Shipping `.exe` verified on a clean machine.** Part A done. |
| **Reserve** | — | 28 – 31 Aug | 4 | Packaging repair, README, final `CREDITS.md`, submission. **Not feature time.** |
| **Phase 8 / 9 — LATER** | B / C | only if Step 30 signed off early | — | Part B stretch, Part C recorded |

**Deadline pressure, stated plainly.** The single scheduling decision that protects the deadline is
**Step 14b — the throwaway package smoke test in week 2** (`design-brief` §A.16 Block 2, §A.17;
leave-off item 8). A first Unreal package reliably breaks something. Doing it on **10 August**
converts the 28–31 August reserve from *discovery* time into *repair* time. **Do not move 14b.**

---

## 2. Guardrails — read once, obey throughout

These are the designer's twelve "must not miss" items (`leave-offs/designer.md`) mapped to the step
that enforces each. The inspector should be able to find every one of them in the sequence below.

| # | Guardrail | Enforced at |
|---|---|---|
| 1 | Re-establish the Unreal MCP connection. **Nothing else can start.** | **Step 0a** |
| 2 | Claim/download every A.14 asset during pre-production; claim every Fab bi-weekly free drop through 1 Sept | **Step 0b**, recurring reminder in **Step 0c** |
| 3 | **`Detect Neutrals` = true** on both sense configs | **Steps 10, 13** |
| 4 | **Press `P` after every level edit**; `Runtime Generation = Dynamic`; `Agent Radius` 55 / `Agent Height` 220 | **Steps 7, 16, 18** |
| 5 | **`Observer Aborts: Both`** on Chase/Investigate decorators | **Steps 10, 13** |
| 6 | **Step 6 is a real decision gate**; do not delete either camera before it | **Steps 2, 3, 6** |
| 7 | **Step 8 fixes the werewolf capsule from the real mesh** — import the character *before* blockout | **Step 8** (gates **Step 15**) |
| 8 | **Step 14b packages a throwaway build in week 2 on purpose** | **Step 14b** |
| 9 | **Re-tune `Sight Radius` at step 21**, after finished lighting exists | **Step 21** |
| 10 | **`List of maps to include in a packaged build`** must name **`L_Title` and `L_Mansion_Slice`** | **Steps 14b, 28** |
| 11 | `TUNING START` = free to change; `LOCKED` = frozen. Tune wolf chase 460 vs player sprint 480 by feel, wolf slower by 10–30 | **Step 14** |
| 12 | **Step 30 is a hard stop.** No Part B until a packaged build runs on a clean machine | **Step 30 / Phase 8 gate** |

Plus these standing prohibitions, all from the brief:

- **No survival timer of any kind.** (`design-brief` §A.15 F18 — anchored to `project-brief.md`
  *"there is no survive-until-sunrise timer"*.) Never add one.
- **No health bar, no permanent HUD, no stamina bar, no scent meter, no minimap, no objective
  marker.** (`design-brief` §A.12 "And what there deliberately is *not*".) Stamina is breath +
  vignette (§A.2); the wolf is sound + silhouette (§A.9, §A.13).
- **The werewolf never dies.** No health variable anywhere, ever — only timers (§B.4).
- **No pure white (`#FFFFFF`) anywhere, including UI** (§A.8 Palette, §A.12).
- **Nothing enters `/Game/Sourced/` unless it is a row in §A.14.** If you cannot name the licence,
  do not import the asset (§A.14 obligation 6).
- **Never import a sourced asset straight into `/Art/`** (§A.1 note on `/Game/Sourced/`).
- **`Print String` is compiled out of Shipping.** Never let real behaviour depend on it
  (§A.2, §A.12, §A.17 breakage 1).
- **Do not author narrative text.** §A.18 lists the empty sockets; fill them with placeholders only.

---
---

# PHASE 0 — GATE & PRE-PRODUCTION (27 – 30 July)

*No feature work happens in this phase. `design-brief` §0 "Calendar", §A.16 Block 0.*

---

### Step 0a — `[—]` Re-establish the Unreal MCP connection · *HAND* · **Implements:** `design-brief` §A.16 Block 0 step 0a; §0 "Notes for MCP-driven Blueprint work"; leave-off item 1

> **THIS STEP IS A HARD GATE. Every step from 0b to 30 is blocked until 0a's smoke test passes.**
> Current state, verified at the time of writing: **there is no `.mcp.json` in the project root and
> no Unreal MCP tools are exposed to the client.** The connection is **NOT** live. It was set up
> once before, so the goal is *recovery*, not first-time invention.

**0a.1 — Find the previous setup before rebuilding it.** Search, in this order:

- `<ProjectRoot>\Plugins\` — an existing `UnrealMCP` / `MCPGameProject`-style plugin folder.
- `<ProjectRoot>\.mcp.json` (absent today) and `<ProjectRoot>\.claude\settings.json`.
- `%APPDATA%\Claude\claude_desktop_config.json` — a prior `mcpServers` entry naming the server
  command and its working directory.
- `%USERPROFILE%\.claude.json` — user-scope MCP server registrations.
- Any sibling checkout of the MCP server repo (Python or Node) with its own `README`.

Whatever is found names the **server command**, the **transport** (almost always `stdio` to a local
Python/Node process, which then talks to the editor over a local TCP socket), and the **port**.

**0a.2 — Enable the editor side.**

- `Edit > Plugins > Scripting` → enable **`Python Editor Script Plugin`** and
  **`Editor Scripting Utilities`**.
- `Edit > Plugins` → search `MCP` → enable the project's Unreal MCP plugin if one exists.
- If the recovered server uses Remote Control rather than a custom plugin:
  `Edit > Plugins > Messaging` → enable **`Remote Control API`** and **`Web Remote Control`**, then
  `Project Settings > Plugins > Web Remote Control` and note the HTTP port (default `30010`).
- **Restart the editor.** Plugin enables do not take effect until restart.

**0a.3 — Register the server with the client.** Create `.mcp.json` in the **project root** (this is
a configuration change and must be made by the user / with explicit approval — an agent must not
write it unilaterally). Shape:

```json
{
  "mcpServers": {
    "unreal": {
      "command": "<python-or-node>",
      "args": ["<absolute path to the recovered server entry point>"],
      "env": { "UNREAL_HOST": "127.0.0.1", "UNREAL_PORT": "<port from 0a.1/0a.2>" }
    }
  }
}
```

**0a.4 — Smoke test, and it must actually pass.** With the editor open on the project:

1. Client reports the `unreal` server **connected** and lists its tools.
2. Through MCP: `Content Browser > Add > Blueprint Class > Actor` → create `/Game/_MCPTest/BP_MCPSmokeTest`.
3. Through MCP: add a `Static Mesh` component, set a property, **compile**, **save**.
4. Through MCP: read the asset back to confirm the property stuck.
5. Delete `/Game/_MCPTest/`.

**Produces:** a live, verified MCP link and a deleted test asset.
**Test (brief's own):** *"MCP responds; a test Blueprint can be created and deleted."*

**0a.5 — Failure path, because the deadline does not move.** If 0a.4 has not passed by **end of
30 July**, stop trying to recover MCP and **build Part A by hand in the editor**. Every step below
is written as editor paths and node names precisely so it is executable either way. Record the
decision; MCP is an accelerator, not a dependency of the deliverable.

> **Gap flagged.** `design-brief.md` requires the MCP connection (§0, §A.16 step 0a) but **never
> names the server implementation, repo, transport or port**. 0a.1 is therefore a recovery search
> rather than a recipe. This is the one place in this document where the brief could not supply the
> specifics, and I have not gone looking for a different answer.

---

### Step 0b — `[FORM]` Claim, download and licence-log every A.14 asset · *HAND* · **Implements:** `design-brief` §A.14 (all 16 rows, **binding**); §A.16 Block 0 step 0b; leave-off item 2

**Editor path / external:** Epic Games Launcher → `Fab` → *Library* / *Free* tab; plus the browser
downloads below. Import into Unreal is **not** done here — only claiming, downloading and logging.

**Do — claim in this order (row numbers are §A.14 rows):**

| A.14 row | Claim / download | Used at step |
|---|---|---|
| 1 | **Paragon: Rampage** (Fab → Epic Games Content) | 8 |
| 2 | **Paragon: Khaimera**, **Paragon: Narbash** (silhouette alternates) | 8 |
| 3 | **Game Animation Sample** (Epic, free, Unreal-only) | 5 |
| 4 | **Paragon: Wraith / Gideon / Revenant / Murdock / Sparrow** (only if TP wins at step 6) | 26 |
| 5 | `SKM_Manny` / `SKM_Quinn` / `IK_Mannequin` — arrive free with the Third Person template | 1 |
| 7 | **ambientCG** stone / plaster / wood / metal / fabric surface sets (**CC0**) | 19 |
| 8 | **Poly Haven** night HDRI + surfaces + furniture-class props (**CC0**) | 20, 22 |
| 9 | **Infinity Blade** Grass Lands / Ice Lands / Fire Lands / Weapons / Adversaries / Effects | 22 |
| 10 | **Every Fab bi-weekly free drop** — claim now and **keep claiming every two weeks through 1 Sept**, used or not (claimed = kept permanently, costs nothing) | opportunistic |
| 11 | **Sonniss GDC Game Audio Bundle** (royalty-free, no attribution) | 11, 25 |
| 12 | **Freesound**, filtered **CC0 first**; CC-BY acceptable *with credit*; **reject CC-BY-NC and Sampling+** | 11, 25 |
| 13 | **Infinity Blade: Effects / Sounds** — creature vocal base, to be pitched down | 11 |
| 14 | **Kevin MacLeod / Incompetech** — exactly two cues (game-over, escape). **CC-BY: attribution REQUIRED** | 25 |
| 15 | **Google Fonts `Cinzel`, `EB Garamond`** (+ optional `UnifrakturMaguntia`) — **SIL OFL 1.1** | 23 |
| 16 | **ambientCG / Poly Haven / Kenney** CC0 paper + icon set for `T_Panel_Vellum` and keybind glyphs | 23 |

**Do not download:** Quixel Megascans (free era ended 31 Dec 2024), Sketchfab (licence types retired
in the Fab migration), Mixamo (deprecation signalled; humanoid-only), any paid listing, any
`Personal`-tier / non-commercial / CC-BY-NC listing. AI text-to-3D is an **academic-integrity
question for the commander**, not a build decision — do not use it. (§A.14 "Sources deliberately
NOT used".)

**Produces:** every Part A asset on disk, claimed under a nameable licence.
**Test (brief's own):** *"Every download has a `CREDITS.md` row **and** a saved licence file."*

---

### Step 0c — `[—]` Stand up the compliance artefacts · *HAND* · **Implements:** `design-brief` §A.14 "Compliance obligations" 1–6; §A.1 `/Game/Sourced/` note

**Editor path / repo:** filesystem, alongside `design-brief.md`.

**Do:**
1. Create `/CREDITS.md` at the repo root with columns: **asset · author · source URL · licence name
   + version · date downloaded · required attribution string · where it is used.** Fill it **as you
   download in 0b**, not afterwards (§A.14 obligation 1 — *"retro-fitting this at the end is how
   projects end up shipping assets they cannot prove"*).
2. Create `/Docs/licences/` and save a copy of each licence (PDF or `.txt`) **captured at download
   date** (§A.14 obligation 3). For any Sketchfab-class source, save the licence page as PDF *at the
   moment of download*.
3. Mark rows **1–6, 9, 13** in `CREDITS.md` as **Unreal-only licences** — nothing from them may be
   exported to another engine or shipped as a standalone model (§A.14 obligation 4).
4. Note in `CREDITS.md` which rows are **CC-BY and therefore must appear in `WBP_Credits`**: row 14
   music, any CC-BY Freesound entries, and the row 15 fonts (§A.14 obligation 2).
5. Diary reminder: **re-claim Fab free drops every two weeks until 1 September.**

**Produces:** `/CREDITS.md`, `/Docs/licences/` — the inputs Step 24 reads to populate `WBP_Credits`.

---
---

# PHASE 1 — "IT MOVES" (31 July – 3 August, days 1–4)

*`design-brief` §A.16 Block 1. Ends at the perspective decision gate.*

---

### Step 1 — `[FN]` Project skeleton, folders, core classes, render settings · *MIXED* · **Implements:** `design-brief` §A.1 (all of it); §A.16 step 1

**1.1 Create the project.** Epic Games Launcher → `Unreal Engine 5.4+` → `Games` →
**`Third Person`** template → **Blueprint** → name **`CapstoneWerewolf`**.
**Not Blank.** §A.1: the template ships `SKM_Manny`, `SKM_Quinn`, `IK_Mannequin` (the `IK Rig` every
retarget in §A.9/§A.10 starts from) and a working locomotion `Animation Blueprint` — this is A.14
row 5 arriving for free. *"Starting Blank throws away days of free work."*

**1.2 Create the folder tree** exactly as §A.1 specifies — `Content Browser > right-click > New Folder`:

```
/Game/Core (+ /Enums) · /Input · /Player · /Werewolf (+ /Tasks) · /World
/Game/UI (+ /Style) · /Art (Materials + /Instances + /Decals, Textures, Blockout, VFX)
/Game/Audio (Ambience, Creature, Player, UI, Music, Classes, Mixes, Attenuation)
/Game/Sourced  ← one subfolder per source · /Game/Maps
```

`/Game/Sourced/` is a **licence-compliance mechanism** (§A.1): one folder per source so
`CREDITS.md` and `WBP_Credits` can be assembled by reading folder names and a problem asset can be
pulled without hunting.

**1.3 Core classes.** `Content Browser > Add > Blueprint Class`:
- `Game Mode Base` → `/Game/Core/GM_Werewolf`
- `Game Instance` → `/Game/Core/GI_Werewolf`
- `Player Controller` → `/Game/Core/PC_Werewolf`

**1.4 `Project Settings > Project > Maps & Modes`:** `Default GameMode` = `GM_Werewolf`;
`Default Pawn Class` = `BP_PlayerCharacter` (set after step 2); `Player Controller Class` =
`PC_Werewolf`; `Game Instance Class` = `GI_Werewolf`; `Editor Startup Map` = `L_Sandbox`;
**`Game Default Map` = `L_Title`** (set after step 24 — until then leave it on `L_Sandbox` and
change it at step 24; §A.1, §A.17).

**1.5 `Project Settings > Engine > Rendering` — set now, once.** §A.1 warns changing these later
invalidates lighting work:

| Setting | Value |
|---|---|
| `Dynamic Global Illumination Method` | `Lumen` |
| `Reflection Method` | `Lumen` |
| `Shadow Map Method` | `Virtual Shadow Maps` |
| `Anti-Aliasing Method` | `TSR` |
| `Default RHI` | `DirectX 12` |
| `Extend default luminance range for Auto Exposure` | **on** (needed for the §A.11 exposure lock) |

**1.6 Maps.** `File > New Level > Empty Level` → save as `/Game/Maps/L_Sandbox`, `L_Mansion_Slice`,
`L_Title`. In `L_Sandbox` place a flat floor box and a `Player Start` (§A.6 item 7).

**Produces:** the project, the folder contract every later path in this document depends on.
**Test (brief's own):** *"PIE launches into an empty box."*

---

### Step 2 — `[FN]` `BP_PlayerCharacter`, both cameras, Enhanced Input, move & look · *MCP* · **Implements:** `design-brief` §A.2 (components, Enhanced Input table); §A.15 F1, F4; §A.16 step 2

**2.1 Create the pawn.** `Content Browser > Add > Blueprint Class > Character` →
`/Game/Player/BP_PlayerCharacter`. Component hierarchy exactly per §A.2:

```
CapsuleComponent (root)
├── Mesh
│   └── Camera_FP                 (Camera)  Parent Socket: head
├── SpringArm_TP                  (Spring Arm)
│   └── Camera_TP                 (Camera)
├── InteractTrace                 (Scene)
├── BreathAudio                   (Audio)
└── AIPerceptionStimuliSource     (AIPerception Stimuli Source)
```

**2.2 Component properties.**
- `AIPerception Stimuli Source`: **`Auto Register as Source` = true**; `Register as Source for
  Senses` = `AISense_Sight`, `AISense_Hearing`. §A.2 makes this explicit even though Pawns
  auto-register for sight.
- `SpringArm_TP`: `Target Arm Length` **300** `TUNING START`, `Socket Offset` Z **60**,
  `Do Collision Test` true, `Use Pawn Control Rotation` true, `Camera Lag` ~**0.1**.
- `Camera_FP`: `Use Pawn Control Rotation` true, attached to the mesh's **`head`** socket, offset
  ~(0, 15, 0).
- `Character Movement`: `Max Walk Speed` 220, `Max Walk Speed Crouched` 120, `Can Crouch` **true**,
  `Crouched Half Height` 45, **`Jump Z Velocity` 0 (no jump — vertical traversal is authored)**,
  `Air Control` 0.1. All `TUNING START` except the no-jump decision.

> **Both cameras exist and neither may be deleted.** §A.2 *"Keeping perspective swappable (do not
> resolve this)"*; §0 *"Perspective… still PROVISIONAL"*; leave-off item 6. The decision happens at
> **Step 6** and nowhere else.

**2.3 Input assets.** `Content Browser > Add > Input`:
- `Input Mapping Context` → `/Game/Input/IMC_Default`
- `Input Action` → `IA_Move` (`Value Type` Axis2D), `IA_Look` (Axis2D), `IA_Sprint` (Digital),
  `IA_Crouch` (Digital), `IA_Interact` (Digital), `IA_TogglePerspective` (Digital, **dev tool**).

**2.4 `IMC_Default` bindings** (§A.2 Enhanced Input table):
`IA_Move` — W with `Swizzle Input Axis Values` (YXZ); S with `Swizzle` + `Negate`; A with `Negate`;
D none; plus Gamepad Left Thumbstick 2D-Axis. `IA_Look` — Mouse XY 2D-Axis with `Negate` on Mouse Y,
plus Right Thumbstick. `IA_Sprint` — Left Shift / Left Shoulder. `IA_Crouch` — Left Ctrl or C / Face
Button Right. `IA_Interact` — E / Face Button Bottom. `IA_TogglePerspective` — **V**.

**2.5 `Event BeginPlay` graph** (§A.2, in execution order):
`Event BeginPlay` → `Get Controller` → `Cast To PlayerController` → `Get Local Player` →
`Get Subsystem` (`EnhancedInputLocalPlayerSubsystem`) → **`Add Mapping Context`** (`IMC_Default`,
Priority 0) → call `ApplyPerspective` (built in step 3).

**2.6 Move / look graphs.**
- `IA_Move` (`Triggered`) → `Get Action Value` → `Break Vector 2D` → two × `Add Movement Input`,
  using **control-rotation-derived** forward/right vectors (`Get Control Rotation` →
  `Get Forward Vector` / `Get Right Vector`, yaw only) — §A.2: one graph that is correct in **both**
  perspectives.
- `IA_Look` (`Triggered`) → `Add Controller Yaw Input` (X) and `Add Controller Pitch Input` (Y).
- `IA_Crouch` (`Started`) → `Branch` on `Is Crouched` → `UnCrouch` / `Crouch`.

**2.7** `Project Settings > Maps & Modes > Default Pawn Class` = `BP_PlayerCharacter`.

**Produces:** a controllable pawn carrying both cameras.
**Test (brief's own):** *"You can walk and look in `L_Sandbox`."*

---

### Step 3 — `[FN]` `ApplyPerspective` + the `V` toggle · *MCP* · **Implements:** `design-brief` §A.2 "Keeping perspective swappable"; §A.15 F4; §A.16 step 3; leave-off item 6

**Editor path:** `BP_PlayerCharacter > My Blueprint > Functions > Add Function` → `ApplyPerspective`.

**3.1 Variables:** `bFirstPerson` (Boolean, **`Instance Editable`**, default `true` `TUNING START` —
§A.2 calls this *"a coin-flip for testing, **not** a decision"*), `bAllowPerspectiveToggle`
(Boolean, default true; **gated off at step 28**).

**3.2 `ApplyPerspective` nodes, in order:**
1. `Branch` on `bFirstPerson`.
2. **True:** `Activate` (`Camera_FP`) → `Deactivate` (`Camera_TP`) → **`Set Owner No See`** on `Mesh`
   = **true** *(§A.2 prefers this over `Set Hidden In Game` — the body still casts a shadow, "a free
   and convincing first-person detail")* → `Set Use Controller Rotation Yaw` (self) = true →
   `Character Movement` → `Set Orient Rotation to Movement` = false.
3. **False:** `Activate` (`Camera_TP`) → `Deactivate` (`Camera_FP`) → `Set Owner No See` = false →
   `Set Use Controller Rotation Yaw` = false → `Set Orient Rotation to Movement` = true →
   `Rotation Rate` = (0, 540, 0).

**3.3 Toggle handler:** `IA_TogglePerspective` (`Started`) → `Branch` on `bAllowPerspectiveToggle`
→ `Set bFirstPerson` = `Not Boolean` (`bFirstPerson`) → `ApplyPerspective`.

**Produces:** runtime-switchable FP/TP, the mechanism Step 6 needs to judge with.
**Test (brief's own):** *"`V` flips FP↔TP and both control correctly."*

---

### Step 4 — `[FN]` Crouch, sprint, stamina, breath, sprint noise · *MCP* · **Implements:** `design-brief` §A.2 "Movement and stamina", "Readable stamina without a HUD bar", "Sprinting is audible"; §A.15 F1, F2, F3, F7; §A.16 step 4

**4.1 Variables on `BP_PlayerCharacter`** (all `TUNING START`): `Stamina` 100, `MaxStamina` 100,
`bSprintHeld`, `SprintSpeed` **480**, `WalkSpeed` **220**, `StaminaDrainPerSec` 18,
`StaminaRegenPerSec` 12, `StaminaRegenDelay` 1.5, `TimeSinceDrain`, `NoiseAccumulator`,
`bShowDebugHUD` (Boolean, default false).

**4.2 Sprint input:** `IA_Sprint` `Started` → `Set bSprintHeld` = true; `Completed` → false.
**Sprint is a speed override, not a mode** (§A.2).

**4.3 `TickStamina(DeltaSeconds)` function, called from `Event Tick`:**
1. `Branch`: `bSprintHeld` **AND** `Stamina > 0` **AND** `Get Velocity` → `Vector Length` > 10.
2. **True:** `Set Max Walk Speed` = `SprintSpeed`; `Stamina` −= `StaminaDrainPerSec * DeltaSeconds`;
   **`Clamp (float)`** 0..`MaxStamina`; reset `TimeSinceDrain` = 0.
3. **False:** `Set Max Walk Speed` = `WalkSpeed`; accumulate `TimeSinceDrain`; once it exceeds
   `StaminaRegenDelay`, `Stamina` += `StaminaRegenPerSec * DeltaSeconds`, `Clamp (float)`.
4. At `Stamina` 0 → force `Set bSprintHeld` = false so the player must **re-press** (§A.2: readable,
   Pillar 2).

**4.4 Diegetic stamina readout — no HUD bar** (§A.2; §A.15 F3):
- Compute `Ratio` = `1 - (Stamina / MaxStamina)`.
- `BreathAudio` looping → **`Set Volume Multiplier`** and **`Set Pitch Multiplier`** driven from
  `Ratio`.
- Add a **`Post Process`** component to `BP_PlayerCharacter`, `Blend Weight` ~**0.4** so it layers
  over §A.11's global grade rather than fighting it, driving
  `Lens > Image Effects > Vignette Intensity` from the same `Ratio`.
- Numeric readout only behind `bShowDebugHUD` via `Print String` — **never depend on it** (§A.17
  breakage 1).

**4.5 Sprinting is audible — Part A's whole detection story** (§A.2):
Inside `TickStamina`, on the sprint branch, accumulate time and at most every **0.35 s**
`TUNING START` call **`Report Noise Event`** (`AI > Perception`):

| Movement | `Loudness` | `Max Range` | `Tag` |
|---|---|---|---|
| Sprint | 1.0 | 1800 | `Footstep_Sprint` |
| Walk | 0.3 | 600 | `Footstep_Walk` |
| **Crouch** | **nothing — silent** | — | — |

`Noise Location` = `Get Actor Location`, `Instigator` = self. Anchor (§A.2): *"Hearing = authored
range (investigates sprinting…)"*.

> **Gap flagged.** §A.2 specifies the `Tag` `Footstep_Sprint` but no Part A consumer ever reads
> `Break AIStimulus > Tag` (§A.3 step 3 decides the sense with `Line Of Sight To` instead). The tags
> are therefore inert in Part A — set them anyway, they cost nothing and Part B may want them.

**Produces:** the LOCKED stamina half of the scent/stamina system, plus the only long-range signal
the werewolf can act on in Part A.
**Test (brief's own):** *"Sprint drains, breath rises, sprint cuts out at zero."*

---

### Step 4a — `[FORM]` Audio mix architecture skeleton · *MCP* · **Implements:** `design-brief` §A.13 "Mix architecture — set this up first, it takes 20 minutes"

> **Inserted step, and here is why.** §A.13 says the mix architecture is the *first* audio job, but
> §A.16 does not give it a number until step 11 — while step 4's `BreathAudio` already needs a
> `Sound Class` to be assigned to. Twenty minutes here prevents re-tagging every `Sound Wave` later.
> This is an ordering fix, not new scope: every asset below is named in §A.13.

**Editor path:** `Content Browser > Add > Audio`.
- **`Sound Class`** → `/Game/Audio/Classes/`: `SC_Master`, and as children of it `SC_Ambience`,
  `SC_SFX`, `SC_Creature`, `SC_UI`, `SC_Music`.
- **`Sound Mix`** → `/Game/Audio/Mixes/`: `SM_Default`, `SM_Chase` (populated at step 11).
- **`Sound Attenuation`** → `/Game/Audio/Attenuation/`: `ATT_Creature` (inner ~600, falloff ~4000,
  **`Enable Air Absorption`** on, **`Enable Occlusion`** on with a low-pass when occluded) and
  `ATT_Prop` (short falloff).
- Assign `BreathAudio`'s sound to **`SC_Player`-equivalent → `SC_SFX`** and confirm every imported
  `Sound Wave` from here on gets a `Sound Class`.

**Produces:** the mix graph everything from step 11 and step 25 hangs off.

---

### Step 5 — `[FORM]` Import Game Animation Sample; build `ABP_Player` · *HAND* · **Implements:** `design-brief` §A.10 "$0 sources, whichever branch wins"; §A.14 row 3; §A.16 step 5

**Editor path:** Epic Games Launcher → Library → **Game Animation Sample** → *Add to project* (or
migrate its `Content` into **`/Game/Sourced/GameAnimationSample/`** — §A.1 forbids importing a
sourced asset straight into `/Art/`).

**Do:**
1. Take the **animations**, not the Motion Matching rig — §A.10: *"a plain `Blend Space 1D` from its
   walk/run/crouch clips is lighter and entirely sufficient, and Motion Matching adds tuning time we
   do not have."*
2. `Content Browser > Add > Animation > Blend Space 1D` on the **UE5 Mannequin skeleton** →
   `/Game/Player/BS_Player_Locomotion`, axis `Speed` 0→500, samples: idle 0, walk ~220, run ~480 —
   **matching §A.2's `WalkSpeed` and `SprintSpeed` so the feet do not skate**.
3. `Content Browser > Add > Animation > Animation Blueprint` (skeleton `SK_Mannequin`) →
   `/Game/Player/ABP_Player`. `AnimGraph`: `State Machine` → `Locomotion` state driving the blend
   space from a `Speed` float set in **`Event Blueprint Update Animation`**
   (`Get Velocity` → `Vector Length`). Add a crouch state fed by `Is Crouched`.
4. `BP_PlayerCharacter > Mesh > Anim Class` = `ABP_Player`.

**Produces:** a non-T-posing player body, which is what makes Step 6's third-person branch judgeable
at all.
**Test (brief's own):** *"No T-pose; no foot skate at 220 and 480 uu/s."*

---

### Step 6 — `[FORM]` **PERSPECTIVE DECISION GATE** · *HAND* · **Implements:** `design-brief` §0 "Things this brief deliberately does NOT decide"; §A.10 (the whole cost table); §A.15 F4; §A.16 step 6; §C.5; leave-off item 6

> **This is a real decision gate and it is scheduled in week one on purpose.** §A.10: first person
> costs **~0.5 extra Form days**, third person costs **~3–5**, *"out of the same 28-day budget as
> the functional work."* Deciding late means paying the cost twice or paying it in the reserve
> window. **Do not resolve it silently in code and do not delete either camera before this step.**

**Do:**
1. In `L_Sandbox`, author a **60-second traverse**: a corridor at the §A.7 clear width (**300 cm**),
   one **200 × 280** doorway, one turn, one open room, and a scripted pass of the werewolf silhouette
   across the far end. (The wolf mesh does not exist until step 8 — for step 6 use `SKM_Manny`
   scaled up as a stand-in shape; §A.10 explicitly permits `SKM_Manny` as *"a step-6 stand-in"*,
   A.14 row 5.)
2. Play the identical traverse in **FP** and in **TP**, toggling with **`V`**.
3. Judge on §A.10's three criteria: **threat legibility** (Pillar 2 is measured in the perspective
   that ships), **doorway framing** in a 300 cm corridor, and **whether the visible body helps or
   hurts**.
4. If TP is winning, sanity-check the §A.10 minimum bar now: `SpringArm_TP` with `Do Collision Test`
   true, `Probe Size` raised, `Camera Lag` ~0.1 — *does the camera clip the corridor walls?*
5. **Write the verdict into `project-brief.md` as a new `LOCKED` line.**

**Produces:** a written verdict; the Form budget for §A.10 is now a known number, which is what steps
26 and the Phase 3/4 day allocation depend on.
**Test (brief's own):** *"A written verdict exists."*

**Branch effect on later steps:**
- **FP wins** → step 26 is ~0.5 day: confirm `Set Owner No See`, optionally add forearms. A.14 row 4
  is not needed.
- **TP wins** → step 26 is ~3–5 days: A.14 row 4 Paragon coat-silhouette hero, `IK Rig` +
  `IK Retargeter` from **`IK_Mannequin`** (naming `IK_<Hero>` / `RTG_Mannequin_<Hero>`),
  re-material to the §A.8 palette, camera tuning. **Take the days out of Phase 3's dressing time,
  not out of the reserve.**

---
---

# PHASE 2 — "IT HUNTS" (4 – 10 August, days 5–11)

*`design-brief` §A.16 Block 2. This phase produces the MVP loop's predator and the first `.exe`.*

---

### Step 7 — `[FN]` Navigation in `L_Sandbox` · *MCP* · **Implements:** `design-brief` §A.6 items 1, 2, 3, 7; §A.15 F13; §A.16 step 7; leave-off item 4

1. `Place Actors > Volumes > Nav Mesh Bounds Volume` in `L_Sandbox`, scaled to enclose the floor plus
   margin. A **`RecastNavMesh-Default`** actor appears in the `Outliner`.
2. `RecastNavMesh-Default > Details > Runtime Generation` = **`Dynamic`** (§A.6 item 2 — doors move,
   and Parts B/C add dynamic obstacles).
3. `Project Settings > Engine > Navigation Mesh > Agent Radius` = **55**, `Agent Height` = **220**
   `TUNING START`, matching §A.4/§A.9's werewolf capsule. **§A.6 item 3: this is the number that
   sizes the architecture** — radius 55 → ~150 cm minimum clear doorway; §A.7 uses **200 cm** for
   margin.
4. **Press `P`.** Green floor or nothing works. **Press `P` after every level edit, forever**
   (§A.6 item 1; leave-off item 4).
5. Learn the debug keys now: apostrophe (**`'`**) toggles the **Gameplay Debugger** in PIE, then
   number keys switch Behavior Tree / Perception / EQS / Navmesh categories (§A.6 item 7,
   Appendix "Debugging"). §A.6: *"This habit saves more hours than anything else in this brief."*

**Test (brief's own):** *"`P` shows green floor."*

---

### Step 8 — `[FORM]` **Werewolf character — and the capsule that sizes the building** · *HAND* · **Implements:** `design-brief` §A.9 (whole section); §A.14 rows 1, 2; §A.15 V6, V7; §A.16 step 8; leave-off item 7

> **This step must happen before blockout (step 15/16).** §A.9: the creature's proportions size the
> doorways via §A.6 → §A.7. Leave-off item 7: *"Import the character before blockout, not after."*

**8.1 Import and compare.** Launcher → Library → add **Paragon: Rampage** (A.14 row 1) and the two
alternates **Khaimera** and **Narbash** (row 2) into `/Game/Sourced/Paragon_Rampage/` etc. Drop all
three into `L_Sandbox` beside `BP_PlayerCharacter` and **judge by silhouette** (§A.9 "Alternates"):
Rampage = hunched, heavy-shouldered, long-armed brute; Khaimera = leaner, feral-human, better in FP;
Narbash = heavier, more mass at distance.

**8.2 Pick one and delete the other two folders.** §A.9: *"Three imported hero characters is ~2 GB
of cook time you do not need."*

**8.3 Re-material the fur** (§A.9 intervention 1 — *"does more than all the others"*): duplicate the
body material into a `Material Instance` in `/Game/Art/Materials/Instances/`; drive `Base Color`
toward **charcoal with a cold brown undertone**; flatten `Roughness` variation; cut `Specular`; and
**remove every emissive and fantasy-coloured element** — Paragon ships team-colour emissives and FX
and they must go.

**8.4 Scale and pose.** `Mesh > Scale` ~**1.1–1.2** `TUNING START`; bias idle/walk poses low —
*"a low-slung head with the shoulders above it is the werewolf read"*. If the set has a crouch/prowl
clip, that is the `Patrol` pose.

**8.5 Build `BS_Werewolf_Locomotion`.** `Add > Animation > Blend Space 1D` →
`/Game/Werewolf/BS_Werewolf_Locomotion`, axis `Speed` **0→500**, samples idle 0 / walk ~**200** /
run ~**460** — **matching §A.4's speed table exactly** or the feet skate.

**8.6 Build `ABP_Werewolf`.** `Add > Animation > Animation Blueprint` on the creature's skeleton →
`/Game/Werewolf/ABP_Werewolf`. **Do not reuse Paragon's shipped `Animation Blueprint`** (§A.9 — it
is built around Paragon's ability system and will fight the Behavior Tree).
- `AnimGraph`: `State Machine` → `Locomotion` state driving `BS_Werewolf_Locomotion` from a `Speed`
  float set in **`Event Blueprint Update Animation`** (`Get Velocity` → `Vector Length`).
- **`Blend Poses by Enum`** on `E_WolfState` to swap prowl vs run pose (the enum arrives at step 9;
  wire this pin then).
- One-shot states / `Play Anim Montage` sockets reserved for the Part B pounce windup.

**8.7 Create `BP_Werewolf` and FIX THE CAPSULE.** `Add > Blueprint Class > Character` →
`/Game/Werewolf/BP_Werewolf`. Assign the chosen `Skeletal Mesh`, `Anim Class` = `ABP_Werewolf`.
`Capsule Component`: **`Capsule Half Height` 110, `Capsule Radius` 55** `TUNING START`, **measured
from the real mesh**. §A.4: these numbers **propagate** — Nav Mesh `Agent Radius`/`Agent Height`
(§A.6) → minimum doorway width → §A.7's modular grid.

**8.8** If the measured mesh disagrees with 110/55, **update `Project Settings > Navigation Mesh`
(step 7.3) to match, then re-derive §A.7's door module** before step 15. Do not let the two drift.

**Produces:** the werewolf's body, animation and — critically — **the capsule number that unlocks
step 15**.
**Test (brief's own):** *"It stands and idles in the sandbox, correctly scaled beside the player, in
charcoal fur with no fantasy emissives. The capsule number is now fixed and A.7's grid can be
finalised."*

**Trademark constraint (A.14 row 1):** the Paragon licence is **Unreal-only** and **the "PARAGON"
trademark may not be used to name or advertise the game.** Credit it in `WBP_Credits` anyway.

---

### Step 9 — `[FN]` Enum, Blackboard, AI Controller, Behavior Tree **Patrol branch only** · *MCP* · **Implements:** `design-brief` §A.4 (whole section); §A.15 F8, F9; §A.16 step 9

**9.1 `E_WolfState`.** `Add > Blueprints > Enumeration` → `/Game/Core/Enums/E_WolfState`.
Enumerators **in this order, all of them, now**: `Patrol`, `Investigate`, `Chase`, then the unused
declarations `ScentPursuit`, `PouncePrep`, `Pounce`, `Charge`, `SearchHiding`, `Staggered`,
`Unconscious`. §A.4: *"Declaring early costs nothing and prevents an enum migration."* Only the
first three are used in Part A.

**9.2 `BB_Werewolf`.** `Add > Artificial Intelligence > Blackboard` → `/Game/Werewolf/BB_Werewolf`:

| Key | Type |
|---|---|
| `TargetActor` | Object (`Actor`) |
| `LastKnownLocation` | Vector |
| `PatrolLocation` | Vector |
| `bHasVisual` | Bool |
| `WolfState` | Enum (`E_WolfState`) |
| `HomeLocation` | Vector |

`Instance Synced` **off** for all keys (single AI in Part A).

**9.3 `BP_WerewolfController`.** `Add > Blueprint Class > AIController` →
`/Game/Werewolf/BP_WerewolfController`. On `BP_Werewolf`: `AI Controller Class` =
`BP_WerewolfController`, `Auto Possess AI` = **`Placed in World or Spawned`**.

**`Event On Possess`** (§A.4 — *not* `BeginPlay`; the pawn is guaranteed valid), in order:
1. **`Run Behavior Tree`** with `BTAsset` = `BT_Werewolf`. **Do not add a Blackboard component
   manually** — this node creates it from the Blackboard assigned inside the tree.
2. `Get Blackboard` → **`Set Value as Vector`** `HomeLocation` =
   `Get Controlled Pawn` → `Get Actor Location`.
3. `Set Value as Enum` `WolfState` = `Patrol`.
4. Start the `DecayMemory` looping timer (built at step 13).

Optionally `Set Generic Team Id` = 1 — but **keep `Detect Neutrals` true regardless** (§A.4).

**9.4 `BT_Werewolf`.** `Add > Artificial Intelligence > Behavior Tree` →
`/Game/Werewolf/BT_Werewolf`. In the Behavior Tree `Details` panel set
**`Blackboard Asset` = `BB_Werewolf`**. Build **only** the Patrol branch now:

```
ROOT
└── Selector "Brain"
    └── Sequence "Patrol"
          ├─ Task: BTT_SetWolfState   (NewState = Patrol)
          ├─ Task: BTT_FindPatrolPoint
          ├─ Task: Move To            Key: PatrolLocation, Acceptable Radius: 80
          └─ Task: Wait               Wait Time: 2.0  Random Deviation: 1.5
```

**9.5 `BTT_FindPatrolPoint`.** `Add > Artificial Intelligence > Behavior Tree Task` (base
**`BTTask_BlueprintBase`**) → `/Game/Werewolf/Tasks/BTT_FindPatrolPoint`:
1. **`Event Receive Execute AI`** → `Controlled Pawn`.
2. **`Get Blackboard Value as Vector`** (`HomeLocation`).
3. **`Get Random Reachable Point in Radius`** — `Origin` = `HomeLocation`, `Radius` = **4000**
   `TUNING START`. §A.4 is explicit: use this, **not** `Get Random Point in Navigable Radius`, *"the
   former guarantees a path exists from the origin, preventing the wolf picking a point across an
   unlinked gap and stalling."*
4. `Branch` on the return bool → **`Set Blackboard Value as Vector`** (`PatrolLocation`) →
   **`Finish Execute`** (Success **true**); else `Finish Execute` (Success **false**).

**9.6 `BTT_SetWolfState`.** Same base → `/Game/Werewolf/Tasks/BTT_SetWolfState`. Instance-editable
inputs `NewState` (`E_WolfState`) and `ClearLastKnown` (Boolean, default false):
1. `Event Receive Execute AI` → `Get AI Controller` → `Get Blackboard` → **`Set Value as Enum`**
   (`WolfState` = `NewState`).
2. Set the pawn's `Max Walk Speed` from §A.4's table **and** call a custom event
   **`OnWolfStateChanged(NewState)`** on `BP_Werewolf`. §A.4: *"One hook, two Form systems"* —
   animation (§A.9) at step 8/9 and audio (§A.13) at step 11.
3. If `ClearLastKnown`: `Clear Value` `LastKnownLocation` **and** `TargetActor`.
4. `Finish Execute` (Success true).

| `WolfState` | `Max Walk Speed` | Rationale (§A.4) |
|---|---|---|
| `Patrol` | 200 `TUNING START` | slow, audible, gives reading time |
| `Investigate` | 320 `TUNING START` | purposeful, still escapable |
| `Chase` | **460** `TUNING START` | **below** the player's sprint (480) |

**9.7** On `BP_Werewolf`, add the custom event `OnWolfStateChanged (E_WolfState NewState)` — empty
for now; step 11 fills it with audio, step 8.6's `Blend Poses by Enum` already reads the Blackboard
enum for pose.

**Test (brief's own):** *"The wolf wanders the sandbox indefinitely without stalling, animating
correctly."*

---

### Step 10 — `[FN]` Sight perception + the Chase branch · *MCP* · **Implements:** `design-brief` §A.3 "`AI Perception` lives on the AI Controller", "Reacting to perception" 1–5; §A.4 `BT_Werewolf`; §A.15 F6, F8; §A.16 step 10; leave-off items 3 and 5

**10.1 Add `AI Perception` to `BP_WerewolfController`** — **on the controller, not the pawn** (§A.3:
the controller outlives possession and is where `Run Behavior Tree` and the Blackboard live).

**10.2 `Senses Config` → add `AI Sight config`:**

| Property | Value |
|---|---|
| `Sight Radius` | 2000 `TUNING START` — **re-tuned at step 21** |
| `Lose Sight Radius` | 2600 `TUNING START` (must exceed `Sight Radius` or the wolf flickers) |
| `Peripheral Vision Half Angle Degrees` | 70 `TUNING START` (140° cone) |
| `Auto Success Range from Last Seen Location` | 400 `TUNING START` |
| `Max Age` | 5.0 `TUNING START` |
| `Detection by Affiliation` → `Detect Enemies` / **`Detect Neutrals`** / `Detect Friendlies` | true / **true** / true |

> **`Detect Neutrals` must be true.** §A.3 "Known failure mode": actors with no Team ID default to
> **Neutral**; leave it unchecked and *"the werewolf never sees the player and the AI looks
> completely broken. This is the single most common cause of 'AI Perception does nothing'."*
> (Leave-off item 3.)

**10.3 `Dominant Sense` = `AISense_Sight`** `TUNING START`, so a confirmed visual overrides a stale
noise (§A.3).

**10.4 Bind `On Target Perception Updated (AIPerception)`** on `BP_WerewolfController` (§A.3
"Reacting to perception", in order):
1. **`Cast To BP_PlayerCharacter`** from `Actor`; fail → return.
2. **`Break AIStimulus`** on `Stimulus` → `Successfully Sensed`, `Stimulus Location`, `Type`.
3. Decide the sense with **`Line Of Sight To`** (an `AIController` node) against the player:
   true → visual, false → noise. §A.3 prefers this over comparing `Type`: it *"behaves identically
   for Part A and avoids awkward sense-ID comparison through MCP."*
4. **Sight (sensed true + line of sight true):** `Get Blackboard` →
   `Set Value as Object` `TargetActor` = player; `Set Value as Bool` `bHasVisual` = true;
   `Set Value as Vector` `LastKnownLocation` = player location; `Set Value as Enum` `WolfState` =
   `Chase`; **`Set Focus`**.
5. **Sight lost (sensed false):** `bHasVisual` = false; `LastKnownLocation` = `Stimulus Location`;
   `WolfState` = `Investigate`; **`Clear Focus`**. **Do not `Clear Value` `TargetActor` here** —
   §A.3: *"short memory is what makes the predator persistent (Pillar 1)."*

**10.5 Add the Chase branch to `BT_Werewolf`, above Patrol:**

```
Selector "Brain"
├── Sequence "Chase"
│     ├─ Decorator: Blackboard   Key Query: Is Set, Key: TargetActor
│     │                          Observer Aborts: BOTH   Notify Observer: On Value Change
│     ├─ Decorator: Blackboard   Key Query: Is Equal To, Key: bHasVisual, Value: true
│     │                          Observer Aborts: Self   Notify Observer: On Value Change
│     ├─ Task: BTT_SetWolfState  (NewState = Chase)
│     └─ Task: Move To           Key: TargetActor, Acceptable Radius: 60,
│                                Observe Blackboard Value: true
└── Sequence "Patrol"            (from step 9)
```

> **`Observer Aborts: Both` is not optional.** §A.4: *"Without them the wolf finishes its patrol walk
> before reacting, which reads as a scripted monster and violates Pillar 1 directly."* (Leave-off
> item 5.)

**Test (brief's own):** *"The wolf abandons patrol mid-step and runs at you on sight."*

---

### Step 11 — `[FORM]` Per-state werewolf audio · *MIXED* · **Implements:** `design-brief` §A.13 (mix architecture, content list, "The sniff is a mechanic"); §A.14 rows 11, 12, 13; §A.15 F12, V13; §A.16 step 11

**11.1 Import creature audio** into `/Game/Sourced/InfinityBlade_Sounds/`, `/Game/Sourced/Sonniss/`,
`/Game/Sourced/Freesound/` — A.14 rows 13, 11, 12. **Pitch down and distort** the Infinity Blade
roars (§A.13). Log every file in `CREDITS.md` **as you go**; CC-BY Freesound entries must be flagged
for `WBP_Credits`.

**11.2 Build three distinguishable loops** as **`MetaSound Source`** assets (or `Sound Cue` with a
`Random` node — §A.13: *"repeated identical samples are the audio equivalent of default grey
material"*), in `/Game/Audio/Creature/`:

| `WolfState` | Content (§A.13) |
|---|---|
| `Patrol` | heavy padding + slow breathing |
| `Investigate` | **sniffing** + low growl + claws on stone |
| `Chase` | roar + fast gallop + impacts |

All assigned `Sound Class` = `SC_Creature` and `Sound Attenuation` = **`ATT_Creature`** with
**`Enable Occlusion`** on. §A.13: occlusion *"is what makes the werewolf audibly behind a wall rather
than vaguely nearby — a Pillar 1/2 requirement, not polish."*

**11.3 Wire `OnWolfStateChanged`** on `BP_Werewolf`: `Switch on E_WolfState` → **`Set Sound`** on a
`CreatureAudio` `Audio` component → `Play`. On entering `Chase`: **`Push Sound Mix Modifier`**
(`SM_Chase`); on leaving: **`Pop Sound Mix Modifier`**. Configure `SM_Chase` to duck `SC_Ambience`
**−6 dB** and lift `SC_Creature` **+3 dB** (§A.13). *"Two nodes; the chase instantly feels
different."*

**11.4 No chase music** (§A.13). Two cues only, both at step 25.

**Test (brief's own, and it is the acceptance test):** ***"Eyes closed, through a wall, you can name
the wolf's state."*** §A.13: *"The sniff is a mechanic"* — if `Investigate` and `Chase` sound alike,
Pillar 2 fails.

---

### Step 12 — `[FN]` Catch → death beat → game over → restart · *MCP* · **Implements:** `design-brief` §A.5 "Catch (lose)" (LOCKED); §A.4 (*catch is not a state*); §A.15 F15; §A.16 step 12

**12.1 `CatchSphere` on `BP_Werewolf`.** Add `Sphere Collision` named **`CatchSphere`**:
`Sphere Radius` **110** `TUNING START` (capsule radius plus a lunge's reach); `Collision Presets` =
`Custom`; `Collision Enabled` = **`Query Only (No Physics Collision)`**; Object Type `Pawn`;
`Overlap` for `Pawn`, **`Ignore` everything else**; `Generate Overlap Events` = true.

> §A.4: **catch is not a `WolfState`** — it is an overlap event, *"so it can never be blocked by a
> mis-transition, which matters because capture is an immediate game over."* Do not add a `Catch`
> enumerator.

**12.2 `On Component Begin Overlap (CatchSphere)`:** `Cast To BP_PlayerCharacter` (fail → return) →
`Branch` on a `bCaught` Boolean guard (return if true, else `Set bCaught` = true) →
`Get Game Mode` → `Cast To GM_Werewolf` → call **`OnPlayerCaught(Player)`**.

**12.3 `GM_Werewolf > OnPlayerCaught(Player)`** — nodes in §A.5's order:
1. **`Disable Input`** on the player.
2. **`Set Ignore Move Input`** / **`Set Ignore Look Input`** = true on `PC_Werewolf`.
3. **The death beat** — **`Delay` 1.2 s** `TUNING START` during which: **`Set View Target with
   Blend`** to a `Camera Actor` on the werewolf (or force the player's look toward it), the catch
   audio sting, and a fade to black via **`Widget Animation`**. §A.5: *"This beat is Form work that
   is also Pillar 2 work — showing the player what got them is how they explain the capture. Do not
   cut straight to a menu."*
4. **`Create Widget`** (`WBP_GameOver`) → **`Add to Viewport`** → **`Play Animation`**.
5. **`Set Input Mode UI Only`** (`In Widget to Focus` = the widget); **`Set Show Mouse Cursor`** = true.
6. **`Set Game Paused`** = true (target: the player controller).

**12.4 `WBP_GameOver`** — `Add > User Interface > Widget Blueprint` → `/Game/UI/WBP_GameOver`.
**Unstyled at this step** (§A.16 step 12 says "(unstyled)"; styling is step 23). Contents: title
(**placeholder wording — §A.18: final copy is narrative TBD, do not author it**), `Restart`,
`Main Menu`, `Quit`.
- `Restart` → `Set Game Paused` false → **`Get Current Level Name`** → **`Open Level (by Name)`**.
  *(Part B replaces this with a safe-haven autosave load — §B.5 item 4. LATER.)*
- `Main Menu` → `Open Level (by Name)` `L_Title`. `Quit` → **`Quit Game`**.

> **Gap flagged and closed by inference.** §A.5 step 3 refers to *"a `Camera Actor` on the
> werewolf"* but never says where it is authored. I am specifying: add a **`Camera`** component named
> **`DeathCam`** to `BP_Werewolf`, positioned to frame the creature's head, and pass it to
> `Set View Target with Blend`. Flagged so the inspector can see it is an inference, not a citation.

**Test (brief's own):** *"Being touched ends the run with a visible death beat; Restart reloads."*

---

### Step 13 — `[FN]` Hearing config, Investigate branch, memory decay, `ResetToPatrol` · *MCP* · **Implements:** `design-brief` §A.3 "Reacting to perception" item 6, "Memory decay and `ResetToPatrol`"; §A.4 `BT_Werewolf`; §A.15 F7, F8, F10; §A.16 step 13

**13.1 Add `AI Hearing config`** to the controller's `AI Perception`: `Hearing Range` **1500**
`TUNING START`, `Max Age` **4.0** `TUNING START`, **`Detection by Affiliation` all true —
`Detect Neutrals` included** (leave-off item 3, again).

**13.2 Hearing handler** (§A.3 item 6): in `On Target Perception Updated`, when `Line Of Sight To` is
false → `Set Value as Vector` `LastKnownLocation` = `Stimulus Location`; `Set Value as Enum`
`WolfState` = `Investigate`. **Do not set `bHasVisual`.**

**13.3 Insert the Investigate branch** into `BT_Werewolf`, **between Chase and Patrol**:

```
├── Sequence "Investigate"
│     ├─ Decorator: Blackboard   Key Query: Is Set, Key: LastKnownLocation
│     │                          Observer Aborts: BOTH   Notify Observer: On Value Change
│     ├─ Task: BTT_SetWolfState  (NewState = Investigate)
│     ├─ Task: Move To           Key: LastKnownLocation, Acceptable Radius: 100
│     ├─ Task: Wait              Wait Time: 2.0  Random Deviation: 1.0
│     └─ Task: BTT_SetWolfState  (NewState = Patrol, ClearLastKnown = true)
```

**13.4 `DecayMemory`** on `BP_WerewolfController`: **`Set Timer by Event`**, **looping, 0.5 s**,
started from `Event On Possess` (step 9.3 item 4). Body: if `bHasVisual` is false **and** `WolfState`
is `Investigate`, increment `SearchTimer`; past **`GiveUpTime` = 12.0** `TUNING START`, call
`ResetToPatrol`. **Any fresh stimulus resets `SearchTimer` to 0** (§A.3).

**13.5 `ResetToPatrol`** — a function on `BP_WerewolfController`, **written once here** because
§B.5's safe haven calls the *same* function (§A.3): `Clear Value` `TargetActor`;
`Set Value as Bool` `bHasVisual` = false; `Clear Value` `LastKnownLocation`;
`Set Value as Enum` `WolfState` = `Patrol`; `SearchTimer` = 0; **`Clear Focus`**.

**Test (brief's own):** *"Sprinting out of sight draws the wolf to where you were; it gives up and
resumes patrol."*

---

### Step 14 — `[FN]` Tune the speed table **and** the blend space play rates together · *HAND* · **Implements:** `design-brief` §A.4 speed table + the "460 vs 480" note; §A.9 `BS_Werewolf_Locomotion`; §A.15 F11; §A.16 step 14; leave-off item 11

**Do:** In `L_Sandbox`, run chases and adjust `BTT_SetWolfState`'s per-state `Max Walk Speed` against
`BS_Werewolf_Locomotion`'s sample speeds **at the same time**. §A.4: *"Speed tuning and animation
play-rate tuning are the same job; doing them separately means doing them twice."*

**The constraint that must survive tuning:** **wolf `Chase` speed stays 10–30 units BELOW the
player's `SprintSpeed`.** Start 460 vs 480. §A.4: *"Faster wolf = unwinnable; much slower = not a
predator."* This is Pillar 5 *Temporary Relief* expressed as two numbers — a sprinting player escapes
*slowly*, and it costs all their stamina.

**Test (brief's own):** *"Sprinting barely escapes a chase and costs all stamina; no foot skate."*

---

### Step 14b — `[FORM]` **THROWAWAY PACKAGE SMOKE TEST** · *HAND* · **Implements:** `design-brief` §A.17 (whole section); §A.16 step 14b; leave-off items 8 and 10

> **Do this on 10 August. Do not move it.** §A.17: *"A first Unreal package reliably breaks
> something… step 14b packages once in week 2 as a smoke test so the reserve window is repair time,
> not discovery time."* This is the single highest-leverage schedule decision in the whole plan
> against a 36-day deadline.

1. `Project Settings > Project > Packaging` → **`List of maps to include in a packaged build`** →
   add **`L_Sandbox`** now, and **`L_Title` and `L_Mansion_Slice`** as soon as they have content.
   §A.17 breakage 2 / leave-off item 10: *"a map reached only via `Open Level (by Name)` is not
   auto-cooked and will fail at runtime with a black screen."* Also set `Use Pak File` on and add any
   soft-path-only content to `Additional Asset Directories to Cook`.
2. `Platforms > Windows > Package Project`, **`Build Configuration` = `Development`** (§A.17: prove
   Development first so you know which class of problem you have).
3. Run the `.exe`. Verify: it launches into `L_Sandbox`, the **navmesh generated at runtime**
   (`Runtime Generation = Dynamic` — §A.17 breakage 4, verify in the `.exe`, not only in PIE), and
   the wolf chases you.
4. Fix whatever broke. Common: missing maps; `Print String`-dependent behaviour (breakage 1);
   toolchain issues — Windows SDK / .NET / `hostfxr.dll` (breakage 3); empty/tiny output folder =
   cook failed even if the UI said it finished, **read the log** (breakage 7).
5. **Discard the build.**

**Test (brief's own):** *"An `.exe` launches into `L_Sandbox` and the wolf chases you."*

---
---

# PHASE 3 — "IT'S A PLACE" (11 – 18 August, days 12–19)

*`design-brief` §A.16 Block 3. Function and Form alternate every step here — this is where the
"finished-looking" requirement is actually earned.*

---

### Step 15 — `[FORM]` Build the modular blockout set · *MIXED* · **Implements:** `design-brief` §A.7 "The grid — the load-bearing decision of the Form track"; §A.15 V1; §A.16 step 15

**Gated by step 8** — the door width derives from the werewolf capsule via `Agent Radius`.

**Editor path:** **`Modeling Mode` → `CubeGrid`** with a **50 cm step** (or `Cube` static meshes
scaled to exact module sizes). Viewport `Grid Snap` = **50** for placement, **10** for detail.

Save each as its own `Static Mesh` in **`/Game/Art/Blockout/`**:

| Module | Dimensions (cm) | Asset |
|---|---|---|
| Wall segment | 400 W × 350 H × 20 T | `SM_Blockout_Wall_400` |
| Half wall | 200 × 350 × 20 | `SM_Blockout_Wall_200` |
| Tall wall (halls) | 400 × 700 × 20 | `SM_Blockout_Wall_400_Tall` |
| Floor / ceiling tile | 400 × 400 × 20 | `SM_Blockout_Floor_400` |
| **Door opening (clear)** | **200 W × 280 H** | `SM_Blockout_DoorFrame_200` |
| Stair run | 400 W, rise 350 over 400 depth | `SM_Blockout_Stair` |
| Column / pilaster | 40 × 40 × 350 | `SM_Blockout_Column` |

Room heights **350 cm** (service/private) and **700 cm** (hub hall). Corridor clear width **300 min**.

> **The rule that makes styling affordable:** *"Never scale a blockout piece to a non-module size; if
> a wall wants to be 437 cm, change the layout."* Saving each module as its own `Static Mesh` means a
> styled mesh of the same dimensions later replaces it by **swapping the `Static Mesh` reference on
> placed actors — no re-layout, no re-lighting, no navmesh rebuild from scratch.** §A.7: *"That swap
> path is the whole reason for the grid."*

**Test (brief's own):** *"Modules snap together with no gaps and no arbitrary scaling."*

---

### Step 16 — `[FN]` Blockout `L_Mansion_Slice` · *HAND* · **Implements:** `design-brief` §A.7 "Required layout properties" 1–9 and "Actors to place"; §A.15 F17; §A.16 step 16; leave-off item 4

**Scope (§A.7): one floor, 8–10 rooms.** Every one of these nine properties is a requirement, not a
suggestion:

1. **A hub with sightlines** — one large 700 cm-ceiling space with **≥3 exits**. Where the player
   first sees the werewolf across distance. It is also the screenshot, so it gets the most Form
   attention.
2. **No dead ends, one deliberate exception** — every room has **two** ways out. §A.7: *"A pursuit in
   a two-exit room is a decision; in a one-exit room it is a coin flip"* — a direct Pillar 2
   violation. The one exception is a small chamber **reserved for Part B's hiding place** (§B.4):
   build the chamber, do not build the mechanic.
3. **At least one loop** — a circuit the player can run so the wolf can be led away and doubled back
   on. Without it, "evade" collapses into "outrun in a straight line".
4. **Vertical interest for one nav link** — a balcony or stairwell drop (wired at step 18).
5. **Spatial separation of key and door** — `BP_KeyItem` in the room **furthest by path length** from
   `BP_EscapeDoor`. *"The forced traverse is the gameplay."*
6. **Werewolf start out of sight of `Player Start`** — two or three rooms away. First 20–40 s should
   be quiet exploration. `HomeLocation` is the centre of the 4000-unit patrol radius; confirm that
   radius covers the floor.
7. **A marked-out safe-haven footprint** — a small side room off the hub. **Do not implement it;
   just do not build over it** (§B.5, LATER).
8. **At least three deliberate silhouette positions** — a lit surface (moonlit window, hearth,
   candle-lit doorway) **behind** a spot the wolf will pass through. §A.7: *"Design these into the
   layout, not the lighting pass… they cannot be added later without moving walls."*
9. **One material story per room** — stone undercroft, panelled study, plastered corridor, draped
   bedchamber, iron service passage (feeds step 19's `MI_*` naming).

**Actors to place now** (§A.7 table; the rest arrive at their own steps): `Player Start` ×1,
`BP_Werewolf` ×1, **`Nav Mesh Bounds Volume` ×1** enclosing everything.

**Navmesh:** set the same `Runtime Generation` = `Dynamic`; confirm `Project Settings > Navigation
Mesh` still reads `Agent Radius` **55** / `Agent Height` **220**. **Press `P`.**

**Test (brief's own):** *"Navmesh reaches every room **including through every doorway**."* A doorway
narrower than `2 × AgentRadius` + margin silently generates no navmesh and the werewolf cannot
follow — *"which looks like broken AI and is actually broken geometry"* (§A.6 item 3).

---

### Step 17 — `[FN]` Interaction, key item, escape door, win · *MCP* · **Implements:** `design-brief` §A.2 "Interaction"; §A.5 "Escape (win)" (LOCKED); §A.15 F5, F16; §A.16 step 17

**17.1 `BP_Interactable`** — `Add > Blueprint Class > Actor` → `/Game/World/BP_Interactable`.
Variables: `PromptText` (Text). Events: a blueprint-implementable **`Interact(Instigator)`**.

**17.2 `TryInteract` on `BP_PlayerCharacter`** (§A.2), bound to `IA_Interact` `Started`:
**`Get Actor Eyes View Point`** → **`Line Trace By Channel`** (`Visibility`, `End` = `Start` +
`Forward Vector` × **250** `TUNING START`) → **`Break Hit Result`** → `Hit Actor` →
**`Cast To BP_Interactable`** → call `Interact` with `Instigator` = self.

**17.3 Prompt loop:** the same trace on a **`Set Timer by Event`** at **0.1 s**, showing/hiding
`WBP_Prompt` with the hit interactable's `PromptText`.

**17.4 `WBP_Prompt`** — `/Game/UI/WBP_Prompt`. Functional now, **styled at step 23**. Copy rules
(§A.12, Pillar 4 — diegetic, no quest text): a **verb phrase about the object**
(`Take the silver candlestick`), **not** `[E] INTERACT`; keybind in its own bordered glyph, separate
from the sentence; sentence case.

**17.5 `bHasEscapeKey`** — Boolean on **`GI_Werewolf`** (Game Instance, *"so it survives Part B's
reload"* — §A.5).

**17.6 `BP_KeyItem`** (child of `BP_Interactable`) → `/Game/World/BP_KeyItem`: `Interact` →
`Get Game Instance` → `Cast To GI_Werewolf` → `Set bHasEscapeKey` = true → **`Destroy Actor`** → a
**diegetic acquisition cue** (a short `WBP_Prompt` line plus a sound). **No inventory pop-up**
(Pillar 4).

**17.7 `BP_EscapeDoor`** (child of `BP_Interactable`) → `/Game/World/BP_EscapeDoor`: `Interact` →
1. `Get Game Instance` → `Cast To GI_Werewolf` → `Branch` on `bHasEscapeKey`.
2. **False:** set `PromptText` to a **diegetic refusal** — §A.5's own example,
   *"the bar is fixed fast — something must lift it"* — and return.
   **No objective marker, no quest text** (Pillar 4).
3. **True:** open the door (**`Timeline`** rotating the mesh) → `Get Game Mode` →
   `Cast To GM_Werewolf` → **`OnPlayerEscaped`**.

**17.8 `GM_Werewolf > OnPlayerEscaped`** — same shape as `OnPlayerCaught` (step 12.3) with
`WBP_Escaped`, and **the opposite Form beat**: the door swings, cold moonlight and fog pour in, the
win music cue (§A.13) starts, then the widget fades up. §A.5: *"The win needs a visual payoff or it
reads as a bug."*

**17.9 `WBP_Escaped`** — `/Game/UI/WBP_Escaped`: placeholder title, `Main Menu`, `Quit`. Styled at 23.

> **Architectural note (§A.5):** this one-key/one-door structure is *deliberately the degenerate case
> of the §C.3 puzzle framework*. Part C replaces `bHasEscapeKey` with a multi-step chain **without
> touching `BP_EscapeDoor`'s shape.** Do not special-case it.

**Test (brief's own):** *"Door refuses, then opens after the key; win screen appears."*

---

### Step 18 — `[FN]` AI-openable doors and one nav link · *MCP* · **Implements:** `design-brief` §A.6 items 4 and 5; §A.15 F13, F14; §A.16 step 18; leave-off item 4

**18.1 `BP_Door`** → `/Game/World/BP_Door`. On the door `Static Mesh` set
**`Can Ever Affect Navigation` = false** so the navmesh runs straight through the doorway (§A.6
item 4). Add a `Box Collision` named **`DoorTrigger`** spanning the opening.
`On Component Begin Overlap` → `Branch`: is the actor `BP_Werewolf` **or** `BP_PlayerCharacter` →
run the open **`Timeline`** and **`Report Noise Event`** (`Loudness` **0.6**, `Max Range` **1200**
`TUNING START`). §A.6: doors are named explicitly in the LOCKED sensory hierarchy.
**Doors are never locked against the wolf in Part A.** This satisfies *"opens doors"* with **no EQS
and no custom nav area**.

**18.2** Place **3–5 `BP_Door`** on the main circulation route (§A.7 actor table).

**18.3 `Nav Link Proxy`** — `Place Actors > Navigation > Nav Link Proxy`, **at least one**, on the
step-16 balcony/stairwell. Set `Point Links` `Left` / `Right` and `Direction` = `Both Ways` (or
`Left to Right` for a one-way drop). §A.6 item 5 anchors *"climbs authored nav links"*; §A.15 F14
wants a traversal **the player cannot use** — so the player learns the wolf takes routes they cannot.

**18.4** `Nav Modifier Volume` with `Area Class` = `NavArea_Null` is **not used in Part A** — it is
how §B.5's safe haven works. Noted so the layout leaves room (§A.6 item 6). **LATER.**

**18.5 Press `P`.** Re-verify navmesh through every doorway after adding doors.

**Test (brief's own):** *"The wolf paths through closed doors and takes a shortcut you cannot."*

---

### Step 19 — `[FORM]` Five master materials + per-room instances · *MIXED* · **Implements:** `design-brief` §A.11 "Five master materials — and no more"; §A.8 "How mismatched free assets are unified" item 3; §A.14 rows 7, 8; §A.15 V2; §A.16 step 19

**19.1 Import CC0 surfaces** from **ambientCG** (row 7) and **Poly Haven** (row 8) into
`/Game/Sourced/ambientCG/` and `/Game/Sourced/PolyHaven/`; the working copies live in
`/Game/Art/Textures/`. Log each in `CREDITS.md` (CC0, no attribution required, but log it anyway).

**19.2 Build exactly five masters** in `/Game/Art/Materials/` — `Add > Material`:

| Master | Covers | Exposed parameters |
|---|---|---|
| `M_Stone` | ashlar, limestone, flags, vaulting | `BaseColorTint`, `Tiling`, `RoughnessScale`, `DirtAmount`, `WetnessAmount` |
| `M_Plaster` | lime plaster, whitewash, cracks | `BaseColorTint`, `Tiling`, `StainAmount` |
| `M_Wood_Dark` | oak panelling, floorboards, furniture | `BaseColorTint`, `Tiling`, `VarnishGloss`, `DirtAmount` |
| `M_Metal_Tarnished` | wrought iron, brass, **silver** | `BaseColorTint`, `Metallic`, `RoughnessScale`, `TarnishAmount` |
| `M_Fabric` | wool, velvet, dust sheets, linen | `BaseColorTint`, `Tiling`, `SheenAmount` |

Each built as: tiling **`Texture Sample`** set (BaseColor / Normal / packed ORD) × a
**`Vector Parameter`** `BaseColorTint`, a **`Scalar Parameter`** `Tiling` on a **`TexCoord`**, and a
grime layer **`Lerp`**ed by `DirtAmount`. **Keep instruction counts modest** — §A.11: Lumen +
volumetric fog + VSM is already the frame budget.

**19.3 Instances** in `/Game/Art/Materials/Instances/`, named `MI_Stone_Hall`, `MI_Wood_Panel_Study`,
… — **one per material-per-room-story** (§A.7 requirement 9), **not one per mesh**.

**19.4 Apply to every blockout actor.** §A.8: *"Never ship a sourced asset on its original material
without checking it against the palette."*

**Palette discipline (§A.8):** ~60% desaturated stone grey / black-green; ~25% bitumen brown, dark
walnut, umber; ~10% bone / ivory / candle-wax cream; ≤3% candle amber; ≤3% moon blue-grey; ≤2%
oxblood; plus a distinct cool **silver** note for the silver resource (prepares Part B, Pillar 3).
**Forbidden: pure white, saturated blue or purple, teal-orange grading, more than one dominant accent
per room.**

**Test (brief's own):** ***"No default grey remains.*** A screenshot reads as stone/wood/plaster, not
boxes."

---

### Step 20 — `[FORM]` Lighting pass — the two-temperature rule · *HAND* · **Implements:** `design-brief` §A.8 "Light — the two-temperature rule"; §A.11 "Lighting build" 1–5; §A.14 row 8; §A.15 V3; §A.16 step 20

**20.1 `Directional Light`** — **moonlight only**. `Intensity` 0.3–1.0 lux `TUNING START`,
**`Use Temperature` on**, `Temperature` **7000 K**, `Volumetric Scattering Intensity` ~1.5. Angle it
through the hub windows and the escape door **and nowhere else useful** — *"this is the light the
player navigates by."*

**20.2 `Sky Light`** — `Source Type` = **`SLS Specified Cubemap`**, `Cubemap` = a **Poly Haven CC0
night HDRI** (A.14 row 8), `Intensity Scale` **0.05–0.2** `TUNING START`. §A.11: *"This value is most
of the difference between 'atmospheric' and 'I can't see'."*

**20.3 Practicals.** `Point Light` for candles/hearths (`Temperature` **1900 K**,
`Attenuation Radius` 300–600, `Intensity Units` **Candelas**, `Source Radius` ~2 for soft shadows);
`Spot Light` for lanterns; **`Rect Light` in window apertures and fireplaces** — *"the cheapest
convincing moonlight-through-glass there is."*

**20.4 All lights `Movable`** under Lumen. **Do not attempt a lightmap bake** (§A.11 item 4 — no
time, and it fights dynamic doors and Part C's navmesh changes).

**20.5 Build the practical Blueprints** — §A.11 item 5: *"A candle is a light and a mesh and a flame
and a sound."* `/Game/World/BP_Candle`, `BP_Sconce`, `BP_Hearth`, each bundling
`Static Mesh` + `Point Light` + Niagara flame (step 22) + `Audio` on **`ATT_Prop`** + a **flicker**
(`Timeline` or `Light Function Material` driving `Intensity` ±10%). Place **25–50** of them.
§A.11: *"Flicker is the highest value-per-minute effect in the whole Form track."*

**20.6 Two-temperature discipline (§A.8):** interior warm **1900–2200 K**; exterior cold
**6500–8000 K**; **corridors and connective space get neither** — near-black, lit only by spill from
the rooms either side. Enable `Use Temperature` on **every** light; **do not tint via `Light Color`.**

**Test (brief's own):** *"Every room is navigable; the wolf silhouettes at all three positions at
400 / 800 / 1500 cm."* §A.8: *"if the player cannot see the werewolf when it matters, the design has
failed"* — that is the floor of the contrast range, and it is Pillar 2.

---

### Step 21 — `[FORM]` Global post-process + fog, then **re-tune `Sight Radius`** · *HAND* · **Implements:** `design-brief` §A.11 "Post-process" and "Fog"; §A.3 "Second failure mode"; §A.15 V4, V5; §A.16 step 21; leave-off item 9

**21.1 `Post Process Volume`**, **`Infinite Extent (Unbound)` = true** (§A.8 unification mechanism 1
— one global grade is what makes six authors' assets read as one game). All `TUNING START`:

| Setting | Value |
|---|---|
| `Exposure > Metering Mode` | **`Manual`** (or `Auto Exposure Histogram` with `Min EV100` = `Max EV100`) |
| `Exposure > Exposure Compensation` | to taste — the one dial that sets overall darkness |
| `Local Exposure > Highlight Contrast Scale` | 0.8 |
| `Color Grading > Global > Saturation` | 0.75 |
| `Color Grading > Shadows > Gain` | slight blue-green push |
| `Color Grading > Highlights > Gain` | slight warm push |
| `Lens > Image Effects > Vignette Intensity` | 0.4 |
| `Film Grain > Film Grain Intensity` | 0.3 |
| `Lens > Bloom > Intensity` | 0.4 |
| `Lens > Chromatic Aberration > Intensity` | 0.15 |
| `Rendering Features > Motion Blur > Amount` | 0.2 |

> **Locking exposure is critical**, not cosmetic. §A.11: *"Auto-exposure brightens dark corridors and
> destroys both the horror and the silhouette read."* And §A.11's closing warning: *"Do not overdrive
> the post-process. Paint with light, fog and materials; the grade is the last 10%, not the first
> 50%."*

**21.2 `Exponential Height Fog`:** `Fog Density` ~**0.02** `TUNING START`, `Fog Height Falloff` ~0.2,
`Fog Inscattering Color` cold blue-grey, **`Volumetric Fog` on**, `Scattering Distribution` ~0.2,
`Albedo` dim grey, `View Distance` tuned so the far end of the hub is hazy **but the werewolf still
reads there**. §A.11: fog does four jobs — atmosphere, asset unification, distance legibility of the
wolf, and hiding the fact that the level is small.

**21.3 RE-TUNE `Sight Radius`** on the `AI Sight config` (step 10.2) **against this finished
lighting.** §A.3 "Second failure mode, specific to this game": in a dark, fog-filled interior the
player is often invisible to the *human eye* at 2000 units while the AI sees perfectly — *"That is a
Pillar 2 violation… **Tune `Sight Radius` against the final lighting, not the grey-box**, and if they
disagree, shorten the radius."* (Leave-off item 9. This is why lighting is Part A.)

**Test (brief's own):** *"Dark rooms stay dark when you look at a candle. AI sight range and human
sight range agree."*

---

### Step 22 — `[FORM]` Set dressing, decals, Niagara · *HAND* · **Implements:** `design-brief` §A.11 "Decals", "Niagara VFX", "Set dressing rule"; §A.8 period cues and anti-cues; §A.14 rows 8, 9, 10; §A.15 V9, V10; §A.16 step 22

**22.1 Props.** Infinity Blade packs (row 9) + Poly Haven CC0 (row 8) + anything claimed from Fab
free drops (row 10), imported into `/Game/Sourced/<source>/`. **Row 9 is stylised fantasy — it must
be re-materialled onto the step-19 masters or limited to neutral stone pieces** (§A.14 row 9, §A.8
mechanism 3). Limit distinct sourced sets to **two or three** (§A.8 mechanism 5 — *"Ten packs produce
ten looks"*).

**22.2 Period cues to place (§A.8):** campaign trunks, crates, bedrolls, a stacked arms rack, a
folding field desk with maps, a surgeon's table, empty bottles, dust sheets over furniture,
dark-varnished portraits, a long refectory table, foxed mirrors, oak wainscot to dado height, nailed
shutters.
**Anti-cues — if one is visible the look has failed:** gas or electric lighting, radiators, plate
glass, modern door hardware, saturated fantasy colour, un-restyled fantasy/sci-fi geometry (glowing
runes, oversized shoulder armour, alien plants), chrome, neon.

**22.3 Set dressing rule (§A.11):** **every room needs one focal object and one story of use.**
*"Three well-placed props beat thirty scattered ones."*

**22.4 Decals — 30+ across 8–10 rooms.** `Decal Actor` with `Material Domain` = **`Deferred Decal`**,
`Blend Mode` = `Translucent`, materials in `/Game/Art/Materials/Decals/`:
`M_Decal_Stain` (water runs below windows and in vaults) · `M_Decal_Soot` (above **every** sconce and
hearth — *"instantly ages a wall"*) · `M_Decal_Scuff` (door thresholds, stair treads) ·
**`M_Decal_Claw`** (gouges **on the werewolf's habitual routes** — §A.11: decoration *and*
signposting; claw marks near the nav-link shortcut *"teach the player something true about the AI"*,
which is Pillar 4 doing gameplay work) · `M_Decal_Blood` (**sparing — target rating T; suggest, do
not depict**).

**22.5 Niagara**, in `/Game/Art/VFX/`, each built from a stock template (`Fountain`,
`Simple Sprite Burst`) — **do not author from empty** (§A.11):

| System | Where | Why (§A.11) |
|---|---|---|
| `NS_DustMotes` | every light shaft, especially the hub | *"Highest ratio of 'looks finished' to authoring time in the project."* |
| `NS_CandleFlame` | inside `BP_Candle` / `BP_Sconce` | a candle light with no visible flame reads as a bug |
| `NS_Embers` | hearths | slow rising sparks; sells warmth |
| `NS_ColdBreath` | player and werewolf in unheated rooms | *"makes the creature feel like it is breathing near you"* |

**22.6** This is also the **only place Part A tells story** (§A.18): dress toward suggestion — whose
room this was, what the occupying unit did here. **Author no text.**

**Test (brief's own):** *"Every room has something to look at. No un-restyled fantasy geometry
visible."*

---
---

# PHASE 4 — "IT'S A GAME YOU CAN READ" (19 – 24 August, days 20–25)

*`design-brief` §A.16 Block 4.*

---

### Step 23 — `[FORM]` UI restyle · *MIXED* · **Implements:** `design-brief` §A.12 (typography, colour and framing, motion); §A.14 rows 15, 16; §A.15 V11; §A.16 step 23

§A.12: *"the cheapest, fastest, most visible Form win in the project — roughly one day changes the
perceived finish of the whole game."*

**23.1 Fonts.** Import the **`Cinzel`** and **`EB Garamond`** `.ttf` files (A.14 row 15, **SIL OFL
1.1**) → Unreal creates a **`Font Face`** → `Add > User Interface > Font` with **`Runtime`** caching
→ `/Game/UI/Style/F_Cinzel` and `F_EBGaramond`. Assign on `Text Block` / `Rich Text Block`.
Role split: `Cinzel` = titles, buttons, headings; `EB Garamond` = body, prompts, credits.
**`UnifrakturMaguntia` at most once, on the title** — §A.12: *"Use blackletter almost never"*, or the
game reads Halloween rather than Napoleonic. **OFL requires crediting the fonts** in the credits
screen / readme.

**23.2 `T_Panel_Vellum`.** Import a CC0 paper texture (A.14 row 16, ambientCG / Poly Haven / Kenney)
→ `/Game/UI/Style/T_Panel_Vellum`.

**23.3 Colour.** Text **warm bone `#E8DFC8`** on near-black — **never `#FFFFFF`**. Accents: oxblood
**`#5A1414`** (danger, game over), tarnished gilt **`#C9A227`** (titles, selection), cool silver
**`#C8D0D8`** (the silver resource, preparing Part B).

**23.4 Framing.** **Every panel gets a frame**: a **`Border`** with `Brush > Draw As` = **`Box`**,
`T_Panel_Vellum` as the image, and **`Margin`** set so it scales without stretching corners. **Nest a
second thin `Border` inset ~8 px as a double rule** — §A.12: *"That double rule alone kills the
'default Unreal UI' read."* Bake aged edges into the texture's alpha; do not attempt it with widget
nodes.

**23.5 Buttons.** `Button > Style > Normal / Hovered / Pressed` brushes tinted from the palette.
**No rounded blue default anywhere.** Hovered = **gilt text**, not a colour block.

**23.6 Motion.** A **`Widget Animation`** on every widget: **0.15–0.3 s opacity** (plus an 8–12 px
upward translate on titles), played in **`Event Construct`** or on the death beat. §A.12: *"Instant
pop-in is the most reliable tell of an unfinished UI."*

**23.7 Apply to `WBP_Prompt`, `WBP_GameOver`, `WBP_Escaped`.**

**Test (brief's own):** *"No pure white, no default blue button, nothing pops in instantly."*

---

### Step 24 — `[FORM]` `L_Title`, `WBP_TitleScreen`, `WBP_Credits` · *MIXED* · **Implements:** `design-brief` §A.12 widget set; §A.14 compliance obligation 2; §A.15 V12; §A.16 step 24; leave-off item 10

**24.1 `L_Title`** — dress **one corner** of the mansion (reuse step 15 modules + step 19 materials +
step 20 lighting), one candle, fog, and a **slow camera drift** (`Camera Actor` + `Level Sequence`,
or a `Timeline` on a level Blueprint). §A.12: *"A large share of 'this is a finished game' for very
little work."*

**24.2 `WBP_TitleScreen`** → `/Game/UI/WBP_TitleScreen`: title in `Cinzel` (**placeholder title —
§A.18, do not author narrative**), `Begin`, `Credits`, `Quit`.
- `Begin` → **`Open Level (by Name)`** `L_Mansion_Slice`.
- `Credits` → `Create Widget` (`WBP_Credits`) → `Add to Viewport`.
- `Quit` → `Quit Game`.
- On construct: `Set Input Mode UI Only`, `Show Mouse Cursor` true.

**24.3 `WBP_Credits`** → `/Game/UI/WBP_Credits`: a scrolling **`Rich Text Block`** populated **from
`/CREDITS.md`** (step 0c). §A.12: it is *"a **licence-compliance artefact**, not a nicety."*
**It must carry, at minimum:** the A.14 **row 14 Incompetech / Kevin MacLeod CC-BY attribution**,
every **CC-BY Freesound** entry (row 12), and the **font credits** (row 15). Credit Paragon,
Game Animation Sample and Infinity Blade too, even though rows 1/3/9 do not require it.

**24.4** `Project Settings > Maps & Modes > **`Game Default Map` = `L_Title`**` (§A.1, §A.17).

**24.5** `Project Settings > Packaging > List of maps to include in a packaged build` → confirm
**both `L_Title` and `L_Mansion_Slice`** are listed. Leave-off item 10; §A.17 breakage 2 — this is
*"the most common Part A failure"* and it presents as a **black screen at runtime**.

**Test (brief's own):** *"Title → Begin → play → Main Menu → Credits all work. Every CC-BY
attribution is present."*

---

### Step 25 — `[FORM]` Full audio pass · *MIXED* · **Implements:** `design-brief` §A.13 (content list, implementation notes); §A.14 rows 11, 12, 14, 16; §A.15 V13; §A.16 step 25

**25.1 Ambience** — **6–10 `Ambient Sound`** actors: wind in chimneys, distant timber creak, rain on
leaded glass, a long-case clock, rats in the wainscot. `Sound Class` = `SC_Ambience`.

**25.2 Reverb** — **4–6 `Audio Volume`** actors, each with a **`Reverb Effect`** preset, **one per
room type** (stone vault, panelled study, plastered corridor, draped bedchamber, great hall). §A.13:
*"the cheapest 'this is a real building' effect in existence, and it gives the player spatial
information — Pillar 4."*

**25.3 Player audio** — footsteps ×2 surfaces (stone, board) with random variation, cloth rustle, the
step-4 breathing loop, a grunt on hard stop. Trigger footsteps with an **`Anim Notify`** on the
step-5 locomotion animation — §A.13: *"better than a timer."*

**25.4 UI sounds** — paper-turn for navigation, low thud for game over, rising chord for escaped,
soft tick for hover. `Sound Class` = `SC_UI`.

**25.5 Music — exactly two cues** (`SC_Music`): a **game-over** cue and an **escape/win** cue, 30–60 s
each, from **Incompetech (A.14 row 14, CC-BY, attribution REQUIRED → already in `WBP_Credits` at step
24.3)**. **No chase music** — §A.13: *"Silence plus the creature's own audio is scarier, cheaper, and
keeps the hearing-based gameplay legible."*

**25.6 Randomisation** — `MetaSound Source` with a `Random` node (or `Sound Cue` + `Random`) for
footsteps and creature vocals.

**25.7 Concurrency** — a **`Sound Concurrency`** asset capping the ~50 looping candle `Audio`
components (§A.13).

**Test (brief's own):** *"Each room sounds different with your eyes shut."*

---

### Step 26 — `[FN]` Player character visual, per the step-6 verdict · *HAND* · **Implements:** `design-brief` §A.10 (whole section); §A.14 rows 3, 4, 5; §A.15 V8; §A.16 step 26

**If FIRST PERSON won at step 6** (~0.5 day):
- Confirm **`Set Owner No See`** = true on `Mesh` in `ApplyPerspective` (step 3.2) — the body still
  casts a shadow, *"which sells presence for free. The cheapest credible Part A."*
- Optional: forearms/hands only.

**If THIRD PERSON won at step 6** (~3–5 days):
- Import a **coat-silhouette Paragon hero** (A.14 row 4: `Wraith`, `Gideon`, `Revenant`, `Murdock`,
  `Sparrow`) into `/Game/Sourced/`. §A.10: *"At third-person distance a greatcoat, boots, high collar
  silhouette **is** 'Napoleonic' — the silhouette carries it, not the buttons."*
- Create an **`IK Rig`** for the hero and an **`IK Retargeter`** from **`IK_Mannequin`** (A.14 row 5,
  ships with the Third Person template), named **`IK_<Hero>`** and **`RTG_Mannequin_<Hero>`**, then
  **`Export Selected Animations`** so the Game Animation Sample clips (row 3) drive it.
  Humanoid-to-humanoid retargeting is reliable: half a day.
- **Re-material to the §A.8 palette** (step 19's masters).
- Tune `SpringArm_TP` so the camera does not clip walls in **300 cm** corridors: `Do Collision Test`
  true, `Probe Size` raised, `Camera Lag` ~0.1.
- **The one people forget (§A.10):** *"confirm the werewolf is still legible when the player's own
  body occupies the centre of the screen. Pillar 2 is measured in the perspective that ships."*
- **`SKM_Manny` / `SKM_Quinn` is not acceptable in the shipped build if third person wins** (§A.10
  option 3 — *"wrong century"*). Authoring a period costume is **3+ days and Part C** (§C.6).
  Do not attempt it here.

**Test (brief's own):** *"The player character looks period-appropriate in the perspective that
ships."*

---

### Step 27 — `[FN]` End-to-end playtest ×5 · *HAND* · **Implements:** `design-brief` §A.16 step 27; §A "Definition of done" items 1–4; Pillars 2 and 4

**Do:** Play the full loop **at least five times**: explore → spotted → chased → escape **or** caught.
**Fix only what breaks the loop or the read.** This is not a polish window.

Check against the brief's own acceptance bars, gathered:
- Can you **name the wolf's state with your eyes closed**, through a wall? (§A.13, step 11)
- Does the wolf **silhouette** at all three step-16 positions at **400 / 800 / 1500 cm**? (§A.8)
- Does **sprinting barely escape** and cost all stamina? (§A.4, step 14)
- Can you **explain every capture**? (Pillar 2 — if not, the cause is usually `Sight Radius` vs
  lighting, step 21.3.)
- Does the navmesh reach **every room through every doorway**? Press **`P`**. (§A.6)
- **No survival timer, no health bar, no HUD** crept in? (§A.15 F18, §A.12)

**Test (brief's own):** *"Five clean runs: explore → spotted → chased → escape or caught."*

---
---

# PHASE 5 — "IT SHIPS" (25 – 27 August, days 26–28, + reserve 28–31 August)

*`design-brief` §A.16 Block 5, §A.17.*

---

### Step 28 — `[FORM]` Full packaging pass · *HAND* · **Implements:** `design-brief` §A.17 (settings and all seven known breakages); §A.2 (dev-tool gating); §A.15 V14; §A.16 step 28; leave-off item 10

**28.1 Gate the dev tools.** Set `bAllowPerspectiveToggle` = false (disables **`IA_TogglePerspective`**
— §A.2: *"a development tool… gate it behind `bAllowPerspectiveToggle` before packaging"*) and
`bShowDebugHUD` = false. **Neither camera is deleted** — the toggle is disabled, not removed
(§0, §C.5 revisits the verdict).

**28.2 `Project Settings > Project > Packaging`:**
- **`List of maps to include in a packaged build`** = **`L_Title`** *and* **`L_Mansion_Slice`**
  (drop `L_Sandbox`). **Leave-off item 10.**
- `Additional Asset Directories to Cook` for anything referenced only by soft path or `Data Table`.
- `Use Pak File` **on**.

**28.3 `Project Settings > Project > Description`:** game name and version.
**`Platforms > Windows > Icon`:** a real icon — §A.17: *"a default Unreal icon on the submitted
`.exe` undoes a surprising amount of the finish work."*

**28.4** Confirm `Maps & Modes > Game Default Map` = **`L_Title`**.

**28.5 Package.** `Platforms > Windows > Package Project`, **`Build Configuration` = `Development`
FIRST, then `Shipping`** (§A.17: *"Confirm Development packages first so you know which class of
problem you have"*).

**28.6 Work the known breakage list in the order it bites (§A.17):**
1. `Print String` / `Draw Debug*` compiled out in Shipping — anything leaning on them fails silently.
2. Missing maps (28.2).
3. Shipping fails where Development succeeds — usually toolchain: Windows SDK / .NET / `hostfxr.dll`.
   Blueprint-only projects package without Visual Studio, but install the launcher prerequisites
   anyway.
4. Navmesh — `Runtime Generation = Dynamic` rebuilds at runtime; **verify in the `.exe`**.
5. **`Set Game Paused` + `Set Input Mode UI Only` + `Show Mouse Cursor` behave differently once the
   mouse is truly captured — test the game-over and escaped screens in the `.exe`.**
6. Performance: Lumen + VSM + volumetric fog + 50 shadow-casting practicals is heavy. If unplayable:
   cap `Attenuation Radius` on practicals, turn **`Cast Shadows` off on the majority of candles**
   (keep 5–10 hero lights), lower `Volumetric Fog > Grid Pixel Size`, reduce
   `Lumen Global Illumination > Final Gather Quality`. **Do this in the `Post Process Volume` and
   light properties — not by abandoning the look.** Measure with `stat unit` / `stat GPU`.
7. Empty or tiny output folder = **cook failed even if the UI said it finished. Read the log.**

**Test (brief's own):** *"A Shipping `.exe` exists."*

---

### Step 29 — `[FORM]` Clean-machine verification · *HAND* · **Implements:** `design-brief` §A "Definition of done" item 5; §A.16 step 29

**Do:** Copy the packaged build to **a machine that never had the Unreal Editor installed** and run
it. Walk the whole loop: **Title → Begin → explore → chased → win → quit**, and separately
**Title → play → caught → Restart**.

**Test (brief's own):** *"Title → play → win → quit, with no editor-only behaviour missing."*

---

### Step 30 — `[—]` Submission package · *HAND* · **Implements:** `design-brief` §A.16 step 30; §A.14 compliance obligations 1–3; leave-off item 12

1. `README.md` at the repo root.
2. **Final `/CREDITS.md`** reconciled against `/Docs/licences/` — every asset has author, source URL,
   licence name + version, download date, attribution string, and where it is used.
3. Confirm **`WBP_Credits` in the shipped `.exe`** matches `CREDITS.md` for every CC-BY row.
4. Assemble the submission package.

> ## **HARD STOP.**
> **Part A is done. Do not start Part B until a packaged build exists and runs on a machine that
> never had the Unreal Editor installed.** (`design-brief` §0 Part B row; §A.16 step 30; leave-off
> item 12.) If the calendar is at 28 August and Step 29 has not passed, **the reserve window is for
> Step 28 repair — not for Phase 8.**

---
---

# PHASE 6 — LATER · Part B, stretch (gated on Step 30)

**Do not begin any of this until Step 30 is signed off.** `design-brief` §B: *"Nothing here may be
started at the cost of Part A's Form work — a working scent trail in a grey-box game is worth less to
this deliverable than a finished-looking game without one."*

**Every subsection is independently shippable.** Build in §B.6's order and **stop wherever the
calendar stops you**. Each carries a small `[FORM]` tail so anything shipped from Part B ships styled
to Part A's bar (§B intro).

---

### Step B1 — `[FN]` **Scent trail** — the breadcrumb system · **Implements:** `design-brief` §B.1; §B.6 order 1 · **LATER**

Unreal has **no built-in smell sense**; §B.1 uses an **actor-based breadcrumb trail** the AI reads
directly — simple, debuggable, no C++.

1. `Project Settings > Engine > Collision > Object Channels` → create a **`Werewolf`** object channel,
   default response **`Ignore`**.
2. `Add > Blueprint Class > Actor` → `/Game/Werewolf/BP_ScentMarker` (no visible mesh). Variables:
   `Strength` (Float), `SpawnTime` (Float, from **`Get Game Time in Seconds`**), **`TrailIndex`
   (Integer, monotonically increasing — "this is what makes it a trail, not a cloud")**.
   `Initial Life Span` = `ScentLifetime` **40 s** `TUNING START` — **lifespan *is* the decay, no
   tick.** `Sphere Collision` `ScentVolume`, radius **250** `TUNING START`, overlap-only vs the
   `Werewolf` channel.
3. `BP_PlayerCharacter`: **`Set Timer by Function Name`**, looping at `ScentInterval` **0.5 s**
   `TUNING START`, spawning markers with `Strength` = the current scent multiplier (B2).
4. `BP_Werewolf`: `Sphere Collision` **`NoseVolume`**, radius **400** `TUNING START`, overlapping the
   `Werewolf` channel. `On Component Begin Overlap` → `Cast To BP_ScentMarker` → **compare
   `TrailIndex` against a `LastSmelledIndex` integer on the wolf: higher = fresher → follow; lower →
   ignore.** §B.1: *"This single comparison is the entire directionality solution… Without it,
   scent-following looks drunk."* Then write `ScentTargetLocation`, `ScentStrength`, `bHasScent` =
   true, `LastSmelledIndex`, `WolfState` = **`ScentPursuit`** (already declared at step 9.1).
5. New `BB_Werewolf` keys: `ScentTargetLocation` (Vector), `ScentStrength` (Float), `bHasScent` (Bool).
6. **Insert `Sequence "ScentPursuit"` between `Investigate` and `Patrol`** — decorator
   `Blackboard` `Is Equal To` `bHasScent` = true, `Observer Aborts: Both`; `BTT_SetWolfState`
   (`ScentPursuit`); `Move To` `ScentTargetLocation`, `Acceptable Radius` 80; `Wait` 0.4.
   **That ordering *is* the LOCKED sensory hierarchy expressed as Behavior Tree priority.**
7. `bHasScent` cleared by the **same `DecayMemory` timer** (step 13.4) after `ScentGiveUp` **8 s**.
8. Performance guard: past `MaxScentMarkers` **150** `TUNING START`, `Destroy Actor` the oldest.
9. `[FORM]` tail: `NS_ScentWisp` on each marker, **off by default**, enabled only by `bShowDebugHUD`.
   *"The player is not supposed to see their own scent."*

**This adds keys, one branch and two overlap handlers and touches NO Part A logic** — the seam §A.3
promised. **Test:** walk a loop in `L_Sandbox` and watch the wolf retrace it.

---

### Step B2 — `[FN]`+`[FORM]` **Three player-readable scent states** · **Implements:** `design-brief` §B.2; §B.6 order 2 · **LATER**

`E_ScentState` at `/Game/Core/Enums/E_ScentState`: `Normal`, `HighScent`, `Masked`. A
`ScentMultiplier` float on `BP_PlayerCharacter` feeds `BP_ScentMarker.Strength` at spawn.

| State | Entered when | `ScentMultiplier` | Marker lifespan | Cue |
|---|---|---|---|---|
| `Normal` | default | 1.0 | 40 s | steady breathing, neutral grade |
| `HighScent` | `Stamina` < `HighScentThreshold` **35%** `TUNING START` **while sprinting** | 2.0 | 80 s | ragged breathing, warm desaturated post-process, rising heartbeat |
| `Masked` | odor supply applied (B3) | 0.25 | 12 s | application cue, cool blue-green tint, fading ambience |

- `HighScent` **persists after stamina recovers** for `HighScentDecay` **25 s** — *"the panic option is
  always available and always costs."*
- `Masked` **overrides but does not clear** `HighScent`, so masking is a decision about **timing**.
- All three cues must be legible **in both perspectives** — audio and post-process, **not**
  third-person-only body animation.
- **No permanent scent meter.** Debug readout behind `bShowDebugHUD` only.

> **Gap the brief itself flags:** `HighScentThreshold` is *"TBD in the brief; this is a starting
> value."* Tune it, do not treat 35% as LOCKED.

---

### Step B3 — `[FN]`+`[FORM]` **Odor masking** · **Implements:** `design-brief` §B.3; §B.6 order 4 · **LATER**

`/Game/World/BP_OdorSupply`, child of `BP_Interactable`, with `E_OdorType` — **`Perfume`, `Cologne`,
`Absinthe`, exactly the three named in `project-brief.md`**. `Interact` → add to an inventory Array →
`Destroy Actor`. `IA_ApplyOdor` → `E_ScentState` = `Masked`, `MaskTimer` of `MaskDuration` **60 s**
`TUNING START`, item removed permanently. **Never respawns** (Pillar 3 **LOCKED**: *"finite… no
respawn"*) — placement is authored, **no spawner**. For the slice the three differ only by
`MaskDuration` and `ScentMultiplier`.
`[FORM]` tail: three distinct period bottles on `M_Metal_Tarnished` / a glass instance, each with its
own application sound — *"a recognisable silhouette on a shelf is how the player learns a resource
exists without a marker."*

---

### Step B4 — `[FN]`+`[FORM]` **Hiding place · pounce · flintlock and silver** · **Implements:** `design-brief` §B.4; §B.6 orders 5, 6, 7 · **LATER**

**Hiding place** — `/Game/World/BP_HidingSpot`, in the **single deliberate dead-end chamber step 16
reserved**. `Interact` → `Set Actor Location` the player to a `SceneComponent` marker inside, disable
movement input, `bHidden` = true, blend the camera to a slit/keyhole view (a **component**, not a
camera, so it works in both perspectives). While hidden: **stop spawning scent markers, stop noise
events, and `Unregister from Perception System`** on the stimuli source; re-register on exit.
**The trail *leading to* the hiding place still exists, so the wolf arrives — that is the point.** It
enters `SearchHiding` and loops `Wait` + investigate for `SearchTime` **15 s** before giving up.
A found player is **caught immediately** (Win/Lose LOCKED).

**Pounce** — activate `PouncePrep` / `Pounce`. Inside the `Chase` sequence add a child `Sequence`
gated by an **`Is At Location`** decorator on `TargetActor`, `Acceptable Radius` **600**.
`PouncePrep`: `BTT_SetWolfState` → `PouncePrep`, `Max Walk Speed` → 100, lowered-profile pose, hold
`PounceWindup` **0.9 s**. **The windup must be visible *and* audible** (Pillar 2).
`Pounce`: **`Launch Character`** toward the player's position **as sampled at the end of windup** —
**no aim tracking during the leap**; committing to a stale point is exactly what makes the LOCKED
sideways-sprint counter work. Landing → `Wait` **1.2 s** recovery → back to `Chase`.
**`CatchSphere` stays exactly as built at step 12** — a connecting pounce catches through the
existing path and the game-over flow needs no changes.

**Flintlock handgun + silver** — `/Game/Player/BP_FlintlockHandgun`. LOCKED as temporary: single-shot,
**silver ball + gunpowder charge per shot**; **body hit = stagger, head hit = unconscious, neither
kills**; handgun reload ~9 s (walk, no sprint).
`IA_Fire` → require `SilverBalls > 0` **AND** `GunpowderCharges > 0` **AND** `bLoaded` →
`Line Trace By Channel` from the camera → decrement both → `bLoaded` = false → **`Report Noise
Event`** `Loudness` **2.0**, `Max Range` **5000** (gunshots are named in the LOCKED sensory
hierarchy). Resolve with **`Break Hit Result > Hit Bone Name`**: `head` → `Unconscious`, else
`Staggered`.
`Staggered`: `WolfState` = `Staggered`, zero `Max Walk Speed`, `Get AI Controller` →
**`Get Brain Component`** → **`Stop Logic`**, `Delay` `StaggerTime` **3 s**, **`Start Logic`**,
restore speed. `Unconscious`: same with **25 s**, plus `Clear Value` `TargetActor` and `bHasScent`
*"so the wolf wakes without knowing where you went."*
> **The wolf never dies (LOCKED). There is no health variable anywhere in this system, only timers.
> Do not add one.**
`[FORM]` tail: `NS_MuzzleFlash` + **smoke that lingers in the volumetric fog** (*"the single most
characterful visual in the whole weapon; do not skip it"*), a heavy report on `SC_SFX`, a full-screen
`Post Process` flash.

---

### Step B5 — `[FN]`+`[FORM]` **Safe haven, autosave, werewolf reset** · **Implements:** `design-brief` §B.5; §B.6 order 3 · **LATER**

Build **one**, in the footprint step 16 reserved. `/Game/World/BP_SafeHaven`, Actor with a
`Box Collision` **`HavenVolume`**.

1. **The werewolf physically cannot enter** — a **`Nav Modifier Volume`** over the interior with
   `Area Class` = **`NavArea_Null`** (§A.6 item 6 reserved exactly this). *"A navigation solution,
   not a scripted one, so it cannot be defeated by a state-machine bug."* Belt and braces: block the
   wolf capsule with collision at the threshold.
2. **Entering ends the pursuit** — `On Component Begin Overlap (HavenVolume)` → cast to player → get
   the werewolf's controller → call **`ResetToPatrol`** (**written once at step 13.5** — this is why)
   plus clear `bHasScent` and `LastSmelledIndex`, and **`Get All Actors of Class`** →
   **`Destroy Actor`** on every live `BP_ScentMarker` so the wolf cannot re-acquire the trail to the
   door.
3. **Autosave, only here** — `/Game/Core/SG_WerewolfSave` (a **`SaveGame`** class) holding
   `PlayerTransform`, `Stamina`, `bHasEscapeKey`, `SilverBalls`, `GunpowderCharges`, `Inventory`,
   **`PickedUpActorIDs`** (so consumed finite resources stay consumed — Pillar 3), `LastHavenID`.
   **`Create Save Game Object`** → fill → **`Async Save Game to Slot`**, slot `"AutoSave"`,
   `User Index` 0. Confirm it **diegetically** — a hearth catching light, a soft chord — **not a
   "Saved" toast** (Pillar 4).
4. **Loading** — `WBP_GameOver`'s `Restart` becomes **`Does Save Game Exist`** (`"AutoSave"`) → true:
   **`Load Game from Slot`** → `Cast To SG_WerewolfSave` → store on **`GI_Werewolf`** →
   `Open Level (by Name)` → on `BP_PlayerCharacter` `BeginPlay` read the pending save off
   `GI_Werewolf` and apply it. False: plain `Open Level`. **Keep the handoff on the Game Instance —
   it is the only object that survives `Open Level`.**
   > §B.5's own warning: *"Applying a save on `BeginPlay` fights anything else that positions the
   > player at startup. Have exactly one authority for the player's initial transform."*
5. **Crafting only here** (LOCKED) — one button on a haven widget: N silver objects → N silver balls.
6. `[FORM]` tail: the haven must be **legible as safe on sight** — the one place the two-temperature
   rule is **broken deliberately**: a warm hearth brighter than anywhere else, visible from the
   doorway, fog thinning. *"Pillar 5 Temporary Relief expressed in light."*

---
---

# PHASE 7 — LATER · Part C, recorded not scheduled

**Off the 1 September critical path.** Recorded here only so nothing from `project-brief.md` is lost
(`design-brief` §C intro). **Do not schedule any of this before 1 September.**

- **C.1 — full werewolf state set.** Complete the LOCKED list: `Charge` (**counterplay is UNDER
  EVALUATION — do not invent it**), richer `SearchHiding` via **`Run EQS Query`** scoring hiding-spot
  actors, door-opening animations via **`Smart Link`** / **`Receive Smart Link Reached`**, "cannot
  swim" as a `Nav Modifier Volume` with a water area class. **`State Tree` only if the Behavior Tree
  becomes unmanageable** — it is sufficient for everything above.
- **C.2 — resource economy at full scale.** Silver finds, gunpowder caches, the rifle (12 s reload,
  no movement), full three-odor differentiation. **Pillar 3's hard constraint holds: the game must
  remain finishable with zero resources**, so every gate needs a non-combat, non-masking solution.
  Audit whenever content is added.
- **C.3 — puzzle framework (do not author solutions).** `BP_PuzzleNode` (child of `BP_Interactable`);
  `BP_PuzzleChain` (Array of nodes + `CheckSolved`, fires an **Event Dispatcher** on solve);
  `BP_AccessGate` (subscribes and changes world access). **Every solve must change navigable
  space** — keep `Runtime Generation = Dynamic` so the navmesh follows. **`BP_EscapeDoor` (step 17)
  is already a `BP_AccessGate` in miniature; generalise it rather than replacing it.**
- **C.4 — world at full scale.** 3–5 areas via **`Level Streaming`** or **World Partition**, keeping
  **one navmesh domain** so the wolf can pursue across boundaries. Resolve mansion-vs-castle **here,
  not before**. The step-15 module set is what makes this affordable.
- **C.5 — perspective decision revisited** with pounce, hiding place and scent cues in play. Confirm
  or reverse step 6's verdict and record it as a LOCKED line in `project-brief.md` — **not silently
  in code.** (This is why step 28 disables the toggle rather than deleting a camera.)
- **C.6 — art, audio and narrative beyond Part A's bar.** Bespoke werewolf sculpt; the 3+ day
  authored greatcoat §A.10 declined; a purpose-built modular Gothic kit replacing blockout meshes
  **module-for-module on the same grid**; bespoke creature vocals; original score; the full narrative
  layer into §A.18's sockets; localisation; **accessibility — note that a very dark game *needs* a
  brightness slider, so promote this if there is any slack.**

---
---

# APPENDIX A — Asset register trace (every asset ↔ an A.14 row ↔ a step)

Per the commander's zero-budget constraint: **every asset referenced anywhere above traces to a row
in `design-brief` §A.14.** Nothing else may be imported.

| A.14 row | Asset | Claimed at | Imported/used at |
|---|---|---|---|
| 1 | Paragon: Rampage | 0b | 8 (`BP_Werewolf`, `ABP_Werewolf`) |
| 2 | Paragon: Khaimera / Narbash | 0b | 8 (silhouette comparison, then deleted) |
| 3 | Game Animation Sample | 0b | 5 (`ABP_Player`), 26 (TP branch) |
| 4 | Paragon Wraith / Gideon / Revenant / Murdock / Sparrow | 0b | 26 (**only if TP wins at 6**) |
| 5 | `SKM_Manny` / `SKM_Quinn` / `IK_Mannequin` | 1 (template) | 5, 6 (stand-in), 26 (retarget source) |
| 6 | MetaHuman | — | **not used** (§A.10 "not recommended") |
| 7 | ambientCG CC0 surfaces | 0b | 19 (five masters) |
| 8 | Poly Haven CC0 (HDRI, surfaces, props) | 0b | 20 (`Sky Light` cubemap), 22 (props) |
| 9 | Infinity Blade packs | 0b | 22 (**re-materialled or neutral stone only**) |
| 10 | Fab bi-weekly free drops | 0b **and every 2 weeks to 1 Sept** | 22 (opportunistic) |
| 11 | Sonniss GDC bundle | 0b | 11 (creature), 25 (ambience, footsteps) |
| 12 | Freesound (**CC0 first**; CC-BY needs credit) | 0b | 11, 25 |
| 13 | Infinity Blade Effects / Sounds | 0b | 11 (creature vocals, pitched down) |
| 14 | Incompetech / Kevin MacLeod — **CC-BY, attribution REQUIRED** | 0b | 25 (two cues), **24.3 (`WBP_Credits`)** |
| 15 | Google Fonts `Cinzel` / `EB Garamond` (OFL) | 0b | 23 (`F_Cinzel`, `F_EBGaramond`), **24.3 credits** |
| 16 | CC0 paper / icons (ambientCG, Poly Haven, Kenney) | 0b | 23 (`T_Panel_Vellum`, keybind glyphs) |

---

# APPENDIX B — Feature trace (`design-brief` §A.15 ↔ step)

| # | Feature | Step |
|---|---|---|
| F1 | Walk / crouch / sprint, control-rotation-relative | 2, 4 |
| F2 | Stamina drain / regen | 4 |
| F3 | Diegetic stamina readout (breath + vignette), no bar | 4 |
| F4 | Both cameras, runtime-toggleable | 2, 3, 6 |
| F5 | Line-trace interaction + diegetic prompt | 17 |
| F6 | `AI Sight config` + `AI Hearing config` | 10, 13 |
| F7 | `Report Noise Event` — sprint loud, walk quiet, crouch silent, doors noisy | 4, 18 |
| F8 | Behavior Tree Patrol / Investigate / Chase, interruptible | 9, 10, 13 |
| F9 | `Get Random Reachable Point in Radius` patrol | 9 |
| F10 | Memory decay → `ResetToPatrol` after ~12 s | 13 |
| F11 | Chase speed just below player sprint | 9, 14 |
| F12 | Per-state creature audio, occluded | 11 |
| F13 | `Runtime Generation = Dynamic`, AI-openable doors | 7, 16, 18 |
| F14 | ≥1 `Nav Link Proxy` the player cannot use | 18 |
| F15 | Contact → death beat → game over → Restart | 12 |
| F16 | Key + escape door → win with visual payoff | 17 |
| F17 | One floor: hub, loop, no dead ends, shortcut, 3 silhouette positions | 16 |
| F18 | **No survival timer of any kind** | guardrail — never built |
| V1 | Modular blockout grid | 15, 16 |
| V2 | Five masters + per-room instances, no default grey | 19 |
| V3 | Two-temperature lighting, dark connective space | 20 |
| V4 | Global post-process, **exposure locked** | 21 |
| V5 | Exponential height fog + volumetric fog | 21 |
| V6 | Sourced werewolf, re-materialled, silhouette-first | 8 |
| V7 | `ABP_Werewolf` matched to the speed table | 8, 14 |
| V8 | Player visual appropriate to the chosen perspective | 26 |
| V9 | Set dressing + 30 decals incl. claw marks | 22 |
| V10 | Niagara motes / flames / embers / breath, light flicker | 20, 22 |
| V11 | Styled UI, no pure white, no permanent HUD | 23 |
| V12 | `WBP_TitleScreen` + `L_Title` + `WBP_Credits` | 24 |
| V13 | Full audio: ambience, reverb, footsteps, creature, UI, 2 cues, `SM_Chase` | 4a, 11, 25 |
| V14 | Packaged Windows build on a clean machine | 14b, 28, 29 |

---

# APPENDIX C — Gaps in `design-brief.md` flagged, not invented around

Per the commander's instruction, gaps are reported rather than filled with outside research.

1. **The Unreal MCP server is never specified.** §0 and §A.16 step 0a require the connection but name
   no repo, plugin, transport or port. **Step 0a is written as a recovery procedure with a hard
   fallback (0a.5) rather than a recipe.** This is the single largest unknown in the plan and it
   gates everything.
2. **The `Camera Actor` in the §A.5 death beat has no stated home.** I specify a `DeathCam` `Camera`
   component on `BP_Werewolf` at step 12.4 and mark it as an inference.
3. **`Report Noise Event` tags are set but never read** in Part A (§A.2 specifies `Footstep_Sprint`;
   §A.3 decides the sense with `Line Of Sight To` instead). Harmless, noted at step 4.5.
4. **Audio mix architecture has no A.16 step number** even though §A.13 says to do it first and §A.2's
   `BreathAudio` (step 4) needs a `Sound Class`. **Inserted as step 4a** — an ordering fix, no new
   scope.
5. **Step 6's "60-second sandbox traverse" content is unspecified.** I define it at 6.1 from §A.7's
   own dimensions (300 cm corridor, 200 × 280 doorway) and §A.10's judging criteria.
6. **`HighScentThreshold` (35%) is flagged TBD by the brief itself** (§B.2). LATER; noted at B2.
7. **Engine version floor is ambiguous** — §0 says 5.4+, while §A.10/§A.14 row 6 references MetaHuman
   requiring 5.6+. Immaterial because MetaHuman is not used, but pick one version and stay on it;
   §A.1's render settings should not be changed mid-project.
8. **The pre-production window is two days shorter than the brief assumed** (brief: 25–30 July;
   actual start: 27 July). Step 0b's downloads are the compressible part; **the 31 July start of
   Block 1 is not**.
