// Read-only. Paste into use_figma (the client's internal Figma file, link in DESIGNERS.md) with ROOT_ID set to a page, a page frame, a
// section, a component set or a draft. Checks the Figma rules in DESIGNERS.md ("Section component rules") and
// returns each break with the layer, its path and the rule. Changes nothing.
// Style rules check the frames and components themselves, not inside instances (their main component is checked
// where it lives). Copy rules (colons, buttons) also read inside instances, because copy lives on the instances.
const SECTIONS_PAGE_ID = "PUT-SECTIONS-PAGE-ID-HERE"; // the Sections page (approved components)
const ROOT_ID = SECTIONS_PAGE_ID; // or a page frame, section, component set or draft
const CAP = 25; // findings returned per rule; the count is always complete
// Not designs: organising sections, notes and annotations, archived drafts (their components are checked on Sections)
const SKIP = /^(Note\b|Label \(annotation\)|Approved — now components)|annotation/i;

const root = await figma.getNodeByIdAsync(ROOT_ID);
if (!root) return { error: "not found" };
let page = root; while (page && page.type !== "PAGE") page = page.parent;
await figma.setCurrentPageAsync(page);

const cols = await figma.variables.getLocalVariableCollectionsAsync();
const colByName = Object.fromEntries(cols.map(c => [c.name, c]));
const varCache = {};
const varOf = async id => (id in varCache ? varCache[id] : (varCache[id] = await figma.variables.getVariableByIdAsync(id)));
const styleCache = {};
const textStyle = async n => {
  const id = n.textStyleId;
  if (!id || id === figma.mixed) return null;
  return id in styleCache ? styleCache[id] : (styleCache[id] = (await figma.getStyleByIdAsync(id))?.name || null);
};
const isHeading = s => /^(Display|H[1-6])\b/.test(s || "");
const isParagraph = s => /^Text (Large|Medium|Main)\b/.test(s || "");

const rules = {
  spacing: "Padding and gaps come from a space variable (DESIGNERS.md: no hand-set gaps)",
  radius: "Corner radius comes from a radius variable",
  colour: "Fills and strokes come from a colour variable or style, no hex",
  border: "Lines use Border/border-primary, not an alpha or primitive colour",
  type: "Text uses one of the file's text styles",
  wrapper: "Every heading and paragraph sits in a Heading / Paragraph wrapper bound to its width variable",
  clip: "Never clip a wrapper or a frame that only holds text",
  slot: "Image slots are plain frames, never auto layout",
  hidden: "Optional elements are switches on their wrapper, never hidden layers",
  names: "Text layers side by side have unique names (Title, Body, Label), so desktop and mobile match",
  grid: "Every section variant and draft has the layout grid (Grid style or bound columns)",
  modes: "Mobile variants use the Mobile modes for Sizes and Typography",
  overlap: "Nothing overlaps on the canvas (Iterations: re-lay out and restack after every draft)",
  colon: "No colon in any heading",
  buttons: "One button in a hero or CTA section",
  icons: "Arrows and icons only on link buttons, never on primary or secondary",
};
const found = Object.fromEntries(Object.keys(rules).map(k => [k, { count: 0, where: {}, items: [] }]));
// the component set, draft or page frame a layer belongs to, so a long list can be read per section
const owner = n => { for (let x = n; x && x.type !== "PAGE"; x = x.parent) if (x.type === "COMPONENT_SET" || (x.type !== "SECTION" && (x.parent?.type === "SECTION" || x.parent?.type === "PAGE"))) return x.name; return n.name; };
const path = n => { const p = []; for (let x = n; x && x !== root.parent && x.type !== "PAGE"; x = x.parent) p.unshift(x.name); return p.slice(-4).join(" › "); };
const add = (rule, n, detail) => { const f = found[rule]; f.count++; const w = owner(n); f.where[w] = (f.where[w] || 0) + 1; if (f.items.length < CAP) f.items.push({ id: n.id, path: path(n), detail }); };

const box = n => n.absoluteBoundingBox;
const overlaps = (a, b) => a && b && a.x < b.x + b.width && b.x < a.x + a.width && a.y < b.y + b.height && b.y < a.y + a.height;
const SPACING = ["paddingLeft", "paddingRight", "paddingTop", "paddingBottom", "itemSpacing", "counterAxisSpacing"];
const CORNERS = ["topLeftRadius", "topRightRadius", "bottomLeftRadius", "bottomRightRadius"];

