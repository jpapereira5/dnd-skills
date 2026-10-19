---
tags: [reference, design, oneshot]
aliases:
  - One-Shot Design
  - One-Shot Guidelines
---
# One-Shot Design

Normative spec for **standalone D&D one-shots**. Compresses [campaign_design](campaign_design.md) (Zone Blueprint + tenets) for single-session tables.

**Ship bar:** **22/22** rubric PASS — applies to **Phase 3 (portable module)** only. See Creation lifecycle.

**Authors:** Author card (design phases). **Critic / generator:** full rubric below (Phase 3).

**Default scope:** `standard` duration, 3–4 hours, level 3, 3–4 PCs. See duration tags and scaling below.

**Mode:** Most sessions run **reframe mode** (hidden truth; the signature). **Honest mode** is a first-class alternative — no concealed truth, the dilemma is open. See Session mode; reframe-dependent rubric items read differently there.

**Smell test (items 19–20):** Read landing read-aloud as a player. If the reframe is guessable — rewrite. Run the **convergence test** as its mirror: walk the clue audit as a player who missed nothing — if a diligent table can hold every clue and still not assemble the reframe, it reads as arbitrary. Target: obvious in retrospect, invisible in advance.

---

## Document map

| Layer | Governs |
|-------|---------|
| **1 — Structure** | ME1 blocks, plots, binary, discovery, shape variants |
| **2 — Table pressure** | Cheat sheet, session craft, scaling |
| **3 — Story soul** | Clues, stake, theme, humanity pass |
| **4 — Delivery** | Narration at table → [dm_profile](dm_profile.md) |

**Production:** `authoring_conventions`, `agent_conventions`

---

## Author card (one page)

Use this while writing. Critic scores the full rubric — you don't need to memorize it.

| # | Check | → Rubric |
|---|-------|----------|
| 1 | Pitch points wrong or incomplete; landing sells **contract** only | 19, 13 |
| 2 | One sentence each: what are we racing? what counts as win? | 1 |
| 3 | Reframe test + whose love/pride/guilt **caused** this? (honest mode: name the open conflict instead) | 2, 20 |
| 4 | Shape declared; ≤2 stops or one bucket; skipping changes finale | 3, 4 |
| 5 | Every fact has a clue channel; reframe over-clued 3–4 ways; red herrings don't contradict audit | 13 |
| 6 | Stake named by end of landing + **straddles both horns** (+ optional player prompt) | 14 |
| 7 | Lock = confrontation; binary costs legible; stall default + third-option priced | 5, 6 |
| 8 | One **hardest** climax — fight, trial, heist, ritual (pick one) | 11, 17 |
| 9 | Played epilogue per branch; one sensory image echoes choice | 7, 15 |
| 10 | Cheat sheet complete — stranger can run blind; wall-clock checkpoints set | 8–12, 18, 21–22 |

---

## Creation lifecycle

Default workflow for new one-shots. Separates **design conversation** from **portable documentation**.

| Phase | Where | Agent default |
|-------|-------|---------------|
| **1 — Conversation** | Chat only | Macro → micro; no vault writes unless asked |
| **2 — Design lock** | `one_shots/<slug>/design.md` | On trigger: decisions in pt-PT bullets |
| **3 — Portable module** | Source MD + runsheets | On explicit request: 22/22 + blind-GM + bilingual table |

Template for Phase 2: `one_shot_design_template` (Drive, `templates/`).

### Agent language

Per `authoring_conventions`:

- **Phases 1–2:** agent speaks **pt-PT** with João (D&D rule terms in English when standard).
- **Phase 3:** source MD (`{slug}.md` / `{gdoc_name}.md`) in **pt-PT**; **`runsheet_en.md`** + **`runsheet_pt.md`** for the table.
- **This guidelines doc:** English (reference, not playable material).

