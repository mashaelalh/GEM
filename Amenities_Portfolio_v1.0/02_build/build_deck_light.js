// GEM™ — Amenities & Packaging · Concept Product Portfolio v1.0
// Structured pptxgenjs deck. Palette and type from GEM V3.0 RC2 (Part A). All mockups CONCEPT / NOT PRODUCTION ARTWORK.
const pptxgen = require("pptxgenjs");
const path = require("path");
const fs = require("fs");
const { applyTheme } = require("/root/.claude/skills/synced/e61aaa9d-c167-408f-b671-3b4ec2a9dadb_4d2c97cb-4ee9-4506-9558-2db6923cc7dd/pptx/scripts/apply_theme.js");

const M = (f) => path.join(__dirname, "mockups_deck", f.replace(/\.png$/, ".jpg"));
const L = (f) => path.join(__dirname, "..", "00_source", "logo", f);
const OUT = path.join(__dirname, "..", "04_release", "GEM_Amenities_and_Packaging_Concept_Portfolio_v1.0.pptx");

const THEME = { name: "GEM V3.0 RC2", headFontFace: "Jost", bodyFontFace: "Inter",
  colors: { dk1: "12171D", lt1: "FFFFFF", dk2: "020202", lt2: "BCACA7", accent1: "12171D", accent2: "BCACA7", accent3: "020202", accent4: "FFFFFF", accent5: "12171D", accent6: "BCACA7", hlink: "12171D", folHlink: "12171D" } };
const INK = "12171D", BEIGE = "BCACA7", BLACK = "020202", WHITE = "FFFFFF";
const STATUS = "CONCEPT / NOT PRODUCTION ARTWORK";
const FOOT = "GEM™ — AMENITIES & PACKAGING · CONCEPT PRODUCT PORTFOLIO v1.0 · CONCEPT / NOT PRODUCTION ARTWORK";

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
pres.theme = { headFontFace: "Jost", bodyFontFace: "Inter" };
pres.author = "GEM™ — Amenities & Packaging"; pres.title = "GEM™ — Amenities & Packaging · Concept Product Portfolio v1.0";
pres.subject = "Concept product portfolio · not production artwork";

// ---- layouts ----
function layout(name, bg, fg, opts = {}) {
  const objects = [];
  if (!opts.noFooter) {
    objects.push({ text: { text: FOOT, options: { x: 0.89, y: 6.82, w: 9.6, h: 0.26, fontFace: "Inter", fontSize: 8, color: fg, charSpacing: 1.5, margin: 0 } } });
  }
  pres.defineSlideMaster({ title: name, background: { color: bg }, objects, slideNumber: opts.noFooter ? undefined : { x: 12.3, y: 6.82, w: 0.6, h: 0.26, fontFace: "Inter", fontSize: 8, color: fg, align: "right" } });
}
layout("DARK", INK, BEIGE); layout("LIGHT", WHITE, INK); layout("BEIGE", BEIGE, INK); layout("COVER", INK, BEIGE, { noFooter: true });

const eyebrow = (s, text, color, x = 0.89, y = 0.89, w = 8) => s.addText(text, { x, y, w, h: 0.26, fontFace: "Inter", fontSize: 9, color, charSpacing: 2.4, margin: 0, isTextBox: true });
const title = (s, text, color, x = 0.89, y = 1.22, w = 6.5, size = 30) => s.addText(text, { x, y, w, h: 1.2, fontFace: "Jost", fontSize: size, color, margin: 0, valign: "top", isTextBox: true });
const body = (s, text, color, x, y, w, h = 1.2, size = 11) => s.addText(text, { x, y, w, h, fontFace: "Inter", fontSize: size, color, margin: 0, valign: "top", isTextBox: true, paraSpaceAfter: 4 });
const stamp = (s, text, color, x = 0.89, y = 6.35, w = 8) => s.addText(text, { x, y, w, h: 0.26, fontFace: "Inter", fontSize: 8, color, charSpacing: 1.8, margin: 0, isTextBox: true, bold: true });
const rule = (s, color, x, y, w) => s.addShape(pres.ShapeType.line, { x, y, w, h: 0, line: { color, width: 0.5 } });
const pic = (s, file, x, y, w, h, alt) => s.addImage({ path: M(file), x, y, w, h, altText: alt || "Concept mockup, not production artwork", sizing: { type: "cover", w, h } });
const lockup = (s, colour, x, y, h, alt) => s.addImage({ path: L(`GEM_Logo_Horizontal_${colour}.png`), x, y, w: h * 654 / 207, h, altText: alt || "GEM primary horizontal signature, supplied raster, PENDING PRODUCTION MASTER" });

