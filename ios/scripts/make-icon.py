#!/usr/bin/env python3
"""Draws ios/icons/icon-1024.png, the App Store icon of Silent Medic Vet for iPhone (1.1 design):
an evergreen field with a paw print, copper toes and a cream main pad carrying a medical cross.
It matches the mark used in the app's header and opening screen (ios/web/smv-ios.js, MARK).
Opaque RGB, no transparency (App Store rule). Run once after changing the design; the PNG is committed."""
import os
from PIL import Image, ImageDraw

IOS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = 4                                   # supersample, then downscale for clean edges
N = 1024 * S
EVER_TOP, EVER_BOTTOM = (36, 86, 63), (17, 42, 31)
COPPER, CREAM, CROSS = (214, 128, 70), (244, 239, 226), (24, 57, 43)

# vertical evergreen gradient
im = Image.new("RGB", (N, N))
px = ImageDraw.Draw(im)
for y in range(N):
    t = y / (N - 1)
    px.line([(0, y), (N, y)], fill=tuple(round(a + (b - a) * t) for a, b in zip(EVER_TOP, EVER_BOTTOM)))

# soft light behind the paw
glow = Image.new("L", (N, N), 0)
ImageDraw.Draw(glow).ellipse([N * .14, N * .12, N * .86, N * .84], fill=46)
from PIL import ImageFilter
glow = glow.filter(ImageFilter.GaussianBlur(N * .08))
im = Image.composite(Image.new("RGB", (N, N), (84, 140, 108)), im, glow)
d = ImageDraw.Draw(im)

def u(v):                               # 64-unit design grid (same as the in-app mark) -> pixels
    return v / 64 * N

def ellipse(cx, cy, rx, ry, fill):
    d.ellipse([u(cx - rx), u(cy - ry), u(cx + rx), u(cy + ry)], fill=fill)

# toes
for cx, cy in ((17.5, 26), (26.5, 16.5), (37.5, 16.5), (46.5, 26)):
    ellipse(cx, cy, 5.6, 7.2, COPPER)

# main pad: a rounded heart-like blob built from overlapping ellipses
ellipse(32, 41, 14.5, 12.5, CREAM)
ellipse(24.5, 46, 8.5, 7.5, CREAM)
ellipse(39.5, 46, 8.5, 7.5, CREAM)
d.rounded_rectangle([u(20), u(40), u(44), u(53.5)], radius=u(6), fill=CREAM)

# medical cross in the pad
w = u(3.6)
d.rounded_rectangle([u(32) - w / 2, u(37), u(32) + w / 2, u(50)], radius=w / 2, fill=CROSS)
d.rounded_rectangle([u(25.5), u(43.5) - w / 2, u(38.5), u(43.5) + w / 2], radius=w / 2, fill=CROSS)

out = os.path.join(IOS, "icons", "icon-1024.png")
os.makedirs(os.path.dirname(out), exist_ok=True)
im.resize((1024, 1024), Image.LANCZOS).save(out)
print("wrote", out)
