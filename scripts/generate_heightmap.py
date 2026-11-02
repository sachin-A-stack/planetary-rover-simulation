import numpy as np
from PIL import Image

# Mars terrain resolution
width = 257
height = 257

# Coordinate grid
x = np.linspace(-1, 1, width)
y = np.linspace(-1, 1, height)
X, Y = np.meshgrid(x, y)

# Base rolling terrain
terrain = (
    0.12 * np.sin(8 * X)
    + 0.10 * np.cos(7 * Y)
    + 0.06 * np.sin(6 * (X + Y))
)

# Mountain peaks: x, y, height, spread
mountains = [
    (-0.55, -0.35, 1.20, 0.16),
    (-0.15,  0.50, 1.50, 0.19),
    ( 0.35,  0.25, 1.30, 0.15),
    ( 0.65, -0.45, 1.60, 0.18),
    ( 0.05, -0.65, 0.90, 0.13),
]

# Generate mountain formations
for mx, my, peak, spread in mountains:
    distance = ((X - mx)**2 + (Y - my)**2)
    terrain += peak * np.exp(-distance / (2 * spread**2))

# Add an elongated mountain ridge
ridge = np.exp(-((Y - 0.10 - 0.25 * X)**2) / (2 * 0.055**2))
ridge *= np.exp(-(X**2) / (2 * 0.65**2))
terrain += 0.55 * ridge

# Normalize to grayscale
terrain -= terrain.min()
terrain /= terrain.max()
terrain *= 255

# Save as a separate test heightmap
image = Image.fromarray(terrain.astype(np.uint8), mode="L")
image.save("models/terrain/heightmap_mountains.png")

print("Mars mountain heightmap generated successfully!")
print("Resolution:", width, "x", height)


