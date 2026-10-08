export const meta = {
  name: 'skyrim-vr-install-spec',
  description: 'Enrich the 275-mod Skyrim VR manifest with per-mod install specs (files, FOMOD, requirements, conflicts, order, verification), verify the MO2/tool procedure, then cross-check consistency',
  phases: [
    { title: 'Enrich', detail: '6 section groups + 1 procedure fact-check' },
    { title: 'Critic', detail: 'cross-consistency: missing requirements, choose-one groups, do-not-install contradictions, ordering' },
  ],
}

const D = (typeof args !== 'undefined' && args && args.root) || 'skyrim-vr-modlist'  // args.root — абсолютный путь к папке проекта, если cwd не её родитель
const K = D + '/data/kit'

const CONTEXT = `
Goal: produce an installation spec that a LOCAL Claude agent will follow to install a Skyrim VR modlist in Mod Organizer 2 correctly — right files, right FOMOD choices, all requirements and patches, conflicts pre-solved. Game: Skyrim VR 1.4.15, SKSEVR 2.0.12, MO2 2.5.2 portable + Root Builder 5.x. Today 2026-10-08. Textures are a later stage.
The full draft manifest (275 mods, with the curator's notes, tags core/rec/opt/alt/try, VR-file hints and research evidence) is ${K}/draft_manifest.json — includes "dont" (do-not-install list), "gen_steps" (final generation pipeline) and "mo2_order".
Data helpers: ${D}/data/rep/*.json = full archive lists of 27 popular Wabbajack lists (9 VR); python3 -I ${D}/tools/whouses.py <nexus id or name> shows which lists use a mod and the EXACT archive file names (reveals which Nexus file variant VR lists pick, e.g. "...VR-12345-...", "PapyrusUtil VR ..."). Web: load WebSearch/WebFetch via ToolSearch; nexusmods.com, modding.wiki, schaken-mods, synergyvr.org are BLOCKED for fetch — use search snippets, GitHub repos/READMEs/release pages (github.com and raw.githubusercontent.com work).
Strict honesty rules: never invent FOMOD option names, file names or requirements. If you don't have evidence, say "неизвестно — общие правила" (the local agent will read the real installer). Mark uncertain facts with confidence low/medium. Write all human-facing text in RUSSIAN, short and imperative.`

const ITEM = {
  type: 'object',
  properties: {
    key: { type: 'string' },
    kind: { type: 'string', enum: ['plugin_only', 'skse_dll', 'assets_only', 'mixed', 'external_tool', 'mo2_plugin', 'root_files', 'guide_steps'] },
    install_target: { type: 'string', enum: ['mo2_mod', 'root_builder', 'external_tool', 'mo2_plugins_folder', 'manual_steps'] },
    files: { type: 'string', description: 'RU: which file(s) to take from the Nexus Files tab (main/optional/VR variant, version pin), based on evidence' },
    fomod: { type: 'string', description: 'RU: known installer choices with evidence, "нет установщика", or "неизвестно — общие правила"' },
    requires: { type: 'array', items: { type: 'string' }, description: 'requirements as "Name (#id)" when known' },
    requires_missing: { type: 'array', items: { type: 'string' }, description: 'requirements NOT present in draft_manifest.json — must be added' },
    incompatible_with: { type: 'array', items: { type: 'string' } },
    choose_one_group: { type: ['string', 'null'], description: 'short id of a mutually-exclusive group, e.g. "shaders", "footprints", "water"' },
    mo2_order: { type: 'string', description: 'RU: left-pane priority/overwrite rule (what must load after/before or win), empty if none' },
    plugin_order: { type: 'string', description: 'RU: plugin load-order rule beyond LOOT, empty if none' },
    config: { type: 'string', description: 'RU: INI/MCM/JSON settings to apply after install, empty if none' },
    verify: { type: 'string', description: 'RU: how to confirm it works in VR (sksevr.log line, in-game check)' },
    risk: { type: 'string', enum: ['low', 'medium', 'high'] },
    confidence: { type: 'string', enum: ['high', 'medium', 'low'] },
    sources: { type: 'string' },
  },
  required: ['key', 'kind', 'install_target', 'files', 'fomod', 'requires', 'requires_missing', 'incompatible_with', 'choose_one_group', 'mo2_order', 'plugin_order', 'config', 'verify', 'risk', 'confidence', 'sources'],
}
const GROUP_SCHEMA = { type: 'object', properties: { items: { type: 'array', items: ITEM }, group_notes: { type: 'string' } }, required: ['items', 'group_notes'] }

