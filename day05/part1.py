with open("input.txt") as file:
    sections = [x.strip() for x in file.read().split("\n\n") if x.strip()]


rules = {}
for row in sections[0].splitlines():
    a, b = row.split("|")
    a, b = int(a), int(b)
    if b in rules:
        rules[b].append(a)
    else:
        rules[b] = [a]


s = 0
for row in sections[1].splitlines():
    data = [int(x.strip()) for x in row.split(",") if x.strip()]
    works = True
    # n squared, who cares?
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            a, b = data[i], data[j]
            if a in rules and b in rules[a]:
                works = False
    if not works:
        continue
    print(data)
    s += data[len(data) // 2]


print(s)
