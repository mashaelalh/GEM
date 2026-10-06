"""GEM Amenities & Packaging concept mockup renderer.
Vector-style product mockups rendered with Pillow + numpy: matte materials, single-source soft light,
Ink / Beige / White / Black only. Logo = supplied raster (scaled, never redrawn). All output is
CONCEPT / NOT PRODUCTION ARTWORK; nothing here carries a dimension, volume or claim."""
import os, math, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "01_mockups")
LOGO = os.path.join(HERE, "..", "00_source", "logo")
FONTS = os.path.expanduser("~/.fonts")
INK, BEIGE, BLACK, WHITE = (0x12, 0x17, 0x1D), (0xBC, 0xAC, 0xA7), (0x02, 0x02, 0x02), (0xFF, 0xFF, 0xFF)
SS = 2  # supersample

def font(fam, size, wght=400):
    path = {"jost": "Jost[wght].ttf", "inter": "Inter[opsz,wght].ttf", "arabic": "NotoSansArabic[wdth,wght].ttf"}[fam]
    f = ImageFont.truetype(os.path.join(FONTS, path), int(size))
    try:
        axes = f.get_variation_axes(); vals = []
        for a in axes:
            n = a["name"].decode() if isinstance(a["name"], bytes) else a["name"]
            if n.lower().startswith("weight"): vals.append(wght)
            elif n.lower().startswith("optical"): vals.append(max(a["minimum"], min(a["maximum"], size / SS)))
            else: vals.append(a["default"])
        f.set_variation_by_axes(vals)
    except Exception: pass
    return f

def tracked(draw, xy, text, f, fill, track_em=0.0, anchor="l"):
    """Draw text with letter tracking (em-relative). anchor l|c|r for x."""
    size = f.size; gap = track_em * size
    widths = [draw.textlength(ch, font=f) for ch in text]
    total = sum(widths) + gap * (len(text) - 1)
    x, y = xy
    if anchor == "c": x -= total / 2
    elif anchor == "r": x -= total
    for ch, w in zip(text, widths):
        draw.text((x, y), ch, font=f, fill=fill); x += w + gap
    return total

def fit_font(draw, fam, text, max_w, size, wght=400, min_size=8):
    """Largest font <= size whose rendered width fits max_w."""
    while size > min_size:
        f = font(fam, size, wght)
        if draw.textlength(text, font=f) <= max_w: return f
        size = int(size * 0.92)
    return font(fam, min_size, wght)

def arabic(text):
    import arabic_reshaper
    from bidi.algorithm import get_display
    return get_display(arabic_reshaper.reshape(text))

def logo(kind="symbol", colour="black", height=100):
    name = {"symbol": "GEM_Symbol_", "lockup": "GEM_Logo_Horizontal_"}[kind] + colour.capitalize() + ".png"
    im = Image.open(os.path.join(LOGO, name)).convert("RGBA")
    scale = height / im.height
    return im.resize((max(1, round(im.width * scale)), max(1, round(height))), Image.LANCZOS)

# ---------- shading helpers ----------
def cylinder_shade(w, h, base, light=0.14, dark=0.22, spec=0.10):
    """Matte cylinder: lambert-ish falloff across x, soft highlight left of centre."""
    x = np.linspace(-1, 1, w)[None, :]
    lam = np.cos(np.clip(x, -1, 1) * math.pi / 2) ** 0.8
    tone = 1 - dark * (1 - lam)                       # darker at edges
    tone += light * np.exp(-((x + 0.35) ** 2) / 0.10)  # soft light from upper-left
    tone += spec * np.exp(-((x + 0.42) ** 2) / 0.006)  # narrow matte highlight
    arr = np.ones((h, w, 3)) * np.array(base)[None, None, :] * tone[..., None]
    return np.clip(arr, 0, 255).astype(np.uint8)

def flat_shade(w, h, base, grad=0.06):
    x = np.linspace(0, 1, w)[None, :]
    tone = 1 + grad * (0.5 - x)
    arr = np.ones((h, w, 3)) * np.array(base)[None, None, :] * tone[..., None]
    return np.clip(arr, 0, 255).astype(np.uint8)

def paper_texture(w, h, base, amount=5, seed=1):
    rng = np.random.default_rng(seed)
    noise = rng.normal(0, amount, (h, w, 1))
    arr = np.ones((h, w, 3)) * np.array(base)[None, None, :] + noise
    return np.clip(arr, 0, 255).astype(np.uint8)

def rounded_mask(w, h, r):
    m = Image.new("L", (w, h), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, w - 1, h - 1), r, fill=255); return m

def paste_shaded(canvas, arr, mask, xy):
    im = Image.fromarray(arr, "RGB").convert("RGBA"); im.putalpha(mask); canvas.alpha_composite(im, xy)

