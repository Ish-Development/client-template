// Turns agent/visual/tokens.json into agent/visual/tokens.css for coded sites (e.g. Astro).
// Run: npm run tokens  (or: node <this file> <path/to/tokens.json>)
// Only copies values. Empty values are skipped, never filled in.
import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";

const input = process.argv[2] ?? "agent/visual/tokens.json";
const output = join(dirname(input), "tokens.css");
const tokens = JSON.parse(readFileSync(input, "utf8"));

// Not CSS values: notes, the brand name, and photography direction.
const SKIP = new Set(["brand", "photography"]);
// Plain numbers in these groups are pixels.
const PX_GROUPS = new Set(["space", "radius"]);

const kebab = (s) => s.replace(/([a-z0-9])([A-Z])/g, "$1-$2").toLowerCase();
const isEmpty = (v) => v === null || v === "" || (Array.isArray(v) && v.length === 0);
const quoteFamily = (f) => (/\s/.test(f) && !/^["']/.test(f) ? `"${f}"` : f);

const lines = [];

function walk(node, path) {
  for (const [key, value] of Object.entries(node)) {
    if (key.startsWith("_") || (path.length === 0 && SKIP.has(key))) continue;
    // family + fallback become one font stack below.
    if (node.family && (key === "family" || key === "fallback")) continue;
    const here = [...path, key];
    if (value && typeof value === "object" && !Array.isArray(value)) {
      walk(value, here);
      // A type style with a family also gets one ready-to-use font stack.
      if (value.family) {
        const stack = [quoteFamily(value.family), value.fallback].filter(Boolean).join(", ");
        lines.push(`  --${here.map(kebab).join("-")}-font: ${stack};`);
      }
      continue;
    }
    if (isEmpty(value) || Array.isArray(value)) continue;
    const css =
      typeof value === "number" && PX_GROUPS.has(here[0]) ? `${value}px` : String(value);
    lines.push(`  --${here.map(kebab).join("-")}: ${css};`);
  }
}

walk(tokens, []);

const css = `/* Made from tokens.json by npm run tokens. Do not edit by hand: change tokens.json and run it again. */
:root {
${lines.join("\n")}
}
`;
writeFileSync(output, css);
console.log(`${output}: ${lines.length} values${lines.length ? "" : " (tokens.json is still empty)"}`);
