---
agent: designer
status: complete
artifact: design-brief.md
---

# Designer leave-off (revision 2 — Part A now includes styling)

> **Provenance note.** The designer agent completed `design-brief.md` (1770 lines, verified on
> disk: all sections present, appendix and sources list intact) but was terminated by an API rate
> limit before it could write this leave-off. The **commander** wrote this file after verifying the
> artifact section by section. The artifact itself is entirely the designer's work.

## What changed in this revision

Revision 1 produced a functionally strong Part A that would have shipped as grey-box — white boxes,
default mannequin, unstyled UI. The commander rejected that as an unacceptable 1 September capstone
deliverable. Part A was re-scoped on two client directives:

1. **Part A = a finished-*looking*, working game.** Two interleaved tracks, tagged throughout:
   `[FN]` Function (the loop: explore → pursued → escape or caught) and `[FORM]` Form (character
   design, environment art, lighting, UI, audio, packaging). Form is interleaved into the build
   order, not bolted on at the end.
2. **Part B dropped to STRETCH**, gated on a packaged Part A build existing and running.
   Part C unchanged: recorded, not scheduled.

## The $0 rule — the binding new constraint

**No purchases.** Two legal sources only: assets we author, and genuinely free assets whose licence
permits a submitted student capstone. §A.14 is a **binding 16-row asset register** — nothing enters
`/Game/Sourced/` unless it is a row there. All rows were verified July 2026.

Headline sourcing decisions:

- **Werewolf → Paragon: Rampage** (Epic, free permanently, Unreal-only licence). Ships rigged with
  animations and FX. Authoring a rigged, animated quadruped from scratch is not achievable in 28
  days alongside the functional build; this is the pragmatic path. Khaimera and Narbash are
  silhouette alternates, compared at step 8.
- **Player animation → Game Animation Sample** (Epic, free, Unreal-only).
- **Surfaces/HDRIs → ambientCG + Poly Haven**, both **CC0**.
- **Props → Infinity Blade packs** (Epic, free) — stylised fantasy, so **must be re-materialled** or
  limited to neutral stone pieces.
- **Audio → Sonniss GDC bundle** (royalty-free, no attribution) + **Freesound filtered to CC0**.
- **Fonts → Google Fonts `Cinzel` / `EB Garamond`** (OFL).

**Explicitly rejected, with reasons in §A.14:** Quixel Megascans (free-for-Unreal era ended
31 Dec 2024), Sketchfab (licence types retired in the Fab migration), Mixamo (Adobe signalled
deprecation, unreliable), all paid marketplace assets, and AI text-to-3D — the last flagged as an
**academic-integrity question for the commander**, not a design decision.

## Compliance obligations — the only hard legal requirements

1. **Maintain `/CREDITS.md` as you download, not at the end.** Retro-fitting is how projects ship
   assets they cannot prove they may use.
2. **`WBP_Credits` in the shipped build must carry every CC-BY attribution** — the Incompetech
   music (row 14) and any CC-BY Freesound entries — plus font credits.
3. **`/Docs/licences/`** holds a saved copy of each licence, captured at download date.
4. **Rows 1–6, 9, 13 are Unreal-only licences** — nothing from them may be exported to another
   engine or shipped as a standalone model.
5. **Never use a `Personal` tier, non-commercial, or CC-BY-NC listing.** A publicly shown capstone
   is exactly the ambiguous case.
6. **If you cannot name the licence, do not import the asset.**

## Things the developer must not miss

1. **Step 0a — re-establish the Unreal MCP connection. Nothing else can start.**
2. **Step 0b — claim and download every A.14 asset during 25–30 July**, before the 28 days begin.
   Downloads are slow and licences must be captured at download time. Also claim **every Fab
   bi-weekly free drop** between now and 1 September even if unused — claimed items are kept
   permanently and cost nothing.
3. **`Detect Neutrals` must be checked** on both sense configs. Actors without a Team ID default to
   Neutral; leave it off and the werewolf never perceives the player and the AI looks broken.
4. **Press `P` after every level edit.** Set `Runtime Generation = Dynamic` and match
   `Agent Radius` 55 / `Agent Height` 220 to the werewolf capsule, or doorways silently generate no
   navmesh.
5. **Do not skip `Observer Aborts: Both`** on the Chase/Investigate decorators, or the wolf finishes
   its patrol walk before reacting — reads as a scripted monster, breaks Pillar 1.
6. **Step 6 is a real decision gate.** The FP-vs-TP comparison happens in week 1, and the verdict is
   written into `project-brief.md` as a new LOCKED line. It is worth ~0.5 day vs ~3–5 days of Form
   budget, so it cannot be deferred. Do **not** delete either camera before it.
7. **Step 8 fixes the werewolf capsule from the real mesh**, which then finalises A.7's grid. Import
   the character *before* blockout, not after.
8. **Step 14b packages a throwaway build in week 2 on purpose.** A first Unreal package reliably
   breaks something; this makes the reserve window repair time instead of discovery time.
9. **Re-tune `Sight Radius` at step 21**, after the finished lighting exists — AI sight range and
   human sight range must agree, or Pillar 2 fails.
10. **`List of maps to include in a packaged build` must name both `L_Title` and
    `L_Mansion_Slice`.** A map reached only via `Open Level (by Name)` is not auto-cooked and fails
    at runtime with a black screen.
11. **Every number tagged `TUNING START` is a starting value**; `LOCKED` numbers come from
    `project-brief.md` and must not change. The one to tune by feel is wolf chase speed (460)
    against player sprint (480) — keep the wolf slower by a small margin.
12. **Part A step 30 is a hard stop.** Do not start Part B until a packaged build exists and runs on
    a machine that never had the Unreal Editor installed.

## Still deliberately open

Perspective (decided at step 6, not by the designer), mansion-vs-castle, narrative (§A.18 lists the
empty sockets), and individual puzzle solutions (§C.3 is framework only).
