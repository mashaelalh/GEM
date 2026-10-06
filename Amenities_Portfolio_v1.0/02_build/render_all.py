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
