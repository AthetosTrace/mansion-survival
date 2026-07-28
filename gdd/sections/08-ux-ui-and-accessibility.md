<!-- GENERATED FILE - do not hand-edit.
     Source of truth is 'CapstoneWerewolf GGD.pdf' at the project root.
     Regenerate with: py -3 tools/extract_gdd.py
     Text is verbatim: whitespace and ligatures repaired, no word changed. -->

# 8. UX, UI and Accessibility

8.1 Camera Decision Prototype The final camera is intentionally open. The team will build the same compact sequence in first person and third person: one exploration section, one pounce encounter and one firearm encounter. The comparison will evaluate environmental inspection, motion comfort, hiding readability, pounce telegraph recognition, headshot aiming, spatial awareness, animation burden and overall horror tone.

8.2 Baseline Information Requirements
- Minimal HUD that still communicates stamina/high-scent risk, loaded/unloaded firearm state, ammunition, gunpowder and active odor masking.
- Clear interaction prompts and state feedback for locked, available, collected, crafted, solved, autosaved and failed states.
- Clue review available inside safe havens at minimum; whether it is available everywhere remains under evaluation.
- No in-world inventory, clue or puzzle interface pauses werewolf recovery, odor or pursuit timers.

8.3 Control Baseline Action group Required behavior Movement Walk, crouch, short sprint and contextual vault; no dodge roll. Interaction Contextual inspect/use/pick up; large-object carry state blocks weapon use. Weapons Aim, fire and manual reload; rifle locks movement for about 12 seconds; handgun allows walking but not sprinting. Inventory / odor Apply finite odor consumable to player; show effect state and expiry feedback. Pause / options Menu behavior and whether true system pause halts simulation are technical/accessibility decisions to resolve.

8.4 Accessibility and Difficulty - Under Evaluation Area Prototype / design question Controls Full remapping, hold/toggle options, aim sensitivity and alternatives for repeated/long holds. Visual readability Subtitle/text scaling, contrast, brightness, non-color state cues and reduced camera shake. Hearing Captions and optional visual equivalents for critical directional werewolf cues without removing uncertainty. Pounce timing Optional wider telegraph/evasion window that preserves the core sideways-sprint counter. Aiming Optional aim assistance or generous head hit volume without turning firearms into reliable offense. Puzzle support Layered hints and repeatable clue review once puzzle content exists. Difficulty Adjust detection forgiveness, resource abundance, save spacing or telegraph windows rather than simply increasing werewolf speed. v0.2 | CONCEPT / PRE-PRODUCTION | PAGE 11