// 01 COVER
{ const s = pres.addSlide({ masterName: "COVER" });
  pic(s, "00_cover_product.png", 7.9, 0, 5.43, 7.5, "Hero: a GEM-packaged shampoo bottle concept on an Ink field");
  lockup(s, "Beige", 0.89, 0.89, 1.1);
  s.addText("Amenities & Packaging", { x: 0.89, y: 3.0, w: 6.6, h: 0.8, fontFace: "Jost", fontSize: 40, color: WHITE, margin: 0, isTextBox: true });
  s.addText("Concept Product Portfolio", { x: 0.89, y: 3.85, w: 6.6, h: 0.5, fontFace: "Inter", fontSize: 16, color: BEIGE, margin: 0, isTextBox: true });
  s.addText("HOSPITALITY, IN PERFECT PROPORTION", { x: 0.89, y: 5.6, w: 6.6, h: 0.3, fontFace: "Jost", fontSize: 13, color: BEIGE, charSpacing: 3.2, margin: 0, isTextBox: true });
  s.addText("CONCEPT / NOT PRODUCTION ARTWORK · v1.0 · 2026-10-06 · Logo shown from supplied raster, PENDING PRODUCTION MASTER", { x: 0.89, y: 6.55, w: 6.8, h: 0.5, fontFace: "Inter", fontSize: 8, color: BEIGE, charSpacing: 1.5, margin: 0, isTextBox: true });
  s.addNotes("Cover. GEM — Amenities & Packaging is a descriptive business stream under the GEM master brand (register C03, C05, T01). Everything shown is a concept; no structure, material, volume, ingredient, claim, supplier, MOQ or price is stated. The logo is the supplied raster, PENDING PRODUCTION MASTER (VAL-02)."); }

// 02 BUSINESS STREAM
{ const s = pres.addSlide({ masterName: "LIGHT" });
  eyebrow(s, "02 · BUSINESS STREAM", INK); title(s, "One master brand. One descriptive stream.", INK, 0.89, 1.22, 6.2);
  body(s, [
    { text: "GEM™ — Amenities & Packaging is a descriptive business stream under the GEM™ master brand. It is not a separate identity: same logo, same palette, same typography, with a descriptive line set in type.", options: { breakLine: true } },
    { text: "", options: { breakLine: true } },
    { text: "GEM is positioned as a hospitality supplier and partner, not a hotel operator. The stream translates the brand's principles of precision, proportion and restraint into the physical touchpoints a guest holds, opens and keeps.", options: { breakLine: true } },
    { text: "", options: { breakLine: true } },
    { text: "What GEM is proposing: a coordinated family of amenities and packaging that one property can adopt as a whole. What GEM can currently prove: the brand system. Commercial scope, capability and supply are CONDITIONAL until validation closes (AC03, VAL-01).", options: {} }
  ], INK, 0.89, 2.7, 5.6, 3.4, 11.5);
  s.addShape(pres.ShapeType.rect, { x: 7.4, y: 1.22, w: 5.0, h: 4.6, fill: { color: INK }, line: { color: INK, width: 0 } });
  s.addText([
    { text: "POTENTIAL OFFER · COMMERCIAL SCOPE PENDING", options: { fontSize: 8, charSpacing: 2, breakLine: true, color: BEIGE } },
    { text: "", options: { breakLine: true } },
    { text: "Product and packaging design", options: { breakLine: true, fontSize: 14, fontFace: "Jost", color: WHITE } },
    { text: "Sourcing and selection", options: { breakLine: true, fontSize: 14, fontFace: "Jost", color: WHITE } },
    { text: "Customisation and property editions", options: { breakLine: true, fontSize: 14, fontFace: "Jost", color: WHITE } },
    { text: "Manufacturing coordination", options: { breakLine: true, fontSize: 14, fontFace: "Jost", color: WHITE } },
    { text: "Replenishment programmes", options: { breakLine: true, fontSize: 14, fontFace: "Jost", color: WHITE } },
    { text: "", options: { breakLine: true } },
    { text: "Register E01–E14: target offer, approved as direction. External capability claims remain CONDITIONAL on operational validation. GEM does not claim manufacturing, warehousing or owned logistics (E06, E10–E12).", options: { fontSize: 9, color: BEIGE } }
  ], { x: 7.75, y: 1.5, w: 4.3, h: 4.1, fontFace: "Inter", color: WHITE, margin: 0, valign: "top", isTextBox: true, paraSpaceAfter: 4 });
  stamp(s, "DESCRIPTIVE STREAM · APPROVED (C03, T01) · CAPABILITY CLAIMS CONDITIONAL (VAL-01)", INK);
  s.addNotes("Positioning per register C08, C09 and AC02: supplier and partner, not an operator. The offer list is the register's target architecture (E01–E14), stated as potential offer only."); }

