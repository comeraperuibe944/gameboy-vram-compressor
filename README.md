# GameBoy-VRAM-Compressor

<p align="center">
  <img src="https://img.shields.io/badge/Target-Game_Boy_%2F_GBC-8B008B?style=for-the-badge&logo=nintendo&logoColor=white" />
  <img src="https://img.shields.io/badge/Tile_Size-8x8_px-007ACC?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-NumPy_%26_PIL-3776AB?style=for-the-badge&logo=python&logoColor=white" />
</p>

An intelligent image tile deduplicator and lossy tile budget optimizer tailored specifically for Game Boy & Game Boy Color VRAM constraints.

## How It Works
The Game Boy background tile memory is limited (typically 256–384 unique 8x8 tiles per bank). This tool:
1. Slices full resolution input images into discrete **8x8 pixel tiles**.
2. Performs frequency hashing and tile deduplication using `collections.Counter`.
3. Retains only the most frequent $N$ base tiles based on user-selected constraints (`light: 320`, `medium: 256`, `aggressive: 192` tiles).
4. Re-maps the remainder of the image by finding the nearest perceptual tile distance.

## Usage
```bash
pip install pillow numpy
python compressor.py
```
