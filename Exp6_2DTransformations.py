import numpy as np
import matplotlib.pyplot as plt

def plot_shape(ax, points, label, color):
    x = points[:, 0]
    y = points[:, 1]

    ax.plot(x, y, color=color, marker="o", label=label)
    ax.fill(x, y, color=color, alpha=0.2)
    ax.set_aspect("equal")
    ax.grid(True)
    ax.legend()

def add_homogeneous(points):
    ones = np.ones((points.shape[0], 1))
    return np.hstack([points, ones])

def apply_transform(points, matrix):
    homogeneous = add_homogeneous(points)
    transformed = homogeneous @ matrix.T
    return transformed[:, :2]

def translation(tx, ty):
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

def scaling(sx, sy):
    return np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])

def rotation(angle_deg):
    rad = np.radians(angle_deg)
    return np.array([
        [np.cos(rad), -np.sin(rad), 0],
        [np.sin(rad),  np.cos(rad), 0],
        [0, 0, 1]
    ])

def shearing(shx, shy):
    return np.array([
        [1, shx, 0],
        [shy, 1, 0],
        [0, 0, 1]
    ])

def reflection(axis):
    if axis == "x":
        return np.array([
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ])
    elif axis == "y":
        return np.array([
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])
    elif axis == "origin":
        return np.array([
            [-1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ])
    else:
        raise ValueError("Axis must be 'x', 'y', or 'origin'")

object_points = np.array([
    [1, 1],
    [4, 1],
    [2.5, 4],
    [1, 1]
])

translated = apply_transform(object_points, translation(3, 2))
scaled = apply_transform(object_points, scaling(1.5, 0.5))
rotated = apply_transform(object_points, rotation(45))
sheared = apply_transform(object_points, shearing(1, 0.2))
reflected = apply_transform(object_points, reflection("x"))

fig, axes = plt.subplots(3, 2, figsize=(12, 12))
axes = axes.flatten()

plot_shape(axes[0], object_points, "Original Object", "black")
axes[0].set_title("Original Object")

plot_shape(axes[1], translated, "Translated", "red")
axes[1].set_title("Translation")

plot_shape(axes[2], scaled, "Scaled", "green")
axes[2].set_title("Scaling")

plot_shape(axes[3], rotated, "Rotated", "blue")
axes[3].set_title("Rotation 45°")

plot_shape(axes[4], sheared, "Sheared", "purple")
axes[4].set_title("Shearing")

plot_shape(axes[5], reflected, "Reflected (X-axis)", "orange")
axes[5].set_title("Reflection (X-axis)")

plt.tight_layout()
plt.savefig("Exp6_Output.png")
plt.show()