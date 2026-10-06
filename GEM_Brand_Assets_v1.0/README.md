# GEM™ Brand Assets v0.1 (working)

**Status: WORKING ASSETS, built from the GEM V3.0 RC2 specification. Not released (AC20 pending).**

## Created (01_svg)
| Asset | Files | Basis |
|---|---|---|
| Tagline, outlined type | 4 colourways (beige on ink, ink on white, white on ink, black on white) | Tagline token: Jost 400, 0.18em, capitals. Fixed wording (M10). |
| Amenities & Packaging descriptive line | 2 colourways | Set in type; no stream logo exists (T01, AC02). Used beside the unchanged GEM lockup. |
| Palette sheet | 1 | Ink #12171D, Beige #BCACA7, Black #020202, White #FFFFFF, with the four approved pairings and ratios. |
| Status labels | 4 | APPROVED filled, CONDITIONAL outline, PENDING VALIDATION dashed, REFERENCE dotted. |

All text is outlined, so no font is needed to display them. Naming follows X12 (`GEM_[STREAM]_[ASSET]_[VARIANT]_vX.Y_YYYYMMDD`); the `BRAND` stream code is a working choice and needs owner confirmation. Font builds remain VAL-05 open.

## Deliberately NOT created
Part A states that the rest of the logo set is "named, not faked", and that proportions will be published from the production master only (slides 27, 28). Redrawing or auto-tracing the raster is prohibited (DS05, L16). Therefore these were not made, and each stays PENDING PRODUCTION MASTER:

- Vector masters of the lockup and symbol (SVG, PDF, EPS), stacked configuration, white standalone symbol
- No-spark micro mark, favicon and app-icon set, embroidery and engraving masters
- Ring, arc, quarter and spark graphic forms, the clearspace diagram and the signature motion sequence, which all depend on the mark's geometry
- Print colour values (Pantone, CMYK): not specified in the guidelines

Rebuild: `python3 02_build/build_assets.py` (needs fontTools and the three brand font files).

## Official logo kit (04_official_kit) · supplied by the project owner
The owner supplied a vector master kit ("GEM Master Asset Kit V3.0": official paths from the Illustrator PDF, no redraw). It contains horizontal, stacked, symbol and no-spark symbol in Ink, Beige, Black and White (SVG, PDF, EPS, PNG, 2u clearspace versions), favicon and app icon set, avatars, a motion reveal, and `logo/metrics.json`. File hashes are in `SHA256SUMS.txt`.

This supersedes the traced replicas made earlier in this branch, which were removed. The kit supplies the stacked configuration, the no-spark micro mark and the white standalone symbol that Part A lists as not supplied.

Evidence gates stay open until the Brand Owner records the kit as the production master: VAL-02 (production masters), VAL-03 and VAL-04 (trademark and ownership), H21 (artwork ID and version in file names; kit names do not follow X12). Do not label the kit a released master until then.
