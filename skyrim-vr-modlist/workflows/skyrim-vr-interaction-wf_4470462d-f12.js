export const meta = {
  name: 'skyrim-vr-interaction',
  description: 'Collect MISSING Skyrim VR interaction/interactivity mods (hands, physical objects, combat, magic, world/NPC interaction, VR UI, locomotion/comfort, haptics) from the 27 popular lists + web, double-verify for VR, consolidate against the Core and Other lists, completeness critic',
  phases: [
    { title: 'Collect', detail: '7 topic agents, every candidate gets a disposition' },
    { title: 'Verify', detail: 'VR-compat skeptic + value/redundancy skeptic per topic' },
    { title: 'Consolidate', detail: 'dedup vs Core/Other, groups, conflicts, order' },
    { title: 'Critic', detail: 'what is still missing' },
  ],
}

const D = (args && args.root) || 'skyrim-vr-modlist'
const ONLY = (args && args.only) || null

const SECTIONS = ['ix_hands', 'ix_combat', 'ix_magic', 'ix_world', 'ix_ui', 'ix_locomotion', 'ix_feedback', 'ix_dont']
const SEC_RU = 'ix_hands=hands, grabbing, physical objects, holsters/wearables; ix_combat=VR combat interaction (blocking, archery, melee, parry, dodge, throwing); ix_magic=spellcasting/shouts/hand magic interaction; ix_world=interaction with world/NPCs/containers/crafting/doors/lockpicking/reading; ix_ui=VR-native UI, menus, quick loot, inventory, dialogue, crosshair, keyboard, map/compass in hand; ix_locomotion=locomotion, comfort, crouch/sit/lean, climbing, swimming, riding; ix_feedback=haptics/controller feedback/audio-visual feedback of interactions; ix_dont=do NOT install in VR'

const CONTEXT = `
Project: a Skyrim VR modlist (Skyrim VR 1.4.15, SKSEVR 2.0.12, MO2, VRIK + HIGGS + PLANCK physics stack). Today 2026-10-09. Two lists already exist:
 (1) "Core 2026" (inventory: ${D}/MODLIST.md, ${D}/data/page_items.txt, ${D}/tools/additions.py) — it already contains the VR interaction backbone: VRIK Player Avatar (+Arctal's VRIK Tweaks, Neutral VR Animations, VRIK Closed Fist), HIGGS, PLANCK (+VR Stability Patch), Physical Collision VR, Interactive Activators VR, Interactive Waters VR (beta), Gift by Hand VR, Magic Sneak Attacks VR + Physical Dodge VR, True Wield VR, Immersive Weapon Penetration VR, etc. READ MODLIST.md (grep VR, HIGGS, PLANCK, VRIK, physical, interactive, hand) to know exactly what is there.
 (2) "Other Mods 2026" first pass (inventory: ${D}/OTHER_MODS.md) and a second pass in progress (${D}/data/partial/other-mods__collect_r2-*.json, may be incomplete).
Do NOT re-propose anything already in them; if a candidate duplicates/extends a listed mod, say which and whether it adds value on top.
THE ASK (from the owner): "collect the MISSING mods for interactivity and interaction in VR". Goal: everything that makes Skyrim VR feel physically interactive — hands, grabbing/throwing/carrying, holstering, wearing, physical combat (blocking/parry/dodge/archery/two-handed), hands-on spellcasting, world/NPC/container/crafting/lockpicking interaction, VR-native UI and menus, comfort/locomotion/body presence, haptics — that is VR-relevant, works in Skyrim VR 1.4.15, and is NOT yet in the lists.
EXCLUDED entirely: quest/new-land content, followers as characters, player homes, big difficulty overhauls (Requiem, Wildlander, Ordinator, Vokrii), spell/shout packs (Apocalypse, Odin, Arcanum, Triumvirate, Thunderchild), narrow SimonRim parts (Aetherius, Scion, Manbeast, Pilgrim), NSFW (OStim etc.). ENB-only things are useless (no ENB here). Textures/appearance are a separate stage.
Data: ${D}/data/rep/*.json = archive lists of 27 popular Wabbajack lists (9 VR: Yggdrasil VR, Stormcrown VR, Panda's Sovngarde, Librum VR, Tahrovin, Tahrovin - Grit, Spirit of Grit, Tempus Maledictum VR, FUS; 18 SE next-gen). Helper: python3 -I ${D}/tools/whouses.py <nexus id or name> → which lists use it + exact archive file names (which FILE VARIANT the VR lists pick, VR patches). CANDIDATE POOL (modded names that appear in >=1 VR list and look interaction-related; noisy): ${D}/data/pools/vr_interaction.txt — scan ALL of it for your topic; it is NOT exhaustive: also use your own knowledge of the Skyrim VR modding scene and web searches (Skyrim VR subreddits/Steam/GitHub/Nexus search snippets; Nexus pages are BLOCKED for fetch — use search snippets, GitHub, Reddit mirrors) for VR interaction mods that no list ships yet (HIGGS/PLANCK add-ons, VR ports of flat mods, GitHub-only VR mods, 2025-2026 releases).
VR rules: SKSE DLLs need a VR build (a file or page that says VR, or "SE/AE/VR" from the author); no-DLL plugins/assets work in VR; Engine Fixes VR 7.x, VR Address Library, SKSEVR 2.0.12 are in the base. Conflict checks that matter: HIGGS/PLANCK/VRIK/CBPC collisions, OAR/Pandora animation replacers, Engine Fixes patches, SkyUI VR, True Wield/Dual Wield mods. Never invent file names, FOMOD options, versions or VR status; evidence required (list names + archive file names from whouses, or URLs/snippets). Human-facing text in RUSSIAN, short.
Quality bar: curated "recommended extras for VR interaction", not a dump. Prefer mods VR lists actually ship (esp. 2026), plus strong VR-native releases with real user evidence; mark unproven ones "try". Think about each mod's interplay with HIGGS/PLANCK/VRIK (does it duplicate, replace or conflict?).`

