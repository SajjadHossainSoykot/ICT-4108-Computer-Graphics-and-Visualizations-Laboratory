import numpy as np
import matplotlib.pyplot as plt
from math import comb

def bezier_curve(control_points, num_points=100):
    n = len(control_points) - 1
    t_values = np.linspace(0, 1, num_points)

    curve_points = []

    for t in t_values:
        point = np.zeros(2)
        for i in range(n + 1):
            bernstein = comb(n, i) * (t ** i) * ((1 - t) ** (n - i))
            point += bernstein * control_points[i]
        curve_points.append(point)

    return np.array(curve_points)

# Define control points
control_points = np.array([
    [0, 0],
    [1, 3],
    [4, 3],
    [5, 0]
])

curve = bezier_curve(control_points)

# Plot
plt.plot(control_points[:, 0], control_points[:, 1], 'ro--', label="Control Polygon")
plt.plot(curve[:, 0], curve[:, 1], 'b', linewidth=2, label="Bezier Curve")

plt.title("Bezier Curve Generation")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.savefig("Exp9_Output.png")
plt.show()