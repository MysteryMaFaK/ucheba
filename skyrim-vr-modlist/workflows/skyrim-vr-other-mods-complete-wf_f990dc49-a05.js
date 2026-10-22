export const meta = {
  name: 'skyrim-vr-other-mods-complete',
  description: 'Second pass for "Other Mods 2026": evaluate EVERY previously unevaluated candidate from the 27 lists (batches by popularity band), double-verify for VR, consolidate duplicates/groups, completeness critic; lower bands run only if a pilot shows they are not dry',
  phases: [
    { title: 'Evaluate', detail: 'one agent per batch: a disposition for every candidate' },
    { title: 'Verify', detail: 'VR-compat skeptic + value/perf/redundancy skeptic per batch' },
    { title: 'Consolidate', detail: 'cross-batch duplicates, choose-one groups, MO2 order notes' },
    { title: 'Critic', detail: 'what is still missing' },
  ],
}

const D = (args && args.root) || 'skyrim-vr-modlist'
const BANDS = (args && args.bands) || ['A', 'B']
const SIZES = (args && args.sizes) || {}
const ONLY = (args && args.only) || null
const DRY = (args && typeof args.dryThreshold === 'number') ? args.dryThreshold : 0.12
const SKIP_CONSOLIDATE = !!(args && args.skipConsolidate)

const SECTIONS = ['start','followers','navigation','controls','russian','saves','cc','equipment','voice','music','niche',
  'tex_strategy','tex_land','tex_flora','tex_water_sky','tex_arch','tex_dungeons','tex_clutter','tex_pbr_tools',
  'chars_body','chars_faces','physics','armor','creatures','city_meshes','clutter_meshes','reshade','misc','dont','none']
const SEC_RU = 'start=alternate start; followers=follower framework; navigation; controls=controls/presets; russian=localization; saves; cc=Creation Club; equipment=gear on body; voice=voice commands; music; niche=haptics/locomotion; tex_strategy=VRAM strategy/tools; tex_land=landscape/mountains; tex_flora; tex_water_sky; tex_arch=cities/architecture textures; tex_dungeons=dungeons/ruins textures; tex_clutter=clutter/furniture textures; tex_pbr_tools=PBR and patchers; chars_body=bodies; chars_faces=faces/hair/eyes/skin; physics=body/cloth physics; armor=armor/weapons/clothing; creatures; city_meshes=city/structure meshes; clutter_meshes=clutter/furniture/food meshes; reshade; misc=other useful tools/additions that fit no section; dont=do-not-install-in-VR list; none=dropped'

