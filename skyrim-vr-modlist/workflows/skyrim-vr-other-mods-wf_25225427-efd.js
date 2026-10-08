export const meta = {
  name: 'skyrim-vr-other-mods',
  description: 'Build the "Skyrim VR Other Mods 2026" list: core gaps, textures, appearance/world assets — mined from 27 popular lists + web, then adversarially verified for VR',
  phases: [
    { title: 'Collect', detail: '2 gap agents, 2 texture agents, 2 appearance/world agents' },
    { title: 'Verify', detail: 'VR-compat skeptic + value/VR-performance skeptic' },
  ],
}

const D = 'skyrim-vr-modlist'
const SECTIONS = ['start','followers','navigation','controls','russian','saves','cc','equipment','voice','music','niche',
  'tex_strategy','tex_land','tex_flora','tex_water_sky','tex_arch','tex_dungeons','tex_clutter','tex_pbr_tools',
  'chars_body','chars_faces','physics','armor','creatures','city_meshes','clutter_meshes','reshade','dont']

const CONTEXT = `
Project: a Skyrim VR modlist (Skyrim VR 1.4.15, SKSEVR 2.0.12, MO2). Today 2026-10-08. A "Core 2026" list already exists (frameworks, fixes, VR physics, Open Shaders 2.17 as the shader stack, Lux + Light Placer + CS Light, Azurite Weathers III, Merethic Grasslands, Happy Little Trees, DynDOLOD, OAR, SimonRim core: Adamant/Mysticism/Thaumaturgy/Apothecary/Mundus, SkyUI VR, RacemenuVR, FSMP opt, XPMSSE + VR skeleton fix, Scaleform Translation++ VR, Dynamic String Distributor, etc.). Its inventory is in ${D}/data/page_items.txt plus additions in ${D}/tools/additions.py — read both and do NOT re-propose those.
Now we build a SECOND list "Skyrim VR Other Mods 2026" with three parts: (1) gaps of the core, (2) textures, (3) appearance & world assets. EXCLUDED entirely: quest/new-land/dungeon content, followers as characters (a follower FRAMEWORK is fine), player homes, big difficulty overhauls (Requiem, Wildlander, Ordinator, Vokrii), new spell/shout packs (Apocalypse, Odin, Arcanum, Triumvirate, Thunderchild), narrow SimonRim parts (Aetherius, Scion, Manbeast, Pilgrim), NSFW.
Data: ${D}/data/rep/*.json = archive lists of 27 popular Wabbajack lists (9 VR: Yggdrasil VR 2026-10, Stormcrown VR 2026-09, Panda's Sovngarde = high-end VR visuals, Librum VR, Tahrovin, Tahrovin - Grit, Spirit of Grit, Tempus Maledictum VR, FUS; 18 SE next-gen: NGVO, CSVO, CSVP, LoreRim, Nordic Souls (+PBR), Elysium, Wunduniik, True North, Morning Star, Winds of the North, Skyrim25, Aldrnari, Apostasy, Lost Legacy, Tomes of Talos, SUP, TNE). Helper: python3 -I ${D}/tools/whouses.py <id or name> → which lists use it + exact archive file names (shows which FILE VARIANT VR lists pick, e.g. 2K vs 4K, VR patches).
Web: load WebSearch/WebFetch via ToolSearch; nexusmods.com, modding.wiki, schaken-mods, synergyvr.org are BLOCKED for fetch — use search snippets, GitHub, Reddit mirrors.
VR rules: no-DLL assets/plugins work in VR; SKSE DLLs need a VR build; ESL via Skyrim VR ESL Support; SE 1.6/CC-dependent plugins need the updated-masters path. VR specifics to weigh: VRAM (two eyes at high res — prefer 2K textures, 4K only for hero assets), draw calls/CPU (heavy city/clutter mods cost more in VR), real-world scale (VR-specific resizing mods), first-person visibility of hands/arms.
Prefer choices that the VR lists (esp. 2026 ones) actually ship; add strong 2025-2026 SE next-gen picks when VR-safe. Never invent file names/FOMOD options; evidence required. Human-facing text in RUSSIAN, short.`

