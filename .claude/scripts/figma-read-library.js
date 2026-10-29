// Read-only. Paste into use_figma (the client's internal Figma file, link in DESIGNERS.md), save the returned JSON as the
// library for jev-design-check.py. Lists every section component set on the Sections page with
// its layouts (Type values), each layout's description (from the variant's component description),
// switches and description. Layout fit in jev-design-check.py only runs where every layout has a description.
const SECTIONS_PAGE_ID = "PUT-SECTIONS-PAGE-ID-HERE"; // the Sections page (approved components)
const sp = await figma.getNodeByIdAsync(SECTIONS_PAGE_ID);
await figma.setCurrentPageAsync(sp);
return sp.findAllWithCriteria({ types: ["COMPONENT_SET"] }).map(s => {
  const defs = s.componentPropertyDefinitions;
  const type = Object.entries(defs).find(([k, v]) => v.type === "VARIANT" && !/breakpoint/i.test(k));
  const layoutDescriptions = {};
  for (const v of s.children) {
    const t = v.type === "COMPONENT" && (v.name.match(/Type=([^,]+)/) || [])[1];
    if (t && !layoutDescriptions[t]) layoutDescriptions[t] = v.description || "";
  }
  return { name: s.name, layouts: type ? type[1].variantOptions : [], layoutDescriptions,
           switches: Object.keys(defs).filter(k => defs[k].type === "BOOLEAN").map(k => k.split("#")[0]),
           description: s.description || "" };
});