const CONTEXT = `
Project: a Skyrim VR modlist (Skyrim VR 1.4.15, SKSEVR 2.0.12, MO2). Today 2026-10-09. Two lists already exist:
 (1) "Core 2026" (275 mods: frameworks, fixes, VR physics, Open Shaders 2.17 as the shader stack, Lux + Light Placer + CS Light, Azurite Weathers III, Merethic Grasslands, Happy Little Trees, DynDOLOD, OAR, SimonRim core, SkyUI VR, RaceMenu VR, etc.). Inventory: ${D}/MODLIST.md, ${D}/data/page_items.txt, ${D}/tools/additions.py.
 (2) "Other Mods 2026", FIRST PASS (128 mods + 23 do-not-install: core gaps, textures, appearance/world). Inventory: ${D}/OTHER_MODS.md (and ${D}/data/other_result.json).
Read the inventories (grep as needed) and do NOT re-propose anything already in them; if a candidate is superseded by or duplicates a listed mod, drop it with a pointer to the listed one.
WHY THIS PASS EXISTS: the first pass was capped (~30 picks per collector) and left ~1000 popular candidates never evaluated. Your batch is part of that unevaluated set (mods used by the 27 popular Wabbajack lists: 9 VR + 18 SE next-gen). Be complete: every candidate gets a disposition.
EXCLUDED entirely (drop with drop_code "excluded_category"): quest/new-land/dungeon content, dialogue/lines packs, followers and NPC-character mods (a follower FRAMEWORK is fine), player homes, big difficulty overhauls (Requiem, Wildlander, Ordinator, Vokrii), new spell/shout packs (Apocalypse, Odin, Arcanum, Triumvirate, Thunderchild), narrow SimonRim parts (Aetherius, Scion, Manbeast, Pilgrim), NSFW. NOT excluded: bodies (CBBE 3BA/HIMBO/BodySlide), NPC faces/hair/eyes, armor/weapon/clothing meshes+textures, creatures, city/structure meshes, clutter/furniture, ReShade, all textures.
Data: ${D}/data/rep/*.json = archive lists of the 27 lists. Helper: python3 -I ${D}/tools/whouses.py <nexus id or name> → which lists use it + exact archive file names (shows which FILE VARIANT the VR lists pick, e.g. 2K vs 4K, VR patches). The batch file items also carry the first archive names and the VR lists.
Web: load WebSearch/WebFetch via ToolSearch; nexusmods.com, modding.wiki, schaken-mods, synergyvr.org are BLOCKED for fetch — use search snippets, GitHub, Reddit mirrors. Use the web only for items you do not already know; do not burn effort on obvious ones.
Shader stack facts: Open Shaders 2.17 (VR fork of Community Shaders) — PBR/Complex Material on it in VR is NOT confirmed by any VR list (Stormcrown VR uses CSX 3.19.1-VR + PGPatcher; Yggdrasil VR with Open Shaders 2.17 ships classic non-PBR textures). So PBR-only texture packs are "try" at best, with a note.
VR rules: no-DLL assets/plugins work in VR; SKSE DLLs need a VR build; ESL via Skyrim VR ESL Support; SE 1.6/CC-dependent plugins need the updated-masters path. VR specifics to weigh: VRAM (two eyes at high res — prefer 2K, 4K only for hero assets, 1K for small clutter), draw calls/CPU (heavy city/clutter mods cost more in VR), real-world scale, first-person visibility of hands/arms, ENB-only add-ons are useless (no ENB in VR here).
Quality bar: this is a CURATED recommended-extras list for a VR build, not a dump of everything popular. Popularity is a prior, not a verdict: keep what adds clear, VR-relevant value and does not fight the core stack. When several mods compete (armor retextures, hair packs, body presets, creature models, landscapes), keep the best one or two and put them in a choose_one group; drop the rest as redundant. Never invent file names, FOMOD options or VR status; evidence required. Human-facing text in RUSSIAN, short.`

const EVAL = { type: 'object', properties: {
  entries: { type: 'array', items: { type: 'object', properties: {
    key: { type: 'string', description: 'copy EXACTLY from the batch item' },
    id: { type: ['integer', 'null'] }, name: { type: 'string' }, url: { type: 'string', description: 'https://www.nexusmods.com/skyrimspecialedition/mods/<id> unless the mod lives elsewhere (GitHub...)' },
    decision: { type: 'string', enum: ['keep', 'dont', 'drop'] },
    drop_code: { type: 'string', enum: ['none', 'excluded_category', 'covered_elsewhere', 'superseded', 'redundant_in_batch', 'vr_incompatible', 'vram_cpu_cost', 'low_value', 'not_an_asset', 'unclear'] },
    section: { type: 'string', enum: SECTIONS }, tag: { type: 'string', enum: ['rec', 'opt', 'alt', 'try', 'dont', 'none'] },
    choose_one_group: { type: ['string', 'null'] },
    what: { type: 'string', description: 'RU <=170 chars; empty for drops' },
    vr_status: { type: 'string', enum: ['works_as_is', 'vr_version_exists', 'vr_native', 'flat_only', 'unknown', 'n/a'] },
    files: { type: 'string', description: 'RU: which file/variant (2K, VR patch), version pin; empty for drops' },
    requires: { type: 'array', items: { type: 'string' } },
    note: { type: 'string', description: 'keep/dont: RU VR caveats, conflicts, perf/VRAM cost, ordering. drop: RU one-line reason (name the listed mod if it is covered elsewhere)' },
    evidence: { type: 'string', description: 'which lists/file names/URLs support the decision' },
    member_ids: { type: 'array', items: { type: 'integer' }, description: 'series items only: Nexus ids of the members to keep (empty = single mod or whole series)' },
  }, required: ['key', 'id', 'name', 'url', 'decision', 'drop_code', 'section', 'tag', 'choose_one_group', 'what', 'vr_status', 'files', 'requires', 'note', 'evidence', 'member_ids'] } },
  batch_notes: { type: 'string', description: 'RU: what stayed unclear, which pages/files must be checked locally on Nexus' },
}, required: ['entries', 'batch_notes'] }