// 03 PORTFOLIO PRINCIPLE
{ const s = pres.addSlide({ masterName: "LIGHT" });
  eyebrow(s, "03 · PORTFOLIO PRINCIPLE", INK); title(s, "ONE SYSTEM. MANY TOUCHPOINTS.", INK, 0.89, 1.22, 7, 28);
  pic(s, "03_one_system_scales.png", 0.89, 2.3, 11.55, 3.8, "Four packaging scales in one system: sachet, small bottle, bottle, carton");
  body(s, "Every product is part of one coordinated guest experience. The same symbol, the same proportions, the same hierarchy and the same quiet surfaces, from a sachet to a carton.", INK, 0.89, 6.15, 8, 0.5, 10);
  stamp(s, STATUS, INK, 9.3, 6.35, 3.2);
  s.addNotes("Family recognition comes from proportion and hierarchy, not from decoration (principles 01–04). Scales shown are relative only; no dimension is implied."); }

// 04–08 product pages
const FAMILY = [
  ["04", "SHAMPOO", "shampoo", "Hair cleanser", "In-room application: guest bathroom vanity.", "07_vanity_scene.png"],
  ["05", "CONDITIONER", "conditioner", "Hair conditioner", "Same system. Differentiated by product name and controlled hierarchy only.", "07_vanity_scene.png"],
  ["06", "BODY WASH", "body_wash", "Body cleanser", "Family logic continues. Wall-mounted and refill formats: [REQUIRES SUPPLIER].", "10_packaging_architecture.png"],
  ["07", "BODY LOTION", "body_lotion", "Body moisturiser", "Guest-room placement and vanity arrangement.", "07_vanity_scene.png"],
  ["08", "HAND WASH", "hand_wash", "Hand cleanser", "Guest bathroom, public washroom, suite. No dispenser or bottle structure is approved.", "08_handwash_washroom.png"],
];
for (const [no, name, key, func, note, scene] of FAMILY) {
  const s = pres.addSlide({ masterName: "LIGHT" });
  eyebrow(s, `${no} · PILOT FAMILY · ${name}`, INK);
  pic(s, `${no}_${key}_front.png`, 0.89, 1.3, 3.0, 4.0, `${name} front concept`);
  pic(s, `${no}_${key}_rear.png`, 4.05, 1.3, 3.0, 4.0, `${name} rear concept with placeholder information panel`);
  pic(s, `${no}_${key}_closeup.png`, 7.2, 1.3, 5.25, 1.9, `${name} label close-up`);
  pic(s, scene, 7.2, 3.4, 5.25, 1.9, `${name} in-room application scene`);
  s.addText([
    { text: `GEM™  ·  [COLLECTION / TIER]  ·  ${name.charAt(0) + name.slice(1).toLowerCase()} · ${func}  ·  [QUANTITY / SIZE]  ·  [INSTRUCTIONS · REQUIRED MARKET INFORMATION]  ·  [SKU / ARTWORK VERSION]`, options: { fontSize: 9, color: INK, breakLine: true } },
    { text: note, options: { fontSize: 10, color: INK } }
  ], { x: 0.89, y: 5.5, w: 11.55, h: 0.7, fontFace: "Inter", margin: 0, valign: "top", isTextBox: true, paraSpaceAfter: 3 });
  stamp(s, `${STATUS} · QUANTITY, INGREDIENTS, CLAIMS, ORIGIN, SUPPLIER: [PENDING]`, INK);
  s.addNotes(`${name}: pilot family product (register T02, T03). Six-level information hierarchy per T05. No formulation, fragrance, volume, claim, origin, supplier, MOQ or price is stated. Structure shown is a concept; any alternative structure is [REQUIRES SUPPLIER].`);
}

