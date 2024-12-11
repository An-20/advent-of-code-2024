import functools
import sys


sys.set_int_max_str_digits(10_000)

with open("input.txt") as file:
    data = [int(x) for x in file.read().strip().split()]


@functools.cache
def blink(num, times):
    if times <= 0:
        return 1
    if num == 0:
        return blink(1, times - 1)
    elif len(str(num)) % 2 == 0:
        split_idx = len(str(num)) // 2
        left = int(str(num)[:split_idx])
        right = int(str(num)[split_idx:])
        return blink(left, times - 1) + blink(right, times - 1)
    else:
        return blink(int(num) * 2024, times - 1)


s = 0
for x in data:
    s += blink(x, 75)


print(s)
