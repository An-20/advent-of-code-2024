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

    px += 10000000000000
    py += 10000000000000

    det = ax * by - bx * ay
    if det == 0:
        # because of nature of input, there is always a solution
        raise Exception("Unimplemented")

    A = (px * by - bx * py) / det
    B = (-(ay * px) + ax * py) / det
    if A.is_integer() and B.is_integer():
        s += int(A * 3 + B)

    # print(A, B)


print(s)