def contact_shadow(canvas, box, blur=40, alpha=90, dy=18, squash=0.35):
    x0, y0, x1, y1 = box; w = x1 - x0; h = int((y1 - y0) * squash)
    sh = Image.new("RGBA", canvas.size, (0, 0, 0, 0)); d = ImageDraw.Draw(sh)
    d.ellipse((x0 - w * 0.05, y1 - h * 0.5 + dy, x1 + w * 0.05, y1 + h * 0.5 + dy), fill=(0, 0, 0, alpha))
    sh = sh.filter(ImageFilter.GaussianBlur(blur)); canvas.alpha_composite(sh)

def canvas(w, h, bg=WHITE, texture=False):
    if texture: return Image.fromarray(paper_texture(w, h, bg, 3), "RGB").convert("RGBA")
    return Image.new("RGBA", (w, h), bg + (255,))

# ---------- packaging primitives ----------
def label_panel(w, h, colour, product, func, lines=None, bilingual=False, tier="[TIER]", symbol_h=None, co_brand=None, cap_mode=False):
    """Printed label: GEM symbol (supplied raster), product, function, placeholders. Colour = paper tone."""
    arr = paper_texture(w, h, colour, 2); im = Image.fromarray(arr, "RGB").convert("RGBA"); d = ImageDraw.Draw(im)
    ink = INK if colour in (WHITE, BEIGE) else BEIGE
    sym = logo("symbol", "black" if ink == INK else "beige", symbol_h or int(h * 0.16))
    pad = int(w * 0.12); y = int(h * 0.10)
    im.alpha_composite(sym, (pad, y)); y += sym.height + int(h * 0.05)
    inner = w - 2 * pad
    f_tier = fit_font(d, "inter", tier.upper(), inner / 1.25, int(h * 0.045), 500); f_prod = fit_font(d, "jost", product, inner, int(h * 0.11)); f_func = fit_font(d, "inter", func, inner, int(h * 0.05))
    tracked(d, (pad, y), tier.upper(), f_tier, ink, 0.12); y += int(h * 0.09)
    d.text((pad, y), product, font=f_prod, fill=ink); y += int(f_prod.size * 1.3)
    if bilingual:
        f_ar = font("arabic", int(h * 0.09), 400)
        d.text((w - pad, y - int(h * 0.02)), arabic(bilingual), font=f_ar, fill=ink, anchor="ra"); y += int(h * 0.12)
    d.text((pad, y), func, font=f_func, fill=ink); y += int(h * 0.08)
    for ln in (lines or ["[QUANTITY] · metric first", "[REQUIRED MARKET INFORMATION]", "[SKU] · ARTWORK v[PENDING]"]):
        fl = fit_font(d, "inter", ln, inner, int(h * 0.038)); d.text((pad, y), ln, font=fl, fill=ink); y += int(h * 0.055)
    if co_brand:
        y = h - int(h * 0.19); d.line((pad, y, w - pad, y), fill=ink, width=max(1, h // 400)); y += int(h * 0.03)
        d.text((pad, y), "Supplied by GEM™ for", font=f_small, fill=ink); y += int(h * 0.05)
        d.text((pad, y), co_brand, font=fit_font(d, "jost", co_brand, inner, int(h * 0.065)), fill=ink)
    return im

def bottle(h, w, body=INK, cap=INK, label=None, shape="cyl", cap_h_ratio=0.12, pump=False, label_rel=(0.14, 0.30, 0.86, 0.80), radius_ratio=0.5):
    """Returns RGBA image of a bottle with transparent background (tight box)."""
    W, H = int(w), int(h); im = Image.new("RGBA", (W, H + (int(H * 0.22) if pump else 0)), (0, 0, 0, 0))
    y_off = int(H * 0.22) if pump else 0
    cap_h = int(H * cap_h_ratio)
    r = int(W * radius_ratio) if shape == "cyl" else int(W * 0.06)
    # body
    body_arr = cylinder_shade(W, H - cap_h, body) if shape == "cyl" else flat_shade(W, H - cap_h, body, 0.10)
    m = rounded_mask(W, H - cap_h, r if shape == "cyl" else int(W * 0.06))
    # cylinder: flatten top corners (shoulder) by using a smaller top radius
    if shape == "cyl":
        m2 = Image.new("L", (W, H - cap_h), 0); dm = ImageDraw.Draw(m2)
        dm.rounded_rectangle((0, 0, W - 1, H - cap_h - 1), int(W * 0.12), fill=255)
        m = m2
    paste_shaded(im, body_arr, m, (0, y_off + cap_h))
    # cap
    cw = int(W * (0.62 if shape == "cyl" else 0.9)); cx = (W - cw) // 2
    cap_arr = cylinder_shade(cw, cap_h, cap, dark=0.28)
    paste_shaded(im, cap_arr, rounded_mask(cw, cap_h, int(cw * 0.08)), (cx, y_off))
    if pump:
        ph = int(H * 0.22); stem_w = int(W * 0.09); sx = (W - stem_w) // 2
        paste_shaded(im, cylinder_shade(stem_w, ph, cap, dark=0.3), rounded_mask(stem_w, ph, 2), (sx, int(ph * 0.25)))
        head_w = int(W * 0.34); head_h = int(ph * 0.22)
        paste_shaded(im, cylinder_shade(head_w, head_h, cap, dark=0.3), rounded_mask(head_w, head_h, int(head_h * 0.5)), (sx - int(head_w * 0.62), int(ph * 0.12)))
        collar_w = int(W * 0.2); paste_shaded(im, cylinder_shade(collar_w, int(ph * 0.14), cap, dark=0.3), rounded_mask(collar_w, int(ph * 0.14), 3), ((W - collar_w) // 2, int(ph * 0.86)))
    if label is not None:
        lx0, ly0, lx1, ly1 = label_rel; lw = int(W * (lx1 - lx0)); lh = int((H - cap_h) * (ly1 - ly0))
        lab = label(lw, lh)
        # bend label slightly with cylinder shading
        if shape == "cyl":
            sh = cylinder_shade(lw, lh, WHITE, light=0.0, dark=0.16, spec=0.0).astype(np.float32) / 255.0
            la = np.array(lab).astype(np.float32); la[..., :3] = np.clip(la[..., :3] * sh, 0, 255); lab = Image.fromarray(la.astype(np.uint8), "RGBA")
        im.alpha_composite(lab, (int(W * lx0), y_off + cap_h + int((H - cap_h) * ly0)))
    return im

def tube(h, w, body=WHITE, cap=INK, label=None):
    W, H = int(w), int(h); im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    cap_h = int(H * 0.16)
    # tapered body: wide at crimp (bottom), narrower at shoulder
    m = Image.new("L", (W, H - cap_h), 0); dm = ImageDraw.Draw(m)
    dm.polygon([(int(W * 0.12), 0), (int(W * 0.88), 0), (W - 1, H - cap_h - 1), (0, H - cap_h - 1)], fill=255)
    dm.rounded_rectangle((int(W * 0.12), 0, int(W * 0.88), int(W * 0.5)), int(W * 0.14), fill=255)
    paste_shaded(im, cylinder_shade(W, H - cap_h, body, dark=0.2), m, (0, cap_h))
    cw = int(W * 0.4); paste_shaded(im, cylinder_shade(cw, cap_h, cap, dark=0.3), rounded_mask(cw, cap_h, int(cw * 0.1)), ((W - cw) // 2, 0))
    d = ImageDraw.Draw(im); d.line((0, H - 2, W, H - 2), fill=tuple(int(c * 0.8) for c in body) + (255,), width=3)
    if label is not None:
        lw = int(W * 0.62); lh = int((H - cap_h) * 0.5); lab = label(lw, lh)
        im.alpha_composite(lab, (int(W * 0.19), cap_h + int((H - cap_h) * 0.28)))
    return im

def carton(h, w, depth, front=INK, side=None, top=None, label=None, lid=True):
    """Two-face box in simple parallel projection: front + right side + top strip."""
    W, H, Dp = int(w), int(h), int(depth); dy = int(Dp * 0.5)
    im = Image.new("RGBA", (W + Dp, H + dy), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    side = side or tuple(int(c * 0.82) for c in front); top = top or tuple(min(255, int(c * 1.08)) for c in front)
    d.polygon([(W, dy), (W + Dp, 0), (W + Dp, H), (W, H + dy)], fill=side + (255,))
    d.polygon([(0, dy), (Dp, 0), (W + Dp, 0), (W, dy)], fill=top + (255,))
    paste_shaded(im, paper_texture(W, H, front, 3), Image.new("L", (W, H), 255), (0, dy))
    if lid: d.line((0, dy + int(H * 0.22), W, dy + int(H * 0.22)), fill=tuple(int(c * 0.9) for c in front) + (255,), width=2)
    if label is not None:
        lab = label(int(W * 0.72), int(H * 0.5)); im.alpha_composite(lab, (int(W * 0.14), dy + int(H * 0.3)))
    return im

def sachet(h, w, colour=BEIGE, label=None):
    W, H = int(w), int(h); im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    m = Image.new("L", (W, H), 0); dm = ImageDraw.Draw(m); dm.rounded_rectangle((0, 0, W - 1, H - 1), int(W * 0.04), fill=255)
    arr = cylinder_shade(W, H, colour, light=0.06, dark=0.10, spec=0.0); paste_shaded(im, arr, m, (0, 0))
    d = ImageDraw.Draw(im); seam = tuple(int(c * 0.9) for c in colour) + (255,)
    for yy in (int(H * 0.08), H - int(H * 0.08)): d.line((int(W * 0.04), yy, W - int(W * 0.04), yy), fill=seam, width=2)
    d.line((int(W * 0.5), 0, int(W * 0.5), int(H * 0.08)), fill=seam, width=2)
    if label is not None:
        lab = label(int(W * 0.7), int(H * 0.55)); im.alpha_composite(lab, (int(W * 0.15), int(H * 0.22)))
    return im

def tag_label(w, h, colour, title, sub="CONCEPT / NOT PRODUCTION ARTWORK", ink=None):
    """Small typeset label for accessories: symbol + title + status."""
    im = Image.fromarray(paper_texture(w, h, colour, 2), "RGB").convert("RGBA"); d = ImageDraw.Draw(im)
    ink = ink or (INK if colour in (WHITE, BEIGE) else BEIGE)
    sym = logo("symbol", "black" if ink == INK else "beige", int(h * 0.24)); pad = int(w * 0.1)
    im.alpha_composite(sym, (pad, int(h * 0.12)))
    d.text((pad, int(h * 0.44)), title, font=fit_font(d, "jost", title, w - 2 * pad, int(h * 0.14)), fill=ink)
    tracked(d, (pad, int(h * 0.66)), sub, fit_font(d, "inter", sub, (w - 2 * pad) / 1.3, int(h * 0.06), 500), ink, 0.08)
    return im

def status_stamp(canvas, text="CONCEPT / NOT PRODUCTION ARTWORK", colour=INK, pos="br", margin=None):
    d = ImageDraw.Draw(canvas); W, H = canvas.size; margin = margin or int(W * 0.03)
    f = font("inter", int(H * 0.018), 500)
    tw = sum(d.textlength(c, font=f) for c in text) + 0.12 * f.size * (len(text) - 1)
    x = W - margin - tw if pos.endswith("r") else margin; y = H - margin - f.size * 1.4 if pos.startswith("b") else margin
    tracked(d, (x, y), text, f, colour, 0.12)

def place(canvas, obj, x, y, shadow=True, shadow_alpha=80, blur=38, dy=14):
    if shadow: contact_shadow(canvas, (x, y, x + obj.width, y + obj.height), blur=blur, alpha=shadow_alpha, dy=dy)
    canvas.alpha_composite(obj, (x, y))

def save(im, name, scale=1 / SS):
    os.makedirs(OUT, exist_ok=True)
    out = im.convert("RGB")
    if scale != 1: out = out.resize((int(out.width * scale), int(out.height * scale)), Image.LANCZOS)
    out.save(os.path.join(OUT, name + ".png"), optimize=True); print("saved", name, out.size)

# ---------- product family definitions ----------
FAMILY = [("Shampoo", "Hair cleanser"), ("Conditioner", "Hair conditioner"), ("Body Wash", "Body cleanser"), ("Body Lotion", "Body moisturiser"), ("Hand Wash", "Hand cleanser")]
AR = {"Shampoo": "شامبو", "Conditioner": "بلسم", "Body Wash": "غسول الجسم", "Body Lotion": "لوشن الجسم", "Hand Wash": "غسول اليدين"}

def family_bottle(product, func, H=1500, W=440, scheme="ink", shape="cyl", pump=False, bilingual=False, co_brand=None):
    body, lab = {"ink": (INK, BEIGE), "beige": (BEIGE, WHITE), "white": (WHITE, WHITE), "inkwhite": (INK, WHITE)}[scheme]
    lbl = lambda w, h: label_panel(w, h, lab, product, func, bilingual=(AR[product] if bilingual else False), co_brand=co_brand)
    return bottle(H, W, body=body, cap=INK if scheme != "ink" else BLACK, label=lbl, shape=shape, pump=pump)

def scene_surface(W, H, top=INK, floor=BEIGE, horizon=0.62):
    """Backdrop: wall + surface, matte, single soft light from upper left."""
    im = canvas(W, H, top, texture=True); d = ImageDraw.Draw(im)
    fl = Image.fromarray(paper_texture(W, int(H * (1 - horizon)) + 2, floor, 3), "RGB").convert("RGBA")
    im.alpha_composite(fl, (0, int(H * horizon)))
    # soft light pool on the wall
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(glow)
    gd.ellipse((-W * 0.2, -H * 0.5, W * 0.8, H * 0.9), fill=(255, 255, 255, 22)); glow = glow.filter(ImageFilter.GaussianBlur(W * 0.08))
    im.alpha_composite(glow); return im

# ---------- compositions ----------
def fb(product, func, hh, scheme="ink", shape="cyl", pump=False, bilingual=False, co_brand=None, ratio=0.28):
    """Family bottle sized by height in canvas px (pump adds 22% on top, so shrink body)."""
    body_h = int(hh / (1.22 if pump else 1.0)); return family_bottle(product, func, H=body_h, W=int(body_h * ratio), scheme=scheme, shape=shape, pump=pump, bilingual=bilingual, co_brand=co_brand)

def row(c, objs, y_base, gap, start=None, center=True, **kw):
    total = sum(o.width for o in objs) + gap * (len(objs) - 1)
    x = start if start is not None else (c.width - total) // 2 if center else int(c.width * 0.06)
    for o in objs:
        place(c, o, x, y_base - o.height, **kw); x += o.width + gap

def render_all():
    os.makedirs(OUT, exist_ok=True)
    W, H = 2400 * SS, 1500 * SS; SHD = dict(shadow_alpha=90, blur=55 * SS, dy=10 * SS); SHL = dict(shadow_alpha=60, blur=50 * SS, dy=8 * SS)
    # hero: three bottles on beige surface, dark wall
    c = scene_surface(W, H, INK, BEIGE, 0.58)
    row(c, [fb("Shampoo", "Hair cleanser", int(H * 0.66)), fb("Hand Wash", "Hand cleanser", int(H * 0.66), pump=True), fb("Body Wash", "Body cleanser", int(H * 0.60))], int(H * 0.84), int(W * 0.05), **SHD)
    status_stamp(c, colour=BEIGE); save(c, "01_hero_family")
    # product pages
    for i, (p, f) in enumerate(FAMILY):
        pump = p == "Hand Wash"; key = f"{i+4:02d}_{p.replace(' ', '_').lower()}"
        c = canvas(1200 * SS, 1600 * SS, WHITE, texture=True); front = fb(p, f, int(c.height * 0.76), pump=pump)
        place(c, front, (c.width - front.width) // 2, int(c.height * 0.90) - front.height, **SHL); status_stamp(c); save(c, key + "_front")
        rear_lbl = lambda w, h: label_panel(w, h, BEIGE, p, f, lines=["[REQUIRED MARKET INFORMATION]", "[INGREDIENTS · REGULATORY REVIEW]", "[WARNINGS · REGULATORY REVIEW]", "[BATCH] · [ORIGIN] · [SKU]", "GEM-[PENDING] · ARTWORK v[PENDING]"])
        bh = int(c.height * 0.76 / (1.22 if pump else 1)); rear = bottle(bh, int(bh * 0.28), body=INK, cap=BLACK, label=rear_lbl, pump=pump, label_rel=(0.14, 0.26, 0.86, 0.86))
        c = canvas(1200 * SS, 1600 * SS, WHITE, texture=True); place(c, rear, (c.width - rear.width) // 2, int(c.height * 0.90) - rear.height, **SHL); status_stamp(c); save(c, key + "_rear")
        c = canvas(1600 * SS, 1200 * SS, INK, texture=True); big_h = int(c.height * 2.4); big = fb(p, f, big_h, pump=pump)
        cap_h = int(big_h / (1.22 if pump else 1) * 0.12); lab_top = (int(big_h * 0.22 / 1.22) if pump else 0) + cap_h + int((big_h / (1.22 if pump else 1) - cap_h) * 0.30)
        place(c, big, int(c.width * 0.22), int(c.height * 0.10) - lab_top, shadow=False); status_stamp(c, colour=BEIGE); save(c, key + "_closeup")
    # vanity scene
    c = scene_surface(W, H, BEIGE, WHITE, 0.66)
    objs = [fb("Shampoo", "Hair cleanser", int(H * 0.58)), fb("Conditioner", "Hair conditioner", int(H * 0.58)), fb("Body Lotion", "Body moisturiser", int(H * 0.50), scheme="beige")]
    tray_w = sum(o.width for o in objs) + int(W * 0.03) * 2 + int(W * 0.06)
    tray = Image.new("RGBA", (tray_w, int(H * 0.03)), INK + (255,)); place(c, tray, int(W * 0.52), int(H * 0.845), shadow_alpha=50, blur=40 * SS)
    row(c, objs, int(H * 0.85), int(W * 0.03), start=int(W * 0.55), **SHD); status_stamp(c); save(c, "07_vanity_scene")
    # washroom scene: dark wall, white counter band
    c = scene_surface(W, H, INK, WHITE, 0.80); hw = fb("Hand Wash", "Hand cleanser", int(H * 0.66), pump=True)
    place(c, hw, int(W * 0.44), int(H * 0.82) - hw.height, **SHD); status_stamp(c, colour=BEIGE); save(c, "08_handwash_washroom")
    # family lineup
    c = canvas(W, H, WHITE, texture=True)
    row(c, [fb(p, f, int(H * (0.62 if p != "Body Lotion" else 0.54)), pump=(p == "Hand Wash")) for p, f in FAMILY], int(H * 0.86), int(W * 0.045), **SHL); status_stamp(c); save(c, "09_family_lineup")
    # packaging architecture
    c = canvas(W, H, BEIGE, texture=True)
    items = [fb("Body Wash", "Body cleanser", int(H * 0.46)),
             tube(int(H * 0.42), int(H * 0.13), body=WHITE, cap=INK, label=lambda w, h: label_panel(w, h, WHITE, "Body Lotion", "Body moisturiser", lines=["[QUANTITY]", "[SKU]"])),
             bottle(int(H * 0.50), int(H * 0.15), body=WHITE, cap=INK, shape="rect", label=lambda w, h: label_panel(w, h, WHITE, "Refill", "[PRODUCT]", lines=["[QUANTITY]", "[SKU]"])),
             carton(int(H * 0.40), int(H * 0.17), int(H * 0.07), front=INK, label=lambda w, h: label_panel(w, h, INK, "Shampoo", "Hair cleanser", lines=["[QUANTITY]", "[SKU]"], symbol_h=int(h * 0.2))),
             sachet(int(H * 0.24), int(H * 0.16), colour=BEIGE, label=lambda w, h: label_panel(w, h, BEIGE, "Hand Wash", "Hand cleanser", lines=["[QUANTITY]"], symbol_h=int(h * 0.22))),
             fb("Hand Wash", "Hand cleanser", int(H * 0.50), pump=True)]
    row(c, items, int(H * 0.80), int(W * 0.035), **SHL); status_stamp(c); save(c, "10_packaging_architecture")
    # primary pack alternatives
    c = canvas(W, H, WHITE, texture=True)
    row(c, [fb("Shampoo", "Hair cleanser", int(H * 0.62)), fb("Shampoo", "Hair cleanser", int(H * 0.62), shape="rect"),
            tube(int(H * 0.56), int(H * 0.17), body=INK, cap=BLACK, label=lambda w, h: label_panel(w, h, BEIGE, "Shampoo", "Hair cleanser"))], int(H * 0.86), int(W * 0.10), **SHL)
    status_stamp(c, "STRUCTURAL CONCEPT · REQUIRES SUPPLIER VALIDATION"); save(c, "11_primary_pack_alternatives")
    # secondary packaging
    c = scene_surface(W, H, INK, BEIGE, 0.60)
    sleeve = carton(int(H * 0.26), int(H * 0.56), int(H * 0.12), front=BEIGE, label=lambda w, h: label_panel(w, h, BEIGE, "Amenity set", "Five pieces · [PENDING]", lines=["[REQUIRED MARKET INFORMATION]", "[SKU]"], symbol_h=int(h * 0.26)), lid=False)
    big_carton = carton(int(H * 0.50), int(H * 0.20), int(H * 0.10), front=INK, label=lambda w, h: label_panel(w, h, INK, "Shampoo", "Hair cleanser", lines=["[QUANTITY]", "[SKU] · v[PENDING]"], symbol_h=int(h * 0.22)))
    setbox = carton(int(H * 0.22), int(H * 0.42), int(H * 0.16), front=WHITE, label=lambda w, h: label_panel(w, h, WHITE, "Property edition", "[PROPERTY NAME] · CONDITIONAL", lines=["[SKU]"], symbol_h=int(h * 0.26)))
    row(c, [sleeve, big_carton, setbox], int(H * 0.84), int(W * 0.06), **SHD); status_stamp(c, colour=BEIGE); save(c, "12_secondary_packaging")
    # extensions
    c = canvas(W, H, WHITE, texture=True); objs = []
    for name in ["Soap", "Dental kit", "Shaving kit", "Vanity kit", "Shower cap", "Comb"]:
        col = [INK, BEIGE, WHITE][len(name) % 3]
        objs.append(carton(int(H * 0.26), int(H * 0.20), int(H * 0.07), front=col, label=lambda w, h, n=name, cc=col: tag_label(w, h, cc, n, "CONCEPT RANGE EXTENSION"), lid=False))
    row(c, objs, int(H * 0.72), int(W * 0.025), **SHL); status_stamp(c, "CONCEPT RANGE EXTENSION · COMMERCIAL SCOPE [PENDING]"); save(c, "13_personal_care_extensions")
    c = canvas(W, H, BEIGE, texture=True); objs = []
    for name, col in [("Sewing kit", INK), ("Slippers", WHITE), ("Laundry bag", INK), ("Tissue box", WHITE), ("Shoe-care kit", INK), ("Cotton pads", WHITE)]:
        objs.append(carton(int(H * 0.28), int(H * 0.21), int(H * 0.08), front=col, label=lambda w, h, n=name, cc=col: tag_label(w, h, cc, n, "CONCEPT · SCOPE [PENDING]"), lid=False))
    row(c, objs, int(H * 0.72), int(W * 0.025), **SHL); status_stamp(c, "GUEST ACCESSORIES · CONCEPT ONLY"); save(c, "14_guest_accessories")
    # room touchpoints
    c = scene_surface(W, H, INK, BEIGE, 0.64); objs = []
    for n, col in [("Stationery", WHITE), ("Coffee & tea", INK), ("Laundry", BEIGE)]:
        objs.append(carton(int(H * 0.30), int(H * 0.24), int(H * 0.09), front=col, label=lambda w, h, nn=n, cc=col: tag_label(w, h, cc, nn, "CONCEPT / NOT PRODUCTION ARTWORK"), lid=False))
    objs.append(fb("Body Lotion", "Body moisturiser", int(H * 0.56), scheme="beige"))
    row(c, objs, int(H * 0.85), int(W * 0.06), **SHD); status_stamp(c, colour=BEIGE); save(c, "15_room_touchpoints")
    # property edition
    c = canvas(W, H, WHITE, texture=True); bh = int(H * 0.72)
    pe = bottle(bh, int(bh * 0.28), body=INK, cap=BLACK, label=lambda w, h: label_panel(w, h, BEIGE, "Shampoo", "Hair cleanser", tier="Property edition · [PROPERTY NAME]"))
    place(c, pe, (W - pe.width) // 2, int(H * 0.88) - pe.height, **SHL); status_stamp(c, "PROPERTY EDITION · CONDITIONAL (AC03, VAL-01) · CONCEPT"); save(c, "16_property_edition")
    # co-branded
    c = canvas(W, H, BEIGE, texture=True)
    cb = bottle(bh, int(bh * 0.28), body=WHITE, cap=INK, label=lambda w, h: label_panel(w, h, WHITE, "Body Wash", "Body cleanser", co_brand="PROPERTY NAME"), label_rel=(0.14, 0.22, 0.86, 0.92))
    place(c, cb, (W - cb.width) // 2, int(H * 0.88) - cb.height, **SHL); status_stamp(c, "CO-BRANDING CONCEPT · SUBJECT TO PARTNER AGREEMENT"); save(c, "17_cobranded")
    # bespoke
    c = scene_surface(W, H, INK, INK, 0.7)
    row(c, [fb("Shampoo", "Hair cleanser", int(H * 0.60), scheme=sc) for sc in ["ink", "inkwhite", "beige"]], int(H * 0.86), int(W * 0.08), **SHD)
    status_stamp(c, "BESPOKE PROGRAMME · CONDITIONAL · CONCEPT", colour=BEIGE); save(c, "18_bespoke")
    # materials
    c = canvas(W, H, WHITE, texture=True); sw = int(W * 0.17); gap = int(W * 0.03); x0 = int(W * 0.08); y0 = int(H * 0.16)
    swatches = [("Warm uncoated paper", BEIGE, 6), ("Matte board", INK, 3), ("Ink surface", INK, 2), ("Beige surface", BEIGE, 2), ("Controlled translucent", (0xE9, 0xE4, 0xE1), 2), ("Neutral plastic", WHITE, 1), ("Restrained tactile", BEIGE, 9), ("Soft-touch matte", INK, 1)]
    d = ImageDraw.Draw(c); f = font("inter", int(H * 0.017), 500); f2 = font("inter", int(H * 0.012))
    for i, (name, col, amt) in enumerate(swatches):
        xx = x0 + (i % 4) * (sw + gap); yy = y0 + (i // 4) * (sw + int(H * 0.13))
        tile = Image.fromarray(paper_texture(sw, sw, col, amt, seed=i), "RGB").convert("RGBA")
        if col == WHITE: ImageDraw.Draw(tile).rectangle((0, 0, sw - 1, sw - 1), outline=BEIGE, width=2)
        place(c, tile, xx, yy, shadow_alpha=40, blur=30 * SS, dy=6 * SS)
        d.text((xx, yy + sw + int(H * 0.02)), name, font=f, fill=INK); tracked(d, (xx, yy + sw + int(H * 0.05)), "PENDING SUPPLIER VALIDATION", f2, INK, 0.08)
    save(c, "19_material_direction")
    c = canvas(W, H, BEIGE, texture=True); x0 = int(W * 0.06); y0 = int(H * 0.18); sw = int(W * 0.19); gap = int(W * 0.03)
    for i, (name, mode) in enumerate([("Blind emboss", "emboss"), ("Deboss", "deboss"), ("Precision die-cut", "cut"), ("Soft-touch matte", "soft")]):
        base = INK if mode == "soft" else BEIGE
        tile = Image.fromarray(paper_texture(sw, sw, base, 4, seed=i), "RGB").convert("RGBA")
        sym = logo("symbol", "beige" if mode == "soft" else "black", int(sw * 0.42)); a = sym.split()[3]; cx, cy = (sw - sym.width) // 2, (sw - sym.height) // 2
        if mode in ("emboss", "deboss"):
            off = max(2, int(sw * 0.008)) * (1 if mode == "emboss" else -1)
            hi = Image.new("RGBA", sym.size, (255, 255, 255, 255)); hi.putalpha(ImageChops.multiply(a, Image.new("L", a.size, 150)))
            lo = Image.new("RGBA", sym.size, (0, 0, 0, 255)); lo.putalpha(ImageChops.multiply(a, Image.new("L", a.size, 120)))
            tile.alpha_composite(lo.filter(ImageFilter.GaussianBlur(3)), (cx + off, cy + off)); tile.alpha_composite(hi.filter(ImageFilter.GaussianBlur(3)), (cx - off, cy - off))
            body_ = Image.new("RGBA", sym.size, base + (255,)); body_.putalpha(a); tile.alpha_composite(body_, (cx, cy))
        elif mode == "cut":
            hole = Image.new("RGBA", sym.size, INK + (255,)); hole.putalpha(a); tile.alpha_composite(hole, (cx, cy))
        else:
            tile.alpha_composite(sym, (cx, cy))
        xx = x0 + i * (sw + gap); place(c, tile, xx, y0, shadow_alpha=50, blur=30 * SS, dy=6 * SS)
        d = ImageDraw.Draw(c); d.text((xx, y0 + sw + int(H * 0.03)), name, font=font("inter", int(H * 0.018), 500), fill=INK); tracked(d, (xx, y0 + sw + int(H * 0.065)), "PENDING PHYSICAL PROOF", font("inter", int(H * 0.012)), INK, 0.08)
    save(c, "20_finish_direction")
    # information hierarchy
    c = canvas(1600 * SS, 1600 * SS, INK, texture=True)
    lab = label_panel(int(c.width * 0.56), int(c.height * 0.74), BEIGE, "[PRODUCT]", "[FUNCTION]", tier="[COLLECTION / TIER]", lines=["[QUANTITY / SIZE] · metric first", "[INSTRUCTIONS · REQUIRED MARKET INFORMATION]", "[REGULATORY COPY · REVIEW REQUIRED]", "[SKU] · ARTWORK v[PENDING]"])
    place(c, lab, int(c.width * 0.22), int(c.height * 0.12), shadow_alpha=100, blur=50 * SS, dy=12 * SS); status_stamp(c, colour=BEIGE); save(c, "21_information_hierarchy")
    # bilingual
    c = canvas(W, H, WHITE, texture=True); bh = int(H * 0.74)
    bl = bottle(bh, int(bh * 0.30), body=INK, cap=BLACK, label=lambda w, h: label_panel(w, h, BEIGE, "Shampoo", "Hair cleanser", bilingual=AR["Shampoo"], lines=["[QUANTITY] · metric first", "[ARABIC COPY PENDING NATIVE REVIEW]", "GEM-[PENDING] · LATIN DIGITS, LTR"]), label_rel=(0.12, 0.22, 0.88, 0.90))
    place(c, bl, (W - bl.width) // 2, int(H * 0.88) - bl.height, **SHL); status_stamp(c, "BILINGUAL CONCEPT · ARABIC PENDING LOCALIZATION APPROVAL"); save(c, "22_bilingual")
    # cover tile
    c = canvas(1400 * SS, 1800 * SS, INK, texture=True); b = fb("Shampoo", "Hair cleanser", int(c.height * 0.84))
    place(c, b, (c.width - b.width) // 2, int(c.height * 0.96) - b.height, shadow_alpha=120, blur=70 * SS, dy=10 * SS); save(c, "00_cover_product")
    # one system, many scales
    c = canvas(W, H, WHITE, texture=True)
    objs = [sachet(int(H * 0.20), int(H * 0.14), colour=BEIGE, label=lambda w, h: label_panel(w, h, BEIGE, "Hand Wash", "Hand cleanser", lines=["[QUANTITY]"], symbol_h=int(h * 0.22))),
            fb("Body Lotion", "Body moisturiser", int(H * 0.38)), fb("Shampoo", "Hair cleanser", int(H * 0.62)),
            carton(int(H * 0.62), int(H * 0.24), int(H * 0.11), front=INK, label=lambda w, h: label_panel(w, h, INK, "Amenity set", "Five pieces · [PENDING]", lines=["[SKU]"], symbol_h=int(h * 0.22)))]
    row(c, objs, int(H * 0.86), int(W * 0.07), **SHL); status_stamp(c); save(c, "03_one_system_scales")

if __name__ == "__main__":
    render_all()
