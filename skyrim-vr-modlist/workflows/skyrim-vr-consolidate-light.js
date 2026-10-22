export const meta = {
  name: 'skyrim-vr-consolidate-light',
  description: 'Light consolidation for "Other Mods 2026": one medium-effort editor per list part (gaps / textures / world) reading one compact file — duplicates, choose-one groups, MO2 order notes, conflicts; stops at the first failure',
  phases: [{ title: 'Consolidate', detail: 'one agent per part' }],
}
// Подготовка: python3 -I tools/merge_other2.py && python3 -I tools/consolidate_input.py -> args {root, sizes}
// После: python3 -I tools/save_journal.py "<Transcript dir>" other-mods  (other-mods__consolidate_r2-<часть>.json)
//        python3 -I tools/merge_other2.py && python3 tools/build_other.py data/other_result.json site/skyrim-vr-other-mods-2026.html OTHER_MODS.md

const D = (args && args.root) || 'skyrim-vr-modlist'
const SIZES = (args && args.sizes) || {}
const SECTIONS = ['start','followers','navigation','controls','russian','saves','cc','equipment','voice','music','niche',
  'tex_strategy','tex_land','tex_flora','tex_water_sky','tex_arch','tex_dungeons','tex_clutter','tex_pbr_tools',
  'chars_body','chars_faces','physics','armor','creatures','city_meshes','clutter_meshes','reshade','misc','dont']

const PROMPT = (part, n) => `
Project: Skyrim VR 1.4.15 modlist, list "Other Mods 2026" (curated extras: core gaps, textures, appearance/world). Stack: Open Shaders 2.17 (PBR in VR unconfirmed), Lux, Azurite Weathers III, Merethic Grasslands, Happy Little Trees, DynDOLOD, VRIK+HIGGS+PLANCK, no ENB.
YOU ARE THE CONSISTENCY EDITOR for part "${part}". Read ONLY ${D}/data/other2/consolidate/${part}.json: "new_round2" = ${n} accepted second-pass picks (you may change them), "first_pass_fixed" = first-pass picks (fixed; do not adjust, only report conflicts). Do NOT read other files, run scripts or search the web.
Tasks: (a) duplicates/overlaps: among new picks and between new and first-pass picks — mark the weaker NEW one drop_duplicate; (b) choose_one groups: harmonise group names (lower-case-with-hyphens, by topic), exactly one default_pick per group, members by name (#id), including first-pass members; (c) MO2 order/overwrite rules that matter here (bodies before armor and BodySlide build, landscape/terrain order, series overwrite order, meshes vs textures); (d) concrete conflicts; (e) retag overlong runs: rec only for clear winners, opt for fine extras, try for unproven. Return an adjustment for EVERY new key (action keep if unchanged). Human-facing text in RUSSIAN, short.`

const CONSOL = { type: 'object', properties: {
  adjustments: { type: 'array', items: { type: 'object', properties: {
    key: { type: 'string' }, action: { type: 'string', enum: ['keep', 'drop_duplicate', 'regroup', 'retag', 'move_section'] },
    section: { type: 'string', enum: SECTIONS }, tag: { type: 'string', enum: ['rec', 'opt', 'alt', 'try', 'dont'] }, choose_one_group: { type: ['string', 'null'] }, reason: { type: 'string' },
  }, required: ['key', 'action', 'section', 'tag', 'choose_one_group', 'reason'] } },
  groups: { type: 'array', items: { type: 'object', properties: { group: { type: 'string' }, members: { type: 'array', items: { type: 'string' } }, default_pick: { type: 'string' }, rule: { type: 'string' } }, required: ['group', 'members', 'default_pick', 'rule'] } },
  order_rules: { type: 'array', items: { type: 'string' } }, conflicts: { type: 'array', items: { type: 'string' } }, notes: { type: 'string' },
}, required: ['adjustments', 'groups', 'order_rules', 'conflicts', 'notes'] }

let stopped = false
const parts = Object.keys(SIZES)
if (!parts.length) return { error: 'no parts: run tools/consolidate_input.py and pass its args' }
phase('Consolidate')
const res = await pipeline(parts, async part => {
  if (stopped) return { part, skipped: true }
  const r = await agent(PROMPT(part, SIZES[part]), { label: `consolidate:r2-${part}`, phase: 'Consolidate', schema: CONSOL, effort: 'medium' })
  if (!r) { stopped = true; log(`${part}: no result — stopping (usage limit?)`); return { part, failed: true } }
  return { part, adjustments: r.adjustments.length, dropped: r.adjustments.filter(a => a.action === 'drop_duplicate').length, groups: r.groups.length, conflicts: r.conflicts.length }
})
return { parts: res, stopped }
