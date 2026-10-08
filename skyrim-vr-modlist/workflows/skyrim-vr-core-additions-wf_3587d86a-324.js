export const meta = {
  name: 'skyrim-vr-core-additions',
  description: 'Mine popular 2026 Wabbajack lists + new modding releases for Skyrim VR core additions, then adversarially verify VR compatibility and redundancy',
  phases: [
    { title: 'Evaluate', detail: '6 category batches from 27 popular SE/VR lists + 1 sweep of 2025-2026 releases' },
    { title: 'Verify', detail: 'two skeptic lenses: VR compatibility, redundancy/value' },
  ],
}

const D = (typeof args !== 'undefined' && args && args.root) || 'skyrim-vr-modlist'  // args.root — абсолютный путь к папке проекта, если cwd не её родитель
const SECTIONS = ['tools','base','frameworks','fixes','vr','ui','gfx','world','land','anim','combat','audio','ai','perf','immersion','dont']

const CONTEXT = `
You are helping build the CORE of a "next-gen 2026" Skyrim VR modlist (Skyrim VR 1.4.15, SKSEVR 2.0.12, MO2). Today is 2026-10-08. Textures are deliberately excluded (handled later). The user plays Skyrim VR, not SE/AE.

What already exists: a curated page. Its full inventory (every mod with Nexus IDs and its section, plus a "do not install in VR" list) is in ${D}/data/page_items.txt — READ IT FIRST. Core choices already made: Open Shaders 2.17 (CS fork; official Community Shaders >=1.7 dropped VR; CSX is the alt), Light Placer + VR DLL, CS Light, Lux (+Via/Orbis), Azurite Weathers III, NGIO + Grass Cache Helper, Merethic Grasslands, Happy Little Trees, OAR, Pandora, VRIK/HIGGS/PLANCK + 2026 Asterrath suite (Physical Collision VR, True Wield VR, Immersive Weapon Penetration VR, Lethal Unarmed VR, Swap Drop and Hold Redux VR), Engine Fixes VR 7.10, Skyrim VR ESL Support, Poached Bugs VR, SkyrimNet/Mantella/CHIM, OpenComposite Unleashed.

Data you can use:
- Status reports (full archive lists) of 27 popular Wabbajack lists updated 2025-2026 are in ${D}/data/rep/*.json. VR lists: Yggdrasil VR (2026-10-04), Stormcrown VR (2026-09-26), Librum VR, Panda's Sovngarde (high-end VR visuals), Tahrovin, Tahrovin - Grit, Spirit of Grit, Tempus Maledictum VR, FUS. SE next-gen lists include NGVO, CSVO, CSVP, LoreRim, Nordic Souls (+PBR), Elysium Remastered, Wunduniik, True North, Morning Star, Winds of the North, Skyrim25, Aldrnari, Apostasy, Lost Legacy, Tomes of Talos, Skyrim Unification Project, The Northern Experience.
- Helper: python3 -I ${D}/tools/whouses.py <nexusModID or name substring>  → prints which lists use the mod and the exact archive file names (file names often reveal a VR file, e.g. "... VR-12345-...").
- Web: use ToolSearch to load WebSearch/WebFetch. nexusmods.com, schaken-mods, modding.wiki, synergyvr.org are BLOCKED for fetch — rely on search-result snippets, GitHub repos/releases (github.com, raw.githubusercontent.com work), Reddit mirrors, Steam discussions.

VR compatibility rules (apply strictly):
- Plugin/mesh/sound/script-only mods (no DLL) generally work in VR. ESL-flagged plugins work via Skyrim VR ESL Support. Mods needing SE 1.6/CC records need the updated-masters path.
- SKSE DLL mods need a VR build: a VR file, a separate "... VR" page, CommonLibSSE-NG/CommonLibVR build stating VR support, or presence in a VR Wabbajack list with a VR-named file. An SE-only DLL does NOT work in VR regardless of comments.
- Flat-only / pointless in VR: first-person animation packs, player third-person movement/attack animation frameworks (MCO/ADXP, BFCO, SCAR, Precision, TDM), camera mods (SmoothCam, Improved Camera), flat HUD/UI (TrueHUD, Wheeler, Untarnished UI), SSE Display Tweaks, keyboard-dodge mods. NPC-side animation packs via OAR ARE useful.

What NOT to propose: textures/PBR/retextures, armor/weapon/clothes/hair/body/face cosmetics, quest/new-land/follower/player-home content, things that duplicate a page choice (say so instead), SE twins of page items (e.g. SSE Engine Fixes, Address Library SE).
Write all human-facing text fields (what, vr_note, reason, overlaps) in RUSSIAN, short and concrete.`