**Dashboard:** launch from vault root **`dashboard.cmd`** only — pick one-shot in browser. Do **not** create `dashboard.cmd` inside `one_shots/<slug>/`.

### Phase 1 — Conversation (default)

| Rule | Detail |
|------|--------|
| **Language** | **pt-PT** |
| **Medium** | Chat only — no vault writes unless asked |
| **Pace** | Macro → micro (ladder below) |
| **Agent** | Propose, question, stress-test; Author card + rubric as **discussion lenses**, not compliance homework |
| **Forbidden** | Part I prose, runsheet blocks, `runsheet_en.md`, `runsheet_pt.md`, critic PASS scoring, “shipping” language |

**Macro → micro ladder** (loop back on feedback; agent may use Portuguese labels in chat):

1. Pitch + player contract (wrong/incomplete ok)
2. Mode (reframe / honest) + shape + duration tag
3. Plot A — question, clock, victory sentence
4. Plot B — reframe or open conflict + human engine
5. Stakes — bonded + **straddle** both horns
6. Discovery — channels, convergence, red herrings
7. Waypoints / bucket + prep that changes finale
8. Lock + binary + stall + third-option pricing
9. Climax pillar + epilogue branches
10. Sanity pass — smell test, convergence test, false symmetry

Agent pauses for **your call** before going deeper (unless you say *continua* / “keep going”).

**Triggers (pt-PT):** *grava o design*, *guarda o design*, *bloqueia o design* → Phase 2 · *torna portátil*, *prepara o módulo*, *escreve os runsheets*, *prep completa*, *22/22* → Phase 3

### Phase 2 — Design lock (`design.md`)

**Triggers:** *save the design* · *grava o design* · *guarda o design* · *bloqueia o design*

**Output:** `one_shots/<slug>/design.md` — **decisions only**, **pt-PT**, not portable prep. No read-aloud paragraphs, statblocks, or runsheet fences.

Create folder if missing; **do not** create runsheets.

### Phase 3 — Portable module (on request only)

**Triggers:** *make it portable* · *torna portátil* · *prepara o módulo* · *escreve os runsheets* · *prep completa* · *22/22*

**Prerequisite:** `design.md` exists **or** explicit *portátil direto do chat* / “skip save, go portable from chat”

| Artifact | Language | Standard |
|----------|----------|----------|
| `{slug}.md` / `{gdoc_name}.md` | **pt-PT** | Part I + II; cheat sheet |
| `runsheet_en.md` | **EN** | Blind-GM runnable; sync from source |
| `runsheet_pt.md` | **pt-PT** | Translate from updated EN runsheet |
| `sources.yaml` | — | If gdoc-backed (no per-folder `dashboard`) |

**Ship bar:** 22/22 PASS + blind-GM — **Phase 3 only**. Sync: source MD → `runsheet_en.md` → `runsheet_pt.md`. Remind João: **`DND/dashboard.cmd`** + F5.

**Runsheet-first path:** After structure skeleton, draft cheat sheet + scenes; derive Part I memorable spine from structure rather than prose first.

---

## Duration tags

| Tag | Runtime | When |
|-----|---------|------|
| `standard` | 3–4h | Default; hub + 2 waypoints or crawl bucket |
| `extended` | 4–6h | Investigation crawl, extra hub scenes |

**Sacred blocks (trim last):** finale + epilogue, lock beat, clue that unlocks binary.

**Compress first:** hub color, optional waypoint fight, secondary NPC beats.

### Wall-clock checkpoints

The diegetic clock drives the fiction; the wall clock protects the finale. The front half **expands** at the table — investigation, social, and combat all overrun — so the failsafe guards the back, not the front. Pin two hard checks to elapsed real time and write them on the cheat sheet.

| Checkpoint | Rule |
|-----------|------|
| **Lock-by** | Lock beat must begin by ~65% of slot (≈2h40 of 4h). Behind? Fire the compressed lock beat; cut the lower-priority waypoint now — don't wait for a break. |
| **Finale-floor** | Reserve the last ~25% (≈60 min of 4h) for finale + epilogue, non-negotiable. If the front half is eating it, trigger per-scene cuts immediately. |

