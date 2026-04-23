import matplotlib.pyplot as plt

def plot_circle_points(xc, yc, x, y, points):
    symmetric_points = [
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
        (xc + y, yc + x),
        (xc - y, yc + x),
        (xc + y, yc - x),
        (xc - y, yc - x)
    ]
    points.extend(symmetric_points)

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r

    points = []
    plot_circle_points(xc, yc, x, y, points)

    while x < y:
        x += 1
        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * x - 2 * y + 1
        plot_circle_points(xc, yc, x, y, points)

    points = list(set(points))
    points.sort()

    print("Generated Coordinates:", points)

    x_coordinates = [point[0] for point in points]
    y_coordinates = [point[1] for point in points]

    plt.plot(x_coordinates, y_coordinates, marker='o', linestyle='None')
    plt.scatter(xc, yc, color="black", marker="x", s=100, label="Center")
    plt.text(xc + 0.5, yc + 0.5, f"Center ({xc}, {yc})")
    plt.title("Midpoint Circle Drawing Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.axis("equal")
    plt.savefig("Exp3_Output.png")
    plt.show()

# Example
midpoint_circle(20, 20, 10)