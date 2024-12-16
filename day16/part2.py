from collections import deque

with open("input.txt") as file:
    maze = [x.strip() for x in file.read().split("\n") if x.strip()]


maze = [list(x.strip()) for x in maze]

start_x = [x.index("S") for x in maze if "S" in x][0]
start_y = [x for x in range(len(maze)) if "S" in maze[x]][0]
end_x = [x.index("E") for x in maze if "E" in x][0]
end_y = [x for x in range(len(maze)) if "E" in maze[x]][0]


DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

visited = {}
distances = {}
prevs = {}

for x in range(len(maze[0])):
    for y in range(len(maze)):
        if maze[y][x] == "#":
            continue
        for d in range(4):
            visited[(x, y, d)] = False
            distances[(x, y, d)] = 1_000_000_000
            prevs[(x, y, d)] = []


distances[(start_x, start_y, 0)] = 0


for idx in range(len(distances)):
    if idx % 1000 == 0:
        print(f"{idx}/{len(distances)}")

    lowest_val = None
    lowest_dist = 1_000_000_000_000

    # O(n^2)
    # but hey its faster to spend 5 minutes waiting than to rewrite this?
    for is_visited, node, distance in zip(visited.values(), distances.keys(), distances.values()):
        if not is_visited and distance < lowest_dist:
            lowest_dist = distance
            lowest_val = node

    if not lowest_val:
        raise ValueError("unreachable!")

    x, y, d = lowest_val
    dist = lowest_dist
    dx, dy = DIRS[d]
    if maze[y + dy][x + dx] != "#":
        if dist + 1 < distances[(x + dx, y + dy, d)]:
            distances[(x + dx, y + dy, d)] = dist + 1
            prevs[(x + dx, y + dy, d)] = [lowest_val]
        elif dist + 1 == distances[(x + dx, y + dy, d)]:
            prevs[(x + dx, y + dy, d)].append(lowest_val)

    for nd in range(4):
        if d == nd:
            continue
        if dist + 1000 < distances[(x, y, nd)]:
            distances[(x, y, nd)] = dist + 1000
            prevs[(x, y, nd)] = [lowest_val]
        elif dist + 1000 == distances[(x, y, nd)]:
            prevs[(x, y, nd)].append(lowest_val)

    visited[(x, y, d)] = True


best = min(distances[(end_x, end_y, d)] for d in range(4))

to_explore = []
for d in range(4):
    if distances[(end_x, end_y, d)] == best:
        to_explore.append((end_x, end_y, d))

tiles = set()
while to_explore:
    node = to_explore.pop()
    x, y, d = node
    tiles.add((x, y))
    to_explore.extend(prevs[node])

print(len(tiles))
