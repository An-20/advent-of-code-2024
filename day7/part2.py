import itertools

with open("input.txt") as file:
    rows = [x.strip() for x in file.read().splitlines() if x.strip()]


s = 0
for ridx, row in enumerate(rows):
    left, data = row.split(":")
    left = int(left)
    data = [int(x.strip()) for x in data.split()]
    for ops in itertools.product(*[[0, 1, 2]] * (len(data) - 1)):
        val = data[0]
        for idx in range(len(ops)):
            if ops[idx] == 0:
                val = val + data[idx + 1]
            elif ops[idx] == 1:
                val = val * data[idx + 1]
            else:
                val = int(str(val) + str(data[idx + 1]))

        if val == left:
            s += left
            break
    print(ridx)

print(s)
