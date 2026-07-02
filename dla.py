import numpy as np
import matplotlib.pyplot as plt
import random
import math
import os

def generate_dla(num_particles=100):

    GRID_SIZE = 601
    CENTER = GRID_SIZE // 2

    grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=np.uint8)
    grid[CENTER, CENTER] = 1

    Rmax = 5
    Rs = 15
    Rkill = 45

    def occupy():
        theta = random.uniform(0, 2 * math.pi)
        x = int(Rs * math.cos(theta))
        y = int(Rs * math.sin(theta))
        return x, y

    def jump(x, y):
        r = random.randint(0, 3)

        if r == 0:
            x += 1
        elif r == 1:
            x -= 1
        elif r == 2:
            y += 1
        else:
            y -= 1

        return x, y

    def check(x, y):
        gx = x + CENTER
        gy = y + CENTER

        if gx < 2 or gx >= GRID_SIZE - 2:
            return "kill"

        if gy < 2 or gy >= GRID_SIZE - 2:
            return "kill"

        r = math.sqrt(x*x + y*y)

        if r > Rkill:
            return "kill"

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                if grid[gx + dx, gy + dy]:
                    return "stick"

        return "walk"

    def aggregate(x, y):
        nonlocal Rmax, Rs, Rkill

        gx = x + CENTER
        gy = y + CENTER

        grid[gx, gy] = 1

        r = math.sqrt(x*x + y*y)

        if r > Rmax:
            Rmax = r
            Rs = int(Rmax + 15)
            Rkill = int(Rmax + 45)

    def long_jump(x, y):
        r = math.sqrt(x*x + y*y)

        if r > Rs:
            theta = random.uniform(0, 2 * math.pi)
            x += int((r - Rs) * math.cos(theta))
            y += int((r - Rs) * math.sin(theta))

        return x, y

    for particle in range(num_particles):

        x, y = occupy()

        while True:

            x, y = jump(x, y)

            result = check(x, y)

            if result == "stick":
                aggregate(x, y)
                break

            elif result == "kill":
                x, y = occupy()

            else:
                r = math.sqrt(x*x + y*y)

                if r > Rs + 10:
                    x, y = long_jump(x, y)

    os.makedirs("static/generated", exist_ok=True)

    filename = "static/generated/dla.png"

    plt.figure(figsize=(8, 8), dpi=250)

    plt.imshow(
        grid,
        cmap="binary",
        origin="lower",
        interpolation="nearest"
    )

    plt.axis("off")

    plt.savefig(filename, bbox_inches="tight")

    plt.close()

    return "/" + filename
