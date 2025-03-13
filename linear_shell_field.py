import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
rho_0 = 1  # C/m^3
epsilon_0 = 8.85e-12  # C^2/(N·m^2)
a = 1  # Inner radius (m)
b = 3  # Outer radius (m)

# Define the r values (radius) for 3D plot
r = np.linspace(0.01, 5, 100)

# Electric field calculation for each region
E_inner = np.zeros_like(r)  # E = 0 for r < a
E_shell = (rho_0 * (r**3 - a**3)) / (3 * epsilon_0 * r**2)  # for a < r < b
E_outer = (rho_0 * (b**3 - a**3)) / (3 * epsilon_0 * r**2)  # for r > b

# Potential calculation for each region
V_inner = np.zeros_like(r)  # Constant potential inside the shell (for simplicity, we take it as 0)
V_shell = (-rho_0 / (3 * epsilon_0)) * (r**2 / 2 + a**3 / r)  # for a < r < b
V_outer = (rho_0 * (b**3 - a**3)) / (3 * epsilon_0 * r)  # for r > b

# Set up 3D plot
fig = plt.figure(figsize=(14, 7))

# Create a 3D axis for the sphere plot
ax1 = fig.add_subplot(121, projection='3d')

# Create a spherical surface for the shell
phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, np.pi, 100)
phi, theta = np.meshgrid(phi, theta)

# Parametric equations for the sphere surface (radius = b)
x = b * np.sin(theta) * np.cos(phi)
y = b * np.sin(theta) * np.sin(phi)
z = b * np.cos(theta)

# Plot the sphere surface
ax1.plot_surface(x, y, z, color='c', alpha=0.3, rstride=5, cstride=5)

# Plot electric field vectors (arrows)
# Define the grid of points for electric field vectors
grid_points = 10  # Number of arrows in the grid
r_arrow = np.linspace(0.5, b-0.5, grid_points)  # Position of arrows in radial direction
theta_arrow, phi_arrow = np.meshgrid(np.linspace(0, np.pi, grid_points), np.linspace(0, 2 * np.pi, grid_points))

# Convert spherical to cartesian coordinates for arrow positions
x_arrow = r_arrow[:, None] * np.sin(theta_arrow) * np.cos(phi_arrow)
y_arrow = r_arrow[:, None] * np.sin(theta_arrow) * np.sin(phi_arrow)
z_arrow = r_arrow[:, None] * np.cos(theta_arrow)

# Calculate electric field magnitudes at each arrow position
E_magnitude = (rho_0 * (r_arrow**3 - a**3)) / (3 * epsilon_0 * r_arrow**2)  # electric field for r > a

# Normalize the electric field vectors for visualizing arrows
E_x = E_magnitude * np.sin(theta_arrow) * np.cos(phi_arrow)
E_y = E_magnitude * np.sin(theta_arrow) * np.sin(phi_arrow)
E_z = E_magnitude * np.cos(theta_arrow)

# Plot the electric field vectors (arrows) using quiver
ax1.quiver(x_arrow, y_arrow, z_arrow, E_x, E_y, E_z, length=0.1, color=plt.cm.viridis(E_magnitude / np.max(E_magnitude)))

# Labels and Title
ax1.set_xlabel('X (m)')
ax1.set_ylabel('Y (m)')
ax1.set_zlabel('Z (m)')
ax1.set_title('Electric Field Vectors and Sphere in 3D')

# Create another 3D axis for the potential plot
ax2 = fig.add_subplot(122, projection='3d')

# Plot the sphere surface for potential
ax2.plot_surface(x, y, z, color='m', alpha=0.3, rstride=5, cstride=5)

# Plot electric field vectors on the sphere
ax2.quiver(x_arrow, y_arrow, z_arrow, E_x, E_y, E_z, length=0.1, color=plt.cm.viridis(E_magnitude / np.max(E_magnitude)))

# Labels and Title
ax2.set_xlabel('X (m)')
ax2.set_ylabel('Y (m)')
ax2.set_zlabel('Z (m)')
ax2.set_title('Electric Field Vectors and Sphere in 3D (Potential Visualization)')

# Display the plot
plt.tight_layout()
plt.show()