async function paints(n, key) {
  const list = n[key];
  if (!Array.isArray(list)) return;
  const styleId = key === "fills" ? n.fillStyleId : n.strokeStyleId;
  for (const p of list) {
    if (p.visible === false || p.type !== "SOLID") continue;
    const vid = p.boundVariables?.color?.id;
    if (!vid) { if (!styleId) add("colour", n, `${key === "fills" ? "fill" : "stroke"} hand-set`); continue; }
    if (key === "strokes") {
      const v = await varOf(vid);
      const col = v && cols.find(c => c.id === v.variableCollectionId);
      if (v && (/alpha/i.test(v.name) || col?.name === "Primitive Colors")) add("border", n, `stroke uses ${v.name}`);
      if (p.opacity !== undefined && p.opacity < 1) add("border", n, `stroke ${v?.name} at ${Math.round(p.opacity * 100)}% opacity`);
    }
  }
}

async function styleChecks(n, inComponent, art) {
  const bv = n.boundVariables || {};
  if ("layoutMode" in n && n.layoutMode !== "NONE") {
    for (const f of SPACING) {
      if (!(n[f] > 0) || bv[f]) continue;
      if (f === "itemSpacing" && (n.primaryAxisAlignItems === "SPACE_BETWEEN" || n.children.length < 2)) continue;
      if (f === "counterAxisSpacing" && n.layoutWrap !== "WRAP") continue;
      add("spacing", n, `${f} ${n[f]}px`);
    }
  }
  if ("cornerRadius" in n && n.type !== "TEXT") {
    const hand = CORNERS.filter(c => n[c] > 0 && !bv[c]);
    if (hand.length) add("radius", n, `${n[hand[0]]}px`);
  }
  // illustrations (groups) are real artwork and photo slots are colour blocks until the photographer delivers
  if (!art) {
    await paints(n, "fills");
    if (n.strokeWeight !== 0) await paints(n, "strokes");
  }

  if (n.type === "TEXT") {
    const s = await textStyle(n);
    if (!s) add("type", n, n.textStyleId === figma.mixed ? "mixed styles" : "no text style");
    if (isHeading(s) || isParagraph(s)) {
      const w = n.parent;
      const kind = isHeading(s) ? "Heading" : "Paragraph";
      if (!w || !/wrapper/i.test(w.name)) add("wrapper", n, `${s} not in a ${kind} wrapper`);
      else {
        const wb = w.boundVariables || {};
        if (!wb.maxWidth && !wb.width && !wb.minWidth) add("wrapper", w, `${w.name} has no width variable`);
      }
    }
  }
  if (/wrapper/i.test(n.name) && n.clipsContent) add("clip", n, "clips content");
  if (/^(Image|Avatar) \d+$/.test(n.name) && "layoutMode" in n && n.layoutMode !== "NONE") add("slot", n, "slot has auto layout");
  if (inComponent && n.visible === false && !n.componentPropertyReferences?.visible) add("hidden", n, "hidden, not on a switch");
}

function componentChecks(c) {
  // two text layers with the same name in one frame (repeated cards may each have a "Title")
  for (const f of [c, ...c.findAllWithCriteria({ types: ["FRAME"] })]) {
    const seen = {};
    for (const t of f.children) if (t.type === "TEXT") (seen[t.name] ||= []).push(t);
    for (const [name, list] of Object.entries(seen)) if (list.length > 1) add("names", list[1], `${list.length} text layers named "${name}" side by side`);
  }
  // section variants: layout grid and breakpoint modes
  if (c.parent?.type === "COMPONENT_SET" && page.id === SECTIONS_PAGE_ID) {
    gridCheck(c);
    const mobile = /Breakpoint=Mobile/i.test(c.name);
    const modes = c.explicitVariableModes || {};
    for (const cn of ["Sizes", "Typography"]) {
      const col = colByName[cn]; if (!col) continue;
      const want = col.modes.find(m => m.name === (mobile ? "Mobile" : "Desktop"));
      const got = modes[col.id];
      if (mobile && got !== want.modeId) add("modes", c, `${cn} not set to Mobile`);
      if (!mobile && got && got !== want.modeId) add("modes", c, `${cn} set to ${col.modes.find(m => m.modeId === got)?.name} on a desktop variant`);
    }
  }
}

