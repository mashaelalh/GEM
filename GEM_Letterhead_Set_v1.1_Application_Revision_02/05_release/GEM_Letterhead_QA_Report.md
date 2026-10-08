# GEM Letterhead QA Report

**Set v1.1 Application Revision 02 • 7 October 2026**

**WORKING APPLICATION / PENDING VALIDATION**

Eight findings pass available technical checks. LH03 remains open because full Arabic plain-text extraction/reader acceptance is not proven; LH08 remains an owner/supplier validation item. This is a controlled working package, not an approved stationery system or production release.

## Source and method

Live repository main SHA reverified: `334744c72dbbb6681034996fcca595213a7623a2`. All governing-file hashes match the audit snapshot. Register > Part A > Part B > Part C > official asset kit > QA/evidence discipline. No External Partners Brief used.

Eight editable templates and twelve QA fixtures rendered using the bundled LibreOffice renderer with the verified working fonts. All template samples are one page. Explicit 2/3-page and automatic-flow fixtures pass pagination in English, Arabic and bilingual; each automatic-flow fixture produces three pages. Long bilingual fields deliberately flow to two pages. All affected visuals reviewed, plus grayscale proofs. No native Word or assistive-technology pass is claimed.

## Finding disposition

| Finding | Original severity | Current result |
|---|---|---|
| LH01 Release versions and checksums disagree | P1 HIGH | PASS |
| LH02 Active typography no longer follows the approved font policy | P1 HIGH | PASS / PENDING PLATFORM RETEST |
| LH03 Arabic PDF text layer does not preserve the source text | P1 HIGH | FAIL REMAINING / PENDING ACCESSIBILITY ACCEPTANCE |
| LH04 Mixed-direction reference token breaks in the bilingual release | P1 HIGH | PASS / PENDING PLATFORM RETEST |
| LH05 English first-page pagination exports incomplete text | P1 HIGH | PASS / PENDING NATIVE RETEST |
| LH06 Localization status does not travel with all continuation pages | P2 MEDIUM | PASS |
| LH07 Tagline size and tracking drift across release variants | P2 MEDIUM | PASS |
| LH08 Digital status and footer sizes lack a documented stationery exception | P2 MEDIUM | PENDING / REQUIRES OWNER / REQUIRES SUPPLIER |
| LH09 Unexpected clipboard-like symbols appear in exports | P2 MEDIUM | PASS / PENDING NATIVE RETEST |
| LH10 Release font embedding contains empty parts | P2 MEDIUM | PASS / PENDING RIGHTS ACCEPTANCE |

## LH01 Release versions and checksums disagree

**Severity:** P1 HIGH. **Result:** PASS.
**Original file:** 05_release/README.md, SHA256SUMS.txt and seven DOCX; 01_templates/; 07_final_audit/corrected_docx/; specification and both delivery PDFs.
**Page/template:** Entire delivery package.
**Problem:** Seven of eight release DOCX fail their recorded SHA-256 values. Bilingual Continuation is the one matching file. The README says release files are identical to 01_templates, but seven are different. Later corrections exist only in 07_final_audit; the PDFs and specification still describe R1. A recipient cannot identify one reproducible version.
**Governing source:** C document/release control; Register AC20; QA open gates VAL-16/VAL-21; local source-preservation and release records. Exact repository paths and hashes appear below and in the source snapshot.
**Correction implemented:** Selected corrected baseline, retained useful release edits, regenerated all companions and synchronized release copies. Original variants archived in place, not overwritten.
**Acceptance still required:** All delivery hashes verify; canonical/release copies agree; PDF/specification settings match selected DOCX. Preserve working status and AC20.
**Owner role:** Design Custodian and Document QA.
**Evidence:** `04_qa/evidence/Technical_Checks.json`, `Render_Results.json`, `PDF_Mapping_Repairs.json`, `Visual_Preservation.json`; `00_source/Reconciliation.json`.

## LH02 Active typography no longer follows the approved font policy

