import heapq

with open("input.txt") as file:
    maze = [x.strip() for x in file.read().split("\n") if x.strip()]


maze = [list(x.strip()) for x in maze]

start_x = [x.index("S") for x in maze if "S" in x][0]
start_y = [x for x in range(len(maze)) if "S" in maze[x]][0]
end_x = [x.index("E") for x in maze if "E" in x][0]
end_y = [x for x in range(len(maze)) if "E" in maze[x]][0]


DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

distances = {}
queue = [(0, start_x, start_y, 0)]

for x in range(len(maze[0])):
    for y in range(len(maze)):
        if maze[y][x] == "#":
            continue
        for d in range(4):
            distances[(x, y, d)] = 1_000_000_000


while queue:
    dist, x, y, d = heapq.heappop(queue)
    dx, dy = DIRS[d]
    if maze[y + dy][x + dx] != "#":
        if dist + 1 < distances[(x + dx, y + dy, d)]:
            distances[(x + dx, y + dy, d)] = dist + 1
            heapq.heappush(queue, (dist + 1, x + dx, y + dy, d))

    for nd in range(4):
        if d == nd:
            continue
        if dist + 1000 < distances[(x, y, nd)]:
            distances[(x, y, nd)] = dist + 1000
            heapq.heappush(queue, (dist + 1000, x, y, nd))


print(min(distances[(end_x, end_y, d)] for d in range(4)))