const PICKS = {
  type: 'object',
  properties: {
    picks: { type: 'array', items: { type: 'object', properties: {
      id: { type: ['integer', 'null'] }, name: { type: 'string' }, url: { type: 'string' },
      section: { type: 'string', enum: SECTIONS },
      tag: { type: 'string', enum: ['rec', 'opt', 'alt', 'try', 'dont'] },
      choose_one_group: { type: ['string', 'null'] },
      what: { type: 'string', description: 'RU <=170 chars' },
      vr_status: { type: 'string', enum: ['works_as_is', 'vr_version_exists', 'vr_native', 'flat_only', 'unknown'] },
      files: { type: 'string', description: 'RU: which file/variant (e.g. 2K, VR patch), version pin' },
      requires: { type: 'array', items: { type: 'string' } },
      note: { type: 'string', description: 'RU: VR caveats, conflicts, perf/VRAM cost, ordering' },
      evidence: { type: 'string' },
    }, required: ['id', 'name', 'url', 'section', 'tag', 'choose_one_group', 'what', 'vr_status', 'files', 'requires', 'note', 'evidence'] } },
    section_leads: { type: 'array', items: { type: 'object', properties: { section: { type: 'string', enum: SECTIONS }, lead: { type: 'string', description: 'RU 1-2 sentences: how to approach this category in VR' } }, required: ['section', 'lead'] } },
    notes: { type: 'string' },
  },
  required: ['picks', 'section_leads', 'notes'],
}

