export const meta = {
  name: 'skyrim-vr-other-mods-cheap',
  description: 'Cheap pass over bands C+D of "Other Mods 2026" (925 candidates after a deterministic prefilter, 12 batches of ~80): one medium-effort triage agent per batch with NO per-item tool calls, then two VR/value verifiers on the kept picks; aborts on repeated failures (usage limit)',
  phases: [
    { title: 'Evaluate', detail: 'one agent per batch, no per-item tool calls' },
    { title: 'Verify', detail: 'VR-compat skeptic + value/redundancy skeptic over the kept picks' },
  ],
}

const D = (args && args.root) || 'skyrim-vr-modlist'
const SIZES = (args && args.sizes) || {}
const ONLY = (args && args.only) || null
const MAX_FAILS = 3

const SECTIONS = ['start','followers','navigation','controls','russian','saves','cc','equipment','voice','music','niche',
  'tex_strategy','tex_land','tex_flora','tex_water_sky','tex_arch','tex_dungeons','tex_clutter','tex_pbr_tools',
  'chars_body','chars_faces','physics','armor','creatures','city_meshes','clutter_meshes','reshade','misc','dont','none']
const SEC_RU = 'start=alternate start; followers=follower framework; navigation; controls=controls/presets; russian=localization; saves; cc=Creation Club; equipment=gear on body; voice=voice commands; music; niche=haptics/locomotion; tex_strategy=VRAM strategy/tools; tex_land=landscape/mountains; tex_flora; tex_water_sky; tex_arch=cities/architecture textures; tex_dungeons=dungeons/ruins textures; tex_clutter=clutter/furniture textures; tex_pbr_tools=PBR and patchers; chars_body=bodies; chars_faces=faces/hair/eyes/skin; physics=body/cloth physics; armor=armor/weapons/clothing; creatures; city_meshes=city/structure meshes; clutter_meshes=clutter/furniture/food meshes; reshade; misc=other useful tools/additions that fit no section; dont=do-not-install-in-VR; none=dropped'

const CONTEXT = `
Project: a Skyrim VR modlist (Skyrim VR 1.4.15, SKSEVR 2.0.12, MO2). Today 2026-10-11. Stack already chosen: Open Shaders 2.17 (VR fork of Community Shaders; PBR/Complex Material on it in VR is NOT confirmed by any VR list), Lux + Light Placer + CS Light, Azurite Weathers III, Merethic Grasslands, Happy Little Trees, DynDOLOD, OAR/Pandora, SimonRim core, SkyUI VR, RaceMenu VR, VRIK+HIGGS+PLANCK, no ENB.
We are doing the SECOND PASS of the list "Other Mods 2026" (textures, appearance, world assets, gaps). Candidates = mods used by the 27 popular Wabbajack lists (9 VR + 18 SE next-gen) that no earlier pass evaluated. This is the cheap pass for the lower-popularity bands (each candidate is used by at least one VR list).
EXCLUDED (drop with drop_code "excluded_category"): quest/new-land/dungeon content, dialogue packs, followers and NPC-character mods, player homes, big difficulty overhauls, spell/shout packs, narrow SimonRim parts (Aetherius, Scion, Manbeast, Pilgrim), NSFW. NOT excluded: bodies, NPC faces/hair/eyes, armor/weapon/clothing, creatures, city/structure meshes, clutter/furniture, ReShade, all textures, small fixes with real value.
FILES: read ONLY (1) the batch file and (2) ${D}/data/other2/inventory_compact.txt (everything already taken: core, first-pass Other, VR-interaction — if a candidate duplicates or is superseded by a line there, drop it with drop_code "covered_elsewhere" and name the listed mod). Do NOT read other files. Do NOT call whouses.py or loop per item: each candidate card already carries what the lists ship (vr/se counts, VR list names, newest date, first archive file name, theme, series members).
Web: the cards are enough for most items; use WebSearch ONLY for at most 5 candidates you truly cannot classify from your own knowledge (search snippets; nexusmods.com pages are blocked). Prefer deciding from knowledge and card evidence; if unsure whether a mod is VR-safe and it ships a DLL, mark tag "try".
VR rules: no-DLL assets/plugins work in VR; SKSE DLLs need a VR build; VRAM (two eyes; prefer 2K, 1K for small clutter), CPU draw calls (heavy city/clutter cost more in VR), real-world scale, ENB-only add-ons are useless.
Quality bar: CURATED recommended extras, not a dump. A mod shipped by few lists is not automatically a keep: it must add clear VR-relevant value and not fight the stack. When several mods compete (armor retextures, hair packs, creature models, landscapes), keep the best one or two and put them in a choose_one group; drop the rest as redundant. Never invent file names or VR status; evidence = the card data (list names, file name) or knowledge you state as such. Human-facing text in RUSSIAN, short.`