---

## Layer 1 — Structure

### Session mode

Declare one in Part I.

**Reframe mode.** The default and the signature. A hidden truth inverts the contract; items 2, 19, 20 apply as written. Most sessions live here.

**Honest mode.** A first-class output, not a waiver exception. No concealed truth — the dragon is a dragon, the conflict is what it looks like. The impossible choice still bites, but it derives from open conflict (value, loyalty, method, sacrifice) rather than a reveal. Items 2/19/20 PASS via the **honest-mode substitute**: the central conflict and its costs are named up front, and the binary still holds (legible costs, straddling stake, stall default). Why ship it on purpose: a regular table's *assumption* of a twist is what lets them pre-solve the next one. An honest session resets the prior and makes the following reframe land at full force. The occasional straight session is the strongest protector of the twisted ones.

### Five-block model (baseline)

| Block | Time (`standard`) | Job |
|-------|-------------------|-----|
| 1 — Landing | 20–35 min | Strong start; contract or open conflict (mode); bonded stake |
| 2 — Waypoint 1 | 30–40 min | Bang, clue, prep reward |
| 3 — Waypoint 2 | 25–35 min | Bang, clue; place-as-clue or alt route |
| 4 — Lock | 15–20 min **or lock beat** | B reframe; point of no return; safety-net |
| 5 — Finale + epilogue | 50–65 min | Binary; clock resolves; symbolic epilogue echo |

**Lock beat vs lock block:** A lock **beat** is a 2–5 minute transition (door seals, lamp leaves, poem begins) inside a scene. A lock **block** is a dedicated scene. Either satisfies the rubric.

### Shape variants

Map blocks to scenes without changing rubric intent.

| Shape | Block mapping | Waypoint rule |
|-------|---------------|---------------|
| **Standard** | Landing → WP1 → WP2 → Lock → Finale | ≤2 waypoints |
| **Crawl** | Landing → **exploration bucket** (one arc, many rooms) → Lock beat → Finale | 1 bucket replaces WP1+WP2 |
| **Social** | Landing hub → **escalation in place** → Lock → Finale | Clues and prep inside hub |

**Clock flexibility:** Social and crawl shapes may use **soft ticks** (relationship shift, discovery threshold) instead of only countdown — still ≤3, still diegetic.

### Three audiences (Part I)

| Audience | Rule |
|----------|------|
| **Pitch** (players) | No reframe spoil |
| **Hook** (DM) | May hint contradiction |
| **Secret** (DM only) | Never spoken by landing NPCs |

### Strong start

In medias res — conflict visible in first 5 minutes. No regional history lecture. Contract before complete theory.

### Plot A

- Dramatic question (one sentence)
- **Clock** — named driver; **≤3 ticks**; **diegetic** (announced at table)
- **Victory sentence:** *"Win = [objective], not annihilation"*
- Resolves this session

### Plot B (all three)

1. **Helps A** — changes finale state if resolved
2. **Mystery → A** — **Reframe Test:** *"We thought ___, but actually ___."* (honest mode: B deepens the open conflict instead of inverting it)
3. **Moral weight** — grey morals; defensible sides

