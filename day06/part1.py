with open("input.txt") as file:
    rows = [x.strip() for x in file.read().splitlines() if x.strip()]


DELTAS = {
    0: (0, -1),
    1: (1, 0),
    2: (0, 1),
    3: (-1, 0)
}


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
    if rows[py][px] == "#":
        rot = (rot + 1) % 4
        continue
    x = px
    y = py
    positions.add((x, y))


print(len(positions))
