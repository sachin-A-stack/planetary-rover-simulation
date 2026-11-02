# Planetary Rover Simulation

A Mars planetary surface simulation project built using Gazebo Sim and SDF.

## Current Progress
- Procedurally generated Martian terrain
- Heightmap-based terrain simulation
- Mars regolith surface texture
- Boulder placement and terrain alignment
- Mountain terrain generation

## Technologies
- Gazebo Sim 8
- SDF 1.10
- Python
- Git and GitHub

## Run the Simulation

```bash
cd ~/planetary_rover
export GZ_SIM_RESOURCE_PATH="$PWD/models"
gz sim -r --render-engine ogre2 worlds/surface_world.sdf
