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
            px1 = bx + dx
            py1 = by + dy
            px2 = ax - dx
            py2 = ay - dy
            if 0 <= px1 < COLS and 0 <= py1 < ROWS:
                antinodes.add((px1, py1))
            if 0 <= px2 < COLS and 0 <= py2 < ROWS:
                antinodes.add((px2, py2))


print(len(antinodes))
