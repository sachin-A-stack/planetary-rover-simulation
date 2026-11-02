from pathlib import Path
import re

path = Path("worlds/surface_world.sdf")
text = path.read_text()

heights = {
    "mars_boulder_01": -2.76,
    "mars_boulder_02": -4.08,
    "mars_boulder_03": 5.01,
    "mars_boulder_04": -1.91,
    "mars_boulder_05": -2.01,
    "mars_boulder_06": 0.49,
}

for name, z in heights.items():
    pattern = (
        r"(<name>" + name + r"</name>\s*"
        r"<pose>[-\d.]+\s+[-\d.]+\s+)"
        r"[-\d.]+(\s+[-\d.]+\s+[-\d.]+\s+[-\d.]+</pose>)"
    )

    text, count = re.subn(
        pattern,
        lambda m: m.group(1) + f"{z:.2f}" + m.group(2),
        text
    )

    if count != 1:
        raise RuntimeError(f"Expected one pose for {name}, found {count}")

path.write_text(text)
print("All six rock positions updated successfully.")