const EVAL = { type: 'object', properties: {
  entries: { type: 'array', items: { type: 'object', properties: {
    key: { type: 'string', description: 'copy EXACTLY from the batch item' },
    id: { type: ['integer', 'null'] }, name: { type: 'string' }, url: { type: 'string', description: 'https://www.nexusmods.com/skyrimspecialedition/mods/<id>' },
    decision: { type: 'string', enum: ['keep', 'dont', 'drop'] },
    drop_code: { type: 'string', enum: ['none', 'excluded_category', 'covered_elsewhere', 'superseded', 'redundant_in_batch', 'vr_incompatible', 'vram_cpu_cost', 'low_value', 'not_an_asset', 'unclear'] },
    section: { type: 'string', enum: SECTIONS }, tag: { type: 'string', enum: ['rec', 'opt', 'alt', 'try', 'dont', 'none'] },
    choose_one_group: { type: ['string', 'null'] },
    what: { type: 'string', description: 'RU <=170 chars; empty for drops' },
    vr_status: { type: 'string', enum: ['works_as_is', 'vr_version_exists', 'vr_native', 'flat_only', 'unknown', 'n/a'] },
    files: { type: 'string', description: 'RU: file/variant the VR lists pick (from the card); empty for drops' },
    requires: { type: 'array', items: { type: 'string' } },
    note: { type: 'string', description: 'keep/dont: RU caveats (VR, conflicts, VRAM/CPU cost, order). drop: RU one-line reason, name the listed mod if covered elsewhere' },
    evidence: { type: 'string', description: 'card data or stated knowledge' },
    member_ids: { type: 'array', items: { type: 'integer' }, description: 'series items only: ids of members to keep (empty = single mod or whole series)' },
  }, required: ['key', 'id', 'name', 'url', 'decision', 'drop_code', 'section', 'tag', 'choose_one_group', 'what', 'vr_status', 'files', 'requires', 'note', 'evidence', 'member_ids'] } },
  batch_notes: { type: 'string' },
}, required: ['entries', 'batch_notes'] }

const VERDICTS = { type: 'object', properties: { verdicts: { type: 'array', items: { type: 'object', properties: {
  key: { type: 'string' }, keep: { type: 'boolean' }, section: { type: 'string', enum: SECTIONS }, tag: { type: 'string', enum: ['rec', 'opt', 'alt', 'try', 'dont'] },
  choose_one_group: { type: ['string', 'null'] }, what: { type: 'string' }, note: { type: 'string' }, reason: { type: 'string' },
}, required: ['key', 'keep', 'section', 'tag', 'choose_one_group', 'what', 'note', 'reason'] } } }, required: ['verdicts'] }

const LENSES = [
  { key: 'vr-compat', prompt: 'You are a VR-COMPATIBILITY SKEPTIC. Try to refute each VR claim (SKSE DLL without VR build, flat-only, needs an SE-only framework, breaks VRIK body/hands, ENB-only, needs unconfirmed PBR path). Use the batch card (VR list names, file names) and at most a few quick searches for the doubtful ones. Unproven but plausible → keep with tag "try" and a note on how to test. Wrong → keep=false (or tag "dont" if people would copy it).' },
  { key: 'value-perf', prompt: `You are a VALUE / VR-PERFORMANCE / REDUNDANCY SKEPTIC. Try to refute each item: duplicates something in ${D}/data/other2/inventory_compact.txt or another pick in this batch (keep the better; enforce choose_one groups), VRAM/CPU cost unjustified in VR, outdated/superseded, EXCLUDED category, or trivial. Assign the best section and tag, write the final RU one-liner and note. Be strict: a short, strong list beats a long one.` },
]

let fails = 0
const aborted = () => fails >= MAX_FAILS
const ids = Object.keys(SIZES).filter(k => !ONLY || ONLY.includes(k)).sort()
if (!ids.length) return { error: 'no batches: pass args.sizes' }

