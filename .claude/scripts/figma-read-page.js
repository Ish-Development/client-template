// Read-only. Paste into use_figma (the client's internal Figma file, link in DESIGNERS.md) with NODE_ID set to a page frame,
// save the returned JSON, then run jev-design-check.py on it. Lists each section's component,
// layout, switches that are off, and its visible text.
const NODE_ID = "PUT-PAGE-FRAME-ID-HERE";
const root = await figma.getNodeByIdAsync(NODE_ID);
if (!root) return { error: "not found" };
let page = root; while (page && page.type !== "PAGE") page = page.parent;
await figma.setCurrentPageAsync(page);
const visibleIn = (n, stop) => { for (let p = n; p && p !== stop; p = p.parent) if (p.visible === false) return false; return true; };
const sections = [];
for (const s of root.children) {
  const sec = { name: s.name, id: s.id };
  if (s.type === "INSTANCE") {
    const mc = await s.getMainComponentAsync();
    sec.component = mc ? (mc.parent && mc.parent.type === "COMPONENT_SET" ? mc.parent.name : mc.name) : null;
    sec.variant = mc ? mc.name : null;
    const props = s.componentProperties || {};
    sec.switchesOff = Object.entries(props).filter(([k, v]) => v.type === "BOOLEAN" && v.value === false).map(([k]) => k.split("#")[0]);
  }
  const texts = "findAllWithCriteria" in s ? s.findAllWithCriteria({ types: ["TEXT"] }) : [];
  sec.text = texts.filter(t => visibleIn(t, s.parent)).map(t => t.characters.slice(0, 400));
  sections.push(sec);
}
return { page: page.name, frame: root.name, id: root.id, sections };
