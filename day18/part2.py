import heapq


with open("input.txt") as file:
    corruptions = [x.strip() for x in file.read().split("\n") if x.strip()]


ROWS = 71
COLS = 71
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
INF = float("inf")

space = [[True for _ in range(COLS)] for _ in range(ROWS)]

start_x, start_y = 0, 0
end_x, end_y = 70, 70

cor_x, cor_y = None, None
for cidx, corruption in enumerate(corruptions):
    # print(f"{cidx} / {len(corruptions)}")
    cor_x, cor_y = corruption.split(",")
    cor_x = int(cor_x)
    cor_y = int(cor_y)
    space[cor_y][cor_x] = False

    distances = {}
    queue = [(0, start_x, start_y)]

    for x in range(COLS):
        for y in range(ROWS):
            distances[(x, y)] = INF
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

    if distances[(end_x, end_y)] == INF:
        break


print(f"{cor_x},{cor_y}")
