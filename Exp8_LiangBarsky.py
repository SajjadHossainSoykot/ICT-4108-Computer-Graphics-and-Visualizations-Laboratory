import matplotlib.pyplot as plt

def liang_barsky(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    dx = x2 - x1
    dy = y2 - y1

    p = [-dx, dx, -dy, dy]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]

    u1 = 0
    u2 = 1

    for i in range(4):
        if p[i] == 0:
            if q[i] < 0:
                return False, None
        else:
            r = q[i] / p[i]

            if p[i] < 0:
                u1 = max(u1, r)
            else:
                u2 = min(u2, r)

    if u1 > u2:
        return False, None

    clipped_x1 = x1 + u1 * dx
    clipped_y1 = y1 + u1 * dy
    clipped_x2 = x1 + u2 * dx
    clipped_y2 = y1 + u2 * dy

    return True, (clipped_x1, clipped_y1, clipped_x2, clipped_y2)


# Example input
x1, y1 = 2, 2
x2, y2 = 10, 8

xmin, ymin = 4, 3
xmax, ymax = 9, 7

accepted, clipped_line = liang_barsky(x1, y1, x2, y2, xmin, ymin, xmax, ymax)

plt.plot([x1, x2], [y1, y2], "r--", label="Original Line")

if accepted:
    cx1, cy1, cx2, cy2 = clipped_line
    print("Clipped Coordinates:", [(cx1, cy1), (cx2, cy2)])
    plt.plot([cx1, cx2], [cy1, cy2], "g", linewidth=2, label="Clipped Line")
else:
    print("Line is completely outside the clipping window.")

plt.plot(
    [xmin, xmax, xmax, xmin, xmin],
    [ymin, ymin, ymax, ymax, ymin],
    "b",
    label="Clipping Window"
)

plt.title("Liang-Barsky Line Clipping")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.savefig("Exp8_Output.png")
plt.show()