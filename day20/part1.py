import heapq


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


s = 0
# next, try every possible cheat
for x in range(COLS):
    for y in range(ROWS):
        for dx, dy in [(-2, 0), (2, 0), (0, 2), (0, -2)]:
            nx = x + dx
            ny = y + dy
            if not 0 <= nx < COLS or not 0 <= ny < ROWS:
                continue
            if distances[(x, y)] == INF or distances[(nx, ny)] == INF:
                continue
            cheat_saving = distances[(x, y)] - distances[(nx, ny)] - (abs(dx) + abs(dy))
            if cheat_saving >= 100:
                s += 1

print(s)
