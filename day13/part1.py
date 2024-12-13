with open("input.txt") as file:
    sections = [x.strip() for x in file.read().split("\n\n") if x.strip()]


s = 0
for section in sections:
    first, second, third = section.splitlines()
    ax, ay = first.split(":")[1].strip().split(",")
    ax = int(ax.split("+")[1].strip())
    ay = int(ay.split("+")[1].strip())

    bx, by = second.split(":")[1].strip().split(",")
    bx = int(bx.split("+")[1].strip())
    by = int(by.split("+")[1].strip())

    px, py = third.split(":")[1].strip().split(",")
    px = int(px.split("=")[1].strip())
    py = int(py.split("=")[1].strip())

    min_tokens = 1_000_000_000
    for i in range(101):
        for j in range(101):
            if (ax * i) + (bx * j) == px and (ay * i) + (by * j) == py:
                tokens = i * 3 + j
                if tokens < min_tokens:
                    min_tokens = tokens
    if min_tokens != 1_000_000_000:
        s += min_tokens


print(s)