const PICKS = { type: 'object', properties: {
  picks: { type: 'array', items: { type: 'object', properties: {
    key: { type: 'string', description: 'id:<nexus id> or n:<normalized name> when no id' },
    id: { type: ['integer', 'null'] }, name: { type: 'string' }, url: { type: 'string' },
    section: { type: 'string', enum: SECTIONS }, tag: { type: 'string', enum: ['rec', 'opt', 'alt', 'try', 'dont'] },
    choose_one_group: { type: ['string', 'null'] },
    what: { type: 'string', description: 'RU <=170 chars: what it does in VR' },
    vr_status: { type: 'string', enum: ['works_as_is', 'vr_version_exists', 'vr_native', 'flat_only', 'unknown'] },
    in_lists: { type: 'string', description: 'which of the 27 lists ship it (names), "none" if no list' },
    files: { type: 'string', description: 'RU: exact file/variant/version the VR lists pick or the author provides' },
    requires: { type: 'array', items: { type: 'string' } },
    interplay: { type: 'string', description: 'RU: relation to HIGGS/PLANCK/VRIK/Physical Collision VR and other Core mods: duplicates? conflicts? needs patch? load order?' },
    note: { type: 'string', description: 'RU: VR caveats, settings to change (INI keys only if evidenced), test advice' },
    evidence: { type: 'string' },
  }, required: ['key', 'id', 'name', 'url', 'section', 'tag', 'choose_one_group', 'what', 'vr_status', 'in_lists', 'files', 'requires', 'interplay', 'note', 'evidence'] } },
  considered_dropped: { type: 'array', description: 'EVERY pool/web candidate you looked at and rejected — nothing silent', items: { type: 'object', properties: { id: { type: ['integer', 'null'] }, name: { type: 'string' }, reason: { type: 'string', description: 'RU one line: already in Core/Other (which), flat-only, superseded by, excluded category, low value...' } }, required: ['id', 'name', 'reason'] } },
  section_lead: { type: 'string', description: 'RU 1-2 sentences: how to approach this area in VR and what the base (HIGGS/PLANCK/VRIK) already covers' },
  notes: { type: 'string', description: 'RU: unverified items, what to check locally on Nexus' },
}, required: ['picks', 'considered_dropped', 'section_lead', 'notes'] }