const JOBS = [
  { key: 'gaps-1', prompt: `PART 1 (gaps), topics: alternate start (Realm of Lorkhan, Alternate Perspective, Ralof or Hadvar, Alternate Start LAL — which work in VR given the VR Playroom start?), follower framework (Nether's Follower Framework or alternatives — VR status), Navigate VR (+ Quest Markers for NavigateVR) and other VR navigation, controls & presets (VRIK configuration presets, controller bindings for Index/G2/Quest, FUS INI presets on GitHub Kvitekvist/FUS, Controller Fix VR, Skyrim VR Configuration Tool), save tools (FallrimTools ReSaver for VR saves), Immersive Equipment Displays (VR status!), voice commands (Dragonborn Speaks Naturally — VR, conflicts with AI-NPC microphone). Candidate pool to scan for relevant lines: ${D}/data/pools/other_world.txt. Sections to use: start, followers, navigation, controls, saves, equipment, voice. Up to 25 picks.` },
  { key: 'gaps-2', prompt: `PART 1 (gaps), topics: Russian localization for a VR modlist (xTranslator/ESP-ESM Translator tool workflow, where Russian translations live, Cyrillic-capable fonts for SkyUI VR/menus, Skyrim VR Strings Fix and Russian strings on the updated-masters path, Scaleform Translation++ VR already in core, Dynamic String Distributor already in core, Russian voice considerations), porting Anniversary Edition Creation Club content to Skyrim VR (infernalryan "Managing Creation Club Content" / "Skyrim Initial Setup (VR)" guidance: what works, what breaks in VR, required fixes), music/soundtrack replacers and additions (e.g. LORKHAN — check VR lists), niche hardware (bHaptics Tactsuit SkyrimVR integration, Natural Locomotion). Candidate pool: ${D}/data/pools/other_world.txt. Sections: russian, cc, music, niche. Up to 25 picks (guides/tools allowed as items with url).` },
  { key: 'tex-nature', prompt: `PART 2 (textures) — nature & terrain: VR texture strategy (2K default, VRAM budget, tools: VRAMr / Paraphernalia, Texture Downscaler, Cathedral Assets Optimizer — which do VR lists use?), landscapes/terrain (incl. PBR landscapes that work with Open Shaders, e.g. Vanilla PBR AIO, Sloppy Vanilla Landscapes PBR, Tomato's landscapes), mountains/rocks, flora textures matching Merethic Grasslands and Happy Little Trees, snow (Simplicity of Snow etc.), water/sky textures (Realistic Galaxy etc.), terrain LOD textures, Terrain Helper / terrain parallax with Open Shaders. Candidate pool: ${D}/data/pools/other_tex_nature.txt (scan all). Sections: tex_strategy, tex_land, tex_flora, tex_water_sky, tex_pbr_tools. Up to 30 picks; give choose_one groups for competing landscape packs.` },
  { key: 'tex-arch', prompt: `PART 2 (textures) — architecture & objects: cities/towns (Tomato's city PBR series, Noble Skyrim, etc.), dungeons/ruins/caves, interiors, clutter/furniture textures, PBR all-in-ones and how they interact with Open Shaders PBR/Complex Material, PGPatcher (ParallaxGen) workflow and Auto Parallax. Candidate pool: ${D}/data/pools/other_tex_arch.txt (scan all). Sections: tex_arch, tex_dungeons, tex_clutter, tex_pbr_tools. Up to 30 picks; give choose_one groups for competing packs.` },
  { key: 'chars-armor', prompt: `PART 3 (appearance) — characters & gear: bodies (CBBE 3BA / HIMBO / BodySlide and how they behave with VRIK hands/body), NPC face overhauls (VR close-up vs performance; high-poly heads), hair (Vanilla hair remake etc., SMP hair needs FSMP), eyes/skin, physics (CBPC VR with VR hand collisions, FSMP), VR-specific bodies (Vampire Body for VR, Werewolf Body for VR), armor/weapon/clothing meshes+textures that VR lists use (Faultier's PBR Armors, aMidianBorn, Cathedral Armory, Rustic Clothing, Vanilla Armor Skirt Clipping Fix, Better weapon collisions for VR). Candidate pool: ${D}/data/pools/other_chars.txt (skip creatures — another agent covers them). Sections: chars_body, chars_faces, physics, armor. Up to 30 picks; choose_one groups for body/face packs.` },
  { key: 'world-creatures', prompt: `PART 3 (appearance & world): creatures (models+textures: Rustic series, Mihail, Dragons SE, Draugrs/Falmer/Hagraven new models, Atronachs SE, "Creatures Resized for VR", animals), city/structure meshes (The Great Cities, Spaghetti's Palaces/Faction Halls, JK's — VR CPU cost!, Medieval Markets, Pleasantrees, FYX 3D meshes, Skyrim 3D Rocks/Signs, GDOS doors, SMIM/SMIM Improvement Mod), clutter/furniture/food meshes (Rally's series, JS series, Food Resized for VR scale), ReShade presets for VR on top of Open Shaders (The Sharper Eye, VrVision, Glamur ReShade VR, Arcturus ReShade II — which still make sense with Open Shaders' built-in sharpening/post-processing?). Candidate pools: ${D}/data/pools/other_world.txt and creature lines in ${D}/data/pools/other_chars.txt. Sections: creatures, city_meshes, clutter_meshes, reshade. Up to 30 picks.` },
]

// args: { only: ['gaps-2','tex-nature','tex-arch','chars-armor','world-creatures'], picksFile: 'skyrim-vr-modlist/data/other_picks.json' }
// Два шага: 1) сбор (only=[...]) -> tools/save_journal.py -> tools/merge_partials.py other-mods; 2) только проверка (picksFile=...) -> save_journal.py -> merge_partials.py
const ONLY = (args && args.only) || null
const PICKS_FILE = (args && args.picksFile) || null
phase('Collect')
const results = PICKS_FILE ? [] : await parallel(JOBS.filter(j => !ONLY || ONLY.includes(j.key)).map(j => () =>
  agent(`${CONTEXT}\n\nYOUR TASK: ${j.prompt}\nAlso add tag "dont" items for things popular in SE lists that should NOT go into VR (flat-only, heavy, superseded) when relevant to your topics. Every pick needs evidence.`,
    { label: `collect:${j.key}`, phase: 'Collect', schema: PICKS, effort: 'high' }).then(r => r ? { src: j.key, ...r } : null)))

