#!/usr/bin/env python3
"""Draws ios/icons/icon-1024.png, the App Store icon, by redrawing the web app icon
(icon-512.png) at 1024 x 1024: same blue field, white cross and green VET badge,
geometry measured from icon-512.png and doubled. Opaque RGB, no transparency (App Store rule).
Run once after changing the design; the PNG is committed."""
import os
from PIL import Image, ImageDraw, ImageFont
IOS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = 4                                   # supersample, then downscale for clean edges
BLUE, WHITE, GREEN = (13, 71, 161), (255, 255, 255), (143, 227, 174)
def r(*v): return [int(round(x * 2 * S)) for x in v]          # 512-space -> supersampled 1024
im = Image.new("RGB", (1024 * S, 1024 * S), BLUE)
d = ImageDraw.Draw(im)
d.rounded_rectangle(r(216, 103, 296, 409), radius=18 * 2 * S, fill=WHITE)   # vertical bar
d.rounded_rectangle(r(103, 216, 409, 296), radius=18 * 2 * S, fill=WHITE)   # horizontal bar
d.rounded_rectangle(r(197, 318, 438, 431), radius=18 * 2 * S, fill=GREEN)   # badge
# Text box measured in icon-512.png: x 212-382, y 334-392. Fit the cap height, align left/top.
tx0, ty0, ty1 = 212 * 2 * S, 334 * 2 * S, 392 * 2 * S
size = 80 * 2 * S
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)
b = d.textbbox((0, 0), "VET", font=font)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", int(size * (ty1 - ty0) / (b[3] - b[1])))
b = d.textbbox((0, 0), "VET", font=font)
d.text((tx0 - b[0], ty0 - b[1]), "VET", font=font, fill=BLUE)
out = os.path.join(IOS, "icons", "icon-1024.png")
os.makedirs(os.path.dirname(out), exist_ok=True)
im.resize((1024, 1024), Image.LANCZOS).save(out)
print("wrote", out)