async function evalBatch(id) {
  if (aborted()) return null
  const n = SIZES[id]
  const file = `${D}/data/other2/batches/${id}.json`
  const base = `${CONTEXT}\n\nSection codes: ${SEC_RU}.\n\nYOUR TASK: triage EVERY item of ${file} (JSON: items[] with key, id, name, vr/se, vr_lists, newest, file, theme, members for series). The batch has exactly ${n} items. Return exactly one entry per item, copying "key" exactly — no omissions, no merging. decision "keep" (goes to verification; fill section/tag/what/files/requires/note/evidence), "dont" (popular but must NOT be installed in VR — say why), or "drop" (drop_code + one-line RU reason in note). For a series item decide for the whole series (keep all, keep best members via member_ids, or drop). Tags: rec = recommended, opt = optional, alt = one of a choose_one group, try = unproven in VR.`
  let entries = [], notes = [], tries = 0
  while (tries < 2 && !aborted()) {
    const have = new Set(entries.map(e => e.key))
    const prompt = tries === 0 ? base : `${base}\n\nRETRY: entries already returned for keys ${JSON.stringify([...have])}. Return entries ONLY for the other items of the batch file.`
    const r = await agent(prompt, { label: `collect:r2-${id}${tries ? '-retry' + tries : ''}`, phase: 'Evaluate', schema: EVAL, effort: 'medium' })
    if (!r) { fails++; log(`${id}: agent returned null (fails ${fails}/${MAX_FAILS})`); break }
    for (const e of r.entries) if (!have.has(e.key)) { entries.push(e); have.add(e.key) }
    notes.push(r.batch_notes)
    tries++
    if (new Set(entries.map(e => e.key)).size >= n) break
  }
  const got = new Set(entries.map(e => e.key)).size
  if (got < n) log(`batch ${id}: ${got}/${n} dispositions`)
  return { id, n, got, entries, notes }
}

async function verifyBatch(ev) {
  if (!ev || aborted()) return ev ? { id: ev.id, n: ev.n, got: ev.got, kept: 0, dont: 0, skippedVerify: true } : null
  const picks = ev.entries.filter(e => e.decision !== 'drop')
  const out = { id: ev.id, n: ev.n, got: ev.got, kept: 0, dont: 0, dropped: ev.entries.length - picks.length }
  if (!picks.length) return out
  const listing = JSON.stringify(picks.map(({ key, id, name, url, section, tag, choose_one_group, what, vr_status, files, requires, note, evidence, member_ids, decision }) => ({ key, id, name, url, decision, section, tag, choose_one_group, what, vr_status, files, requires, note, evidence, member_ids })))
  const lens = await parallel(LENSES.map(l => () => agent(`${CONTEXT}\n\n${l.prompt}\n\nSection codes: ${SEC_RU}.\nReturn one verdict per key (all ${picks.length}). Batch card file: ${D}/data/other2/batches/${ev.id}.json. PICKS:\n${listing}`, { label: `verify:${l.key}-r2-${ev.id}`, phase: 'Verify', schema: VERDICTS, effort: 'high' })))
  if (lens.some(r => !r)) { fails++; log(`${ev.id}: a verifier returned null (fails ${fails}/${MAX_FAILS})`) }
  const maps = lens.map(r => new Map((r ? r.verdicts : []).map(v => [v.key, v])))
  for (const p of picks) { const a = maps[0].get(p.key), b = maps[1].get(p.key); if (a && b && a.keep && b.keep) { if (a.tag === 'dont' || b.tag === 'dont' || b.section === 'dont') out.dont++; else out.kept++ } }
  return out
}

phase('Evaluate')
const res = (await pipeline(ids, id => evalBatch(id), ev => verifyBatch(ev))).filter(Boolean)
const nn = res.reduce((s, r) => s + r.n, 0), kk = res.reduce((s, r) => s + r.kept + r.dont, 0)
log(`${res.length}/${ids.length} batches, ${nn} candidates, kept by both ${kk}${aborted() ? ' — ABORTED after repeated failures (usage limit?); resume later' : ''}`)
return { batches: res.length, candidates: nn, dispositions: res.reduce((s, r) => s + r.got, 0), keptByBoth: kk, aborted: aborted(), incomplete: res.filter(r => r.got < r.n || r.skippedVerify).map(r => `${r.id}:${r.got}/${r.n}${r.skippedVerify ? ' (no verify)' : ''}`) }