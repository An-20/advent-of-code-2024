DEBUG = False


with open("input.txt") as file:
    sections = [x.strip() for x in file.read().split("\n\n") if x.strip()]


warehouse = [list(x.strip()) for x in sections[0].split("\n")]
movements = sections[1].strip()

robot_x = [x.index("@") for x in warehouse if "@" in x][0]
robot_y = [x for x in range(len(warehouse)) if "@" in warehouse[x]][0]


for idx, movement in enumerate(movements):
    if movement not in "^>v<":
        continue
    dx, dy = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}[movement]

    check_x = robot_x
    check_y = robot_y
    can_move = False
    while True:
        check_x += dx
        check_y += dy
        if warehouse[check_y][check_x] == "#":
            break
        elif warehouse[check_y][check_x] == ".":
            can_move = True
            break

    if not can_move:
        if DEBUG:
            print("\n" * 5, f"\nIdx: {idx}, Move: {movement}",
                  "\n" + "\n".join("".join(x).replace(".", "-") for x in warehouse))
        continue

    # progressively move everything
    cur_x = robot_x
    cur_y = robot_y
    last = "."
    while True:
        new_last = warehouse[cur_y][cur_x]
        warehouse[cur_y][cur_x] = last

        if new_last == ".":
            break
        last = new_last

        cur_x += dx
        cur_y += dy

    robot_x += dx
    robot_y += dy

    if DEBUG:
        print("\n" * 5, f"\nIdx: {idx}, Move: {movement}",
              "\n" + "\n".join("".join(x).replace(".", "-") for x in warehouse))


s = 0
for ridx, row in enumerate(warehouse):
    for cidx, char in enumerate(row):
        if char == "O":
            s += ridx * 100 + cidx

print(s)
