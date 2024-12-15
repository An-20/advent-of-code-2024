import time

from utils.silk import execute_parallel


with open("input.txt") as file:
    rows = [x.strip() for x in file.read().splitlines() if x.strip()]


def fn(oby, rows=None):
    DELTAS = {
        0: (0, -1),
        1: (1, 0),
        2: (0, 1),
        3: (-1, 0)
    }

    s = 0

    for obx in range(len(rows[0])):
        rot = 0
        x = None
        y = None
        for ridx, row in enumerate(rows):
            for cidx, char in enumerate(row):
                if char == "^":
                    x = cidx
                    y = ridx

        positions = {(x, y)}

        while True:
            dx, dy = DELTAS[rot]
            px = x + dx
            py = y + dy
            if not 0 <= py < len(rows) or not 0 <= px < len(rows[0]):
                break
            if rows[py][px] == "#" or (px == obx and py == oby):
                rot = (rot + 1) % 4
                continue
            x = px
            y = py
            if (x, y, rot) in positions:
                s += 1
                break
            positions.add((x, y, rot))

    return s


ROWS = len(rows)
COLS = len(rows[0])


def main():
    out = execute_parallel(
        [fn] * ROWS, [[x] for x in range(ROWS)], [{"rows": rows}] * ROWS
    )
    print(sum(x.obj for x in out))


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(end_time - start_time)
