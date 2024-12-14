with open("input.txt") as file:
    rows = [x.strip() for x in file.read().splitlines() if x.strip()]


HEIGHT = 103
WIDTH = 101


quadrants = [0, 0, 0, 0]
for row in rows:
    l, r = row.split()
    l = l.split("=")[1]
    r = r.split("=")[1]
    px, py = l.split(",")
    vx, vy = r.split(",")
    px, py, vx, vy = int(px), int(py), int(vx), int(vy)

    fx = (px + vx * 100) % WIDTH
    fy = (py + vy * 100) % HEIGHT

    mx = WIDTH // 2
    my = HEIGHT // 2
    if fx < mx and fy < my:
        i = 0
    elif fx < mx and fy > my:
        i = 1
    elif fx > mx and fy < my:
        i = 2
    elif fx > mx and fy > my:
        i = 3
    else:
        continue

    quadrants[i] += 1


print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])