const PICKS = {
  type: 'object',
  properties: {
    picks: { type: 'array', items: { type: 'object', properties: {
      id: { type: ['integer', 'null'], description: 'Nexus SSE mod id, null if not on Nexus' },
      name: { type: 'string' },
      url: { type: 'string', description: 'Nexus or GitHub URL' },
      section: { type: 'string', enum: SECTIONS },
      what: { type: 'string', description: 'RU, <=160 chars: what it does and why it matters' },
      vr_status: { type: 'string', enum: ['works_as_is', 'vr_version_exists', 'vr_native', 'flat_only', 'unknown'] },
      vr_note: { type: 'string', description: 'RU: which file/page to take for VR, or why flat-only' },
      evidence: { type: 'string', description: 'concrete evidence: VR lists using it (from whouses.py), file names, URLs/snippets' },
      verdict: { type: 'string', enum: ['add_rec', 'add_opt', 'warn_dont'] },
      overlaps: { type: 'string', description: 'RU: overlaps/conflicts with page items or requirements; empty if none' },
      reason: { type: 'string', description: 'RU: why include (or why warn)' },
    }, required: ['id', 'name', 'url', 'section', 'what', 'vr_status', 'vr_note', 'evidence', 'verdict', 'overlaps', 'reason'] } },
    triage_note: { type: 'string', description: 'brief: how many candidates triaged, main skip reasons' },
  },
  required: ['picks', 'triage_note'],
}

const BATCHES = [
  { key: 'b1_fixes_frameworks', focus: 'engine/bug fixes, SKSE frameworks, distributors, Papyrus libraries, crash/freeze fixes' },
  { key: 'b2_animation_physics', focus: 'NPC animation packs (OAR), behavior tools, physics (CBPC/SMP), idles; separate useful NPC-side packs from flat-only player animations' },
  { key: 'b3_visuals_world', focus: 'VFX, lighting add-ons, weather/sky, water, snow/ash, grass/tree meshes, LOD tools, shader add-ons (Open Shaders already includes Skylighting, Wetness, Grass Lighting/Collision, Terrain Variation/Blending etc. — those are NOT separate installs)' },
  { key: 'b4_gameplay_systems', focus: 'combat/magic/perk/skill systems, encounter zones and loot, economy, survival, NPC AI behavior' },
  { key: 'b5_ui_audio_misc', focus: 'UI/QoL, audio/music/ambience, and miscellaneous systems (Base Object Swapper dynamic-world mods, immersion)' },
  { key: 'b6_misc', focus: 'miscellaneous systems and VR-specific leftovers (many VR-only mods appear here)' },
]

const evalPrompt = b => `${CONTEXT}

YOUR BATCH: ${D}/data/${b.key}.txt — candidates mined from those lists that are NOT yet on the page (one per line: #id | name | VR-lists count | SE-lists count | newest file date | which VR lists use it | sample files). Focus area: ${b.focus}.

Task: triage EVERY line. Most will be skipped (content, cosmetics, minor, outdated, flat-only). For the promising ones, verify VR status (whouses.py file names + targeted web search/GitHub) and decide.
Return:
- verdict add_rec: clearly valuable for a next-gen VR core and VR-compatible (evidence required).
- verdict add_opt: nice-to-have, VR-compatible.
- verdict warn_dont: POPULAR in SE next-gen lists but flat-only or harmful in VR AND not already in the page's do-not-install list — so the user knows not to copy it.
Prefer recent (2025-2026) and widely used items; also keep proven VR-specific mods that many VR lists use. Cap: at most 25 add_* picks and 10 warn_dont picks — choose the most impactful. Every pick needs concrete evidence.`

const SWEEP_PROMPT = `${CONTEXT}

YOUR TASK (multi-modal sweep for the newest developments): find notable Skyrim modding developments from 2025-2026 that a "next-gen 2026" VR core should consider and that are NOT on the page and probably not common in Wabbajack lists yet. Search angles (do several): new SKSE frameworks/fixes released 2025-2026; new Skyrim VR mods released 2025-2026 (r/skyrimvr, YouTube titles, "Skyrim VR mod 2026"); Open Shaders/Community Shaders companion mods and features relevant to VR; new animation/physics tech (e.g. physics-based reactions, active ragdoll, procedural systems); performance tools for VR (shader cache, upscaling, CPU tools); AI/NPC tech beyond SkyrimNet/Mantella/CHIM; MO2/LOD tooling changes in 2026 (DynDOLOD/xLODGen/ParallaxGen/PGPatcher, Synthesis patchers). Check each finding's VR status with the rules. You may also check ${D}/data/rep/*.json via whouses.py to see if any list already uses it.
Return up to 20 add_* picks (and warn_dont if you find hyped 2026 flat-only mods people might copy into VR), each with evidence (URLs/snippets, dates).`