// barrier: dedup across agents and give verifiers the full set for cross-item overlap checks
const all = [], seen = new Map(), leads = []
for (const r of results.filter(Boolean)) {
  leads.push(...r.section_leads.map(l => ({ ...l, src: r.src })))
  for (const p of r.picks) {
    const key = p.id ? `id:${p.id}` : `n:${p.name.toLowerCase().replace(/[^a-z0-9а-я]+/g, '')}`
    if (seen.has(key)) { seen.get(key).also.push(r.src); continue }
    const it = { key, src: r.src, also: [], ...p }; seen.set(key, it); all.push(it)
  }
}
log(`Collected ${all.length} unique picks`)
const notes = results.filter(Boolean).map(r => `${r.src}: ${r.notes}`)
if (!PICKS_FILE && !all.length) return { notes, leads, verified: [] }
if (ONLY && !PICKS_FILE) return { notes, leads, picks: all }  // только сбор; проверка — вторым запуском с picksFile

const VERDICTS = { type: 'object', properties: { verdicts: { type: 'array', items: { type: 'object', properties: {
  key: { type: 'string' }, keep: { type: 'boolean' }, section: { type: 'string', enum: SECTIONS }, tag: { type: 'string', enum: ['rec', 'opt', 'alt', 'try', 'dont'] },
  choose_one_group: { type: ['string', 'null'] }, what: { type: 'string', description: 'RU polished one-liner <=170' }, note: { type: 'string', description: 'RU corrected VR/file/conflict note' }, reason: { type: 'string' },
}, required: ['key', 'keep', 'section', 'tag', 'choose_one_group', 'what', 'note', 'reason'] } } }, required: ['verdicts'] }
const listing = PICKS_FILE ? `read the JSON file ${PICKS_FILE} (array under "picks", each has key, name, url, section, tag, choose_one_group, what, vr_status, files, requires, note, evidence)` : JSON.stringify(all.map(({ key, id, name, url, section, tag, choose_one_group, what, vr_status, files, requires, note, evidence }) => ({ key, id, name, url, section, tag, choose_one_group, what, vr_status, files, requires, note, evidence })), null, 1)
const LENSES = [
  { key: 'vr-compat', prompt: 'You are a VR-COMPATIBILITY SKEPTIC. Try to refute each VR claim (DLL without VR build, flat-only, needs SE-only framework, breaks with VRIK body). Check with whouses.py file names and quick searches. Unproven but plausible → keep with tag "try" and a note on how to test. Wrong → keep=false (or tag "dont" if people would copy it).' },
  { key: 'value-perf', prompt: 'You are a VALUE / VR-PERFORMANCE / REDUNDANCY SKEPTIC. Try to refute each item: duplicates the core list or another pick (keep the better; enforce choose_one groups), VRAM/CPU cost unjustified in VR (4K everywhere, heavy cities), outdated/superseded by a 2025-2026 option, falls into an EXCLUDED category (content, difficulty overhauls, spell packs, narrow SimonRim, NSFW, followers-as-characters). Assign the best section and tag, write the final RU one-liner and note.' },
]
phase('Verify')
const lens = await parallel(LENSES.map(l => () => agent(`${CONTEXT}\n\n${l.prompt}\n\nReturn one verdict per key. PICKS:\n${listing}`, { label: `verify:${l.key}`, phase: 'Verify', schema: VERDICTS, effort: 'high' })))
const maps = lens.map(r => new Map((r ? r.verdicts : []).map(v => [v.key, v])))
const verified = all.map(p => { const a = maps[0].get(p.key), b = maps[1].get(p.key); return { ...p, compat: a || null, value: b || null, keep: !!(a && b && a.keep && b.keep) } })
if (PICKS_FILE) return { lens: lens.map(r => r ? r.verdicts : []) }  // склейка с кандидатами — tools/merge_partials.py
log(`Kept by both: ${verified.filter(v => v.keep).length}/${verified.length}`)
return { notes, leads, verified }