**Severity:** P1 HIGH. **Result:** PASS / PENDING PLATFORM RETEST.
**Original file:** 05_release/GEM_Letterhead_Bilingual_First_Page.docx; GEM_Letterhead_Executive.docx.
**Page/template:** Bilingual metadata brackets; Executive subject.
**Problem:** The fresh headless bilingual export uses TimesNewRomanPSMT for four bracket characters. Executive subject exports as Jost-Bold rather than the Regular 400 used in R1/corrected files. These are active rendering facts, not inferred from unused style definitions. Font substitution must not be accepted silently.
**Governing source:** A typography, slides 34–35; B slides 9–12; Register L01/L04/L06/L08; user font-fallback rule. Exact repository paths and hashes appear below and in the source snapshot.
**Correction implemented:** Inter LTR identifiers remain whole; Executive subject is Jost Regular; fresh exports use only Inter/Jost/Noto Regular. Specification theme-font inheritance also removed after the final check detected an unintended substitute. No active substitute or synthetic Bold observed. Native Word platform matrix pending.
**Acceptance still required:** Every active exported text run uses Inter/Jost/Noto Sans Arabic as intended, with Regular 400 weight; no Times New Roman or silent fallback.
**Owner role:** Document QA and Typography Custodian.
**Evidence:** `04_qa/evidence/Technical_Checks.json`, `Render_Results.json`, `PDF_Mapping_Repairs.json`, `Visual_Preservation.json`; `00_source/Reconciliation.json`.

## LH03 Arabic PDF text layer does not preserve the source text

**Severity:** P1 HIGH. **Result:** FAIL REMAINING / PENDING ACCESSIBILITY ACCEPTANCE.
**Original file:** 05_release/GEM_Letterhead_Digital.pdf and Print.pdf; 07_final_audit/evidence/word_renders/ Arabic and bilingual PDFs; fresh private exports of both DOCX families.
**Page/template:** Delivery portfolio pages 3–6; Arabic/bilingual first and continuation proofs.
**Problem:** Pypdf and pdfplumber independently expose damaged Arabic character mapping. The older Digital PDF inserts digit 7 into the Arabic contractual-disclaimer phrase and I into the signatory word. Word evidence PDFs replace dots/diacritics with symbols and digits. Fresh corrected exports also contain malformed extracted Arabic. Visual shaping can look correct while copy/paste, search and assistive reading lose the intended wording. This contradicts the earlier assumption that R1 Arabic extraction was fully correct.
**Governing source:** Register V05/V13; B Arabic/localization mechanics and accessibility; qa/PartB_RC2_RTL_Localization_QA_Report.md; VAL-07/VAL-08/VAL-15. Exact repository paths and hashes appear below and in the source snapshot.
**Correction implemented:** Repaired omitted Arabic combining-mark ToUnicode entries from exporter ActualText, corrected base/mark cluster allocation, and preserved logical source paragraph ActualText. Pypdf layout and pdfplumber independently match the complete Arabic glyph inventory; semantic source paragraphs match DOCX. Generic plain extraction still reverses/omits mixed RTL fragments. This finding is not closed. Native copy/search and AT must pass before controlled real-world PDF use.
**Acceptance still required:** Two independent extractors return source-equivalent Arabic; native copy/paste/search and Arabic assistive reading are tested. Tag presence and visual readability alone do not pass.
**Owner role:** Document Accessibility QA and Arabic Lead.
**Evidence:** `04_qa/evidence/Technical_Checks.json`, `Render_Results.json`, `PDF_Mapping_Repairs.json`, `Visual_Preservation.json`; `00_source/Reconciliation.json`.

## LH04 Mixed-direction reference token breaks in the bilingual release

