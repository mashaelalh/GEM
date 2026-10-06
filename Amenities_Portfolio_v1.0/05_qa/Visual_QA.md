# Visual QA · GEM_Amenities_and_Packaging_Concept_Portfolio_v1.0

(Filled in after the final render; see the slide-by-slide table below.)

## Method
Deck built with pptxgenjs (structured deck, GEM theme), exported to PDF with LibreOffice with Jost, Inter and Noto Sans Arabic installed, rendered to PNG at 60 dpi contact sheets and 110 dpi spot checks. Mockups rendered twice: first pass rejected (bottles exceeded the frame, product names clipped on narrow labels, pump head crude, swatch captions overlapping); second pass with frame-relative sizing, auto-fitted label type and a refined pump.

## Checklist
| Check | Result |
|---|---|
| All pages rendered | see table |
| No text overflow | see table |
| No distorted logo (supplied raster scaled proportionally only) | PASS by construction (`logo()` resizes with the source aspect ratio; symbol and lockup never redrawn) |
| No unsupported claims / invented ingredients / regulatory data / dimensions / supplier specs | `QA_Report.md` automated scan |
| No unapproved Arabic copy | Only working strings, labelled PENDING LOCALIZATION APPROVAL / [ARABIC COPY PENDING NATIVE REVIEW] |
| All concepts labelled | every slide carries a status line (automated) |
| Portfolio reads as one family | one bottle family, one label system, one symbol scale, one light direction |
| Visual system matches GEM | four colours only (automated XML check), Jost/Inter only, ring on the closing page, no spark used |
| Mockups premium and believable | matte cylinder shading, paper texture, contact shadows; no gloss, no gradients as decoration |
| Works for senior B2B audiences | minimal copy, status on every page, offer vs proof separated on slide 02 |

## Slide-by-slide
| Slide | Content | Overflow / overlap / substitution | Result |
|---|---|---|---|
| 1 | Cover: lockup, product hero, tagline, status | none | PASS |
| 2 | Business stream, offer panel | none | PASS |
| 3 | One system, four scales | none | PASS |
| 4 | Shampoo front/rear/close-up/scene | none | PASS |
| 5 | Conditioner | none | PASS |
| 6 | Body Wash | none | PASS |
| 7 | Body Lotion | none | PASS |
| 8 | Hand Wash | none | PASS |
| 9 | Family lineup | none | PASS |
| 10 | Packaging architecture | none | PASS |
| 11 | Primary pack formats | none | PASS |
| 12 | Secondary packaging | none | PASS |
| 13 | Personal-care extensions | none | PASS |
| 14 | Guest accessories | none | PASS |
| 15 | Room touchpoints | none | PASS |
| 16 | Property Edition | none | PASS |
| 17 | Co-branded application | none | PASS |
| 18 | Bespoke Programme | none | PASS |
| 19 | Material direction | none | PASS |
| 20 | Finish direction | none | PASS |
| 21 | Information hierarchy | none | PASS |
| 22 | Bilingual packaging (Arabic shaped natively, right-aligned) | none | PASS |
| 23 | Concept to production | none | PASS |
| 24 | Closing | none | PASS |

Export: 24 pages, tagged PDF, fonts embedded Jost-Regular, Inter-Regular (variable builds; 500 weights render from the same file). Mockup pass history: pass 1 rejected (frame overflow, clipped names, crude pump, caption overlap, invisible stamps on beige floors, reversed Arabic); pass 2 accepted.
