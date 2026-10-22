export const meta = {
  name: 'skyrim-vr-interaction-r2',
  description: 'Round 2 for the VR-interaction collection: research and double-verify the gaps the completeness critic found (Precision Physic Bodies, Immersive Equip VR, MageVR Reborn, Physical Checkout, Object Impact Framework family, DovaVR, lockpick fixes, GitHub watch-list, unexplored areas)',
  phases: [
    { title: 'Collect', detail: '6 research agents, one per gap group' },
    { title: 'Verify', detail: 'VR-compat skeptic + value/redundancy skeptic over all new picks' },
  ],
}

const D = (args && args.root) || 'skyrim-vr-modlist'
const SECTIONS = ['ix_hands', 'ix_combat', 'ix_magic', 'ix_world', 'ix_ui', 'ix_locomotion', 'ix_feedback', 'ix_dont']
const SEC_RU = 'ix_hands=hands, grabbing, physical objects, holsters/wearables/equip by hand; ix_combat=VR combat interaction; ix_magic=spellcasting/shouts/hand magic; ix_world=world/NPC/containers/crafting/doors/lockpicking/trade; ix_ui=VR-native UI, menus, loot, inventory; ix_locomotion=locomotion, comfort, riding, swimming; ix_feedback=haptics/feedback/impact reactions of objects; ix_dont=do NOT install in VR'

const CONTEXT = `
Project: a Skyrim VR modlist (Skyrim VR 1.4.15, SKSEVR 2.0.12, MO2, VRIK + HIGGS + PLANCK stack). Today 2026-10-11. Lists: "Core 2026" (${D}/MODLIST.md — contains VRIK, HIGGS, PLANCK, Physical Collision VR, True Wield VR, Interactive Activators VR, Gift by Hand VR, Spell Wheel VR, Magic Improvements for VR, QuickLoot IE, Trade and Barter (opt), Dismembering Framework (opt), Core Impact Framework (opt), OpenComposite Unleashed, etc.), "Other Mods 2026" (${D}/OTHER_MODS.md), and the VR-interaction collection of round 1 (${D}/VR_INTERACTION.md and ${D}/data/vr_interaction_result.json: kept + rejected + dropped lists). Do NOT re-propose anything already kept there; do not resurrect a candidate round 1 rejected unless you have NEW evidence (say what is new).
THE ASK: the owner wants the MISSING mods for interactivity and interaction in VR. A completeness critic found the gaps below that round 1 missed or dropped on thin evidence. Your job: research ONE gap group properly and return evidence-based picks.
EXCLUDED: quest/new-land content, followers as characters, player homes, big difficulty overhauls, spell/shout packs, narrow SimonRim parts, NSFW (if a mod has optional adult integrations, note it and recommend the safe configuration; do not recommend the adult parts). ENB-only is useless.
Tools: load WebSearch/WebFetch via ToolSearch. nexusmods.com pages are BLOCKED for fetch (DNS) — use search snippets ("<name> at Skyrim Special Edition Nexus" style queries), GitHub README/raw files via WebFetch (github.com repository pages and raw.githubusercontent.com often work), Reddit mirrors. Helper: python3 -I ${D}/tools/whouses.py <nexus id or name> shows which of the 27 popular lists ship a mod and the exact archive file names; archives are in ${D}/data/rep/*.json.
VR rules: SKSE DLLs need a VR build (state exactly what evidence you have: page says VR / file name says VR / a VR list ships it / author says "tested in VR" / author has no headset). Conflict checks that matter: HIGGS/PLANCK/VRIK/Physical Collision VR/True Wield VR/Gift by Hand VR/OAR-Pandora/Engine Fixes VR. Never invent file names, FOMOD options, versions or VR status. Where a page could not be read say so and set tag "try". Human-facing text in RUSSIAN, short.`

const PICKS = { type: 'object', properties: {
  picks: { type: 'array', items: { type: 'object', properties: {
    key: { type: 'string', description: 'id:<nexus id> or n:<normalized name> when no id' },
    id: { type: ['integer', 'null'] }, name: { type: 'string' }, url: { type: 'string' },
    section: { type: 'string', enum: SECTIONS }, tag: { type: 'string', enum: ['rec', 'opt', 'alt', 'try', 'dont'] },
    choose_one_group: { type: ['string', 'null'] }, what: { type: 'string', description: 'RU <=170 chars' },
    vr_status: { type: 'string', enum: ['works_as_is', 'vr_version_exists', 'vr_native', 'flat_only', 'unknown'] },
    in_lists: { type: 'string' }, files: { type: 'string' }, requires: { type: 'array', items: { type: 'string' } },
    interplay: { type: 'string', description: 'RU: relation to HIGGS/PLANCK/VRIK/Physical Collision VR and Core mods; duplicates/conflicts/order' },
    note: { type: 'string', description: 'RU: caveats, settings, test advice, what could not be verified' },
    evidence: { type: 'string' },
  }, required: ['key', 'id', 'name', 'url', 'section', 'tag', 'choose_one_group', 'what', 'vr_status', 'in_lists', 'files', 'requires', 'interplay', 'note', 'evidence'] } },
  considered_dropped: { type: 'array', items: { type: 'object', properties: { id: { type: ['integer', 'null'] }, name: { type: 'string' }, reason: { type: 'string' } }, required: ['id', 'name', 'reason'] } },
  notes: { type: 'string' },
}, required: ['picks', 'considered_dropped', 'notes'] }

