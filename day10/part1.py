import time
import functools

with open("input.txt") as file:
    rows = [x.strip() for x in file.read().splitlines() if x.strip()]


ROWS = len(rows)
COLS = len(rows[0])


@functools.lru_cache
def count(x: int, y: int, depth: int = 0):
    if rows[y][x] == "9" and depth == 9:
        return {(x, y)}
    if int(rows[y][x]) != depth:
        return set()
    s = set()
    for step in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        dx, dy = step
        nx = x + dx
        ny = y + dy
        if not (0 <= nx < COLS and 0 <= ny < ROWS):
            continue
        s.update(count(nx, ny, depth + 1))
    return s


def main():
    s = 0
    for row in range(ROWS):
        for col in range(COLS):
            s += len(count(col, row, 0))
    print(s)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(end_time - start_time)