const VERDICTS = { type: 'object', properties: { verdicts: { type: 'array', items: { type: 'object', properties: {
  key: { type: 'string' }, keep: { type: 'boolean' }, section: { type: 'string', enum: SECTIONS }, tag: { type: 'string', enum: ['rec', 'opt', 'alt', 'try', 'dont'] },
  choose_one_group: { type: ['string', 'null'] }, what: { type: 'string', description: 'RU polished one-liner <=170' }, note: { type: 'string', description: 'RU corrected VR/file/conflict note' }, reason: { type: 'string' },
}, required: ['key', 'keep', 'section', 'tag', 'choose_one_group', 'what', 'note', 'reason'] } } }, required: ['verdicts'] }

const LENSES = [
  { key: 'vr-compat', prompt: 'You are a VR-COMPATIBILITY SKEPTIC. Try to refute each VR claim (SKSE DLL without VR build, flat-only, needs an SE-only framework, breaks with VRIK body/hands, ENB-only, needs PBR path unconfirmed on Open Shaders 2.17). Check with whouses.py file names and quick searches. Unproven but plausible → keep with tag "try" and a note on how to test. Wrong → keep=false (or tag "dont" if people would copy it).' },
  { key: 'value-perf', prompt: 'You are a VALUE / VR-PERFORMANCE / REDUNDANCY SKEPTIC. Try to refute each item: duplicates the Core list, the first-pass Other list (read OTHER_MODS.md) or another pick in your batch (keep the better; enforce choose_one groups), VRAM/CPU cost unjustified in VR (4K everywhere, heavy cities/clutter), outdated/superseded by a 2025-2026 option, falls into an EXCLUDED category, or is a trivial low-value tweak. Assign the best section and tag, write the final RU one-liner and note. Be strict: a short, strong list beats a long one.' },
]

const ids = []
for (const b of BANDS) for (const [k] of Object.entries(SIZES)) if (k[0] === b && (!ONLY || ONLY.includes(k))) ids.push(k)
ids.sort()
if (!ids.length) return { error: 'no batches: pass args.sizes and args.bands/only' }

