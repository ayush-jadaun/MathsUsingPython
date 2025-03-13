import numpy as np
import matplotlib.pyplot as plt

x, y, z = np.meshgrid(np.linspace(-2, 2, 10),
                      np.linspace(-2, 2, 10),
                      np.linspace(-2, 2, 10))
r = np.sqrt(x**2 + y**2 + z**2)


mask = r > 0


r[~mask] = 1  




Fx = x / r**2
Fy = y / r**2
Fz = z / r**2

Fx[~mask], Fy[~mask], Fz[~mask] = 0, 0, 0


fig = plt.figure(figsize=(8, 8))


ax = fig.add_subplot(111, projection='3d')

ax.quiver(x, y, z, Fx, Fy, Fz, length=0.2, normalize=True, color='blue', linewidth=0.5)



# Set plot limits and labels
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Radial Vector Field: $\\frac{\\hat{r}}{r^2}$')

plt.show()
