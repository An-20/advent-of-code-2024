with open("input.txt") as file:
    lines = [x.strip() for x in file.read().split("\n") if x.strip()]


s = 0
for line in lines:
    data = [int(x) for x in line.split(" ")]
    diffs = []
    for i in range(1, len(data)):
        diffs.append(data[i] - data[i - 1])
    if all(1 <= abs(x) <= 3 for x in diffs) and (all(x < 0 for x in diffs) or all(x > 0 for x in diffs)):
        s += 1
print(s)
