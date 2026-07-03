import numpy as np
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import random
import math

from io import BytesIO


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
        return (
            int(Rs * math.cos(theta)),
            int(Rs * math.sin(theta))
        )

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

        if math.sqrt(x * x + y * y) > Rkill:
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

        r = math.sqrt(x * x + y * y)

        if r > Rmax:

            Rmax = r
            Rs = int(Rmax + 15)
            Rkill = int(Rmax + 45)

    for _ in range(num_particles):

        x, y = occupy()

        while True:

            x, y = jump(x, y)

            result = check(x, y)

            if result == "stick":

                aggregate(x, y)
                break

            elif result == "kill":

                x, y = occupy()

    fig = plt.figure(figsize=(8, 8), dpi=200)

    plt.imshow(
        grid,
        cmap="binary",
        origin="lower",
        interpolation="nearest"
    )

    plt.axis("off")

    buffer = BytesIO()

    plt.savefig(
        buffer,
        format="png",
        bbox_inches="tight"
    )

    plt.close(fig)

    buffer.seek(0)

    return buffer
