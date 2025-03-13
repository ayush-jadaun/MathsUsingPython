import numpy as np
import matplotlib.pyplot as plt

# Constants
k = 1  # Arbitrary constant for charge density
epsilon_0 = 1  # Permittivity of free space
a = 1  # Inner radius of the shell
b = 2  # Outer radius of the shell

# Radial values
r_vals = np.linspace(0, 3, 100)  # From 0 to 3 (beyond the shell)
E_vals = np.zeros_like(r_vals)

# Electric field calculations
# Region 1: r < a
E_vals[r_vals < a] = 0
# Region 2: a <= r <= b
region_2 = (r_vals >= a) & (r_vals <= b)
E_vals[region_2] = k * (r_vals[region_2] - a) / (epsilon_0 * r_vals[region_2]**2)
# Region 3: r > b
region_3 = r_vals > b
E_vals[region_3] = k * (b - a) / (epsilon_0 * r_vals[region_3]**2)

# Generate a 3D grid for the spherical coordinates
theta = np.linspace(0, 2 * np.pi, 100)  # Angular coordinate
r_grid, theta_grid = np.meshgrid(r_vals, theta)  # Radial and angular coordinates
x = r_grid * np.cos(theta_grid)  # X-coordinates
y = r_grid * np.sin(theta_grid)  # Y-coordinates
z = r_grid  # Z-coordinates (height proportional to radius)

# Map |E| values to the grid
E_mapped = np.zeros_like(r_grid)
for i in range(len(r_vals)):
    E_mapped[:, i] = E_vals[i]

# Plot the 3D field
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surface = ax.plot_surface(x, y, z, facecolors=plt.cm.viridis(E_mapped / np.max(E_mapped)),
                          rstride=2, cstride=2, alpha=0.8)
ax.set_title("Electric Field Magnitude in 3D")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Electric Field Magnitude")
plt.colorbar(surface, label='Normalized |E|')
plt.show()
