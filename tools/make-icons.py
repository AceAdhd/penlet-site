# Lager nettsidens ikoner fra det offisielle Penlet-ikonet (penlet-icon.webp her, samme fil som
# store/penlet-icon.webp i app-repoet: ark med signatur og penn på blå flis). Kjør fra tools/:
#   python make-icons.py
# Skriver ../public/assets/icon.png (logoen i toppfeltet) og icon-48/180/192/512.png.
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / 'public/assets'

src = np.asarray(Image.open(HERE / 'penlet-icon.webp').convert('RGB')).astype(np.float32)
# Flisen: alt som ikke er nesten hvitt og sammenhengende med bildekanten
near_white = (255 - src).max(axis=2) < 12
labels, _ = ndimage.label(near_white)
edge = set(np.unique(np.concatenate([labels[0], labels[-1], labels[:, 0], labels[:, -1]]))) - {0}
inside = ~np.isin(labels, list(edge))
ys, xs = np.nonzero(inside)
y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
side = max(y1 - y0, x1 - x0)
cy, cx, h = (y0 + y1) // 2, (x0 + x1) // 2, side // 2
rgb, mask = src[cy - h:cy + h, cx - h:cx + h], inside[cy - h:cy + h, cx - h:cx + h]

alpha = ndimage.gaussian_filter((mask * 255).astype(np.float32), 0.7).clip(0, 255).astype(np.uint8)
tile = Image.fromarray(rgb.clip(0, 255).astype(np.uint8)).convert('RGBA')
tile.putalpha(Image.fromarray(alpha))

for s in (48, 180, 192, 512):
    tile.resize((s, s), Image.LANCZOS).save(OUT / f'icon-{s}.png', optimize=True)
tile.resize((144, 144), Image.LANCZOS).save(OUT / 'icon.png', optimize=True)
print('skrev icon.png og icon-48/180/192/512.png i', OUT)