const VERDICTS = { type: 'object', properties: { verdicts: { type: 'array', items: { type: 'object', properties: {
  key: { type: 'string' }, keep: { type: 'boolean' }, section: { type: 'string', enum: SECTIONS }, tag: { type: 'string', enum: ['rec', 'opt', 'alt', 'try', 'dont'] },
  choose_one_group: { type: ['string', 'null'] }, what: { type: 'string', description: 'RU polished one-liner <=170' }, note: { type: 'string', description: 'RU corrected VR/file/conflict note' }, reason: { type: 'string' },
}, required: ['key', 'keep', 'section', 'tag', 'choose_one_group', 'what', 'note', 'reason'] } } }, required: ['verdicts'] }

const LENSES = [
  { key: 'vr-compat', prompt: 'You are a VR-COMPATIBILITY SKEPTIC. Try to refute each claim: SKSE DLL without a VR build, flat-only, depends on an SE-only framework, hooks that fight HIGGS/PLANCK/VRIK (grab/collision/animation), needs first-person/third-person camera behavior VR lacks, uses a mouse/keyboard UI. Check with whouses.py file names (does any VR list ship the VR file?) and quick searches. Unproven but plausible → keep with tag "try" and a note on how to test. Wrong → keep=false (or tag "dont" if people would copy it).' },
  { key: 'value-perf', prompt: 'You are a VALUE / REDUNDANCY / STABILITY SKEPTIC. Try to refute each item: duplicates or is superseded by something already in Core/Other (read ${D}/MODLIST.md and ${D}/OTHER_MODS.md) or another pick, trivial cosmetic tweak, outdated vs a 2025-2026 option, script-heavy/risky (save-bloat, CTD reports), falls into an EXCLUDED category, or would conflict with the HIGGS/PLANCK/VRIK stack. Enforce choose_one groups. Assign best section and tag and write the final RU one-liner and note. Be strict: a short, strong list beats a long one.' },
]

