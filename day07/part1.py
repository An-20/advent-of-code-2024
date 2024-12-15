import itertools

with open("input.txt") as file:
    rows = [x.strip() for x in file.read().splitlines() if x.strip()]


s = 0
for row in rows:
    left, data = row.split(":")
    left = int(left)
    data = [int(x.strip()) for x in data.split()]
    for ops in itertools.product(*[[True, False]] * (len(data) - 1)):
        val = data[0]
        for idx in range(len(ops)):
            if ops[idx]:
                val = val + data[idx + 1]
            else:
                val = val * data[idx + 1]
        if val == left:
            s += left
            break

print(s)