// 09 FAMILY LINEUP
{ const s = pres.addSlide({ masterName: "LIGHT" });
  eyebrow(s, "09 · PACKAGING SYSTEM · FAMILY LINEUP", INK);
  pic(s, "09_family_lineup.png", 0.89, 1.3, 11.55, 4.8, "The five pilot products together on a white field");
  body(s, "Consistent proportion, hierarchy, typography, spacing and colour. Recognition comes from the family, not from any single pack.", INK, 0.89, 6.15, 8, 0.4, 10);
  stamp(s, STATUS, INK, 9.3, 6.35, 3.2);
  s.addNotes("Pilot family: Shampoo, Conditioner, Body Wash, Body Lotion, Hand Wash (T03). Relative sizes are illustrative."); }

// 10 PACKAGING ARCHITECTURE
{ const s = pres.addSlide({ masterName: "BEIGE" });
  eyebrow(s, "10 · PACKAGING ARCHITECTURE", INK);
  pic(s, "10_packaging_architecture.png", 0.89, 1.3, 11.55, 4.3, "Structural concept directions: bottle, tube, refill, carton, sachet, pump");
  s.addText([
    { text: "Bottle · Tube · Refill · Carton · Sachet · Pump / dispenser · Presentation set", options: { fontFace: "Jost", fontSize: 14, color: INK, breakLine: true } },
    { text: "Every structural format is a concept direction. Structure, closure, resin or substrate, decoration method and carton construction are [REQUIRES SUPPLIER] (Part C slide 32). No dimension is stated.", options: { fontSize: 10, color: INK } }
  ], { x: 0.89, y: 5.7, w: 11.55, h: 0.7, fontFace: "Inter", margin: 0, valign: "top", isTextBox: true, paraSpaceAfter: 3 });
  stamp(s, "STRUCTURAL CONCEPT · [REQUIRES SUPPLIER] · " + STATUS, INK);
  s.addNotes("Structural framework per Part C slide 32: bottle or tube format, resin, closure, decoration method, carton and inner pack are supplier decisions tested before release."); }

// 11 PRIMARY PACK
{ const s = pres.addSlide({ masterName: "LIGHT" });
  eyebrow(s, "11 · PRIMARY PACK · THREE CONCEPT FORMATS", INK);
  pic(s, "11_primary_pack_alternatives.png", 0.89, 1.3, 11.55, 4.5, "Cylindrical bottle, rectangular bottle and soft tube carrying the same label system");
  s.addText("Cylindrical bottle  ·  Rectangular bottle  ·  Soft tube", { x: 0.89, y: 5.9, w: 11.55, h: 0.3, fontFace: "Jost", fontSize: 14, color: INK, margin: 0, isTextBox: true });
  stamp(s, "STRUCTURAL CONCEPT · REQUIRES SUPPLIER VALIDATION · NONE OF THESE IS AN APPROVED STRUCTURE", INK);
  s.addNotes("Three alternative primary-pack formats on one label system. None is approved; the supplier dieline is the only dieline (Part C slide 31)."); }

