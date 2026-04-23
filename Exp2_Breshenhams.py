import matplotlib.pyplot as plt

def bresenham(x0, y0, x1, y1):
    x_coordinates = []
    y_coordinates = []

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    x, y = x0, y0

    sx = 1 if x1 > x0 else -1
    sy = 1 if y1 > y0 else -1

    if dx > dy:
        p = 2 * dy - dx
        for i in range(dx + 1):
            x_coordinates.append(x)
            y_coordinates.append(y)

            x += sx
            if p < 0:
                p += 2 * dy
            else:
                y += sy
                p += 2 * (dy - dx)
    else:
        p = 2 * dx - dy
        for i in range(dy + 1):
            x_coordinates.append(x)
            y_coordinates.append(y)

            y += sy
            if p < 0:
                p += 2 * dx
            else:
                x += sx
                p += 2 * (dx - dy)

    coordinates = list(zip(x_coordinates, y_coordinates))
    print("Generated Coordinates:", coordinates)

    plt.plot(
        x_coordinates,
        y_coordinates,
        color="blue",
        marker="o",
        markersize=5,
        markerfacecolor="red"
    )
    plt.title("Bresenham Line Generation")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.savefig("Exp2_Output.png")
    plt.show()


# Example
bresenham(10, 15, 20, 30)