const TOPICS = [
  { key: 'hands-objects', sec: 'ix_hands', prompt: 'TOPIC 1 — hands and physical objects: grabbing/throwing/carrying/dropping objects beyond HIGGS defaults (More Interactive Objects - Throwing Things VR port, Physical Torch Lighting VR, throwable weapons), two-handed weapon grip and weapon-stance mods (Dead Weight VR, VRIK weapon offsets), holsters/sheathing/wearables on the body (VR holsters, IED status in VR, quivers, backpacks, wearable lanterns and their VR patches, potions/ingredients on the body: VR Equip Potions And Ingredients), hand models/closed fist/gloves, HIGGS/VRIK add-ons and config presets that the lists ship.' },
  { key: 'combat', sec: 'ix_combat', prompt: 'TOPIC 2 — physical combat interaction: blocking (Dual Wield Block VR, Blocking and Flash VR, Shield of Stamina VR, Fixed Bound Sword/Dagger Collision), parry (Pseudo Physical Weapon Collision and Parry — the AE SE VR build and the config/tweaked variants), archery/crossbows in VR (Simple Realistic Archery VR and its fixes, sighted crossbows + iron sights VR, MArc Muken\'s Arcane Archery, VR Bound Bow FX), melee impact and locational damage (Locational Damage SKSE VR), hand-to-hand (Adamant Hand to Hand VR DLL and tweaks), power attacks in VR, dodge (Crouch To Dodge VR, Physical Dodge VR already in Core), grapple/pull (GRAPPLE VR), combat AI/combo mods that have VR builds (SCAR VR, BFCO Attack Behavior Framework), QTE VR Framework (+music pack), stamina/attack-cost mods with VR patches, Fake Edge VR.' },
  { key: 'magic', sec: 'ix_magic', prompt: 'TOPIC 3 — hands-on magic: spellcasting gestures and hand FX (3D Casting FX - Fire and Frost Hand FX Replacer, SpellBender VR, SkyrimVR Strange Runes - Spellcasting Enhanced, Elemental Fury VR, Enhanced Invisibility VR, Enchantment Art Extender VR), staff/spell physical interaction, shouts by voice (Dragonborn Speaks Naturally and VR-specific voice-shout mods; conflicts with the AI-NPC microphone), spell-casting aids (magelight/candlelight VR fixes — Rally\'s Candlelight and Magelight Fix SE - VR), spell selection by gesture or wrist menus, magic-targeting aids for VR (crosshair/lock-on), concentration/dual-casting fixes with VR builds. Exclude new spell packs.' },
  { key: 'world-npc', sec: 'ix_world', prompt: 'TOPIC 4 — interaction with world, NPCs, containers and crafting: physical knocking and doors (Physical VR Knocking - Simply Knock), lockpicking and pickpocket in VR (Pickpocket Reset - VR, Security Overhaul SKSEVR parts: Lock Variations VR — judge whether it is "interaction" or content), reading/books and diaries (Dear Diary VR variants), NPC poses/ragdoll (Simple NPC Poser and Ragdoller for VR and SE), NPC reactions to physical touch, container/loot interaction, crafting stations and hands-on smithing/alchemy/cooking (Campfire VR, Realistic Mining for VR, Immersive Tree Chopping VR, Wade in Water VR if it fits), gesture-based dialogue (VR Smooth Dialogue Mesh, Transparent Dialogue VR), mount/horse interaction, carriage, sitting on furniture. Skip anything that is quest content.' },
  { key: 'vr-ui', sec: 'ix_ui', prompt: 'TOPIC 5 — VR-native UI and menus: quick loot (Quickloot VR), inventory/favorites for VR (moreHUD Inventory Edition VR, Edge UI - VR Edition, Dear Diary VR - Paper SkyUI and Categorized Favorites, VR Equip menus), subtitles (Subtitles VR, Floating Subtitles in Core), crosshair/cursor (Eagle Eye Cursor Replacer for Skyrim VR, Crosshairs with different colours VR), message boxes (Centered Messages Box VR), wrist/hand menus and in-hand map/compass (Navigate VR family is in Other-1: only add-ons), virtual keyboard (VR Keyboard is in Core), mouse-menu fixes (VR Menu Mouse Fix), controller remapping and binding presets (Controller Fix VR, Alternate Oculus Vanilla Bindings, Narsil Bindings, Oculus Controller Remapping Tool), RaceMenu VR layout/position fixes, loading-screen/hand UI helpers. Check what Core/Other-1 already have so you only add the missing ones.' },
  { key: 'locomotion', sec: 'ix_locomotion', prompt: 'TOPIC 6 — locomotion, comfort and body presence: roomscale/physical crouch and sit (crouch/sneak mods, VRIK crouch settings, lean), climbing and ledge-grabbing in VR, swimming and wading (Wade in Water VR), riding (horse/mount VR mods), teleport/smooth locomotion options, comfort mods (vignette, snap turn, no-movement-blur), Natural Locomotion integration (Other-1 has it as niche), Virtual Reality General Enhancements, Small VR Fixes, Skyrim VR Configuration Tool presets, fast-travel/map handling for VR (Disable Fast Travel SKSEVR), world-scale/player-scale tweaks (Creatures Resized for VR, Food Resized, VR Refit family — check Other-1 first).' },
  { key: 'feedback', sec: 'ix_feedback', prompt: 'TOPIC 7 — feedback and presence: haptics/controller vibration for hits, spells, bows, blocking, grabbing (HIGGS haptic settings, bHaptics integrations, other vibration mods for Skyrim VR), audio feedback of physical interaction (impact/collision sounds for hands and weapons, footsteps on surfaces, hand-contact sounds), visual feedback of interactions (hit flash/blood — Wash That Blood Off 2 VR, Blocking and Flash), body-presence extras (Vampire Body for VR, Werewolf Body for VR — check Other-1), AnimObject Swapper VR, Immersive VR transformations (Yelling At The Sky - Immersive VR Transformations), Sacrilege Vampire Lord VR fix, Fuz Ro D-oh VR, plus any "VR general enhancements" that fit no other topic and are interaction-relevant.' },
]