// 12 SECONDARY PACKAGING
{ const s = pres.addSlide({ masterName: "DARK" });
  eyebrow(s, "12 · SECONDARY PACKAGING", BEIGE);
  pic(s, "12_secondary_packaging.png", 0.89, 1.3, 11.55, 4.5, "Sleeve, carton and presentation box concepts in Ink, Beige and White board");
  body(s, "Carton · Sleeve · Box · Multi-product set. Restraint and geometry do the work: one symbol, one hairline, matte board. No decorative luxury cues, no foil by default, no gold.", BEIGE, 0.89, 5.9, 11.55, 0.5, 10);
  stamp(s, STATUS + " · DIELINE [REQUIRES SUPPLIER]", BEIGE);
  s.addNotes("Print principles per Part C slide 22 and finish direction U01–U10: uncoated warm paper, deep Ink board, deboss or blind emboss, soft-touch selectively; foil only if specifically approved; no chrome, holographic or heavy gloss."); }

// 13 PERSONAL CARE EXTENSIONS
{ const s = pres.addSlide({ masterName: "LIGHT" });
  eyebrow(s, "13 · POTENTIAL RANGE EXTENSIONS · PERSONAL CARE · CONCEPT ONLY", INK);
  pic(s, "13_personal_care_extensions.png", 0.89, 1.3, 11.55, 4.3, "Six complementary amenity packaging concepts");
  body(s, "Soap · Dental kit · Shaving kit · Vanity kit · Shower cap · Comb. Examples of packaging opportunities only. GEM does not currently claim to manufacture or supply them; contents and specifications are not defined.", INK, 0.89, 5.7, 11.55, 0.6, 10);
  stamp(s, "CONCEPT RANGE EXTENSION · COMMERCIAL SCOPE [PENDING]", INK);
  s.addNotes("Exploratory only. Not approved product lines (register C10: show only approved active streams; these are packaging opportunities within the approved stream, not new streams)."); }

// 14 GUEST ACCESSORIES
{ const s = pres.addSlide({ masterName: "BEIGE" });
  eyebrow(s, "14 · POTENTIAL RANGE EXTENSIONS · GUEST ACCESSORIES · CONCEPT ONLY", INK);
  pic(s, "14_guest_accessories.png", 0.89, 1.3, 11.55, 4.3, "Six packaged hospitality accessory concepts");
  body(s, "Sewing kit · Slippers · Laundry bag · Tissue box · Shoe-care kit · Cotton pads. Compact packaging, one hierarchy, one family. Contents and specifications are not defined.", INK, 0.89, 5.7, 11.55, 0.6, 10);
  stamp(s, "CONCEPT RANGE EXTENSION · COMMERCIAL SCOPE [PENDING]", INK);
  s.addNotes("Packaging opportunities only; no supply claim."); }

// 15 ROOM TOUCHPOINTS
{ const s = pres.addSlide({ masterName: "DARK" });
  eyebrow(s, "15 · ROOM TOUCHPOINTS", BEIGE);
  pic(s, "15_room_touchpoints.png", 0.89, 1.3, 11.55, 4.5, "Bedside stationery, coffee point, wardrobe and bathroom concepts in one scene");
  body(s, "Bedside stationery · Coffee point · Wardrobe · Bathroom vanity. One identity creates continuity across guest moments; the objective is coherence, not completeness.", BEIGE, 0.89, 5.9, 11.55, 0.5, 10);
  stamp(s, STATUS, BEIGE);
  s.addNotes("Guest journey per Part A slide 55: arrival, stay, dining, service, departure, return. Only the packaging layer is shown."); }

// 16 PROPERTY EDITION
{ const s = pres.addSlide({ masterName: "LIGHT" });
  eyebrow(s, "16 · PROPERTY EDITION · CONDITIONAL", INK); title(s, "A controlled adaptation for one property.", INK, 0.89, 1.22, 5.5, 26);
  body(s, "Property Edition is named in the register (E14) and in Part A slide 60; its scope is CONDITIONAL until commercial validation closes (AC03, VAL-01).\n\nThe adaptation is controlled: the GEM identity is unchanged; the property is named as a typeset descriptive line at the tier level. No separate logo, no new palette, no stream symbol (C04, C11, C12).\n\nTier naming: Property Edition and Bespoke Programme are register names; the name of the standard range is [REQUIRES OWNER].", INK, 0.89, 2.8, 5.3, 3.3, 11);
  pic(s, "16_property_edition.png", 6.7, 1.22, 5.75, 4.9, "Shampoo concept with a typeset Property Edition line");
  stamp(s, "PROPERTY EDITION · CONDITIONAL (AC03, VAL-01) · CONCEPT", INK);
  s.addNotes("Property-specific content stays CONDITIONAL or CONCEPT per the source documents. Whether a family or property name may occupy the collection/tier level is [REQUIRES OWNER · Product / Amenities Lead]."); }

