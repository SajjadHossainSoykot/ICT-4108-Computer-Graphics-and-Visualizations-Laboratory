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

def bresenham_circle(xc, yc, r):
    x = 0
    y = r
    p = 3 - 2 * r

    points = []

    while x <= y:
        plot_circle_points(xc, yc, x, y, points)

        if p < 0:
            p = p + 4 * x + 6
        else:
            p = p + 4 * (x - y) + 10
            y -= 1

        x += 1

    points = list(set(points))
    points.sort()

    print("Generated Coordinates:", points)

    x_coordinates = [point[0] for point in points]
    y_coordinates = [point[1] for point in points]

    plt.plot(x_coordinates, y_coordinates, marker="o", linestyle="None")
    plt.title("Bresenham Circle Drawing Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.axis("equal")
    plt.savefig("Exp4_Output.png")
    plt.show()


# Example
bresenham_circle(20, 20, 10)