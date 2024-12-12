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
        to_visit = deque([(cidx, ridx)])
        while to_visit:
            cur = to_visit.popleft()
            cur_x, cur_y = cur
            if cur in visited:
                continue
            for delta in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dx, dy = delta
                nx = cur_x + dx
                ny = cur_y + dy
                if not (0 <= nx < COLS and 0 <= ny < ROWS):
                    continue
                if rows[ny][nx] == region_type and (nx, ny) not in visited:
                    to_visit.append((nx, ny))
            visited.add(cur)
            region_plots.add(cur)

        min_x, max_x = min(x[0] for x in region_plots), max(x[0] for x in region_plots)
        min_y, max_y = min(x[1] for x in region_plots), max(x[1] for x in region_plots)
        region_sides = 0

        # search for vertical sides
        for x in range(min_x, max_x + 2):
            side_type = None
            for y in range(min_y, max_y + 1):
                left = (x - 1, y) in region_plots if x != min_x else False
                right = (x, y) in region_plots if x != (max_x + 1) else False
                new_side_type = "L" if left and not right else "R" if right and not left else None
                if side_type != new_side_type:
                    # change in side
                    if new_side_type is not None:
                        region_sides += 1
                    side_type = new_side_type

        # search for horizontal sides
        for y in range(min_y, max_y + 2):
            side_type = None
            for x in range(min_x, max_x + 1):
                up = (x, y - 1) in region_plots if y != min_y else False
                down = (x, y) in region_plots if y != (max_y + 1) else False
                new_side_type = "U" if up and not down else "D" if down and not up else None
                if side_type != new_side_type:
                    # change in side
                    if new_side_type is not None:
                        region_sides += 1
                    side_type = new_side_type

        # print(region_type, region_sides, len(region_plots))
        s += region_sides * len(region_plots)

print(s)