const GROUPS = [
  { key: 'g1a_tools_base_frameworks', hint: 'tools (MO2, Root Builder, xEdit, LOOT, BethINI Pie, Pandora, Synthesis, DynDOLOD, xLODGen...), masters/USSEP paths A and B, SKSEVR and libraries. Pay special attention to install_target root_builder (SKSEVR loader/dll, Engine Fixes VR Part 2), the "main mod + VR DLL overwrites" pattern (Papyrus Extender, po3 Tweaks, CDF, Light Placer), and which file variant VR lists pick (PapyrusUtil VR, JContainers VR, KID VR file, SkyPatcher VR file, I4 VR file).' },
  { key: 'g1b_fixes', hint: 'engine/bug fixes and performance plugins. Identify DLL vs plugin, VR file variants (e.g. PrivateProfileRedirector VR 0.6.2), overlaps with Engine Fixes VR / Poached Bugs VR / Papyrus Tweaks NG.' },
  { key: 'g2_gfx_world_land', hint: 'Open Shaders vs CSX (choose one), Light Placer/CS Light/Lux/Embers XD interplay (CS Light options), Azurite III add-ons, water choose-one, Moons and Stars 2.0.2 + SKSEVR DLL pin, Splashes VR DLLs, grass (NGIO cache config: GrassControl.ini keys), trees+DynDOLOD add-on, snow/footprints choose-one groups, perf items (OpenComposite Unleashed — root files, VR FPS Stabilizer).' },
  { key: 'g3_vr_hitech_ui', hint: 'VRIK/HIGGS/PLANCK chain and their add-ons (exact dependency chains: Physical Collision VR → True Wield VR etc., Pull Arrows VR needs Broken Feathers + Weapon Throw VR), hitech 2026 items (Helios + Luma/MMSF/XEMI version pins, Smooth Terrain, Inventory Selfie VR Redux needs VRIK 0.8.7+), UI (SkyUI VR, Floating Subtitles VR needs ImGui VR Helper and base Floating Subtitles?, Essential Favorites VR, RacemenuVR vs RaceMenu VR 2 choose-one).' },
  { key: 'g4_anim_combat', hint: 'OAR packs (OAR-only variants, not DAR), XPMSSE + VR first-person skeleton fix ordering, FSMP VR variant, SimonRim (Adamant/Mysticism/Thaumaturgy/Apothecary/Mundus) + Poached Bugs VR Simonrim Choice Config, Blade and Blunt + VR, DF + asset packs, CIF + Sanguine Symphony.' },
  { key: 'g5_immersion_audio_ai', hint: 'AI behavior plugins (AI Overhaul file choice per USSEP path), CPR + VR DLL, Enhanced Reanimation + VR file, FEC VR page, audio stack (AOS + RSE + RISE + ASIF vs ISC choose-one, SRD requirement), AI-NPC choose-one (SkyrimNet/Mantella/CHIM) with their VR requirements.' },
]

const enrichPrompt = g => `${CONTEXT}

YOUR GROUP: ${K}/${g.key}.json (array of draft manifest items; keep each item's "key"). Focus: ${g.hint}
For EVERY item return a spec object. Use the curator note + research fields as the starting point, then verify/extend with whouses.py file names, GitHub READMEs and search snippets. Requirements: list real dependencies (most SKSE DLLs need SKSEVR + VR Address Library — state that explicitly when it is a DLL). Put any dependency that is not itself in draft_manifest.json into requires_missing (e.g. "Broken Feathers"). Use choose_one_group consistently with these ids when applicable: shaders, water, footprints, snow-deformation, grass, ai-npc, behavior-engine, subtitles, racemenu, hud-clean, audio-stack, masters-path, opencomposite, climbing, item-info (I4/I5), mcm-backup.`

