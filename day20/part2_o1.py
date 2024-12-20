import time
import heapq

from utils.silk import execute_parallel


with open("input.txt") as file:
    maze = [x.strip() for x in file.read().split("\n") if x.strip()]


ROWS = len(maze)
COLS = len(maze[0])
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
INF = float("inf")


start_x = [x.index("S") for x in maze if "S" in x][0]
start_y = [x for x in range(len(maze)) if "S" in maze[x]][0]
end_x = [x.index("E") for x in maze if "E" in x][0]
end_y = [x for x in range(len(maze)) if "E" in maze[x]][0]


# first, find the shortest path without cheats to generate the distance matrix
distances = {}
for x in range(COLS):
    for y in range(ROWS):
        distances[(x, y)] = INF
distances[(start_x, start_y)] = 0

queue = [(0, start_x, start_y)]
while queue:
    dist, x, y = heapq.heappop(queue)
    for nd in range(4):
        dx, dy = DIRS[nd]
        nx = x + dx
        ny = y + dy
        if not 0 <= nx < COLS or not 0 <= ny < ROWS:
            continue
        if maze[ny][nx] == "#":
            continue

        if dist + 1 < distances[(nx, ny)]:
            distances[(nx, ny)] = dist + 1
            heapq.heappush(queue, (dist + 1, nx, ny))


# precompute the allowed diffs to avoid branching
diffs = []
for dx in range(-20, 21):
    for dy in range(-20, 21):
        cheat_len = abs(dx) + abs(dy)
        if cheat_len > 20:
            continue
        diffs.append((dx, dy, cheat_len))


def fn(_distances: dict[tuple[int, int], int], _diffs: list[(int, int, int)], x: int, cols: int, rows: int):
    INF = float("inf")
    s = 0
    for y in range(rows):
        for _dx, _dy, _cheat_len in _diffs:
            _nx = x + _dx
            _ny = y + _dy
            if not 0 <= _nx < cols or not 0 <= _ny < rows:
                continue
            if _distances[(x, y)] == INF or _distances[(_nx, _ny)] == INF:
                continue
            cheat_saving = _distances[(x, y)] - _distances[(_nx, _ny)] - _cheat_len
            if cheat_saving >= 100:
                s += 1
    return s


def main():
    out = execute_parallel(
        [fn] * COLS, [[distances, diffs, x, COLS, ROWS] for x in range(COLS)], [{}] * COLS
    )
    print(sum(x.obj for x in out))


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(end_time - start_time)