// 17 CO-BRANDED
{ const s = pres.addSlide({ masterName: "BEIGE" });
  eyebrow(s, "17 · CO-BRANDED APPLICATION · CONCEPT", INK); title(s, "GEM™ + PROPERTY NAME", INK, 0.89, 1.22, 5.5, 26);
  body(s, "Partners stand beside GEM, not inside it (Part A slide 31). The supplier relationship is shown as a typeset line: \"Supplied by GEM™ for PROPERTY NAME\". Optical balance, each brand's clearspace, a hairline where appropriate.\n\nNever merge, recolour, contain or redraw either identity. Precedence follows the approved agreement; the equal-partner arrangement is a default, not a mandate (I10, I11).\n\nPROPERTY NAME is a fictional placeholder; no real partner is approved.", INK, 0.89, 2.8, 5.3, 3.3, 11);
  pic(s, "17_cobranded.png", 6.7, 1.22, 5.75, 4.9, "Body wash concept with a typeset supplied-by line for a fictional property");
  stamp(s, "CO-BRANDING CONCEPT · SUBJECT TO PARTNER AGREEMENT", INK);
  s.addNotes("Co-branding rules per Part A slide 31 and register I10–I12."); }

// 18 BESPOKE
{ const s = pres.addSlide({ masterName: "DARK" });
  eyebrow(s, "18 · BESPOKE PROGRAMME · CONDITIONAL", BEIGE); title(s, "Controlled customisation. The identity stays dominant.", WHITE, 0.89, 1.22, 5.5, 26);
  body(s, "Bespoke programmes are named in the register (E14) as part of the intended offer; the tier is CONDITIONAL (Part A 60, Part C 27).\n\nWhat may flex: label tone within the four colours, surface, format and information set per property.\n\nWhat never flexes: the symbol, the palette, the typography, the hierarchy, the one-spark rule. Customisation is not unrestricted design; every variant is approved through brand governance (C06, C07).", BEIGE, 0.89, 2.8, 5.3, 3.3, 11);
  pic(s, "18_bespoke.png", 6.7, 1.22, 5.75, 4.9, "Three label-tone variants of the same shampoo concept");
  stamp(s, "BESPOKE PROGRAMME · CONDITIONAL · CONCEPT", BEIGE);
  s.addNotes("Any future stream or programme inherits the identity and never forks it (Part A slide 17)."); }

// 19 MATERIAL DIRECTION
{ const s = pres.addSlide({ masterName: "LIGHT" });
  eyebrow(s, "19 · MATERIAL DIRECTION · PENDING SUPPLIER VALIDATION", INK);
  pic(s, "19_material_direction.png", 0.89, 1.3, 11.55, 4.8, "Eight material-direction swatches");
  body(s, "Warm uncoated paper · Matte board · Ink and Beige surfaces · Controlled translucent material · Neutral plastics · Restrained tactile finishes. Feel before shine. No substrate, GSM, polymer, resin, recycled content or certification is stated.", INK, 0.89, 6.15, 11.55, 0.45, 9.5);
  stamp(s, "MATERIAL DIRECTION · PENDING SUPPLIER VALIDATION", INK, 0.89, 6.55, 8);
  s.addNotes("Direction per Part A slide 63 and Part C slide 23 (paper and board attributes [REQUIRES SUPPLIER / OWNER]); register U01–U03."); }