const list = TOPICS.filter(t => !ONLY || ONLY.includes(t.key))

async function collect(t) {
  const prompt = `${CONTEXT}\n\nSection codes: ${SEC_RU}.\n\nYOUR TASK (${t.key}): ${t.prompt}\nScan the whole pool file for your topic (grep/sed in chunks), run whouses.py for promising ids, then search the web for VR interaction mods of this topic that no list ships. Return up to 40 picks with evidence (default section ${t.sec}; use others when a mod fits better). Return EVERY candidate you looked at and rejected in considered_dropped with a one-line reason — no silent drops. Also add tag "dont" picks for popular things that should NOT be installed in VR for this topic (flat-only, conflicting with HIGGS/PLANCK/VRIK).`
  const r = await agent(prompt, { label: `collect:ix-${t.key}`, phase: 'Collect', schema: PICKS, effort: 'high' })
  return r ? { ...r, topic: t.key } : null
}

async function verify(c, t) {
  if (!c || !c.picks.length) return c ? { ...c, verdicts: [], kept: [] } : null
  const listing = JSON.stringify(c.picks.map(({ key, id, name, url, section, tag, choose_one_group, what, vr_status, in_lists, files, requires, interplay, note, evidence }) => ({ key, id, name, url, section, tag, choose_one_group, what, vr_status, in_lists, files, requires, interplay, note, evidence })), null, 1)
  const lens = await parallel(LENSES.map(l => () => agent(`${CONTEXT}\n\n${l.prompt.replace('${D}', D).replace('${D}', D)}\n\nSection codes: ${SEC_RU}.\nReturn one verdict per key (all ${c.picks.length}). PICKS:\n${listing}`, { label: `verify:${l.key}-ix-${t.key}`, phase: 'Verify', schema: VERDICTS, effort: 'high' })))
  const maps = lens.map(r => new Map((r ? r.verdicts : []).map(v => [v.key, v])))
  const kept = []
  for (const p of c.picks) {
    const a = maps[0].get(p.key), b = maps[1].get(p.key)
    if (a && b && a.keep && b.keep) kept.push({ ...p, section: b.section || p.section, tag: (a.tag === 'try' && b.tag !== 'dont') ? 'try' : (b.tag || p.tag), choose_one_group: b.choose_one_group || a.choose_one_group || p.choose_one_group, what: b.what || p.what, note: [b.note, a.note && a.note !== b.note ? a.note : ''].filter(Boolean).join(' ') || p.note })
  }
  log(`${t.key}: ${c.picks.length} picks, ${c.considered_dropped.length} dropped by collector, kept by both ${kept.length}`)
  return { ...c, kept }
}

phase('Collect')
const res = (await pipeline(list, t => collect(t), (c, t) => verify(c, t))).filter(Boolean)
const kept = res.flatMap(r => r.kept)
const bySection = {}
for (const k of kept) bySection[k.section] = (bySection[k.section] || 0) + 1
log(`kept ${kept.length}: ${JSON.stringify(bySection)}`)