**Severity:** P1 HIGH. **Result:** PASS / PENDING PLATFORM RETEST.
**Original file:** 05_release/GEM_Letterhead_Bilingual_First_Page.docx.
**Page/template:** Page 1 date/reference metadata.
**Problem:** The fresh render displays the reference as REFERENCE] on one line and [NUMBER on the next. Brackets fall outside their intended token order, and a short placeholder already wraps poorly. This is a usable-field defect, not a preference for one bilingual visual arrangement.
**Governing source:** B slides 12–13: Latin technical IDs stay LTR and isolated; Register M05–M08; RTL QA. Exact repository paths and hashes appear below and in the source snapshot.
**Correction implemented:** Separated date and reference into editable lines; full technical ID uses one explicit Inter LTR run. Short/long codes render in correct bracket order. Email/URL/phone test fields are fixtures only, never company details.
**Acceptance still required:** Short and long reference codes retain bracket/punctuation order; English identifiers, phone, email and URL remain LTR on one-, two- and three-page letters.
**Owner role:** Arabic Lead and Document QA.
**Evidence:** `04_qa/evidence/Technical_Checks.json`, `Render_Results.json`, `PDF_Mapping_Repairs.json`, `Visual_Preservation.json`; `00_source/Reconciliation.json`.

## LH05 English first-page pagination exports incomplete text

**Severity:** P1 HIGH. **Result:** PASS / PENDING NATIVE RETEST.
**Original file:** 05_release/GEM_Letterhead_English_First_Page.docx.
**Page/template:** Page 1 footer, including later-page conditional field behaviour.
**Problem:** The fresh bundled-renderer export shows Page of without page numbers. This file contains a nested IF/NUMPAGES/PAGE field construction; the corrected companion exports Page 1 of 1. Complex fields exist, so they must not be misreported as absent or ordinary typed text. The failure is verified in this export engine, not universally asserted for Microsoft Word.
**Governing source:** C release/preflight discipline; local letterhead specification: live PAGE/NUMPAGES; Register W03/V13. Exact repository paths and hashes appear below and in the source snapshot.
**Correction implemented:** Selected robust live PAGE/NUMPAGES fields with 9 pt Inter formatting. One-page templates and 2/3-page explicit/automatic-flow fixtures show correct page values in the bundled renderer. No incomplete Page of output.
**Acceptance still required:** No orphan Page of text. One-, two- and three-page Word/PDF outputs show correct numbers or intentionally suppress the whole label.
**Owner role:** Document QA.
**Evidence:** `04_qa/evidence/Technical_Checks.json`, `Render_Results.json`, `PDF_Mapping_Repairs.json`, `Visual_Preservation.json`; `00_source/Reconciliation.json`.

## LH06 Localization status does not travel with all continuation pages

**Severity:** P2 MEDIUM. **Result:** PASS.
**Original file:** 01_templates and 05_release Arabic/Bilingual First Page and Continuation DOCX; delivery Digital/Print pages 3–6.
**Page/template:** All automatic continuation pages and footer variants.
**Problem:** PENDING LOCALIZATION APPROVAL is in sample body text, but absent from the release footer variants. Once the sample body is replaced or a continuation page flows automatically, the localization gate can disappear. Later corrected candidates already carry the marker in all relevant footers.
**Governing source:** Register AC10/AC20; B open-localization status; RTL QA; local pending-status discipline. Exact repository paths and hashes appear below and in the source snapshot.
**Correction implemented:** Working and localization status retained in all first/default footers of Arabic and bilingual templates, including automatic continuations.
**Acceptance still required:** Every Arabic/bilingual page retains the correct pending marker after sample replacement and multipage flow.
**Owner role:** Arabic Lead and Design Custodian.
**Evidence:** `04_qa/evidence/Technical_Checks.json`, `Render_Results.json`, `PDF_Mapping_Repairs.json`, `Visual_Preservation.json`; `00_source/Reconciliation.json`.

## LH07 Tagline size and tracking drift across release variants

**Severity:** P2 MEDIUM. **Result:** PASS.
**Original file:** 05_release/GEM_Letterhead_Executive.docx; English_First_Page.docx; Arabic/Bilingual first-page headers require style reconciliation.
**Page/template:** First-page tagline.
**Problem:** Executive explicitly sets 8.5 pt with 38 twips expanded spacing: about 0.224em, rather than 0.18em, and below the 12 CSS px threshold at which tracking is permitted. The release English tagline lacks the explicit spacing run used in R1. R1/corrected first-page taglines consistently use 10.5 pt and 38 twips, approximately 0.181em.
**Governing source:** Register B03/L09; A slides 23/36; B slides 10–11; local specification page 2. Exact repository paths and hashes appear below and in the source snapshot.
**Correction implemented:** Selected corrected Jost Regular tagline at 10.5 pt, 38 twips (~0.181em). Body and Arabic have zero expanded tracking.
**Acceptance still required:** All retained taglines share the approved tracking treatment and the selected application size; no tracking below the digital threshold.
**Owner role:** Typography Custodian.
**Evidence:** `04_qa/evidence/Technical_Checks.json`, `Render_Results.json`, `PDF_Mapping_Repairs.json`, `Visual_Preservation.json`; `00_source/Reconciliation.json`.

## LH08 Digital status and footer sizes lack a documented stationery exception

**Severity:** P2 MEDIUM. **Result:** PENDING / REQUIRES OWNER / REQUIRES SUPPLIER.
**Original file:** All DOCX families; 05_release/GEM_Letterhead_Digital.pdf; Specification.pdf.
**Page/template:** Footers/status; specification footer and source labels.
**Problem:** Delivery PDF uses 6.5 pt working-status text and 7.5 pt contact/footer text. Part B labelSmall is 12 CSS px (9 pt), with a 14 px caption style. These page-based application values are documented, but no stationery-specific digital exception or legibility evidence is approved. This is not a claim that Part B web-body sizing must be mechanically applied to A4 letters, or that 9 pt is a validated physical-print minimum.
**Governing source:** B slide 10 and type tokens; C physical-size/process-test gates; Register accessibility and owner approval. Exact repository paths and hashes appear below and in the source snapshot.
**Correction implemented:** Raised essential footer/status and SAMPLE CONTENT to 9 pt; footer explicitly 12.6 pt exact leading. Visual/grayscale review passed with no collision. This is a working digital application choice, not a newly approved stationery/physical minimum. Owner digital legibility and supplier print proof remain required.
**Acceptance still required:** Approved application decision plus real digital/print legibility evidence; no tiny text carrying essential status without validation.
**Owner role:** Accessibility QA, Brand Owner and Production Lead.
**Evidence:** `04_qa/evidence/Technical_Checks.json`, `Render_Results.json`, `PDF_Mapping_Repairs.json`, `Visual_Preservation.json`; `00_source/Reconciliation.json`.

## LH09 Unexpected clipboard-like symbols appear in exports

**Severity:** P2 MEDIUM. **Result:** PASS / PENDING NATIVE RETEST.
**Original file:** 05_release/GEM_Letterhead_English_Continuation.docx and Executive.docx when exported with the bundled renderer.
**Page/template:** After continuation-text placeholder; beside Executive SAMPLE CONTENT.
**Problem:** The fresh PDF proofs contain clipboard-like symbols that are absent from the R1 delivery portfolio and corrected candidate renders. No matching ordinary emoji text or body-picture record was found, so their exact source/export cause remains unconfirmed. They are visible unintended output artifacts, not asserted to be newly drawn GEM assets.
**Governing source:** A restrained applications/composition; B functional-glyph consistency; C output preflight. Exact repository paths and hashes appear below and in the source snapshot.
**Correction implemented:** Selected clean editable corrected source and discarded corrupt release re-save structures while preserving originals. No unintended clipboard-like symbol appears in fresh exports. Exact original renderer/add-in cause is not asserted.
**Acceptance still required:** No clipboard-like or other unintended symbol appears in native and PDF exports.
**Owner role:** Document QA.
**Evidence:** `04_qa/evidence/Technical_Checks.json`, `Render_Results.json`, `PDF_Mapping_Repairs.json`, `Visual_Preservation.json`; `00_source/Reconciliation.json`.

## LH10 Release font embedding contains empty parts

**Severity:** P2 MEDIUM. **Result:** PASS / PENDING RIGHTS ACCEPTANCE.
**Original file:** Seven changed 05_release DOCX, excluding Bilingual_Continuation.docx.
**Page/template:** Package fontTable relationships and embedded font payloads.
**Problem:** Each changed file carries four zero-byte font payloads referenced as Inter/Noto Sans Arabic variants; English First Page has a fifth zero-byte part. Files grew to roughly 6 MB and include many unused embedded variants. Empty files do not prove that every currently used Regular font is missing, but they are not valid embedded-font evidence. Active fallback is separately reported in LH02.
**Governing source:** B font deployment/acceptance gate VAL-05; C manifest/handoff; official font/license record; local font manifest. Exact repository paths and hashes appear below and in the source snapshot.
**Correction implemented:** Preserved three valid Regular-only font payloads from the corrected candidate. Every payload decoded as a usable TTF with cmap; decoded hashes recorded. No zero-byte embedded parts. Acceptance/licence gate remains open.
**Acceptance still required:** All referenced embedded fonts decode and match the manifest; only intended active families/weights render; package size and embedding status are truthfully documented.
**Owner role:** Typography Custodian and Document QA.
**Evidence:** `04_qa/evidence/Technical_Checks.json`, `Render_Results.json`, `PDF_Mapping_Repairs.json`, `Visual_Preservation.json`; `00_source/Reconciliation.json`.

## Technical checks and evidence gates

| Area | Result | Evidence / remaining action |
|---|---|---|
| DOCX editable paragraphs, real subject heading, retained styles | PASS / PENDING | Package/XML checks and successful bundled reopening; native edit/save/reopen pending |
| Fields, header/footer anchoring, signature and multi-page flow | PASS / PENDING | Headless fixtures including automatic 3-page flow; native Word remains pending |
| Word Mac / Windows / Online | PENDING | Microsoft Word access was rejected by automatic approval review: computer use for that app was not approved. No native automation workaround attempted |
| RTL and mixed email/URL/phone/reference punctuation | PASS visual / PENDING | Explicit RTL paragraphs and LTR token runs; fresh fixture visuals; native Arabic lead review pending |
| Fonts and font substitution | PASS working renderer / PENDING | Embedded Regular payloads decode; all active fonts are required families. Host Office/font acceptance remains pending; stop on fallback |
| PDF A4, fonts, selectable text and metadata | PASS structural | All pages A4; subset fonts embedded; author unset; primary language assigned |
| Arabic generic logical plain extraction | FAIL remaining | Character integrity repaired; pypdf default extraction still omits some RTL fragments and layout/pdfplumber ordering is visual. Inventory equality is not logical-reading acceptance |
| PDF reading order and accessibility | PENDING | Paragraph ActualText, H1, language tags, vector-logo Figure alternatives and bookmarks inspected; parent-tree/page references retained in merged PDF. AT not exercised, no PDF/UA/WCAG completion claim |
| Links / field replacement | PENDING completed-letter retest | Public templates contain replaceable fields, not invented contacts; fixture uses reserved example.invalid. Real link targets must be verified after replacement |
| Logo source, colour, geometry and whitespace | PASS working application | Official SVG/PNG hashes unchanged, supplied colours, no extra geometry, image behind body or competing decoration |
| Digital/Print PDF visual equality | PASS | Repairs are pixel-identical to eight DOCX exports; Digital and Print page content streams identical |
| Grayscale / low ink | PASS screen proof / PENDING physical | No background flood or colour-only meaning; Minimal no rule/tagline. Printer/device physical proof not performed |
| CMYK/Pantone/stock/profile/tolerances | REQUIRES SUPPLIER | Not invented; print PDF is RGB print candidate, not PDF/X/prepress-accepted artwork |
| Localization, S07 correspondence hierarchy, footer acceptance, asset/font masters, rights and AC20 | REQUIRES OWNER / PENDING | All original evidence gates remain open; no Brand Owner authorization inferred |

## Required acceptance sequence

1. Document QA opens all eight templates in Word, replaces fields, saves/closes/reopens, updates fields, checks font substitution and re-exports explicit/automatic 1–3-page and long-field letters.
2. Arabic Lead and Accessibility QA compare whole normalized logical Arabic text, punctuation, marks and mixed IDs using two independent extraction engines plus native copy/search and Arabic assistive technology. Close LH03 only on evidence, not glyph inventory alone.
3. Brand Owner validates the 9 pt digital footer and proposed bilingual correspondence application; localization wording and master/font/rights gates remain separate.
4. Supplier records prepress standard/profile, print conversion and physical legibility/proof evidence before commercial printing. AC20 remains open until authorized by the named owner.

## Governing repository paths

- `GEM_V3_RC2/00_originals/GEM_V3_Final_Brand_Approval_Register_Prefilled.xlsx` SHA256 `ccce46135a4f2244dbff21cef94a6160e9d2b6fd96a63647c1e5ea6b662e7ab3`
- `GEM_V3_RC2/04_release/GEM Brand Guidelines V3.0 — Part A — RC2.pptx` SHA256 `c50dd3d0c45d6e2753e81b0f978879ed7e596ce52bdd24f7910ae6fcf16243d0`
- `PartB_RC2/05_release/GEM Digital Design System V3.0 — Part B — RC2.pptx` SHA256 `b0326b6a6d9c2af6e1128911c2da5b4e2990ddfdc1961c9bc9f30fef240f0312`
- `GEM_V3_RC2/04_release/GEM Production Standards V3.0 — Part C — RC2.pptx` SHA256 `f9f968d2e51d715658796c69e63c83dfe324bf783f6dc530b49bfc0c6fd3462b`
- `PartB_RC2/05_release/tokens/gem-tokens.v3.0-rc2.json` SHA256 `8f625821abd162f92ed7bf2ab0e2d7f979007ef2b1bec8e01a74b37dc7b686b9`
- `GEM_Brand_Assets_v1.0/README.md` SHA256 `8a76c692cfb45672cd9ef86593a62196254e90fa6d6e8a6e507ffd163ac8bae3`
- `qa/PartB_RC2_Accessibility_QA_Report.md` SHA256 `58d53720a68da7cd32891c684ad73ad1ec27f5d2cd6026bcd595bfb35e358c15`
- `qa/PartB_RC2_RTL_Localization_QA_Report.md` SHA256 `0c956cb567dac39df0532b2f93aa8abc438dcdeb07e0c49280e4999165c8ffe9`
- `qa/GEM_V3_RC2_Final_Open_Evidence_Register.md` SHA256 `aea1bad240f2124f457fefc3887f300f9af804702db8f63a939f2036de0931ca`

## Package discipline

Original v1.0 files and unrelated Part D work remain unchanged. The new v1.1 release copies are identical to the canonical working files. Original source creation/modification dates are recorded separately; revision date is 2026-10-07. All manifests and SHA256SUMS belong only to this new working revision. Re-exporting Word files does not automatically retain the controlled PDF mapping/semantic repair; every completed letter requires a new validation cycle.