async function evalBatch(id) {
  const n = SIZES[id]
  const file = `${D}/data/other2/batches/${id}.json`
  const base = `${CONTEXT}\n\nSection codes: ${SEC_RU}.\n\nYOUR TASK: evaluate EVERY item of the batch file ${file} (JSON: items[] with key, id, name, vr/se list counts, vr_lists, files = archive names, theme, and for series "members"). The batch has exactly ${n} items. Return exactly one entry per item, copying "key" exactly — no omissions, no merging (the script re-asks for any missing key). Procedure per item: 1) python3 -I ${D}/tools/whouses.py <id> (batch it with a shell loop to save turns); 2) identify what the mod is (your knowledge first; web only when unsure); 3) decide: decision "keep" (goes to the verifier stage; set section/tag/what/files/requires/note/evidence), "dont" (popular in SE lists but must NOT be installed in VR — say why in note), or "drop" (drop_code + one-line RU reason in note). For a series item decide for the series as a whole: keep all members, or keep only the best ones via member_ids, or drop. Tags: rec = recommended, opt = optional, alt = one of a choose_one group, try = VR claimed but unproven (install one by one), dont = do-not-install. Evidence for every keep/dont.`
  let entries = [], notes = [], tries = 0
  while (tries < 3) {
    const have = new Set(entries.map(e => e.key))
    const prompt = tries === 0 ? base : `${base}\n\nRETRY: you (or a previous agent) already returned entries for these keys: ${JSON.stringify([...have])}. Evaluate ONLY the items of the batch file whose key is NOT in that list (${n - have.size} items) and return entries for exactly those.`
    const r = await agent(prompt, { label: `collect:r2-${id}${tries ? '-retry' + tries : ''}`, phase: 'Evaluate', schema: EVAL, effort: 'high' })
    if (r) { for (const e of r.entries) if (!have.has(e.key)) { entries.push(e); have.add(e.key) } notes.push(r.batch_notes) }
    tries++
    if (new Set(entries.map(e => e.key)).size >= n) break
  }
  const got = new Set(entries.map(e => e.key)).size
  if (got < n) log(`batch ${id}: only ${got}/${n} dispositions after ${tries} tries`)
  return { id, n, got, entries, notes }
}

async function verifyBatch(ev) {
  if (!ev) return null
  const picks = ev.entries.filter(e => e.decision !== 'drop')
  const out = { id: ev.id, n: ev.n, got: ev.got, kept: 0, dont: 0, dropped: ev.entries.length - picks.length, picks: [] }
  if (!picks.length) return out
  const listing = JSON.stringify(picks.map(({ key, id, name, url, section, tag, choose_one_group, what, vr_status, files, requires, note, evidence, member_ids, decision }) => ({ key, id, name, url, decision, section, tag, choose_one_group, what, vr_status, files, requires, note, evidence, member_ids })), null, 1)
  const lens = await parallel(LENSES.map(l => () => agent(`${CONTEXT}\n\n${l.prompt}\n\nReturn one verdict per key (all ${picks.length}). Batch file with the full original context of each candidate: ${D}/data/other2/batches/${ev.id}.json. PICKS:\n${listing}`, { label: `verify:${l.key}-r2-${ev.id}`, phase: 'Verify', schema: VERDICTS, effort: 'high' })))
  const maps = lens.map(r => new Map((r ? r.verdicts : []).map(v => [v.key, v])))
  for (const p of picks) {
    const a = maps[0].get(p.key), b = maps[1].get(p.key)
    const keep = !!(a && b && a.keep && b.keep)
    out.picks.push({ ...p, compat: a || null, value: b || null, keep })
    if (keep) { if ((a.tag === 'dont' || b.tag === 'dont' || b.section === 'dont')) out.dont++; else out.kept++ }
  }
  return out
}

function trim(p) {
  const v = p.value || {}, c = p.compat || {}
  return { key: p.key, id: p.id, name: p.name, section: v.section || p.section, tag: (c.tag === 'try' && v.tag !== 'dont') ? 'try' : (v.tag || p.tag), group: v.choose_one_group || c.choose_one_group || p.choose_one_group, what: v.what || p.what, files: p.files, requires: p.requires, note: v.note || p.note, vr: p.vr_status, members: p.member_ids }
}

async function runBatches(list, label) {
  const res = (await pipeline(list, id => evalBatch(id), (ev) => verifyBatch(ev))).filter(Boolean)
  const nn = res.reduce((s, r) => s + r.n, 0), kk = res.reduce((s, r) => s + r.kept + r.dont, 0)
  log(`${label}: ${res.length}/${list.length} batches, ${nn} candidates, kept by both ${kk} (${nn ? Math.round(100 * kk / nn) : 0}%)`)
  return res
}

