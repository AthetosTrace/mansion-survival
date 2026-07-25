# Project Brief — Capstone Werewolf (working title: TBD)

This is the commander's seed brief and the single input the **designer** agent
consumes. It is distilled from the capstone **GDD** (`CapstoneWerewolf GGD.pdf`,
v0.2), which is the source of truth. Everything downstream must trace back to
something here. Where the GDD marks a decision LOCKED, treat it as fixed; where it
marks PROVISIONAL / UNDER EVALUATION / TBD, treat it as open and do not invent a
commitment.

> Note for the crew: there is **no "survive-until-sunrise" timer** in this game.
> The win condition is **escape**. Any earlier phrasing about sunrise is void.

## Build priority — MVP first (read this before anything else)
The real goal of the capstone is a **working, playable game that embodies the general
idea**, not a full simulation. Prioritize in this order:

1. **MVP (required first):** the player explores the mansion/castle; a werewolf
   actively pursues; the player either reaches an **escape** (win) or is caught
   (immediate game over). Stand this up in Unreal as **Blueprints**.
2. **Secondary (later passes):** the scent-trail simulation, fine-grained sensory
   detection (how the wolf finds the player), odor masking, the silver crafting
   economy, environmental puzzles, multiple areas, and the safe-haven economy. These
   enrich the game but are **not** required for the first working build.

For this pass the **designer** should temper toward the MVP: the general mansion game
and **how to set up the Blueprints to get it working in Unreal**. Keep the richer
systems below as clearly-labeled "later" so they are not lost, but do not let them
block a first playable build. Downstream, the developer will implement via an **Unreal
MCP**, so keep the design concrete and Blueprint-oriented.

## The game in one line
A Napoleonic-era Gothic survival-horror where the player explores a sealed mansion
(or castle) while a werewolf tracks them by **scent**, and must solve environmental
puzzles, manage scarce silver ammunition and odor-masking supplies, and **escape** a
creature that can be delayed but never killed.

## Platform / engine / framing (LOCKED unless noted)
- Engine: Unreal Engine, Blueprint-first. PC. Target rating T.
- Genre: stealth, exploration, atmospheric survival horror, environmental puzzle adventure.
- Perspective: **OPEN / PROVISIONAL.** First-person vs third-person is an unresolved
  prototype question — the plan is to build the same short sequence in both and
  compare. Do **not** lock a perspective; design so either can be prototyped.
- Target playtime: ~2–4 hours for a first playthrough.

## Core loop (LOCKED)
Observe the environment and listen for the predator → choose a route and pace →
search for clues, silver, gunpowder, odor supplies, and puzzle objects → solve or
advance an environmental puzzle → evade, hide, mask against, or temporarily
neutralize the werewolf → reach a safe haven or unlock a new route → repeat until the
final escape condition is met.

## Win / lose (LOCKED)
- **Win:** open an escape route and leave the trapped location.
- **Lose:** immediate game over the moment the werewolf physically reaches the
  player. There is no health bar.

## Design pillars (LOCKED)
1. **Persistent Predator** — the werewolf actively searches, tracks, and re-enters
   the player's plans; it is not a scripted-scene monster.
2. **Readable Lethality** — attacks are deadly but have recognizable cues and
   consistent counterplay; the player can explain why a capture happened.
3. **Scarcity with Agency** — silver, gunpowder, and odor supplies are finite and
   never respawn; the game stays finishable with zero resources, just much harder.
4. **Atmospheric Discovery** — architecture, objects, and sound communicate layout,
   puzzles, and history without constant objective markers.
5. **Temporary Relief** — safe havens and neutralizations give short, limited control
   that never removes the long-term threat.

## Key systems the design must account for
- **Scent / stamina (LOCKED core):** smell is the werewolf's primary sense outside
  direct sight or hearing. Sprinting drains stamina; past a threshold the player
  enters a high-scent state (stronger, longer-lasting trail). Walk/crouch/rest
  recover stamina. Exact thresholds and multipliers are TBD.
- **Sensory hierarchy:** Sight = direct line of sight (confirms and chases). Hearing
  = authored range (investigates sprinting, doors, gunshots, loud machinery). Smell =
  primary otherwise. Exact ranges/FOV are TBD.
- **Werewolf AI states:** random patrol, scent pursuit, sound investigation, visual
  chase, pounce preparation, pounce, charge, hiding-place search, staggered (silver
  body hit), unconscious (silver head hit). Travels all zones, opens doors, climbs
  authored nav links, searches hiding places; cannot enter safe havens; cannot swim.
- **Pounce (LOCKED):** telegraphed by a lowered profile; countered by a timed
  sideways sprint at the moment of commitment. No dodge-roll invulnerability. Charge
  counterplay is UNDER EVALUATION.
- **Defensive combat (LOCKED as temporary):** flintlock rifle + handgun, single-shot,
  sharing silver-ball ammo and consuming a gunpowder charge per shot. Body hit =
  stagger; head hit = unconsciousness; neither kills. Rifle reload ~12s (no movement);
  handgun reload ~9s (walk, no sprint).
- **Finite resources (LOCKED, no respawn):** silver objects → one ball each;
  gunpowder caches; odor supplies (perfume, cologne, absinthe) applied to the player
  to weaken the scent trail. Crafting is instant and only inside safe havens.
- **Safe havens (LOCKED):** 2–3 total; autosave only there; entering ends the pursuit
  and resets the werewolf to random patrol; werewolf cannot enter.
- **World:** one mansion or castle (mansion-vs-castle is PROVISIONAL), organized into
  **3–5 major areas** (e.g. central/public, residential/private, service/storage,
  military/medical, exterior grounds; optional underground) plus supporting rooms.
- **Puzzles:** each major area owns at least one puzzle chain that changes world
  access; puzzle logic must fit the building's function and period. Individual puzzles
  are TO BE CRAFTED — do not invent specific solutions; design the framework.
- **Narrative:** protagonist, reason trapped, werewolf origin, safe-haven fiction,
  and ending are TBD. Do not author narrative; note where it will hook in.

## What the designer should resolve and produce
- How the werewolf's sensory + state model is realized in Unreal (AI Perception,
  Behavior Tree / state machine, Nav Mesh, nav links).
- How the scent trail is represented and tuned (data model, player-readable states:
  normal / high-scent / odor-masked).
- How safe havens, autosave, and the werewolf-reset are structured.
- What the vertical slice must contain: per the GDD's "Risk prototype" milestone —
  movement + stamina/high-scent threshold + scent trail + odor masking + one hiding
  place + one pounce + one firearm + one safe haven.
- The minimum feature list for that playable slice, each item anchored to a pillar,
  a locked decision, or a named system above.

That is all the designer needs to begin. Anchor every decision to this brief; leave
PROVISIONAL/TBD items open rather than resolving them by invention.
