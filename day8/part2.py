import math


with open("input.txt") as file:
    rows = [x.strip() for x in file.read().splitlines() if x.strip()]


antennas = {}
for ridx, row in enumerate(rows):
    for cidx, char in enumerate(row):
        if char != ".":
            if char not in antennas:
                antennas[char] = [(cidx, ridx)]
            else:
                antennas[char].append((cidx, ridx))

ROWS = len(rows)
COLS = len(rows[0])

antinodes = set()
for antenna_list in antennas.values():
    for a in range(len(antenna_list)):
        for b in range(a + 1, len(antenna_list)):
            ax, ay = antenna_list[a]
            bx, by = antenna_list[b]
            dx = bx - ax
            dy = by - ay
            dx //= math.gcd(dx, dy)
            dy //= math.gcd(dx, dy)

            px = ax
            py = ay
            while True:
                if not (0 <= px < COLS and 0 <= py < ROWS):
                    break
                antinodes.add((px, py))
                px -= dx
                py -= dy

            px = ax
            py = ay
            while True:
                if not (0 <= px < COLS and 0 <= py < ROWS):
                    break
                antinodes.add((px, py))
                px += dx
                py += dy


print(len(antinodes))
