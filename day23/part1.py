with open("input.txt") as file:
    INPUT_DATA = [x.strip() for x in file.readlines() if x.strip()]


connections = {}
for row in INPUT_DATA:
    a, b = row.split("-")
    if len(a) == 1 or len(b) == 1:
        print(a, b)
    if a not in connections:
        connections[a] = {b}
    else:
        connections[a].add(b)
    if b not in connections:
        connections[b] = {a}
    else:
        connections[b].add(a)


interconnected = set()
for a in connections:
    for b in connections[a]:
        c = connections[a].intersection(connections[b])
        interconnected.update({tuple(sorted((a, b, c1))) for c1 in c if (a[0] == "t" or b[0] == "t" or c1[0] == "t")})
print(len(interconnected))