function gridCheck(f) {
  const g = f.layoutGrids || [];
  if (!g.length) return add("grid", f, "no layout grid");
  if (!f.gridStyleId && !g.some(x => x.boundVariables && Object.keys(x.boundVariables).length)) add("grid", f, "layout grid hand-set, not the Grid style or bound to grid/*");
}

function overlapCheck(parent) {
  // canvas only: frames and sections side by side on a page or in a section (a navbar over a hero image is fine)
  if (parent.type !== "SECTION" && parent.type !== "PAGE") return;
  const kids = parent.children.filter(k => k.visible !== false && box(k));
  for (let i = 0; i < kids.length; i++) for (let j = i + 1; j < kids.length; j++)
    if (overlaps(box(kids[i]), box(kids[j]))) add("overlap", kids[i], `overlaps "${kids[j].name}" (${kids[j].id})`);
}

// copy rules, read through instances
async function buttonType(inst) {
  const mc = await inst.getMainComponentAsync();
  const set = mc?.parent?.type === "COMPONENT_SET" ? mc.parent : null;
  if (!set || set.name !== "Button") return null;
  return inst.componentProperties?.Type?.value || null;
}
async function copyChecks(n) {
  if (n.type === "TEXT" && n.visible) {
    const s = await textStyle(n);
    if (isHeading(s) && n.characters.includes(":")) add("colon", n, `"${n.characters.slice(0, 60)}"`);
  }
  if (n.type === "INSTANCE" && /button/i.test(n.name)) {
    const t = await buttonType(n);
    if ((t === "Primary" || t === "Secondary") && n.findAll(k => k.visible && (k.type === "INSTANCE" || k.type === "VECTOR")).length)
      add("icons", n, `${t} button with an icon`);
  }
  if (n.type === "INSTANCE" && /hero|cta/i.test(n.name)) {
    const mc = await n.getMainComponentAsync();
    const setName = mc?.parent?.type === "COMPONENT_SET" ? mc.parent.name : mc?.name || "";
    if (/hero|cta/i.test(setName) && !/links|buttons/i.test(mc?.name || "")) {
      let count = 0;
      for (const b of n.findAll(k => k.type === "INSTANCE" && /button/i.test(k.name)))
        if (isShown(b, n) && ["Primary", "Secondary"].includes(await buttonType(b))) count++;
      if (count > 1) add("buttons", n, `${count} buttons`);
    }
  }
}
const isShown = (n, stop) => { for (let p = n; p && p !== stop; p = p.parent) if (p.visible === false) return false; return true; };

let nodes = 0;
async function walk(n, inComponent, inInstance, art) {
  if (SKIP.test(n.name)) return;
  nodes++;
  if (n.type !== "PAGE") {
    // On the Sections page only components count; the group frames around them just organise the page
    const organising = n.type === "SECTION" || n.type === "COMPONENT_SET" || (page.id === SECTIONS_PAGE_ID && !inComponent && n.type !== "COMPONENT");
    art = art || n.type === "GROUP" || /^(Image|Avatar) \d+$/.test(n.name);
    if (!inInstance && !organising) await styleChecks(n, inComponent, art);
    if (inInstance || n.type === "INSTANCE" || n.type === "TEXT") await copyChecks(n);
  }
  if (n.type === "COMPONENT") componentChecks(n);
  if (/^Draft/.test(n.name) && n.type === "FRAME") gridCheck(n);
  if (!("children" in n)) return;
  if (!inInstance) overlapCheck(n);
  const comp = inComponent || n.type === "COMPONENT" || n.type === "COMPONENT_SET";
  const inst = inInstance || n.type === "INSTANCE";
  for (const k of n.children) if (inst ? k.visible : true) await walk(k, comp, inst, art);
}
await walk(root, root.type === "COMPONENT" || root.type === "COMPONENT_SET" || !!(function up(x) { for (; x; x = x.parent) if (x.type === "COMPONENT") return true; })(root.parent), false, false);

const result = { root: `${root.name} (${root.id})`, page: page.name, nodes, findings: {} };
for (const [k, f] of Object.entries(found)) if (f.count) result.findings[k] = { rule: rules[k], count: f.count, where: f.where, items: f.items };
result.clean = Object.keys(rules).filter(k => !found[k].count);
return result;
