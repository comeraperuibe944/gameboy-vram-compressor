from PIL import Image
import numpy as np
from collections import Counter

TILE = 8
INPUT = "image.png"

# Quantos tiles base manter
PRESETS = {
    "light": 320,
    "medium": 256,
    "aggressive": 192,
}

def tile_distance(a, b):
    return np.sum(a != b)

def main():
    img = Image.open(INPUT).convert("RGB")
    arr = np.array(img)
    h, w, _ = arr.shape

    tiles = []
    positions = []

    for y in range(0, h, TILE):
        for x in range(0, w, TILE):
            t = arr[y:y+TILE, x:x+TILE].copy()
            tiles.append(t)
            positions.append((x, y))

    # Contar tiles mais comuns
    keys = [t.tobytes() for t in tiles]
    counts = Counter(keys)

    # Escolher os N mais comuns
    for name, keep in PRESETS.items():
        base_keys = [k for k, _ in counts.most_common(keep)]
        base_tiles = [np.frombuffer(k, dtype=np.uint8).reshape(8,8,3) for k in base_keys]

        out = arr.copy()

        for i, t in enumerate(tiles):
            best = 0
            best_d = 10**18
            for j, b in enumerate(base_tiles):
                d = tile_distance(t, b)
                if d < best_d:
                    best_d = d
                    best = j
            x, y = positions[i]
            out[y:y+TILE, x:x+TILE] = base_tiles[best]

        Image.fromarray(out).save(f"out_{name}.png")
        print(f"{name}: usando {keep} tiles base")

if __name__ == "__main__":
    main()