// 20 FINISH DIRECTION
{ const s = pres.addSlide({ masterName: "BEIGE" });
  eyebrow(s, "20 · FINISH DIRECTION · PENDING PHYSICAL PROOF", INK);
  pic(s, "20_finish_direction.png", 0.89, 1.3, 11.55, 4.8, "Blind emboss, deboss, precision die-cut and soft-touch matte finish samples");
  body(s, "Blind emboss · Deboss · Precision die-cut · Soft-touch matte. Avoid decorative gold foil, chrome, holographic finishes and heavy gloss. Depth, pressure, plate, minimum feature size and tooling are defined only by supplier trials.", INK, 0.89, 6.15, 11.55, 0.45, 9.5);
  stamp(s, "FINISH DIRECTION · PENDING PHYSICAL PROOF", INK, 0.89, 6.55, 8);
  s.addNotes("Part C slides 24–25; register U04–U10."); }

// 21 INFORMATION HIERARCHY
{ const s = pres.addSlide({ masterName: "DARK" });
  eyebrow(s, "21 · INFORMATION HIERARCHY · APPROVED ORDER (T05)", BEIGE); title(s, "Six levels. Read from the top, down.", WHITE, 0.89, 1.22, 5.5, 26);
  s.addText([
    { text: "01  GEM™", options: { breakLine: true, fontFace: "Jost", fontSize: 18 } },
    { text: "02  [COLLECTION / TIER]", options: { breakLine: true, fontFace: "Jost", fontSize: 16 } },
    { text: "03  [PRODUCT] · [FUNCTION]", options: { breakLine: true, fontFace: "Jost", fontSize: 14 } },
    { text: "04  [QUANTITY / SIZE] · metric first", options: { breakLine: true, fontSize: 12 } },
    { text: "05  [INSTRUCTIONS · REQUIRED MARKET INFORMATION] · [REGULATORY COPY]", options: { breakLine: true, fontSize: 11 } },
    { text: "06  [SKU] · [ARTWORK VERSION]", options: { fontSize: 10 } }
  ], { x: 0.89, y: 2.6, w: 5.6, h: 3.2, fontFace: "Inter", color: BEIGE, margin: 0, valign: "top", isTextBox: true, paraSpaceAfter: 8 });
  pic(s, "21_information_hierarchy.png", 6.9, 1.22, 5.55, 5.1, "Flat label showing the six-level hierarchy with placeholders");
  stamp(s, "HIERARCHY APPROVED (T05) · ALL CONTENT PLACEHOLDER · REGULATORY COPY: REGULATORY REVIEW REQUIRED", BEIGE);
  s.addNotes("Hierarchy per register T05 and Part A slide 61 / Part C slide 29. Ingredients, claims, warnings, origin and regulatory text are supplied by the accountable owner and reviewed per market (Part C slide 33)."); }

// 22 BILINGUAL
{ const s = pres.addSlide({ masterName: "LIGHT" });
  eyebrow(s, "22 · BILINGUAL PACKAGING · ARABIC PENDING LOCALIZATION APPROVAL", INK); title(s, "English and Arabic, with equal care.", INK, 0.89, 1.22, 5.5, 26);
  body(s, "Arabic is planned as mandatory for Saudi-market packaging unless a qualified regulatory review confirms an exception (T11).\n\nTrue right-to-left setting. No tracking on Arabic. The logo is never mirrored. Technical identifiers (SKU, batch, codes) stay in Latin digits, left to right (M11, M12).\n\nWhich language leads on a pack is set per market policy: [REQUIRES OWNER]. The Arabic shown is a working string; all Arabic copy remains PENDING LOCALIZATION APPROVAL until native review (M16, VAL-07). Regulatory text: [ARABIC COPY PENDING NATIVE REVIEW].", INK, 0.89, 2.8, 5.3, 3.4, 10.5);
  pic(s, "22_bilingual.png", 6.7, 1.22, 5.75, 4.9, "Shampoo concept label with an Arabic working string beside the English product name");
  stamp(s, "BILINGUAL CONCEPT · ARABIC PENDING LOCALIZATION APPROVAL · NOT APPROVED COPY", INK);
  s.addNotes("Bilingual rules per Part A slides 37–39 and Part B RC2 slides 12–13. The register's Arabic-first default (S07) is scoped to wayfinding; the packaging language order is not decided and is marked [REQUIRES OWNER]."); }

