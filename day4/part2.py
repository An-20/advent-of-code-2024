with open("input.txt") as file:
    lines = [x.strip() for x in file.read().split("\n") if x.strip()]

ROWS = 140
COLS = 140

s = 0
for x in range(0, COLS - 2):
    for y in range(0, ROWS - 2):
        if lines[y+1][x+1] != "A":
            continue
        tl, tr = lines[y][x], lines[y][x+2]
        bl, br = lines[y+2][x], lines[y+2][x + 2]
        if not ((tl == "M" and br == "S") or (tl == "S" and br == "M")):
            continue
        if not ((tr == "M" and bl == "S") or (tr == "S" and bl == "M")):
            continue
        s += 1

print(s)