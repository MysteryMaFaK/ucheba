export const meta = {
  name: 'skyrim-vr-hitech-2026',
  description: 'Verify user-provided 2026 high-tech mods for Skyrim VR and sweep for similar new 2026 SKSE tech, then adversarially verify',
  phases: [
    { title: 'Seed', detail: 'verify the 5 user examples + 3 themed sweeps of 2026 releases' },
    { title: 'Verify', detail: 'VR-compat skeptic + redundancy/value skeptic' },
  ],
}

const D = 'skyrim-vr-modlist'
const SECTIONS = ['tools','base','frameworks','fixes','vr','ui','gfx','world','land','anim','combat','audio','ai','perf','immersion','dont']

const CONTEXT = `
You are helping build the CORE of a "next-gen 2026" Skyrim VR modlist (Skyrim VR 1.4.15, SKSEVR 2.0.12, MO2). Today is 2026-10-08. Textures are excluded (handled later). The user plays Skyrim VR, not SE/AE. The user LOVES new high-tech SKSE mods with genuinely new functions (their examples: Dynamic Terrain Deformation SKSE — real-time footprints/deformation in snow/sand/mud; Smooth Terrain — SKSE plugin subdividing terrain meshes; Helios — weather-driven interior window lighting, successor to DIAL; Show Player In Inventory — 3D player preview in inventory; Grid Inventory — weight-becomes-space grid inventory).

Existing page inventory (READ FIRST, avoid duplicates): ${D}/data/page_items.txt. Core choices: Open Shaders 2.17 (CS fork; official CS >=1.7 dropped VR; includes Skylighting, Wetness, Grass Lighting/Collision, Terrain Blending/Variation, Light Limit Fix, DLSS, foveated rendering), Light Placer + VR DLL, CS Light, Lux, Azurite Weathers III, NGIO, OAR, Pandora, VRIK/HIGGS/PLANCK + Asterrath 2026 suite, Engine Fixes VR 7.10, Skyrim VR ESL Support, Poached Bugs VR, SkyUI VR.

Data:
- ${D}/data/new2026_in_lists.txt — 536 mods FIRST UPLOADED IN 2026 (Nexus id >= 168000) that popular Wabbajack lists (2025-2026) already use; columns: id | name | VR-lists | SE-lists | newest file date | which VR lists | sample file.
- ${D}/data/rep/*.json — full archive lists of 27 popular lists; helper: python3 -I ${D}/tools/whouses.py <id or name> prints which lists use it and exact file names (a VR-named file is strong evidence).
- Web: load WebSearch/WebFetch via ToolSearch. nexusmods.com, schaken-mods, modding.wiki, synergyvr.org are BLOCKED for fetch — use search snippets (Nexus pages show up in search results with descriptions/tags like "Skyrim VR"), GitHub (github.com/raw works), Reddit mirrors, YouTube titles.

VR rules: no-DLL mods generally work; SKSE DLLs need a VR build (VR file/page, NG/CommonLibVR build stating VR, "Skyrim VR" tag on Nexus, or VR list shipping it). SE-only DLL = does not work regardless of comments. Flat-only/pointless in VR: 1st-person animations/camera/FOV mods, player 3rd-person movement/attack frameworks, flat HUD/inventory UIs that rely on flat menus (check whether SkyUI VR menus can host them), SSE Display Tweaks. Many 2026 mods carry an "AI Assisted"/"AI Generated" tag — note it, it is not a disqualifier by itself but lowers confidence.
Write human-facing text (what, vr_note, reason, overlaps) in RUSSIAN, short, concrete.`

const PICKS = {
  type: 'object',
  properties: {
    picks: { type: 'array', items: { type: 'object', properties: {
      id: { type: ['integer', 'null'] },
      name: { type: 'string' },
      url: { type: 'string' },
      released: { type: 'string', description: 'first upload / last update dates if known' },
      section: { type: 'string', enum: SECTIONS },
      what: { type: 'string', description: 'RU <=160 chars' },
      vr_status: { type: 'string', enum: ['works_as_is', 'vr_version_exists', 'vr_native', 'flat_only', 'unknown'] },
      vr_note: { type: 'string' },
      evidence: { type: 'string' },
      ai_tag: { type: 'boolean', description: 'mod page carries AI Assisted/Generated tag' },
      verdict: { type: 'string', enum: ['add_rec', 'add_opt', 'warn_dont', 'unverified_try'] },
      overlaps: { type: 'string' },
      reason: { type: 'string' },
    }, required: ['id', 'name', 'url', 'released', 'section', 'what', 'vr_status', 'vr_note', 'evidence', 'ai_tag', 'verdict', 'overlaps', 'reason'] } },
    notes: { type: 'string' },
  },
  required: ['picks', 'notes'],
}

