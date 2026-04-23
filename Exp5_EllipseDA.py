import matplotlib.pyplot as plt

def plot_ellipse_points(xc, yc, x, y, points):
    symmetric_points = [
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y)
    ]
    points.extend(symmetric_points)

def ellipse_drawing(xc, yc, rx, ry):
    x = 0
    y = ry

    rx2 = rx * rx
    ry2 = ry * ry

    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)

    points = []
    plot_ellipse_points(xc, yc, x, y, points)

    while (2 * ry2 * x) <= (2 * rx2 * y):
        x += 1

        if p1 < 0:
            p1 = p1 + (2 * ry2 * x) + ry2
        else:
            y -= 1
            p1 = p1 + (2 * ry2 * x) - (2 * rx2 * y) + ry2

        plot_ellipse_points(xc, yc, x, y, points)

    p2 = (ry2 * (x + 0.5) ** 2) + (rx2 * (y - 1) ** 2) - (rx2 * ry2)

    while y >= 0:
        y -= 1

        if p2 > 0:
            p2 = p2 - (2 * rx2 * y) + rx2
        else:
            x += 1
            p2 = p2 + (2 * ry2 * x) - (2 * rx2 * y) + rx2

        plot_ellipse_points(xc, yc, x, y, points)

    points = list(set(points))
    points.sort()

    print("Generated Coordinates:", points)

    x_coordinates = [point[0] for point in points]
    y_coordinates = [point[1] for point in points]

    # plt.plot(x_coordinates, y_coordinates, marker="o", linestyle="None")
    # plt.title("Ellipse Drawing Algorithm")
    # plt.xlabel("X-axis")
    # plt.ylabel("Y-axis")
    # plt.grid(True)
    # plt.axis("equal")
    # plt.savefig("Exp5_Output.png")
    # plt.show()
    plt.plot(x_coordinates, y_coordinates, marker="o", linestyle="None")

    plt.scatter(xc, yc, color="black", marker="x", s=100, label="Center")
    plt.text(xc + 0.5, yc + 0.5, f"Center ({xc}, {yc})")

    plt.title("Ellipse Drawing Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.axis("equal")
    plt.legend()
    plt.savefig("Exp5_Output.png")
    plt.show()


# Example
ellipse_drawing(20, 20, 10, 15)