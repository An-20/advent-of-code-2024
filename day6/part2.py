with open("input.txt") as file:
    rows = [x.strip() for x in file.read().splitlines() if x.strip()]


DELTAS = {
    0: (0, -1),
    1: (1, 0),
    2: (0, 1),
    3: (-1, 0)
}


def loops(obx, oby):
    rot = 0
    x = None
    y = None
    for ridx, row in enumerate(rows):
        for cidx, char in enumerate(row):
            if char == "^":
                x = cidx
                y = ridx

    positions = {(x, y)}

    while True:
        dx, dy = DELTAS[rot]
        px = x + dx
        py = y + dy
        if not 0 <= py < len(rows) or not 0 <= px < len(rows[0]):
            break
        if rows[py][px] == "#" or (px == obx and py == oby):
            rot = (rot + 1) % 4
            continue
        x = px
        y = py
        if (x, y, rot) in positions:
            return True
        positions.add((x, y, rot))
    return False


s = 0
for xp in range(len(rows[0])):
    for yp in range(len(rows)):
        if rows[yp][xp] == "#" or rows[yp][xp] == "^":
            continue
        if loops(xp, yp):
            s += 1
    # print(f"{xp}/{len(rows[0])}")
print(s)