const PROCEDURE_PROMPT = `${CONTEXT}

YOUR TASK: fact-check the PROCEDURE the local agent will follow, for Skyrim VR specifically. For each topic give the correct steps, exact paths/arguments where you can verify them, and a confidence + source. Topics:
1) MO2 2.5.2 portable instance for Skyrim VR; profile-specific INIs and saves; where modlist.txt/plugins.txt/loadorder.txt live and their ordering semantics (is modlist.txt top = highest priority?); how separators are stored; meta.ini basics; whether editing these files with MO2 closed is safe.
2) Root Builder 5.x (Kezyma) for Skyrim VR: the "Root" folder convention inside a mod, copy vs link vs usvfs modes, what to put there (sksevr_loader.exe + sksevr_1_4_15.dll, Engine Fixes VR Part 2 files, OpenComposite openvr_api.dll), how to launch SKSEVR via MO2 executables.
3) SKSEVR 2.0.12 install specifics; sksevr.log location (Documents/My Games/Skyrim VR/SKSE/?) and how a failed plugin load appears.
4) Engine Fixes VR 7.x: Part 1/Part 2, config file name and the MaxStdio setting key/section; required by Skyrim VR ESL Support.
5) OpenComposite for Skyrim VR (OpenComposite Unleashed #171182 if info exists; otherwise generic): which file replaces what, opencomposite.ini, OpenXR runtime selection (SteamVR/VDXR/Oculus).
6) xEdit in VR mode (-tes5vr / TES5VREdit naming) and Quick Auto Clean of Update/Dawnguard/HearthFires/Dragonborn.
7) LOOT with Skyrim VR in MO2.
8) Pandora Behaviour Engine+ for Skyrim VR: run from MO2, output folder/mod, VR caveats (4.1.2 re-added VR).
9) DynDOLOD 3 for Skyrim VR: TES5VR mode (exe naming/argument -tes5vr), TexGen, output as mods, DynDOLOD DLL NG; xLODGen for VR (TES5VRLODGenx64 naming or -tes5vr), terrain resource.
10) NGIO grass precache in Skyrim VR: GrassControl.ini keys, PrecacheGrass.txt location for VR, MO2 Precache Grass plugin, Grass Cache Helper NG.
11) Synthesis with Skyrim VR (game release selection), output to its own mod.
12) BethINI Pie + Skyrim VR plugin; INI locations for VR (Documents/My Games/Skyrim VR/SkyrimVR.ini, SkyrimPrefs.ini) vs MO2 profile INIs.
13) Updated-masters path A (infernalryan "Skyrim Initial Setup (VR)" / "Updating Game Masters"): what is copied (masters, strings, 4 free CC files), packaged as an MO2 mod, plus Strings Fix / Survival prompt removal; and path B (USSEP 4.2.5b + #91475).
Return structured facts.`

const FACTS = {
  type: 'object',
  properties: { facts: { type: 'array', items: { type: 'object', properties: {
    topic: { type: 'string' }, steps: { type: 'string', description: 'RU, precise steps/paths/args' },
    confidence: { type: 'string', enum: ['high', 'medium', 'low'] }, sources: { type: 'string' },
  }, required: ['topic', 'steps', 'confidence', 'sources'] } }, caveats: { type: 'string' } },
  required: ['facts', 'caveats'],
}