const VERDICTS = { type: 'object', properties: { verdicts: { type: 'array', items: { type: 'object', properties: {
  key: { type: 'string' }, keep: { type: 'boolean' }, section: { type: 'string', enum: SECTIONS }, tag: { type: 'string', enum: ['rec', 'opt', 'alt', 'try', 'dont'] },
  choose_one_group: { type: ['string', 'null'] }, what: { type: 'string' }, note: { type: 'string' }, reason: { type: 'string' },
}, required: ['key', 'keep', 'section', 'tag', 'choose_one_group', 'what', 'note', 'reason'] } } }, required: ['verdicts'] }

const LENSES = [
  { key: 'vr-compat', prompt: 'You are a VR-COMPATIBILITY SKEPTIC. Try to refute each claim: DLL without VR evidence, flat-only, hooks that fight HIGGS/PLANCK/VRIK/Physical Collision VR, adult-integration risks, beta/prototype stability. Re-check key facts yourself (GitHub README via WebFetch, search snippets, whouses.py). Unproven but plausible → keep with tag "try" and a note on how to test. Wrong or unsafe → keep=false.' },
  { key: 'value-perf', prompt: `You are a VALUE / REDUNDANCY / STABILITY SKEPTIC. Try to refute each item: duplicates or is superseded by something in Core (${D}/MODLIST.md), Other-1 (${D}/OTHER_MODS.md) or round 1 (${D}/VR_INTERACTION.md), conflicts with a listed Core mod, script-heavy/risky, beta that could break saves, or excluded category. Enforce choose_one groups. Assign best section and tag, write the final RU one-liner and note. Be strict.` },
]

