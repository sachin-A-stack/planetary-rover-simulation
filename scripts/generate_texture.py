from PIL import Image
import numpy as np

width = 512
height = 512

# Generate natural colour variation
noise = np.random.normal(0, 8, (height, width))

# Create RGB colour channels
red = 165 + noise
green = 78 + noise * 0.5
blue = 48 + noise * 0.3

# Combine channels
texture = np.stack([red, green, blue], axis=2)

# Keep pixel values within 0-255
texture = np.clip(texture, 0, 255)

# Convert into an RGB image
image = Image.fromarray(texture.astype(np.uint8), "RGB")

# Save texture
image.save("models/terrain/materials/textures/mars_soil.png")

print("Mars soil texture generated successfully!")
