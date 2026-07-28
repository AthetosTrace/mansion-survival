<!-- GENERATED FILE - do not hand-edit.
     Source of truth is 'CapstoneWerewolf GGD.pdf' at the project root.
     Regenerate with: py -3 tools/extract_gdd.py
     Text is verbatim: whitespace and ligatures repaired, no word changed. -->

# 5. Defensive Combat, Resources and Crafting

5.1 Combat Philosophy Combat is temporary neutralization, not victory. The werewolf cannot be permanently killed. Firearms exist to interrupt an attack, create distance, open a short puzzle window or make a dangerous route temporarily safer. Scarcity prevents the game from becoming a shooter.

5.2 Firearm Specification Property Flintlock long rifle Flintlock handgun Capacity Single shot. Single shot. Ammunition Shared silver-ball ammunition; each shot also consumes one gunpowder charge. Same. Reload Manual, approximately 12 seconds in real time. Manual; duration 9 seconds in real time.. Movement during reload Player cannot move. Player may move but cannot sprint. Accuracy Best range and deliberate headshot potential; accuracy improves while standing still. More practical in confined spaces; accuracy also improves while standing still. Misfire No random misfires. No random misfires. Open questions Reload interruption/stage persistence; aim sway; perspective-specific handling. Reload duration; aim sway; close-range hit reliability.

5.3 Hit Outcomes Hit result Werewolf response Player opportunity Body shot Immediate stagger and attack interruption for a short duration. Escape one room, break line of sight, enter a route, or finish a brief interaction. Headshot Collapse and temporary unconsciousness for a substantially longer duration. Explore nearby rooms, move a large object, complete a puzzle stage, or reach another zone. Miss No defensive benefit; resources are consumed. Player must continue evasion or reload under the weapon’s restrictions. Head hit volume, aim assistance, sway, pounce/charge shooting and exact neutralization timers remain UNDER EVALUATION. All in-world timers continue during inventory, clue review, puzzle interactions and crafting; no diegetic interface pauses recovery or odor duration.

5.4 Finite Resource Economy Resource Source and conversion Rules Silver objects Authored silverware, jewelry and approved decorative items. Each eligible silver object converts to exactly one silver ball. No respawn. Gunpowder Finite authored caches such as powder horns, military storage, armories or secured rooms. One charge is consumed per shot. Silver without gunpowder is not usable ammunition. Odor supplies Perfume, cologne and absinthe placed in authored locations. Applied to the player only in the current design; temporarily weakens scent. Quantity does not respawn. Key / puzzle objects Area-specific discoveries. Important narrative or puzzle objects cannot be accidentally melted or consumed. v0.2 | CONCEPT / PRE-PRODUCTION | PAGE 7

5.5 Odor Masking
- Perfume, cologne and absinthe are applied directly to the player.
- The effect weakens or obscures the scent trail and places the werewolf into randomized patrol/pathing when no sight or sound cue overrides it.
- Odor does not make the player invisible and does not suppress nearby noise.
- When the player hides while masked and the werewolf lacks direct confirmation, it stalls in a search animation and eventually resumes patrol.
- Additional uses - throwing, scent barriers, lures, item-specific strengths, or interaction with sprinting - are UNDER EVALUATION and not required for the first prototype.

5.6 Crafting, Inventory and Safe Havens System Locked rule Crafting location Crafting occurs inside true safe havens. Crafting speed Instantaneous once the player chooses eligible silver objects and has gunpowder. Inventory Player carries both firearms, ammunition, gunpowder, a small number of odor consumables, key items and small puzzle objects. Large objects Physically carried; occupy the hands and prevent weapon use. Water containers have no general defensive interaction and are included only if a puzzle/endgame requires them. Resource exhaustion No resource respawns. The game remains completable after every bullet is missed and every odor item is wasted, but becomes extremely difficult. Exact quantities Determined after level layout, encounter count, expected accuracy and optional exploration rewards are known.
