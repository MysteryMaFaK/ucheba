export const meta = {
  name: 'skyrim-vr-verify-light',
  description: 'Light verification for "Other Mods 2026" round 2: ONE verifier per chunk of ~100 picks (value + VR checklist in one pass), no per-item tool calls, medium effort; stops at the first failure (usage limit)',
  phases: [{ title: 'Verify', detail: 'one agent per chunk' }],
}
// Подготовка: python3 -I tools/verify_chunks.py  -> печатает args {root, sizes}. Повторный запуск verify_chunks.py
// исключает уже проверенное, поэтому продолжать надо не через resumeFromRunId (кэш ломается при смене порядка вызовов),
// а заново: verify_chunks.py -> новые args -> этот скрипт.
// После: python3 -I tools/save_journal.py "<Transcript dir>" other-mods  (файлы other-mods__verify_single-V*.json)
//        python3 -I tools/merge_other2.py

const D = (args && args.root) || 'skyrim-vr-modlist'
const SIZES = (args && args.sizes) || {}
const SECTIONS = ['start','followers','navigation','controls','russian','saves','cc','equipment','voice','music','niche',
  'tex_strategy','tex_land','tex_flora','tex_water_sky','tex_arch','tex_dungeons','tex_clutter','tex_pbr_tools',
  'chars_body','chars_faces','physics','armor','creatures','city_meshes','clutter_meshes','reshade','misc','dont']

const PROMPT = (cid, n) => `
Project: Skyrim VR 1.4.15 modlist (SKSEVR 2.0.12, MO2; Open Shaders 2.17 — PBR on it in VR unconfirmed; Lux, Azurite Weathers III, Merethic Grasslands, Happy Little Trees, VRIK+HIGGS+PLANCK; no ENB). List "Other Mods 2026": textures, appearance, world assets and core gaps — a CURATED list of recommended extras, not a dump.
YOU ARE THE SINGLE VERIFIER for ${n} picks a triage agent proposed. Read ONLY two files: ${D}/data/other2/verify_chunks/${cid}.json (picks with cards; field legend inside; also "already_kept_round2" = names already accepted in this pass) and ${D}/data/other2/inventory_compact.txt (everything already in Core / first-pass Other / VR-interaction). Do NOT read other files, do NOT run scripts, do NOT search the web — decide from the cards and your own knowledge.
For each pick decide keep=true/false. Drop (keep=false) when ANY holds: duplicates or is superseded by something in the inventory, in already_kept_round2 or by a better pick in this chunk (keep the better one, give competing packs one choose_one_group); trivial/low value for VR; VRAM/CPU cost not justified in VR (4K everywhere, heavy city/clutter); outdated vs a 2025-2026 option; excluded category (quests/new lands, dialogue packs, followers/NPC characters, player homes, big difficulty overhauls, spell/shout packs, narrow SimonRim parts, NSFW); ENB-only.
VR checklist (same pass): an SKSE DLL with no VR evidence (vr=0, no VR list, file not VR) → tag "try" if plausible, else drop; flat-only → tag "dont" if people would copy it, else drop; unconfirmed PBR-only → "try". Shipped by VR lists (vr>=1) is evidence the asset works in VR.
Be strict: in earlier rounds ~40% of proposals were dropped at this stage, mostly as redundant or low value. Write the final section, tag (rec/opt/alt/try/dont), choose_one_group, a polished RU one-liner (what, <=170 chars) and a short RU note (VR caveats, order, conflicts). Return exactly one verdict per key (${n}). Human-facing text in RUSSIAN.`

const VERDICTS = { type: 'object', properties: { verdicts: { type: 'array', items: { type: 'object', properties: {
  key: { type: 'string' }, keep: { type: 'boolean' }, section: { type: 'string', enum: SECTIONS }, tag: { type: 'string', enum: ['rec', 'opt', 'alt', 'try', 'dont'] },
  choose_one_group: { type: ['string', 'null'] }, what: { type: 'string' }, note: { type: 'string' }, reason: { type: 'string', description: 'RU, short' },
}, required: ['key', 'keep', 'section', 'tag', 'choose_one_group', 'what', 'note', 'reason'] } } }, required: ['verdicts'] }

let stopped = false
const ids = Object.keys(SIZES).sort()
if (!ids.length) return { error: 'no chunks: run tools/verify_chunks.py and pass its args' }
phase('Verify')
const res = await pipeline(ids, async cid => {
  if (stopped) return { cid, skipped: true }
  const r = await agent(PROMPT(cid, SIZES[cid]), { label: `verify:single-${cid}`, phase: 'Verify', schema: VERDICTS, effort: 'medium' })
  if (!r) { stopped = true; log(`${cid}: no result — stopping (usage limit?). Re-run tools/verify_chunks.py later; finished chunks will not be redone.`); return { cid, failed: true } }
  const kept = r.verdicts.filter(v => v.keep).length
  log(`${cid}: ${r.verdicts.length}/${SIZES[cid]} verdicts, kept ${kept}`)
  return { cid, verdicts: r.verdicts.length, kept }
})
return { chunks: res, stopped }