// 23 FROM CONCEPT TO PRODUCTION
{ const s = pres.addSlide({ masterName: "LIGHT" });
  eyebrow(s, "23 · FROM CONCEPT TO PRODUCTION", INK); title(s, "This document does not replace Part C.", INK, 0.89, 1.22, 7, 26);
  const steps = ["Concept direction", "Product / commercial scope confirmation", "Supplier structure", "Dieline", "Regulatory information", "Artwork development", "Supplier proof", "Physical sample", "Approval", "Production release"];
  steps.forEach((t, i) => {
    const col = i % 5, row = Math.floor(i / 5); const x = 0.89 + col * 2.33, y = 2.5 + row * 1.6;
    s.addShape(pres.ShapeType.rect, { x, y, w: 2.15, h: 1.3, fill: { color: WHITE }, line: { color: INK, width: 0.75 } });
    s.addText(String(i + 1).padStart(2, "0"), { x: x + 0.15, y: y + 0.12, w: 1.8, h: 0.3, fontFace: "Inter", fontSize: 9, color: INK, charSpacing: 2, margin: 0, isTextBox: true });
    s.addText(t, { x: x + 0.15, y: y + 0.45, w: 1.9, h: 0.75, fontFace: "Jost", fontSize: 13, color: INK, margin: 0, valign: "top", isTextBox: true });
  });
  body(s, "GEM™ Production Standards V3.0 — Part C — RC2 governs steps 03 to 10: supplier dielines, materials, finishes, proof levels P1–P5, golden samples, regulatory review and release (14-step workflow, Part C slide 5). THIS DOCUMENT DOES NOT REPLACE PART C PRODUCTION STANDARDS.", INK, 0.89, 5.8, 11.55, 0.6, 10);
  stamp(s, "CONCEPT PORTFOLIO · PRODUCTION CONTROLS: PART C RC2 · WORKING EDITION / PENDING PRODUCTION VALIDATION", INK, 0.89, 6.45, 11.5);
  s.addNotes("Mapping to Part C: supplier structure (slide 32), dieline (31, App. G), regulatory copy (33, App. H), preflight (19, App. C), proofs (49), physical sample (36, App. I), release (5, App. A)."); }

// 24 CLOSING
{ const s = pres.addSlide({ masterName: "COVER" });
  lockup(s, "Beige", 0.89, 0.89, 0.9);
  s.addShape(pres.ShapeType.ellipse, { x: 8.6, y: 1.4, w: 7.5, h: 7.5, fill: { type: "none" }, line: { color: BEIGE, width: 1 } });
  s.addText("EVERY DETAIL, IN PROPORTION.", { x: 0.89, y: 3.2, w: 7.5, h: 0.8, fontFace: "Jost", fontSize: 30, color: WHITE, charSpacing: 2, margin: 0, isTextBox: true });
  s.addText("GEM™ — Amenities & Packaging  ·  CONCEPT PRODUCT PORTFOLIO", { x: 0.89, y: 4.1, w: 7.5, h: 0.4, fontFace: "Inter", fontSize: 12, color: BEIGE, margin: 0, isTextBox: true });
  s.addText("All products, structures, materials and applications shown are conceptual unless explicitly identified as approved. Final specifications require commercial, supplier, regulatory and production validation.", { x: 0.89, y: 5.3, w: 7.2, h: 0.8, fontFace: "Inter", fontSize: 9.5, color: BEIGE, margin: 0, valign: "top", isTextBox: true });
  s.addText("HOSPITALITY, IN PERFECT PROPORTION", { x: 0.89, y: 6.55, w: 7, h: 0.3, fontFace: "Jost", fontSize: 11, color: BEIGE, charSpacing: 3, margin: 0, isTextBox: true });
  s.addNotes("Closing. The headline is an editorial line for this portfolio; the primary tagline remains HOSPITALITY, IN PERFECT PROPORTION, fixed (B04)."); }

(async () => {
  fs.mkdirSync(path.dirname(OUT), { recursive: true });
  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("written", OUT);
})();
