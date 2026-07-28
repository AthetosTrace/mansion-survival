<!-- GENERATED FILE - do not hand-edit.
     Source of truth is 'CapstoneWerewolf GGD.pdf' at the project root.
     Regenerate with: py -3 tools/extract_gdd.py
     Text is verbatim: whitespace and ligatures repaired, no word changed. -->

# 3. Player Movement, Stamina and Scent

3.1 Movement Set
- Walking, crouching, short-duration sprinting and contextual vaulting are the complete planned traversal set.
- There is no dodge roll and no complex parkour.
- Player climbing is not part of the current scope unless a specific level requirement proves necessary.
- Large carried objects prevent firearm use and create deliberate vulnerability during transport.

3.2 Stamina-to-Scent Relationship Stamina is both a movement limiter and a tracking-risk meter. Sprinting consumes stamina. Once expenditure crosses a tuning threshold, the player enters a high-scent state: the trail becomes stronger, may persist longer, and is easier for the werewolf to reacquire. Walking, crouching and resting restore stamina. Exact durations, thresholds, recovery and scent multipliers are UNDER EVALUATION. v0.2 | CONCEPT / PRE-PRODUCTION | PAGE 4 Player states Relative detection Design purpose Crouch Stealth / slow movement Lowest planned baseline; exact reduction TBD. Lower noise radius. Supports cautious traversal and quieter repositioning. Walk Normal continuous scent trail. Default sustainable exploration pace. Sprint below threshold Elevated scent with immediate escape value. Allows tactical movement without instantly maximizing tracking risk. Sprint beyond threshold Strong scent trail with longer persistence and faster reacquisition. Makes panic running a meaningful long-term cost. Odor-masked Trail temporarily weakened or obscured. Breaks scent pursuit but does not defeat sight or nearby hearing.

3.3 Feedback Requirements
- The player receives readable stamina feedback through breathing, movement performance, animation and/or a restrained interface element.
- Crossing the high scent threshold is not communicated; the player must deduct it.
- The game must distinguish active odor masking, odor expiration, direct visual detection and sound investigation through animation, audio, effects and or HUD support.
