"""Dessine les icônes de l'app : hommage à « Icare » de Matisse (Jazz, 1947), façon papier découpé.

Composition originale (silhouette, cœur rouge, étoiles jaunes sur fond bleu), pas une copie de l'œuvre.
Usage : python3 outils/icones.py app/icons
"""
import math, random, sys
from PIL import Image, ImageDraw, ImageFilter
S = 2048
random.seed(7)
BLUE, BLACK, RED, YEL = (27, 58, 150), (17, 17, 20), (214, 38, 40), (247, 205, 40)

def wobble(pts, amp):
    """Bord légèrement irrégulier, comme du papier découpé aux ciseaux."""
    return [(x + random.uniform(-amp, amp), y + random.uniform(-amp, amp)) for x, y in pts]

def star(cx, cy, r_out, r_in, n, rot, amp=6):
    pts = []
    for i in range(n * 2):
        r = (r_out if i % 2 == 0 else r_in) * random.uniform(0.82, 1.12)
        a = rot + i * math.pi / n + random.uniform(-0.08, 0.08)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return wobble(pts, amp)

def blob(cx, cy, rx, ry, rot=0, n=48, amp=0.04):
    pts = []
    for i in range(n):
        a = 2 * math.pi * i / n
        k = 1 + amp * math.sin(3 * a + 1) + amp * 0.6 * math.sin(5 * a)
        x, y = rx * k * math.cos(a), ry * k * math.sin(a)
        pts.append((cx + x * math.cos(rot) - y * math.sin(rot), cy + x * math.sin(rot) + y * math.cos(rot)))
    return pts

def spline(pts, steps=14):
    """Catmull-Rom fermée : contour arrondi qui passe par les points de contrôle."""
    out, n = [], len(pts)
    for i in range(n):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[(i + 1) % n], pts[(i + 2) % n]
        for k in range(steps):
            t = k / steps; t2, t3 = t * t, t * t * t
            out.append(tuple(0.5 * ((2 * p1[j]) + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t2
                                    + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t3) for j in (0, 1)))
    return out


def make(scale=1.0):
    im = Image.new("RGB", (S, S), BLUE); d = ImageDraw.Draw(im)
    c = S / 2
    T = lambda pts: [(c + (x - c) * scale, c + (y - c) * scale) for x, y in pts]
    # étoiles jaunes (disposition originale)
    for cx, cy, ro, ri, n, rot in [(260, 270, 140, 54, 6, 0.3), (1830, 760, 125, 48, 7, 1.0), (1760, 1180, 165, 62, 6, 0.6),
                                   (300, 1300, 140, 54, 7, 0.2), (1700, 1800, 125, 48, 6, 0.9), (330, 1790, 115, 44, 6, 0.4),
                                   (1290, 230, 95, 36, 6, 0.1), (720, 200, 80, 30, 6, 0.5)]:
        d.polygon(T(star(cx, cy, ro, ri, n, rot)), fill=YEL)
    # silhouette noire d'un seul tenant, contour souple (spline), bras ouverts vers le haut, jambes fléchies
    body = [(985, 600), (905, 640), (790, 600), (640, 520), (500, 470), (395, 480), (360, 540), (420, 575), (530, 590),
            (660, 650), (790, 745), (860, 830), (875, 960), (850, 1110), (790, 1280), (705, 1450), (625, 1590),
            (575, 1690), (640, 1740), (720, 1650), (820, 1500), (930, 1330), (1010, 1235), (1080, 1290), (1160, 1430),
            (1250, 1570), (1320, 1690), (1395, 1660), (1340, 1520), (1260, 1330), (1200, 1130), (1180, 960),
            (1200, 830), (1300, 730), (1440, 620), (1570, 520), (1665, 470), (1700, 410), (1630, 395), (1520, 445),
            (1370, 540), (1220, 625), (1110, 640), (1060, 600)]
    d.polygon(T(spline(body)), fill=BLACK)
    d.polygon(T(blob(1025, 470, 92, 112, 0.25, amp=0.05)), fill=BLACK)            # tête
    # cœur rouge
    d.polygon(T(blob(1075, 800, 70, 62, 0.4, amp=0.09)), fill=RED)
    return im

full = make(1.0); safe = make(0.84)
out = sys.argv[1]
full.resize((180, 180), Image.LANCZOS).save(f"{out}/apple-touch-icon.png")
full.resize((192, 192), Image.LANCZOS).save(f"{out}/icon-192.png")
safe.resize((512, 512), Image.LANCZOS).save(f"{out}/icon-512.png")
