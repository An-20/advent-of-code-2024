from collections import Counter

with open("input.txt") as file:
    lines = [x.strip() for x in file.read().split("\n") if x.strip()]


a = []
b = []
for line in lines:
    a1, b1 = line.split("   ")  # why lol
    a.append(int(a1))
    b.append(int(b1))


c = Counter(b)
s = 0

for a2 in a:
    s += a2 * c.get(a2, 0)
print(s)
