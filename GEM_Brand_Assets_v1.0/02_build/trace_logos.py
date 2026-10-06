"""Vector replicas of the five supplied logo rasters (Part A slide 27). Alpha channel is upsampled 8x
(Lanczos), thresholded and traced with potracer, so the SVG follows the supplied artwork; nothing is redrawn.
STATUS: WORKING REPLICA, PENDING PRODUCTION MASTER (VAL-02). Source resolution is 654x207 / 229x207."""
import numpy as np, pathlib
from PIL import Image, ImageFilter
import potrace
ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT.parent / "Amenities_Portfolio_v1.0/00_source/logo"; OUT = ROOT / "03_logo_replica"
K = 8
JOBS = [("GEM_Logo_Horizontal_Beige", "#BCACA7", "LOCKUP-HORIZONTAL", "BEIGE"), ("GEM_Logo_Horizontal_Black", "#020202", "LOCKUP-HORIZONTAL", "BLACK"),
        ("GEM_Logo_Horizontal_White", "#FFFFFF", "LOCKUP-HORIZONTAL", "WHITE"), ("GEM_Symbol_Beige", "#BCACA7", "SYMBOL", "BEIGE"), ("GEM_Symbol_Black", "#020202", "SYMBOL", "BLACK")]
def path_d(plist, s):
    d = []
    for c in plist:
        p = c.start_point; d.append(f"M{p.x/s:.2f} {p.y/s:.2f}")
        for seg in c.segments:
            if seg.is_corner: d.append(f"L{seg.c.x/s:.2f} {seg.c.y/s:.2f}L{seg.end_point.x/s:.2f} {seg.end_point.y/s:.2f}")
            else: d.append(f"C{seg.c1.x/s:.2f} {seg.c1.y/s:.2f} {seg.c2.x/s:.2f} {seg.c2.y/s:.2f} {seg.end_point.x/s:.2f} {seg.end_point.y/s:.2f}")
        d.append("Z")
    return "".join(d)
for stem, col, asset, var in JOBS:
    im = Image.open(SRC / f"{stem}.png"); a = im.getchannel("A"); w, h = a.size
    big = a.resize((w * K, h * K), Image.LANCZOS).filter(ImageFilter.GaussianBlur(K * 0.3))
    bm = potrace.Bitmap(np.array(big) <= 127)
    pl = bm.trace(turdsize=3, turnpolicy=potrace.POTRACE_TURNPOLICY_MINORITY, alphamax=1.0, opttolerance=0.4)
    d = path_d(pl, K)
    name = f"GEM_BRAND_{asset}_{var}_v0.1-REPLICA_20261006.svg"
    (OUT / name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d">\n<title id="t">GEM logo{" symbol" if asset=="SYMBOL" else ""}</title>\n<desc id="d">Working vector replica traced from the supplied artwork. PENDING PRODUCTION MASTER (VAL-02). Not for print, fabrication or favicon release.</desc>\n<path fill="{col}" fill-rule="evenodd" d="{d}"/>\n</svg>\n')
    print(name, len(d))
