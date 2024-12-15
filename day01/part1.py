with open("input.txt") as file:
    lines = [x.strip() for x in file.read().split("\n") if x.strip()]


a = []
b = []
for line in lines:
    a1, b1 = line.split("   ")  # why lol
    a.append(int(a1))
    b.append(int(b1))


a = sorted(a)
b = sorted(b)
s = 0
for a2, b2 in zip(a, b):
    s += abs(a2 - b2)
print(s)
