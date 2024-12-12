from collections import deque


with open("input.txt") as file:
    rows = [x.strip() for x in file.read().splitlines() if x.strip()]


ROWS = len(rows)
COLS = len(rows[0])


s = 0
visited = set()
for ridx in range(ROWS):
    for cidx in range(COLS):
        if (cidx, ridx) in visited:
            continue
        # start a new region
        region_type = rows[ridx][cidx]
        region_plots = set()
        region_sides = 0
        to_visit = deque([(cidx, ridx)])
        while to_visit:
            cur = to_visit.popleft()
            curx, cury = cur
            if cur in visited:
                continue
            sides = 4
            for delta in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dx, dy = delta
                nx = curx + dx
                ny = cury + dy
                if not(0 <= nx < COLS and 0 <= ny < ROWS):
                    continue
                if (nx, ny) in region_plots:
                    sides -= 2
                if rows[ny][nx] == region_type and (nx, ny) not in visited:
                    to_visit.append((nx, ny))
            region_sides += sides
            visited.add(cur)
            region_plots.add(cur)
        # print(region_type, region_sides, len(region_plots))
        s += region_sides * len(region_plots)

print(s)
