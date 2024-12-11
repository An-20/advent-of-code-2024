import functools
import sys


sys.set_int_max_str_digits(10_000)

with open("input.txt") as file:
    old = [int(x) for x in file.read().strip().split()]


new = []
for _ in range(25):
    new = []
    for x in old:
        if x == 0:
            new.append(1)
        elif len(str(x)) % 2 == 0:
            split_idx = len(str(x)) // 2
            new.append(int(str(x)[:split_idx]))
            new.append(int(str(x)[split_idx:]))
        else:
            new.append(int(x) * 2024)
    old = new


print(len(new))
