import itertools
from utils.silk import execute_parallel


with open("input.txt") as file:
    rows = [x.strip() for x in file.read().splitlines() if x.strip()]


def loops(obx, oby, rows=None):
    DELTAS = {
        0: (0, -1),
        1: (1, 0),
        2: (0, 1),
        3: (-1, 0)
    }

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
            return 1
        positions.add((x, y, rot))
    return 0


ROWS = len(rows)
COLS = len(rows[0])
TOTAL = ROWS * COLS


def main():
    out = execute_parallel(
        [loops] * TOTAL, list(itertools.product(range(COLS), range(ROWS))), [{"rows": rows}] * TOTAL
    )
    print(sum(x.obj for x in out))


if __name__ == "__main__":
    main()
