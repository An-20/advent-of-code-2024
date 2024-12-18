import heapq


with open("input.txt") as file:
    corruptions = [x.strip() for x in file.read().split("\n") if x.strip()]


ROWS = 71
COLS = 71
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

space = [[True for _ in range(COLS)] for _ in range(ROWS)]

for row in corruptions[:1024]:
    x, y = row.split(",")
    x = int(x)
    y = int(y)
    space[y][x] = False

start_x = 0
start_y = 0
end_x = 70
end_y = 70


distances = {}
queue = [(0, start_x, start_y)]

for x in range(COLS):
    for y in range(ROWS):
        distances[(x, y)] = 1_000_000_000
distances[(start_x, start_y)] = 0


while queue:
    dist, x, y = heapq.heappop(queue)
    for nd in range(4):
        dx, dy = DIRS[nd]
        nx = x + dx
        ny = y + dy
        if not 0 <= nx < COLS or not 0 <= ny < ROWS:
            continue
        if not space[ny][nx]:
            continue

        if dist + 1 < distances[(nx, ny)]:
            distances[(nx, ny)] = dist + 1
            heapq.heappush(queue, (dist + 1, nx, ny))


print(distances[(end_x, end_y)])
