# GEM™ — Amenities & Packaging · Concept Product Portfolio v1.0 · Change and Source Log

**File:** `GEM_Amenities_and_Packaging_Concept_Portfolio_v1.0.pptx` (+ PDF review copy) · 24 slides · issued 2026-10-06 · **CONCEPT / NOT PRODUCTION ARTWORK**.

## A. Rules taken from the GEM V3.0 RC2 documents (not invented)

| Element in the portfolio | Source | Rule applied |
|---|---|---|
| Master brand name GEM™; stream named "GEM™ — Amenities & Packaging" as a descriptive line in type, no stream logo | Register B01, C03, C04, C05, C11, C12; Part A RC2 slides 16–17, 60 | No new logo, symbol, colour or sub-brand |
| Primary tagline HOSPITALITY, IN PERFECT PROPORTION (capitals, Jost, tracked, one line); secondary line "Every arrival, precisely composed." | Register B04–B08; Part A 23–24 | Tagline unaltered on cover and closing; closing headline "EVERY DETAIL, IN PROPORTION." is an editorial line for this document, not a tagline |
| Palette Ink #12171D, Beige #BCACA7, Black #020202, White #FFFFFF; no gold, gradients, shadows as decoration, accent colours | Register J01–J13; Part A 32–33 | Mockup lighting is photographic shading on matte objects, not a graphic gradient |
| Typography Jost (display), Inter (body, labels), Noto Sans Arabic (interim) | Register L01–L08, M02; Part A 34–37 | Labels: Jost 400 for product names, Inter 400/500 for information; tracking only on capitals |
| Four principles; ring / arc / quarter / spark; one spark maximum | Register N01–N11; Part A 8–11, 42–44 | One ring on the closing page only; no spark used (none needed) |
| Positioning: supplier and partner, not a hotel operator | Register C08, C09, AC02; Part A 12–13 | Slide 02 |
| Potential offer list (design, sourcing, customisation, manufacturing coordination, replenishment); no manufacturing, warehousing or owned logistics claims | Register E01–E14 (approved as target offer, claims CONDITIONAL) | Slide 02, labelled POTENTIAL OFFER · COMMERCIAL SCOPE PENDING |
| Pilot family Shampoo, Conditioner, Body Wash, Body Lotion, Hand Wash | Register T02, T03; Part A 62; Part C 28 | Slides 04–09 |
| Six-level information hierarchy | Register T05; Part A RC2 61; Part C RC2 29; Part B RC2 27 | Slide 21 and every label |
| Tiers Property Edition and Bespoke Programme named; all tiers CONDITIONAL; name of the standard range [REQUIRES OWNER] | Register E14, AC03, VAL-01; Part A RC2 60; Part C RC2 27 | Slides 16, 18 |
| Co-branding: partners beside GEM, equal-partner default, precedence per agreement, no real partner | Register I10–I12; Part A 31 | Slide 17, fictional PROPERTY NAME |
| Materials: warm uncoated stock, Ink board, Beige, deboss, blind emboss, soft-touch, precision die-cut; avoid gold, chrome, holographic, heavy foil, gloss | Register U01–U10; Part A 63; Part C 22–25 | Slides 19–20 |
| Structure, closure, resin, decoration, carton: supplier decisions; supplier dieline is the only dieline; no dimensions | Part C 20, 31, 32 | Slides 10–12 [REQUIRES SUPPLIER] |
| Regulatory copy supplied by the accountable owner and reviewed per market; Arabic mandatory for Saudi packaging pending review | Register T10, T11, Y05; Part C 33 | Slides 21–22 placeholders |
| Bilingual mechanics: true RTL, no tracking on Arabic, logo never mirrored, technical IDs Latin/LTR; all Arabic PENDING LOCALIZATION APPROVAL | Register M05, M06, M08, M11, M12, M16; Part A 37–39; Part B RC2 12–13 | Slide 22 |
| Status vocabulary and placeholders | Register AA01–AA04; Part A RC2 4; Part C RC2 3 | Every slide carries its status |
| Logo: supplied raster used unchanged (scaled only), PENDING PRODUCTION MASTER; never traced or redrawn | Register H01–H03, H16, DS05; Part A 26–27; Part C 7 | Symbol and lockup PNGs extracted from Part A RC2 media |
| Production route: Part C 14-step workflow, proof levels P1–P5, golden sample | Part C RC2 5, 49, 50 | Slide 23 |

## B. Elements that are conceptual (created for this portfolio)

| Element | Nature | Label carried |
|---|---|---|
| Bottle, tube, rectangular bottle, pump, sachet, carton, sleeve, set-box shapes | Illustrative structures; proportions arbitrary; no dimension or volume | STRUCTURAL CONCEPT · REQUIRES SUPPLIER VALIDATION |
| Label layouts (symbol, tier line, product, function, placeholders) | Concept art direction applying the T05 hierarchy | CONCEPT / NOT PRODUCTION ARTWORK |
| Function descriptors ("Hair cleanser", "Body moisturiser"…) | Plain functional naming per T04; not claims | — |
| In-room, washroom and vanity scenes | Rendered compositions (Pillow); not photography | CONCEPT / NOT PRODUCTION ARTWORK |
| Material swatches and finish samples | Rendered textures; not physical samples | MATERIAL DIRECTION · PENDING SUPPLIER VALIDATION / PENDING PHYSICAL PROOF |
| Range-extension products (soap, dental kit, …, coffee packaging) | Packaging opportunities only; no supply claim; contents undefined | CONCEPT RANGE EXTENSION · COMMERCIAL SCOPE [PENDING] |
| Arabic product-name strings (شامبو etc.) | Working layout strings for shaping and scale only | PENDING LOCALIZATION APPROVAL / [ARABIC COPY PENDING NATIVE REVIEW] |
| "Property edition · [PROPERTY NAME]" and "Supplied by GEM™ for PROPERTY NAME" lines | Typeset descriptive lines, fictional partner | CONDITIONAL / CO-BRANDING CONCEPT |
| Closing headline "EVERY DETAIL, IN PROPORTION." | Editorial line for this document only | — |

## C. Deliberately absent (would be invention)
Ingredients, fragrances, formulations, claims (incl. sustainability, recyclable, organic, vegan, dermatological), country of origin, supplier names, certifications, bottle volumes, dimensions, GSM, polymers, MOQs, prices, lead times, approved Arabic copy, regulatory text, dispenser approvals, real hotel brands.

## D. Build and QA record
- Mockups: `02_build/mockups.py` (Pillow + numpy, 2× supersampled, exported at full resolution to `01_mockups/`), logo rasters unchanged.
- Deck: `02_build/build_deck.js` (pptxgenjs, structured deck, GEM theme colours, Jost/Inter).
- Fonts installed for rendering: Jost, Inter, Noto Sans Arabic (OFL builds; licence/build validation VAL-05 remains open).
- Every slide rendered to PDF and PNG and inspected (see `05_qa/Visual_QA.md`).