phase('Evaluate')
const jobs = BATCHES.map(b => ({ kind: 'batch', b }))
jobs.push({ kind: 'sweep' })
const evals = await parallel(jobs.map(j => () =>
  agent(j.kind === 'batch' ? evalPrompt(j.b) : SWEEP_PROMPT, {
    label: j.kind === 'batch' ? `eval:${j.b.key}` : 'sweep:2025-2026',
    phase: 'Evaluate', schema: PICKS, effort: 'high',
  }).then(r => r ? { src: j.kind === 'batch' ? j.b.key : 'sweep', ...r } : null)
))

// barrier justified: dedup across batches+sweep, and verifiers need the full proposal set to spot cross-proposal overlaps
const all = []
const seen = new Map()
for (const e of evals.filter(Boolean)) {
  for (const p of e.picks) {
    const key = p.id ? `id:${p.id}` : `n:${p.name.toLowerCase().replace(/[^a-z0-9а-я]+/g, '')}`
    if (seen.has(key)) { seen.get(key).also.push(e.src); continue }
    const item = { key, src: e.src, also: [], ...p }
    seen.set(key, item); all.push(item)
  }
}
log(`Proposals after dedup: ${all.length} (add: ${all.filter(p => p.verdict !== 'warn_dont').length}, warn: ${all.filter(p => p.verdict === 'warn_dont').length})`)
const triage = evals.filter(Boolean).map(e => `${e.src}: ${e.triage_note}`)
if (!all.length) return { all, triage, verified: [] }

const VERDICTS = {
  type: 'object',
  properties: { verdicts: { type: 'array', items: { type: 'object', properties: {
    key: { type: 'string' },
    keep: { type: 'boolean' },
    vr_status: { type: 'string', enum: ['works_as_is', 'vr_version_exists', 'vr_native', 'flat_only', 'unknown'] },
    vr_note: { type: 'string', description: 'RU corrected note on what to install for VR' },
    section: { type: 'string', enum: SECTIONS },
    tag: { type: 'string', enum: ['rec', 'opt', 'dont'] },
    what: { type: 'string', description: 'RU polished one-liner for the page, <=170 chars, plain direct style' },
    reason: { type: 'string', description: 'RU: why kept or rejected, citing evidence' },
  }, required: ['key', 'keep', 'vr_status', 'vr_note', 'section', 'tag', 'what', 'reason'] } } },
  required: ['verdicts'],
}

const listing = JSON.stringify(all.map(p => ({ key: p.key, id: p.id, name: p.name, url: p.url, section: p.section, verdict: p.verdict, what: p.what, vr_status: p.vr_status, vr_note: p.vr_note, evidence: p.evidence, overlaps: p.overlaps, reason: p.reason })), null, 1)

const LENSES = [
  { key: 'vr-compat', prompt: `You are a VR-COMPATIBILITY SKEPTIC. For every proposal below, try to REFUTE its VR claim. For add_* items: is there really a VR build / is it really DLL-free / does a VR list actually ship it (run whouses.py — check the archive FILE NAMES for a VR file)? An SE-only SKSE DLL means keep=false. For warn_dont items: confirm it is genuinely flat-only/harmful in VR (if it actually works in VR, keep=false). If evidence is missing and you cannot confirm, default keep=false. Spot-check uncertain items with web search/GitHub.` },
  { key: 'value-redundancy', prompt: `You are a REDUNDANCY / VALUE / PERFORMANCE SKEPTIC. For every proposal below, try to REFUTE that it belongs in this VR core: does it duplicate something already on the page (read page_items.txt) or another proposal in this list (pick the better one, reject the other)? Is it already built into Open Shaders, Engine Fixes VR, Poached Bugs VR, po3 Tweaks? Is it outdated/abandoned or superseded by a 2025-2026 alternative? Is its VR frame-time cost unjustified? Is it content/cosmetics rather than core? Keep only items that add real value. Assign the best page section and tag (rec/opt for adds, dont for warnings) and write the final RU one-liner.` },
]

phase('Verify')
const lensResults = await parallel(LENSES.map(l => () =>
  agent(`${CONTEXT}

${l.prompt}

Return one verdict per proposal (use its key). PROPOSALS (${all.length}):
${listing}`, { label: `verify:${l.key}`, phase: 'Verify', schema: VERDICTS, effort: 'high' })
))

const byLens = lensResults.map(r => new Map((r ? r.verdicts : []).map(v => [v.key, v])))
const verified = all.map(p => {
  const a = byLens[0].get(p.key), b = byLens[1].get(p.key)
  return { ...p, compat: a || null, value: b || null, keep: !!(a && b && a.keep && b.keep) }
})
log(`Kept by both lenses: ${verified.filter(v => v.keep).length}/${verified.length}`)
return { triage, verified }
