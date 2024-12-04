import collections

with open("input.txt") as file:
    lines = [x.strip() for x in file.read().split("\n") if x.strip()]

ROWS = 140
COLS = 140


SEARCHES = [
    ((0, 1), [(x, 0) for x in range(COLS)]),
    ((0, -1), [(x, ROWS-1) for x in range(COLS)]),
    ((1, 0), [(0, y) for y in range(ROWS)]),
    ((-1, 0), [(COLS-1, y) for y in range(ROWS)]),

    ((1, 1), [(x, 0) for x in range(1, COLS)]),
    ((-1, -1), [(x, ROWS - 1) for x in range(COLS - 1)]),
    ((1, 1), [(0, y) for y in range(ROWS)]),
    ((-1, -1), [(COLS - 1, y) for y in range(ROWS)]),

    ((-1, 1), [(x, 0) for x in range(1, COLS - 1)]),
    ((1, -1), [(x, ROWS - 1) for x in range(1, COLS)]),
    ((1, -1), [(0, y) for y in range(ROWS)]),
    ((-1, 1), [(COLS - 1, y) for y in range(ROWS)]),
]


s = 0
for (dx, dy), starts in SEARCHES:
    for x, y in starts:
        buf = collections.deque()
        while 0 <= x < COLS and 0 <= y < ROWS:
            if len(buf) == 4:
                buf.popleft()
            buf.append(lines[y][x])
            if len(buf) == 4 and buf[0] == "X" and buf[1] == "M" and buf[2] == "A" and buf[3] == "S":
                s += 1
            x += dx
            y += dy

print(s)
