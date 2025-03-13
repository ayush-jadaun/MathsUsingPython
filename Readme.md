# Electric Field Visualization Project

This project provides a collection of Python scripts to visualize electric fields and potentials in various configurations, with a focus on spherical charge distributions. The visualizations use 3D plots to represent electric field vectors and potential surfaces.

## Features

- 3D visualization of electric fields and potentials
- Multiple visualization approaches for charged spherical shells
- Vector field representation with arrows (quiver plots)
- Color-coded magnitude representations
- Cross-sectional views for better insight

## Dependencies

- NumPy
- Matplotlib
- mpl_toolkits.mplot3d

## File Descriptions

### 1. `spherical_shell_field.py`

This script visualizes the electric field and potential around a spherical shell with volume charge density:
- Displays electric field vectors as arrows
- Shows the spherical shell boundary
- Calculates the exact field in each region (inner, shell, outer)
- Provides two 3D visualizations side-by-side

### 2. `linear_shell_field.py`

Implements a simplified model of electric field for a spherical shell:
- Uses a linear charge density variation
- Shows field strength with color mapping
- Presents a 3D surface plot with color representing field magnitude

### 3. `radial_vector_field.py`

Creates a basic radial vector field visualization:
- Demonstrates the 1/r² behavior typical of Coulomb's law
- Provides a clear visualization of radial vectors around a central point
- Handles the singularity at the origin correctly

## Physics Concepts

This project illustrates several important electromagnetic concepts:
- Gauss's Law for electric fields
- Coulomb's Law for point charges
- Spherical symmetry in electromagnetic problems
- Variation of electric field with distance (1/r² behavior)
- Boundary conditions at charge interfaces

## Usage

To run any of the visualizations:

```bash
python spherical_shell_field.py
python linear_shell_field.py
python radial_vector_field.py
```

## Example Output

When running these scripts, you'll see 3D visualizations showing:
- Electric field vectors (arrows pointing in the direction of the field)
- Color-coded magnitudes (brighter colors typically represent stronger fields)
- Spherical boundaries where charge is distributed

## Theoretical Background

The electric field E due to a spherical shell with volume charge density ρ is given by:
- E = 0 for r < a (inside inner radius)
- E = [ρ(r³-a³)]/(3ε₀r²) for a < r < b (within the shell)
- E = [ρ(b³-a³)]/(3ε₀r²) for r > b (outside the shell)

Where:
- ρ is the charge density
- ε₀ is the permittivity of free space
- a is the inner radius
- b is the outer radius
- r is the distance from the center

## Future Improvements

Potential enhancements for this project include:
- Interactive controls to adjust charge densities and radii
- Animation showing time-varying fields
- Addition of magnetic field visualizations
- Inclusion of dielectric materials and boundary conditions
- Comparative visualizations with analytical solutions

## License
Feel free to use and modify the code for educational and research purposes.