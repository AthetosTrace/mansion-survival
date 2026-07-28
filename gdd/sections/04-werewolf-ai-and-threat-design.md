<!-- GENERATED FILE - do not hand-edit.
     Source of truth is 'CapstoneWerewolf GGD.pdf' at the project root.
     Regenerate with: py -3 tools/extract_gdd.py
     Text is verbatim: whitespace and ligatures repaired, no word changed. -->

# 4. Werewolf AI and Threat Design LOCKED Smell is the main sensory driver when the player is not in direct line of sight or within hearing range. Sight and sound become decisive only when their local conditions are met.

4.1 Sensory Hierarchy Sense Trigger / range Result Status Sight Direct line of sight. Confirms the player and supports immediate chase, charge or pounce transitions. Line-of-sight loss returns the system to search/reacquisition logic. Core rule locked; exact FOV and persistence TBD. Hearing Within an authored hearing distance; exact range TBD. Investigates sprinting, vaulting, doors, dropped objects, firearm discharge and loud puzzle machinery. Range and source loudness under evaluation. Smell Primary sense outside sight/hearing conditions. Follows the player’s scent trail at a slow search/chase pace and locates unmasked hiding places. Core rule locked; trail model/tuning TBD.

4.2 Core Behaviour Loop 1. The werewolf continuously searches the active environment rather than waiting for the player. 2. When it intersects or reacquires a usable scent trail, it follows that trail at a slow pursuit pace. 3. Direct sight or sufficiently close sound escalates the pursuit and may enable a charge or pounce. 4. When odor masking weakens the trail and no stronger sensory evidence exists, the werewolf transitions to randomized patrol/pathing. 5. After losing direct information, it searches the local area, then resumes patrol until it reacquires the player.

4.3 State Model State Typical trigger Behaviour / exit Random patrol No reliable scent, sight or sound target; safe-haven reset; successful odor masking. Moves through valid zones and selected routes. Exits when a sensory cue is acquired. v0.2 | CONCEPT / PRE-PRODUCTION | PAGE 5 State Typical trigger Behaviour / exit Scent pursuit Usable player scent trail. Follows the trail at a slow tracking pace. Strong sprint scent improves reacquisition. Sound investigation Audible event in hearing range. Moves toward the source and searches. Exact certainty and duration TBD. Visual chase Direct line of sight. Runs or positions for a charge/pounce according to distance and geometry. Pounce preparation Player enters a valid pounce distance/angle. Lowers profile and visibly commits weight before launching. Pounce Telegraph completes. Leaps toward the player; player can counter by sprinting sideways at the moment of commitment. Charge Longer clear pursuit route. High-speed ground sprint toward the player. Turning, collision and counterplay are under evaluation. Hiding-place search Scent leads to a hiding place or local search reaches it. Unmasked player is found and pulled out. Masked player causes a stalled search animation, after which patrol resumes. Staggered Silver body hit. Short interruption; duration TBD; returns to pursuit/search after recovery. Unconscious Silver head hit. Extended neutralization; duration TBD; eventually recovers and resumes hunting.

4.4 Navigation and Space Rules
- The werewolf can travel between all active zones.
- It passes through open doors.
- It can climb using authored navigation links and animations.
- It can search hiding places finding the player hiding spot results in game over.
- Door breaking is OPTIONAL and depends on destruction assets, animation and navigation feasibility.
- Werewolf-only shortcuts are UNDER EVALUATION. They must not create visible teleportation or unfair instant reappearance.
- True safe havens are inaccessible to the werewolf.

4.5 Pounce Rules
- At a valid distance, the werewolf lowers its profile and displays a recognizable preparation animation.
- The player counters by timing a sideways sprint as the werewolf commits to the leap.
- There is no dodge-roll invulnerability; success comes from reading the animation and moving out of the committed path.
- A missed pounce must create a brief recovery window. Activation distance, telegraph time, trajectory width, midair correction and recovery duration are UNDER EVALUATION.
- The sprint used to evade raises scent risk, linking immediate survival to later tracking pressure.

4.6 Fairness Rules
- The player should be able to identify the sensory cause of a chase or capture.
- Major lethal actions require readable visual and audio cues.
- No normal-pathing teleportation in the player’s view.
- Every required route must remain survivable without ammunition or odor supplies, although the no-resource path may be extremely difficult.
- Charge counterplay, hiding edge cases and direct-sight interaction with odor masking must be resolved by prototype before content lock. v0.2 | CONCEPT / PRE-PRODUCTION | PAGE 6