const GROUPS = [
  { key: 'ppb', prompt: 'GAP 1 — Precision Physic Bodies (Nexus #186100, GitHub Telord72612/Precision-Physic-Bodies v2.2.0 beta): ~130 body capsules instead of ragdoll balls, finger/palm colliders for HIGGS, NPC pushes/reactions, clothing grab. Verify requirements (HIGGS, PLANCK, VRIK, XP32/XPMSSE, CBBE-based body), the optional adult integrations (how to install WITHOUT them), conflicts with Gift by Hand VR, VR Equip, Dismembering Framework (deadlock?), Physical Collision VR, CBPC, and whether the README states VR testing. Also check related Telord72612 projects only if they are interaction-relevant and safe.' },
  { key: 'equip-magevr', prompt: 'GAP 2 — Immersive Equip VR (Nexus #186897 + GitHub djhert/ImmersiveEquipVR): equip/unequip armor and jewelry with hands; verify what is real, whether the Nexus page and the repo are the same project, VR testing status, requirements, conflicts with Gift by Hand VR / VR Equip / PPB equip gestures. AND GAP 3 — MageVR Reborn (Nexus #184866, GitHub Telord72612/MageVR-Reborn v2.1): VR Backpack + VR SpellBook, FOMOD with two parts, requirements (VRIK, HIGGS, SkyUI VR, MCM Helper 1.3+, VR ESL Support, ElSopa HD Big Backpack for the backpack), conflicts with Spell Wheel VR (Core core), Magic Improvements for VR, Spell Auto-Aim VR, OpenComposite Unleashed hold-button overlap; round 1 put the OLD MageVR #21297 in ix_dont, so state clearly whether Reborn replaces it. Is it an alternative to Spell Wheel VR or additive? Give a recommendation as a choose_one group if it replaces.' },
  { key: 'checkout-oif', prompt: 'GAP 4 — Physical-Checkout-VR (Nexus #190966: take goods with a HIGGS hand to the counter, pay by releasing; requires HIGGS + Papyrus Extender VR): verify description, version, VR file, conflicts with Trade and Barter (Core opt). AND the Object Impact Framework family: OIF #149484 (shipped 1.6.8 by Panda\'s Sovngarde) and dependents Break The Lock #154901, Throwing Things Makes Noise #155761, Flammable Alcohol #150895 (Tempus + Panda\'s), Cooking with Fire #153449, Burn Those Books #151000, Dynamic Fire Sconce #160736, Immersive Hanging Dead Animal Harvest #151806. Use whouses.py for exact file names and which VR lists ship them; check DLL VR status, the interplay with Throw Stuff VR / More Interactive Objects / Core Impact Framework (actors vs objects), HIGGS-throw dependency, config files (OIF does nothing without configs — which dependents are worth it). Return the family as ONE pack pick (key n:oif-pack, files listing which members to install) plus individual optional extras.' },
  { key: 'locomotion-loot', prompt: 'GAP 5 — DovaVR Locomotion (Nexus #154803: arm-swing walking with cadence detection, swimming/riding switches): verify features, VR status, conflicts with Im Walkin\' Here VR (Core opt), Natural Locomotion (Other-1 niche), VR Climbing, Wade in Water VR. AND GAP 7 — Take All Lockpicks VR (Nexus #188691) and No Lockpick Activate VR (#25072; alt SKSE build #26790): verify VR status (SKSE VR 2.0.10/2.0.12), conflicts with QuickLoot IE (Core), Quickloot VR, Interactive Door Actions VR (round-1 pick, lockpicking). Small fixes → tag opt.' },
  { key: 'watchlist', prompt: 'GAP 6 — GitHub watch-list (README via WebFetch; check Releases / tags / Nexus page existence for each): djhert/CookingVR, djhert/InteractiveAnimalSkinningVR, GabeAlvess/True-Grip-SkyrimVR, SamuelJohnBrown (Neck Snap VR, Biting Axes & Swords VR, Weapons & Shields Unlocked), Treatid2 (DynamicHavokVR, BlockingStateRepairVR), xNicklaj (SkyrimVR-Apply-Poison, SkyrimVR-AimAssist), the Reddit "Immersive VR Actions" project, Telord72612/VRTouchEvents (adult leaning — do NOT recommend). For each: is there an installable release/Nexus page now, does it state VR/HIGGS/PLANCK requirements, overlap with Core (True Wield VR, Immersive Weapon Penetration VR, Dual Casting Fix VR). Return only the installable ones as picks (tag try, install-by-hand notes); everything else goes to considered_dropped with reason "список наблюдения: нет релиза" etc.' },
  { key: 'unexplored', prompt: 'GAP 8 — unexplored areas the critic could not cover: physical books and maps (read/hold/open by hand), mirrors in VR, left-handed mode (Weapons and Shields Unlocked is in GAP 6), Nexus #184623 (shows up next to 2026 HIGGS mods — identify it), "Parry - Simple Weapon Parrying" #133437 (VR/DLL status; Pseudo Physical Parry already covers the function but conflicts with Physical Collision VR — recommend what to do about the Other-1 pick #100781), Locational Damage SKSE VR #26447 (7 of 9 VR lists ship it; round 1 made it an alt vs Accuracy + Core Impact Framework: give a clear recommendation), plus a fresh search of 2026 Skyrim VR interaction releases (HIGGS/PLANCK add-ons, VR ports) that no earlier round named. Return picks with evidence.' },
]

phase('Collect')
const res = (await parallel(GROUPS.map(g => () => agent(`${CONTEXT}\n\nSection codes: ${SEC_RU}.\n\nYOUR TASK (${g.key}): ${g.prompt}\nReturn picks with evidence and EVERYTHING you looked at but did not pick in considered_dropped with a one-line reason.`,
  { label: `collect:ix2-${g.key}`, phase: 'Collect', schema: PICKS, effort: 'high' })))).filter(Boolean)
const picks = []
const seen = new Set()
for (const r of res) for (const p of r.picks) if (!seen.has(p.key)) { seen.add(p.key); picks.push(p) }
log(`round 2: ${picks.length} picks from ${res.length} agents`)
if (!picks.length) return { picks: 0 }

phase('Verify')
const listing = JSON.stringify(picks, null, 1)
const lens = await parallel(LENSES.map(l => () => agent(`${CONTEXT}\n\n${l.prompt}\n\nSection codes: ${SEC_RU}.\nReturn one verdict per key (all ${picks.length}). PICKS:\n${listing}`, { label: `verify:${l.key}-ix2-all`, phase: 'Verify', schema: VERDICTS, effort: 'high' })))
const maps = lens.map(r => new Map((r ? r.verdicts : []).map(v => [v.key, v])))
const kept = picks.filter(p => maps[0].get(p.key) && maps[1].get(p.key) && maps[0].get(p.key).keep && maps[1].get(p.key).keep)
return { picks: picks.length, keptByBoth: kept.length, kept: kept.map(k => `${k.name} [${maps[1].get(k.key).tag}]`), dropped: res.reduce((s, r) => s + r.considered_dropped.length, 0) }