// args: { only: ['g3_vr_hitech_ui', ..., 'procedure', 'critic'], specsFile: 'skyrim-vr-modlist/data/specs_merged.json' }
const ONLY = (args && args.only) || null
const SPECS_FILE = (args && args.specsFile) || null
phase('Enrich')
const jobs = GROUPS.filter(g => !ONLY || ONLY.includes(g.key)).map(g => () => agent(enrichPrompt(g), { label: `enrich:${g.key}`, phase: 'Enrich', schema: GROUP_SCHEMA, effort: 'high' }).then(r => r ? { group: g.key, ...r } : null))
if (!ONLY || ONLY.includes('procedure')) jobs.push(() => agent(PROCEDURE_PROMPT, { label: 'procedure:fact-check', phase: 'Enrich', schema: FACTS, effort: 'high' }).then(r => r ? { group: 'procedure', ...r } : null))
const res = await parallel(jobs)
const groups = res.filter(Boolean).filter(r => r.group !== 'procedure')
const procedure = res.filter(Boolean).find(r => r.group === 'procedure') || null
const specs = groups.flatMap(g => g.items)
log(`Enriched specs: ${specs.length}; procedure facts: ${procedure ? procedure.facts.length : 0}`)

// barrier justified: the critic must see ALL specs at once to find cross-mod contradictions
if (ONLY && !ONLY.includes('critic')) return { specs, group_notes: groups.map(g => `${g.group}: ${g.group_notes}`), procedure }
const compact = specs.map(s => ({ key: s.key, kind: s.kind, target: s.install_target, files: s.files, fomod: s.fomod, requires: s.requires, missing: s.requires_missing, incompatible: s.incompatible_with, group: s.choose_one_group, mo2_order: s.mo2_order, plugin_order: s.plugin_order }))
const CRITIC = {
  type: 'object',
  properties: {
    add_requirements: { type: 'array', items: { type: 'object', properties: { name: { type: 'string' }, id: { type: ['integer', 'null'] }, needed_by: { type: 'array', items: { type: 'string' } }, separator_section: { type: 'string' }, note: { type: 'string' } }, required: ['name', 'id', 'needed_by', 'separator_section', 'note'] } },
    choose_one_groups: { type: 'array', items: { type: 'object', properties: { group: { type: 'string' }, members: { type: 'array', items: { type: 'string' } }, default: { type: 'string' }, rule: { type: 'string' } }, required: ['group', 'members', 'default', 'rule'] } },
    contradictions: { type: 'array', items: { type: 'object', properties: { keys: { type: 'array', items: { type: 'string' } }, problem: { type: 'string' }, fix: { type: 'string' } }, required: ['keys', 'problem', 'fix'] } },
    order_rules: { type: 'array', items: { type: 'string' }, description: 'RU: consolidated MO2 left-pane overwrite rules, most important first' },
    plugin_rules: { type: 'array', items: { type: 'string' }, description: 'RU: consolidated plugin load-order rules beyond LOOT' },
  },
  required: ['add_requirements', 'choose_one_groups', 'contradictions', 'order_rules', 'plugin_rules'],
}
phase('Critic')
const critic = await agent(`${CONTEXT}

You are the CONSISTENCY CRITIC for the whole spec. Inputs: draft manifest ${K}/draft_manifest.json (items + "dont" list) and the enriched specs below. Find and fix: (1) requirements referenced anywhere that are not in the manifest (deduplicate, give Nexus id if you can verify; skip if it is only needed by an optional mod AND you cannot identify it — then put it in contradictions with fix "уточнить вручную"); (2) mutually exclusive mods both marked core/rec without a choose-one group; (3) any manifest item that matches the "dont" list or an SE-only twin; (4) circular or contradictory ordering rules; (5) items whose kind/target look wrong (e.g. root files not via Root Builder). Consolidate the MO2 overwrite rules and plugin rules into ordered lists.

${SPECS_FILE ? `ENRICHED SPECS: read the JSON file ${SPECS_FILE} (array under "specs"; each item has key, kind, install_target, files, fomod, requires, requires_missing, incompatible_with, choose_one_group, mo2_order, plugin_order). The manifest ${K}/draft_manifest.json lists all mods.` : `ENRICHED SPECS (${compact.length}):\n${JSON.stringify(compact)}`}`, { label: 'critic:consistency', phase: 'Critic', schema: CRITIC, effort: 'high' })

return { specs, group_notes: groups.map(g => `${g.group}: ${g.group_notes}`), procedure, critic }
