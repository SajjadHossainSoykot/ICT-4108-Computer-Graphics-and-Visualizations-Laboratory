import matplotlib.pyplot as plt

def DDA(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0

    steps = int(max(abs(dx), abs(dy)))

    if steps == 0:
        print("Generated Coordinates:", [(x0, y0)])
        return

    xinc = dx / steps
    yinc = dy / steps

    x = float(x0)
    y = float(y0)

    x_coordinates = []
    y_coordinates = []

    for i in range(steps + 1):
        x_coordinates.append(round(x))
        y_coordinates.append(round(y))
        x += xinc
        y += yinc

    # Coordinate format output
    coordinates = list(zip(x_coordinates, y_coordinates))
    print("Generated Coordinates:", coordinates)

    # Plot
    plt.plot(x_coordinates, y_coordinates, marker='o')
    plt.title("DDA Line Generation")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.savefig("Exp1_Output.png")
    plt.show()


# Example
DDA(10, 15, 20, 25)