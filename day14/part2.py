with open("input.txt") as file:
    rows = [x.strip() for x in file.read().splitlines() if x.strip()]


HEIGHT = 103
WIDTH = 101


robots = []
for row in rows:
    l, r = row.split()
    l = l.split("=")[1]
    r = r.split("=")[1]
    px, py = l.split(",")
    vx, vy = r.split(",")
    px, py, vx, vy = int(px), int(py), int(vx), int(vy)
    robots.append((px, py, vx, vy))


i = 0
while i < 10000:
    i += 1

    new_robots = []
    for robot in robots:
        px, py, vx, vy = robot
        nx = (px + vx) % WIDTH
        ny = (py + vy) % HEIGHT
        new_robots.append((nx, ny, vx, vy))
    robots = new_robots

    grid = [["-" for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for robot in robots:
        px, py, _, _ = robot
        grid[py][px] = "#"

    # search for row with length > 20
    if any("##########" in "".join(x) for x in grid):
        print("\n" * 10)
        print(i)
        for row in grid:
            print("".join(row))
