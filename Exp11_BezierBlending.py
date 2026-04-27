import numpy as np
import matplotlib.pyplot as plt
from math import comb

def bezier_blending_function(n, i, t):
    return comb(n, i) * (t ** i) * ((1 - t) ** (n - i))

# Number of control points
control_points = 4
degree = control_points - 1

# Parameter values
t = np.linspace(0, 1, 200)

plt.figure(figsize=(8, 5))

for i in range(control_points):
    blending_values = bezier_blending_function(degree, i, t)
    plt.plot(t, blending_values, label=f"B{i},{degree}(t)")

plt.title("Bezier Blending Functions")
plt.xlabel("t")
plt.ylabel("Blending Function Value")
plt.grid(True)
plt.legend()
plt.savefig("Exp11_Output.png")
plt.show()