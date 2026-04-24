import numpy as np
import matplotlib.pyplot as plt

def b_spline_basis(i, k, t, knots):
    if k == 0:
        if knots[i] <= t < knots[i + 1]:
            return 1
        return 0

    denominator1 = knots[i + k] - knots[i]
    denominator2 = knots[i + k + 1] - knots[i + 1]

    term1 = 0
    term2 = 0

    if denominator1 != 0:
        term1 = ((t - knots[i]) / denominator1) * b_spline_basis(i, k - 1, t, knots)

    if denominator2 != 0:
        term2 = ((knots[i + k + 1] - t) / denominator2) * b_spline_basis(i + 1, k - 1, t, knots)

    return term1 + term2

def b_spline_curve(control_points, degree, num_points=200):
    n = len(control_points) - 1
    knots = np.concatenate((
        np.zeros(degree),
        np.linspace(0, 1, n - degree + 2),
        np.ones(degree)
    ))

    curve_points = []

    for t in np.linspace(0, 1, num_points):
        point = np.zeros(2)

        for i in range(n + 1):
            basis = b_spline_basis(i, degree, t, knots)
            point += basis * control_points[i]

        curve_points.append(point)

    return np.array(curve_points)

# Define control points
control_points = np.array([
    [0, 0],
    [1, 3],
    [3, 4],
    [5, 2],
    [6, 0]
])

degree = 3
curve = b_spline_curve(control_points, degree)

plt.plot(control_points[:, 0], control_points[:, 1], "ro--", label="Control Polygon")
plt.plot(curve[:, 0], curve[:, 1], "b", linewidth=2, label="B-Spline Curve")

plt.title("B-Spline Curve Generation")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.savefig("Exp10_Output.png")
plt.show()