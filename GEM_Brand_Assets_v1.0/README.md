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

## Logo replicas (03_logo_replica) · added
Five vector replicas of the supplied logo set (Part A slide 27): horizontal lockup in beige, black and white; symbol in beige and black. Each SVG is a single filled path produced by upsampling the supplied PNG's alpha channel and tracing it (`02_build/trace_logos.py`). No geometry was redrawn by hand, and nothing was mirrored, recoloured or altered.

**Status: WORKING REPLICA, PENDING PRODUCTION MASTER (VAL-02, H16, H17).** Limits you should know before use:
- The source rasters are only 654 x 207 and 229 x 207 px, so curve edges are approximations of the supplied pixels, not the original construction. Do not use for print, fabrication, embroidery, engraving or favicon release (DS05).
- The small ™ mark did not survive tracing at this resolution and is reduced to specks. Use the replica only where the ™ is carried separately, or wait for the production master.
- Part A prohibits auto-tracing for production masters. These files are provided at the owner's request as working digital layout references and replace nothing in the approval path.
- Still not created because the guidelines have no source for them: stacked configuration, no-spark micro mark, white standalone symbol.