**B ↔ A types:** same enemy different face · solution is the problem · helper complicit · victim is the key · **the catastrophe is already past (you're in the aftermath, not the prevention)** · **the party is the unwitting cause**

**Human engine:** One intimate act — love, pride, guilt, protection — **caused** the crisis. Name it in Part I. *e.g. a protective gesture that accidentally fed the curse.*

Without a human engine, grey morals stay abstract.

### Waypoints / exploration bucket

- Prep changes finale if skipped
- ≥2 approaches (fight / talk / sneak → same prep, different complication)
- **Place-as-clue:** location mechanics teach reframe (e.g. guardians dying to protect the "victim"; bodies beside the true source)

### Binary (finale only)

- Neither option ideal; costs **legible before** choice
- **Personal and political** (Tenet 1)
- **Stall default** written in prep (template below)
- Foregone combat: vary **how**, don't fake a second binary

**Impossible-choice taxonomy** (pick primary; optional undertone):

| Type | Structure |
|------|-----------|
| Value | Two goods that exclude each other |
| Loyalty | Two sides you care about, opposite needs |
| Method | Same goal, incompatible approaches |
| Sacrifice | Success costs something precious |
| Knowledge | Now you know — you must act |

**Cost textures:** Practical · Moral · Identity

**Straddle check.** The bonded stake must pull toward **both** horns. If the PC is bonded to only one side, the "impossible" choice is easy — pick your side. Bind the stake to both, or the dilemma collapses into a values-preference (the table picks their value and feels nothing). Legible costs are for fairness; the straddle is what makes them hurt.

**Third options.** Tables attack the frame — invent a third path, refuse both horns, try for neither or both. Honour the attempt; it's the agency the binary exists to provoke. But the third option must carry its own legible cost, or it's a strictly-dominant escape and the binary becomes a false binary relocated. Let them have it — and let it cost. If you can't price it honestly on the spot, the clock and the stall default are your levers: the world moves while they improvise.

**Stall default template:**
```
IF TABLE FROZEN [N] ROUNDS AT BINARY:
 - World action: [clock tick / ritual advances / NPC acts]
 - Forced state: [worse branch — not TPK]
 - Last chance: [one line from environment or NPC]
```

### Moral trap

Systemic reward for ugly play without blocking heroic play — never underlined at table. Not a second binary.

*e.g. a posted bounty that pays for the wrong kind of violence while the truth demands mercy.*

**Waiver:** If no trap fits, document in Part I: *"No systemic ugly reward — pressure is clock and binary only."*

### Table-split

Document in Part I two **defensible** positions the table might take after the reframe — each with why a reasonable player would choose it. Critic checks presence, not which side wins.

- Document **power**: who has leverage, who doesn't — critic fails **false symmetry** (both sides equally "right" when one party is coerced or erased).
- **Likely split** in Part I is enough for prep; **emergent split** at table is PASS if two defensible positions appeared and costs were **legible before commitment**.

*e.g. destroy the stolen beacon vs reignite it for the coast — both with named costs.*

### Discovery — four channels

| Channel | Delivers |
|---------|----------|
| Objects | Letters, diaries, posters |
| Environment | Absence, decay, wrong state |
| Behavior | Flinch, lie, unexpected care |
| Overheard | Rumors, gossip |

**Prep checkpoint:** Per *supporting* fact, assign 1–2 channels. The **keystone reframe is the exception** — clue it 3–4 ways on purpose so a missed scene can't kill the reveal (three-clue rule). The failure isn't breadth, it's narration: if the *DM states* a fact outright instead of letting a channel deliver it → redesign.

**Codex:** Optional depth; never mandatory for completion.

**Clue audit line:**
```
[B-MYSTERY] fact → channel(s) → scene → finale impact
```

Default **2+1** clues (3+1 investigation). **Gumshoe:** required conclusions never behind a single failed roll.

**Red herrings:** May misdirect; must not contradict the clue audit. Critic auto-fails contradictions.

**Don't sell the twist:** Landing NPCs voice **contract theory** only. Critic auto-fails if secret appears in landing read-aloud.

**They never lied:** Antagonists and allies can be truthful within their frame; tragedy is structural, not gotcha betrayal. See Tenet 5 in [campaign_design](campaign_design.md).

### Consequences

| Tier | When |
|------|------|
| Immediate | Same scene |
| Delayed | Same-session epilogue — played scene |

Optional one-line campaign hook. Multi-session echoes: [campaign_design](campaign_design.md) Tenet 3.

**Invisible reputation (one-shot):** Epilogue shows consequence through NPC behavior, access, or environment — never announced as a score. See Tenet 3 in [campaign_design](campaign_design.md).

---

## Layer 2 — Table pressure

Lives on **DM cheat sheet** and runsheet `dm` notes — not narrative prep prose.

| Item | Rule |
|------|------|
| Bang or breath per block | Forced decision in first 5 min **or** deliberate held breath (escalation without new menu) |
| Lock | Confrontation, not briefing |
| Bypass clause | Skip hub: how, penalty, compressed B |
| Fail-forward | Success + complication on every gate |
| Contingencies ×3 | Document on cheat sheet |
| Secrets ×5 | Droppable; distinct from B-mystery |
| Flags ×3–5 | Booleans |
| One decisive climax | Hardest beat of session; waypoints skippable; optional early lesson fight |
| Three pillars | Social + exploration + combat **present and reachable with stakes** — combat needn't be the climax or be forced |
| Endure don't grind | Win ≠ kill everything |
| Statblocks | `creature_ref` + skin + climax trait on boss + `creatures:` |
| Prep surface | Read-aloud/scene; explicit DCs (moderate band 10–15); foreshadowing map |
| Time cuts | Per-scene trim list + wall-clock checkpoints (lock-by, finale-floor) |

### Endure, don't grind

| Avoid | Target |
|-------|--------|
| Clear all spawns to win | Complete objective under clock |
| Timer = TPK | Timer = worse state |
| Failed check blocks | Failed check costs time |
| Infinite waves | Finite pool |

**Pressure valve** on cheat sheet.

### Scaling (3 / 4 / 5 PCs)

| PCs | Typical adjustment |
|-----|-------------------|
| 3 | Reduce enemy count ~25%; keep the clock tight enough to preserve the squeeze — don't ease numbers *and* clock or the finale goes trivial |
| 4 | As written |
| 5 | Add a minion or a turn (action economy) and/or +1–2 climax save DC; tighten clock start. Avoid flat boss HP — it lengthens the fight and eats finale time without raising threat. Don't add puzzle steps |

**Resource-aware climax:** Read finale difficulty by slots and HP burned, not headcount alone.

**Preserve the squeeze:** Scale to hold finale pressure constant across party sizes, not to keep the fight winnable. A smaller party should feel the clock as hard as a larger one.

### Templates

**Bypass:**
```
IF PARTY SKIPS HUB:
 - Reachable via: [how]
 - Penalty: [missing prep]
 - B reveal: compressed at lock
 - No invisible walls
```

**Flags:** `waypoint_1_prep` · `waypoint_2_prep` · `b_mystery_known` · `binary_path` · `ending`

### Session craft checklist

Quick author tick-list keyed to the rubric — scoring lives there (items 8–12, 17), not here.

- [ ] One decisive climax; waypoints skippable
- [ ] Three pillars present with stakes
- [ ] Victory sentence + pressure valve
- [ ] Fail-forward on gates
- [ ] `creature_ref` + `creatures:` registered
- [ ] Read-aloud per scene; foreshadowing payoffs named
- [ ] Clue audit complete
- [ ] Wall-clock checkpoints set

### Blind-GM test

A stranger DM can run the session from **runsheet + cheat sheet** without reading Part II prose. If not → enrich runsheet, not prep novella.

---

## Layer 3 — Story soul

| Item | Rule |
|------|------|
| Fair-play clues | 2+1 or 3+1; channel audit |
| Bonded stake | PC or NPC hook by end of landing; **straddles the binary (pulls toward both horns)**; optional player stake prompts at landing |
| Theme | One sentence in Part I — for prep, not sermon at table |
| Anchor motifs | 3 named sensory images + scene citations in Part I |
| Denouement | 5–10 min played per branch; sensory anchor each |
| Symbolic echo | Object, board, or line ironic to choice — pays off theme without stating it |
| NPC cap | ≤4 plot NPCs (stake, mystery, antagonist, ally) |
| Humanity pass | See glossary |

**Player stake prompts (optional at landing):** *"Who do you protect?"* · *"What won't you do for gold?"*

**Recruitable NPC:** May join; not a DMPC — no spotlight theft, no solving the binary for the party.

**Treasure:** Thematic loot; no mandatory magic item to pass.

### Session craft

Scoring lives in the rubric (items 8–12, 17) and the operational inventory in Layer 2. Not restated here — one source of truth.

---

## Layer 4 — Delivery

Structure is this doc. **Narration:** [dm_profile](dm_profile.md). **Combat flavor:** `combat_reference`.

| Moment | Habit |
|--------|-------|
| Scene entry | Progressive disclosure |
| Locations | Architecture-first; function |
| NPCs | External-first; gesture on reveals; distinct voice |
| Binary | Silence and pause before world reacts |
| Epilogue | Fade on emotional beat |

**Delivery checks (rubric item 18):** read-aloud per scene · no lore monologue opens · progressive disclosure in first paragraph · mechanics at point of use.

---

## Rubric — 22 items

**PASS** = ship. **PARTIAL** = run with friction; enrich before reuse. **FAIL** = redesign.

**Scope:** Applies to **Phase 3 (portable module)**. During Phases 1–2, use items as **review prompts** only — do not score for ship.

**Mode note:** Items 2, 19, 20 assume **reframe mode**. In **honest mode** (declared in Part I / `design.md`) they PASS via the honest-mode substitute — open conflict and costs named up front, binary still biting. Honest mode is a first-class output, not a waiver.

### Structure (7)

| # | Item | PASS | PARTIAL | FAIL |
|---|------|------|---------|------|
| 1 | Plot A + clock | Question + named driver + ≤3 diegetic ticks + victory sentence | Clock exists but not announced at table | No clock or no bad default |
| 2 | Plot B | Reframe test + helps A + moral weight + B↔A type named (honest mode: open conflict deepened, not inverted) | B helps A weakly (lore only) | No reframe/conflict or B optional |
| 3 | Waypoints / bucket | Shape declared; skipping changes finale; ≤2 WPs or 1 crawl bucket | Extra stop without finale impact | Fetch waypoint |
| 4 | Prep / alt route | ≥1 waypoint with 2+ approaches or alternate route | One approach only | Railroad single path |
| 5 | Lock | Confrontation or lock beat + safety-net if clues missed | Safety-net is lore dump | No point of no return |
| 6 | Binary | One finale binary; taxonomy; 3 cost textures; **stake straddles both horns**; stall default + third-option priced | Obvious best option, or stake binds one side | False binary or mid-adventure second binary |
| 7 | Denouement | Played scene per branch; sensory anchor + symbolic echo each | Handout-only ending | No epilogue |

### DM craft (5)

| # | Item | PASS | PARTIAL | FAIL |
|---|------|------|---------|------|
| 8 | Bangs or breath | Decision in first 5 min of each block **or** deliberate held breath | One block with neither | Two+ blocks without bang or breath |
| 9 | Bypass | Documented skip-hub clause | Penalty vague | Invisible wall |
| 10 | Fail-forward / endure | Every gate; victory ≠ kill all; pressure valve | Some gates hard-stop | Grind or TPK clock |
| 11 | Climax / approaches | One decisive climax (any pillar); waypoints skippable | Extra mandatory grind beat | Combat crawl or padded finale |
| 12 | Cheat sheet | 3 contingencies + 5 droppable secrets + flags + wall-clock checkpoints on sheet | On prep only, not runsheet | Missing |

### Literary (6)

| # | Item | PASS | PARTIAL | FAIL |
|---|------|------|---------|------|
| 13 | Clues + channels | 2+1 audit; supporting facts 1–2 channels, reframe over-clued 3–4; gumshoe; no twist in landing | One clue roll-gated | Exposition dump |
| 14 | Bonded stake | Named by end of landing; one played beat landing→lock; **straddles the binary**; in binary + epilogue | Stake appears late, or binds one side only | Abstract stakes only |
| 15 | Theme + motifs | Theme in Part I + (3 anchor motifs with cites **or** symbolic echo in epilogue) | Theme only, no motifs or echo | No theme |
| 16 | NPC cap | ≤4 plot NPCs | 5 plot NPCs | Name soup |
| 17 | Pillars + no fetch | Social + exploration + combat present with stakes (combat reachable, not necessarily climax or forced); no fetch quests | Missing one pillar | Fetch-only |
| 18 | Humanity + delivery | Passes glossary auto-fail; delivery checks | Review flags only | Auto-fail triggered |

### Memorable spine (4)

| # | Item | PASS | PARTIAL | FAIL |
|---|------|------|---------|------|
| 19 | Inverted contract | Pitch wrong or incomplete; truth only via clues, and clues **converge** on the reframe (not merely permit it) | Pitch hints reframe; or clues permit but don't converge | Pitch or landing spoils secret |
| 20 | Human engine | Named intimate act caused crisis in Part I (honest mode: named open cause) | Implied but not named | Abstract factions only |
| 21 | Table-split | Two defensible positions + power noted **or** emergent split with legible costs | One position documented | False symmetry; obvious binary |
| 22 | Moral trap or waiver | Systemic ugly reward **or** documented waiver in Part I | Trap exists but underlined at table | Neither trap nor waiver |

**Scoring:** 22/22 PASS to ship (Phase 3 only) · any PARTIAL = enrich before reuse · any FAIL = redesign

**Table override:** If players leave arguing the choice and felt heroic struggle at the table, document emergent items (esp. 21) — does not waive Phase 3 portable requirements when building the module.

---

## Rubric ↔ runsheet mapping

| Rubric # | Runsheet / Part I location |
|----------|----------------------------|
| 1 | `clock` frontmatter · ` ```clock` block · scene `duration` |
| 2 | Briefing secret · Part I reframe |
| 3–4 | ` ```scene` blocks · `if_then` · `check` |
| 5 | Lock transition `read_aloud` · `note` |
| 6 | ` ```choice` · stall + third-option pricing in `dm` note |
| 7 | ` ```scene` epilogue · per-branch `read_aloud` |
| 8 | First `read_aloud` or `check` per scene |
| 9 | Briefing bypass `dm` section |
| 10 | `on_fail` on checks · victory sentence in Briefing |
| 11 | Climax ` ```combat` **or** hardest-beat ` ```scene` / ` ```choice` with flag in `dm` note |
| 12 | Cheat-sheet `secret` / `note` blocks + wall-clock checkpoints |
| 13 | ` ```clue` blocks · clue audit in Part I |
| 14 | ` ```npc` in landing scene |
| 15 | Part I theme + motif list |
| 16 | Elenco cast count |
| 17 | Scene `objective` names finale impact |
| 18 | Glossary + read-aloud per scene |
| 19 | Pitch vs secret in Part I; landing read-aloud |
| 20 | Part I human engine paragraph |
| 21 | Part I table-split section |
| 22 | Briefing `secret` moral trap or Part I waiver |

---

## Critic glossary

| Term | Definition | Auto-fail? |
|------|------------|------------|
| **Fetch quest** | Retrieve X; X doesn't change finale tactics | Yes |
| **False binary** | One option dominates on practical + moral grounds | Yes |
| **Quantum ogre** | NPC reacts the same regardless of approach | Yes |
| **Name soup** | >4 plot NPCs players must track | Yes |
| **Lore monologue** | DM narrates backstory block unprompted | Yes |
| **Twist in scene 1** | Secret stated by landing NPC | Yes |
| **Red herring contradiction** | Herring disproves an audited clue | Yes |
| **False symmetry** | Table-split treats unequal power as two equal "rights" | Yes |
| **Non-converging clues** | Clues permit the reframe but no diligent player would assemble it | Review |
| **Generic bandits** | Combat without location or moral tie | Review |
| **Rescue-victim trope** | "Victim" has no agency in binary or epilogue | Review |
| **3-paragraph read-aloud** | Scene opener too long | Review |
| **Identical waypoints** | Same structure twice in a row | Review |

---

## Out of scope (explicit)

| Topic | Note |
|-------|------|
| **Music / maps** | Table assets; not scored |
| **Full Tenet 7 PC arcs** | Campaign; binary identity texture only |
| **Campaign consequence tracker** | Optional hook only |
| **Per-group reframe tracking** | Deferred — adopt only if a group starts pre-solving the twist; the session index already supports it. Honest mode is the standing mitigation. |

### Safety

- **Public tables:** lines/veils at start (`cena_dnd_lisboa` notes community norm).
- **Human engine:** When prep involves intimacy, coercion, or vulnerable NPCs — note themes in Part I; offer fade-to-black; no surprise harm in read-aloud.
- Other safety tools: DM discretion; not scored in rubric.

### Optional appendices (not in rubric)

- **Pre-gens:** 3–4 L3; role spread; no session-zero required
- **Genre modifiers:** investigation +1 clue; horror faster clock; comedy lighter moral weight
- **Phase classifier:** `conversation` (chat only) · `design_locked` (`design.md` exists) · `portable` (full module requested)

---

## When to read upstream

| Task | Open |
|------|------|
| Tenets, faction test, impossible-choice types | [campaign_design](campaign_design.md) |
| Voice, progressive disclosure, object exposition | [dm_profile](dm_profile.md) |
| Combat narration | `combat_reference` |
| Runsheet blocks, NPC tiers, dashboard | `agent_conventions` |
| pt-PT source, sync order | `authoring_conventions` |

---

## Output artifacts

| Phase | Artifact | Contents |
|-------|----------|----------|
| **2** | **`design.md`** | pt-PT decisions — pitch, secret, mode, shape, blocks sketch, binary, open questions |
| **3** | **Part I** (source MD) | Full briefing: mode, shape, theme, motifs, clue audit, human engine, table-split (power), binary (straddle + third-option), stall, flags, moral trap or waiver |
| **3** | **DM cheat sheet** | Clock ticks, wall-clock checkpoints, flags, victory sentence, pressure valve, contingencies |
| **3** | **`runsheet_en.md`** | Scenes, checks, choice, clues — blind-GM runnable |
| **3** | **`runsheet_pt.md`** | Portuguese table — translate from EN runsheet |

**Not in one-shot folder:** `dashboard.cmd` — use vault root `dashboard.cmd`.

---

## Generator / enrich pipeline

1. **Detect phase** — `conversation` / `design_locked` / `portable`
2. If **conversation** → macro→micro ladder (pt-PT); stop unless asked to save
3. If **design_locked** → update `design.md` only (pt-PT)
4. If **portable** → structure (mode, shape, A → B + human engine → waypoints → lock → binary straddle + third-option)
5. **Discovery** — channel audit (reframe over-clued); don't-sell-twist; convergence check
6. **Memorable spine** — table-split, moral trap or waiver, motifs
7. **Cheat sheet** — flags, bypass, contingencies, secrets, wall-clock checkpoints
8. **Critic** — 22-item rubric + glossary (mode-aware)
9. **Delivery pass** — Layer 4
10. **Blind-GM test**
11. Emit source MD (pt-PT) + `runsheet_en` + `runsheet_pt`

**Enrich priority (portable):** memorable spine (19–22) → cheat sheet → stall default → bypass → lock beat

---

*Standalone one-shot design spec. Upstream: [campaign_design](campaign_design.md).*