let consolidation = null, critic = null
if (kept.length) {
  phase('Consolidate')
  consolidation = await agent(`${CONTEXT}\n\nSection codes: ${SEC_RU}.\n\nYOU ARE THE CONSISTENCY EDITOR for the new "VR interaction" set (${kept.length} picks verified twice). Read ${D}/MODLIST.md and ${D}/OTHER_MODS.md. Resolve: (a) duplicates across topics and against Core/Other-1 (drop_duplicate the weaker NEW one); (b) choose_one groups with exactly one default_pick each; (c) the interplay matrix with the Core stack: for every kept mod that touches grab/collision/weapon-offset/animation — does it need a patch, a setting, or a load-order rule relative to HIGGS, PLANCK, Physical Collision VR, VRIK, True Wield VR, OAR; (d) MO2 order and plugin order rules; (e) concrete conflicts; (f) retag: rec only for clear winners. Return an adjustment for EVERY key. PICKS:\n${JSON.stringify(kept.map(k => ({ key: k.key, id: k.id, name: k.name, section: k.section, tag: k.tag, group: k.choose_one_group, what: k.what, files: k.files, requires: k.requires, interplay: k.interplay, note: k.note, vr: k.vr_status, lists: k.in_lists })), null, 1)}`,
    { label: 'consolidate:ix', phase: 'Consolidate', effort: 'high', schema: { type: 'object', properties: {
      adjustments: { type: 'array', items: { type: 'object', properties: { key: { type: 'string' }, action: { type: 'string', enum: ['keep', 'drop_duplicate', 'regroup', 'retag', 'move_section'] }, section: { type: 'string', enum: SECTIONS }, tag: { type: 'string', enum: ['rec', 'opt', 'alt', 'try', 'dont'] }, choose_one_group: { type: ['string', 'null'] }, reason: { type: 'string' } }, required: ['key', 'action', 'section', 'tag', 'choose_one_group', 'reason'] } },
      groups: { type: 'array', items: { type: 'object', properties: { group: { type: 'string' }, members: { type: 'array', items: { type: 'string' } }, default_pick: { type: 'string' }, rule: { type: 'string' } }, required: ['group', 'members', 'default_pick', 'rule'] } },
      interplay_rules: { type: 'array', items: { type: 'string' }, description: 'RU: concrete rules/patches/settings vs HIGGS, PLANCK, VRIK, Physical Collision VR, True Wield VR, OAR' },
      order_rules: { type: 'array', items: { type: 'string' } }, conflicts: { type: 'array', items: { type: 'string' } }, notes: { type: 'string' },
    }, required: ['adjustments', 'groups', 'interplay_rules', 'order_rules', 'conflicts', 'notes'] } })

  phase('Critic')
  critic = await agent(`${CONTEXT}\n\nYOU ARE THE COMPLETENESS CRITIC for the VR-interaction collection. ${res.length} topic agents returned; kept by both verifiers: ${kept.length} (${JSON.stringify(bySection)}). Their rejected candidates: ${res.reduce((s, r) => s + r.considered_dropped.length, 0)}. Task: find what is STILL MISSING. Method: (1) list the interaction-related mods of the 3 most VR-focused lists (Stormcrown VR, Panda's Sovngarde, Yggdrasil VR, FUS) via ${D}/tools/whouses.py / the archives in ${D}/data/rep and check each against Core (${D}/MODLIST.md), Other-1 (${D}/OTHER_MODS.md) and the kept names: ${JSON.stringify(kept.map(k => k.name))}; (2) web-check the Skyrim VR scene for 2025-2026 interaction mods that nobody covered (HIGGS/PLANCK add-ons, GitHub-only VR mods); (3) name concrete gaps with candidate Nexus ids/URLs. Return gaps as data; do not edit files.`,
    { label: 'critic:ix', phase: 'Critic', effort: 'high', schema: { type: 'object', properties: {
      verdict: { type: 'string', enum: ['complete_enough', 'needs_another_round'] },
      missing: { type: 'array', items: { type: 'object', properties: { topic: { type: 'string' }, why: { type: 'string' }, candidate: { type: 'string' } }, required: ['topic', 'why', 'candidate'] } },
      notes: { type: 'string' },
    }, required: ['verdict', 'missing', 'notes'] } })
}

return {
  topics: res.map(r => ({ topic: r.topic, picks: r.picks.length, dropped: r.considered_dropped.length, kept: r.kept.length })),
  keptByBoth: kept.length, bySection,
  conflicts: consolidation ? consolidation.conflicts : [], interplay: consolidation ? consolidation.interplay_rules : [],
  critic,
}