phase('Evaluate')
const main = ids.filter(i => BANDS.includes(i[0]) && 'AB'.includes(i[0]))
let results = main.length ? await runBatches(main, 'bands A+B') : []

// lower bands: pilot first (4 evenly spaced batches), the rest only if the pilot is not dry
const dryLog = []
for (const b of ['C', 'D']) {
  if (!BANDS.includes(b)) continue
  const list = ids.filter(i => i[0] === b)
  if (!list.length) continue
  const step = Math.max(1, Math.ceil(list.length / 4))
  const pilot = list.filter((_, i) => i % step === 0)
  const pr = await runBatches(pilot, `band ${b} pilot`)
  const n = pr.reduce((s, r) => s + r.n, 0), k = pr.reduce((s, r) => s + r.kept + r.dont, 0), rate = n ? k / n : 0
  results.push(...pr)
  if (rate >= DRY) {
    log(`band ${b} not dry (${Math.round(rate * 100)}% >= ${Math.round(DRY * 100)}%): running the remaining ${list.length - pilot.length} batches`)
    results.push(...await runBatches(list.filter(i => !pilot.includes(i)), `band ${b} rest`))
    dryLog.push({ band: b, pilotRate: rate, ranAll: true })
  } else {
    log(`band ${b} DRY (${Math.round(rate * 100)}% < ${Math.round(DRY * 100)}%): NOT evaluated: ${list.length - pilot.length} batches (${list.filter(i => !pilot.includes(i)).join(',')})`)
    dryLog.push({ band: b, pilotRate: rate, ranAll: false, skipped: list.filter(i => !pilot.includes(i)) })
    break
  }
}

const kept = results.flatMap(r => r.picks.filter(p => p.keep))
const bySection = {}
for (const p of kept) { const t = trim(p); bySection[t.section] = (bySection[t.section] || 0) + 1 }
const dropCodes = {}
for (const r of results) for (const p of r.picks) {}
log(`kept by both: ${kept.length}; by section: ${JSON.stringify(bySection)}`)