const SEEDS = [
  { key: 'user-examples', prompt: `TASK: Deep-verify the user's 5 example mods for Skyrim VR: (1) Dynamic Terrain Deformation skse by NearMidnightNow (v1.1, uploaded 2026-09-21, updated 2026-09-26, tags: Total Conversion, Overhaul, AI Assisted); (2) Smooth Terrain by hakasapl, Nexus 186875, v0.6.0 (2026-07-30/2026-08-27, tags include "Skyrim VR", AI Assisted; used by Yggdrasil VR); (3) Helios by isoprovophlex, Nexus 181533 (2026-07-07/08, weather reflection system for interior lighting, successor to DIAL; used by Stormcrown VR); (4) Show Player In Inventory by ItzIvy, Nexus 178689, v1.6.1 (2026-04-28/2026-08-31, SKSE, UI); (5) Grid Inventory by ISmoothl (v1.6.5, 2026-08-18/2026-10-01, SKSE, UI, AI-Generated Content). For each: find Nexus id if missing, what it does technically, requirements, VR support (VR file? CommonLib NG with VR? "Skyrim VR" tag? reports in comments/bugs from snippets?), conflicts/interplay with page items (e.g. Open Shaders terrain features, Terrain Helper, DynDOLOD/xLODGen terrain LOD, Lux/CS Light/Light Placer, SkyUI VR, Better Dynamic Snow), VR frame-time concerns. Verdict: add_rec/add_opt if VR-confirmed; unverified_try if plausible but unconfirmed (tell the user exactly how to test); warn_dont if flat-only. Also add up to 5 close relatives you discover (e.g. other terrain/snow/footprint/interior-light 2026 tech).` },
  { key: 'world-render-tech', prompt: `TASK: Sweep for NEW (released 2025-10 .. 2026-10) high-tech SKSE mods in WORLD/RENDERING tech, similar in spirit to the user's examples: terrain/geometry processing, deformation, procedural snow/ash/wetness accumulation, weather-driven lighting, wind/particles (e.g. Particle Wind SKSE), blood/decals (Dynamic Bloodpool Framework), sky/horizon fixes, LOD tech, interior ambience, cold breath, Open Shaders companion features. Use new2026_in_lists.txt first (scan ALL lines, pick world/render tech), then web search for very recent ones not yet in lists. Verify VR status for each. Up to 15 add_*/unverified_try picks + warn_dont for flat-only hyped items.` },
  { key: 'systems-ui-anim-tech', prompt: `TASK: Sweep for NEW (released 2025-10 .. 2026-10) high-tech SKSE mods in SYSTEMS / UI / ANIMATION / AI tech: new inventory or menu systems (grid inventory, 3D previews, icon injectors), horse riding overhauls (e.g. HorsePower), traversal (StepUpOnto), NPC behavior/perception, physics reactions, procedural animation, A-pose/behavior runtime fixes, MCM tooling (MCM Unlocked, MCM Memory), faction/reputation systems, Simonrim SKSE addons. Use new2026_in_lists.txt first (scan ALL lines), then web search. For UI mods, check carefully whether they work inside Skyrim VR's menus (SkyUI VR) — many do not. Verify VR status for each. Up to 15 add_*/unverified_try picks + warn_dont for flat-only hyped items.` },
  { key: 'vr-specific-2026', prompt: `TASK: Sweep for NEW (released 2025-10 .. 2026-10) VR-SPECIFIC mods and VR stability/perf tech not on the page: e.g. VRIK Closed Fist, Pull Arrows VR, Floating Subtitles VR, Telekinesis Aim Fix VR, Collision Sentinel crash fix, Pickpocket Reset VR, Lights Conflict Resolver, new HIGGS/PLANCK add-ons, VR body/hand interaction, VR UI, VR performance (shader cache, CPU, streaming), Open Shaders VR companions. Use new2026_in_lists.txt (VR-lists column) and web search (r/skyrimvr, "Skyrim VR" 2026 Nexus). Up to 15 add_*/unverified_try picks.` },
]