let consolidation = [], critic = null
if (!SKIP_CONSOLIDATE && kept.length) {
  phase('Consolidate')
  const CLUSTERS = [
    ['tex_strategy', 'tex_pbr_tools', 'tex_land', 'tex_flora', 'tex_water_sky'],
    ['tex_arch', 'tex_dungeons', 'tex_clutter', 'city_meshes', 'clutter_meshes'],
    ['chars_body', 'chars_faces', 'physics'],
    ['armor'],
    ['creatures', 'reshade', 'misc'],
    ['start', 'followers', 'navigation', 'controls', 'russian', 'saves', 'cc', 'equipment', 'voice', 'music', 'niche'],
    ['dont'],
  ]
  const CONSOL = { type: 'object', properties: {
    adjustments: { type: 'array', items: { type: 'object', properties: {
      key: { type: 'string' }, action: { type: 'string', enum: ['keep', 'drop_duplicate', 'regroup', 'retag', 'move_section'] },
      section: { type: 'string', enum: SECTIONS }, tag: { type: 'string', enum: ['rec', 'opt', 'alt', 'try', 'dont'] }, choose_one_group: { type: ['string', 'null'] }, reason: { type: 'string' },
    }, required: ['key', 'action', 'section', 'tag', 'choose_one_group', 'reason'] } },
    groups: { type: 'array', items: { type: 'object', properties: { group: { type: 'string' }, members: { type: 'array', items: { type: 'string' } }, default_pick: { type: 'string' }, rule: { type: 'string', description: 'RU: how to choose' } }, required: ['group', 'members', 'default_pick', 'rule'] } },
    order_rules: { type: 'array', items: { type: 'string' }, description: 'RU: MO2 order / overwrite / patch-order rules for these sections (bodies before armor, BodySlide, landscape order, etc.)' },
    conflicts: { type: 'array', items: { type: 'string' }, description: 'RU: concrete conflicts among kept mods or with Core/first-pass Other' },
    notes: { type: 'string' },
  }, required: ['adjustments', 'groups', 'order_rules', 'conflicts', 'notes'] }
  const jobs = CLUSTERS.map((secs, i) => ({ secs, items: kept.map(trim).filter(t => secs.includes(t.section)) })).filter(j => j.items.length)
  consolidation = (await parallel(jobs.map((j, i) => () => agent(`${CONTEXT}\n\nYOU ARE A CONSISTENCY EDITOR for sections [${j.secs.join(', ')}]. Below are the NEW second-pass picks (already verified twice). The FIRST-pass picks of these sections are in ${D}/OTHER_MODS.md (read the same sections) and the Core is in ${D}/MODLIST.md. Resolve across ALL of them: (a) duplicates/overlaps between new picks, and between new and first-pass picks (drop_duplicate the weaker NEW one; never touch first-pass items — instead say so in conflicts); (b) choose_one groups: consistent group names, exactly one default_pick per group, members listed by name (#id); (c) MO2 order and patch rules that matter for these sections (bodies before armor, BodySlide build, landscape/terrain-helper order, series overwrite order); (d) concrete conflicts with the Core or each other; (e) retag overlong lists: keep rec for the clear winners, opt for fine extras, try for unproven. Return an adjustment for EVERY key below (action keep if unchanged). NEW PICKS (${j.items.length}):\n${JSON.stringify(j.items, null, 1)}`,
    { label: `consolidate:r2-${i}`, phase: 'Consolidate', schema: CONSOL, effort: 'high' })))).filter(Boolean)

  phase('Critic')
  critic = await agent(`${CONTEXT}\n\nYOU ARE THE COMPLETENESS CRITIC. The second pass evaluated ${results.reduce((s, r) => s + r.n, 0)} candidates (bands ${BANDS.join('+')}; dry log: ${JSON.stringify(dryLog)}) and kept ${kept.length} by both verifiers. Kept per section: ${JSON.stringify(bySection)}. Inventories: ${D}/OTHER_MODS.md (first pass), ${D}/MODLIST.md (core). Task: find what is STILL MISSING for a complete VR "other mods" set. Method: (1) pick the 3 most graphics-focused VR lists (Panda's Sovngarde, Stormcrown VR, Yggdrasil VR) and for each major section (landscape, flora, architecture, dungeons, clutter, bodies, faces/hair, armor, creatures, city meshes, reshade) check with ${D}/tools/whouses.py and the archive files in ${D}/data/rep which of their mods in that section are in neither of our lists (list = OTHER_MODS.md + Core + the new picks you can infer from the section counts); (2) check the dry log: were any bands skipped; (3) name concrete missing topics with candidate Nexus ids. Return the gaps as data; do not edit files.`,
    { label: 'critic:r2', phase: 'Critic', effort: 'high', schema: { type: 'object', properties: {
      verdict: { type: 'string', enum: ['complete_enough', 'needs_another_round'] },
      missing: { type: 'array', items: { type: 'object', properties: { topic: { type: 'string' }, why: { type: 'string' }, candidate_ids: { type: 'array', items: { type: 'integer' } } }, required: ['topic', 'why', 'candidate_ids'] } },
      weak_sections: { type: 'array', items: { type: 'string' } }, notes: { type: 'string' },
    }, required: ['verdict', 'missing', 'weak_sections', 'notes'] } })
}

return {
  batches: results.length, candidates: results.reduce((s, r) => s + r.n, 0), dispositions: results.reduce((s, r) => s + r.got, 0),
  keptByBoth: kept.length, bySection, dryLog,
  incomplete: results.filter(r => r.got < r.n).map(r => `${r.id}:${r.got}/${r.n}`),
  consolidationNotes: consolidation.map(c => c.notes), conflicts: consolidation.flatMap(c => c.conflicts),
  critic,
}