phase('Seed')
const results = await parallel(SEEDS.map(s => () =>
  agent(`${CONTEXT}\n\n${s.prompt}\nEvery pick needs concrete evidence (list usage via whouses.py, file names, URLs, snippet text, dates).`,
    { label: `seed:${s.key}`, phase: 'Seed', schema: PICKS, effort: 'high' })
    .then(r => r ? { src: s.key, ...r } : null)
))

// barrier justified: dedup across seeds and give verifiers the whole set for cross-proposal overlap checks
const all = [], seen = new Map()
for (const r of results.filter(Boolean)) for (const p of r.picks) {
  const key = p.id ? `id:${p.id}` : `n:${p.name.toLowerCase().replace(/[^a-z0-9а-я]+/g, '')}`
  if (seen.has(key)) { seen.get(key).also.push(r.src); continue }
  const it = { key, src: r.src, also: [], ...p }; seen.set(key, it); all.push(it)
}
log(`Seed proposals after dedup: ${all.length}`)
const notes = results.filter(Boolean).map(r => `${r.src}: ${r.notes}`)
if (!all.length) return { notes, verified: [] }

const VERDICTS = {
  type: 'object',
  properties: { verdicts: { type: 'array', items: { type: 'object', properties: {
    key: { type: 'string' }, keep: { type: 'boolean' },
    vr_status: { type: 'string', enum: ['works_as_is', 'vr_version_exists', 'vr_native', 'flat_only', 'unknown'] },
    vr_note: { type: 'string' }, section: { type: 'string', enum: SECTIONS },
    tag: { type: 'string', enum: ['rec', 'opt', 'try', 'dont'] },
    what: { type: 'string', description: 'RU polished one-liner <=170 chars' },
    reason: { type: 'string' },
  }, required: ['key', 'keep', 'vr_status', 'vr_note', 'section', 'tag', 'what', 'reason'] } } },
  required: ['verdicts'],
}
const listing = JSON.stringify(all.map(({ key, id, name, url, released, section, verdict, what, vr_status, vr_note, evidence, ai_tag, overlaps, reason }) => ({ key, id, name, url, released, section, verdict, what, vr_status, vr_note, evidence, ai_tag, overlaps, reason })), null, 1)
const LENSES = [
  { key: 'vr-compat', prompt: `You are a VR-COMPATIBILITY SKEPTIC. Try to REFUTE each VR claim. add_* needs real evidence of VR support (VR file/page, NG build stating VR, Nexus "Skyrim VR" tag, VR list shipping it — run whouses.py and check file names). If support is plausible but unproven, keep=true with tag "try" and a vr_note telling exactly how to test (sksevr.log line, what to look for). SE-only DLL → keep=false (or tag dont if it is popular and people would copy it). warn_dont: confirm it is really flat-only.` },
  { key: 'value-redundancy', prompt: `You are a REDUNDANCY / VALUE / PERFORMANCE SKEPTIC. Try to REFUTE that each item belongs: duplicate of a page item (page_items.txt) or of another proposal (keep the better)? Already built into Open Shaders / Engine Fixes VR / Poached Bugs VR / po3 Tweaks? Superseded? Heavy VR frame-time cost without payoff? Content/cosmetic rather than tech? Keep real value; assign section and tag (rec/opt/try/dont) and write the final RU one-liner.` },
]
phase('Verify')
const lens = await parallel(LENSES.map(l => () =>
  agent(`${CONTEXT}\n\n${l.prompt}\n\nReturn one verdict per proposal key. PROPOSALS (${all.length}):\n${listing}`,
    { label: `verify:${l.key}`, phase: 'Verify', schema: VERDICTS, effort: 'high' })))
const maps = lens.map(r => new Map((r ? r.verdicts : []).map(v => [v.key, v])))
const verified = all.map(p => { const a = maps[0].get(p.key), b = maps[1].get(p.key); return { ...p, compat: a || null, value: b || null, keep: !!(a && b && a.keep && b.keep) } })
log(`Kept by both: ${verified.filter(v => v.keep).length}/${verified.length}`)
return { notes, verified }
