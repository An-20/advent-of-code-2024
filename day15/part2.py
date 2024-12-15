with open("input.txt") as file:
    sections = [x.strip() for x in file.read().split("\n\n") if x.strip()]


for a, b in {"#": "##", "O": "[]", ".": "..", "@": "@."}.items():
    sections[0] = sections[0].replace(a, b)
warehouse = [list(x.strip()) for x in sections[0].split("\n")]
movements = sections[1].strip().replace("\n", "")

robot_x = [x.index("@") for x in warehouse if "@" in x][0]
robot_y = [x for x in range(len(warehouse)) if "@" in warehouse[x]][0]


for idx, movement in enumerate(movements):
    if movement not in "^>v<":
        continue
    dx, dy = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}[movement]

    if dy == 0:
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
            # print("\n" * 5)
            # print(idx, f"Move: {movement}")
            # for row in warehouse:
            #     print("".join(row).replace(".", "-"))
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
        # print("\n" * 5)
        # print(idx, f"Move: {movement}")
        # for row in warehouse:
        #     print("".join(row).replace(".", "-"))

    else:
        # uh oh spaghetti code for checking moving multiple boxes
        box_lefts = []
        box_rights = []
        check_xs = [robot_x]
        check_y = robot_y
        can_move = True

        # what is this control flow
        last_row_explored = False
        while not last_row_explored:
            check_y += dy
            last_row_explored = True

            new_check_xs = check_xs[:]

            for check_x in check_xs:
                if warehouse[check_y][check_x] == "#":
                    can_move = False
                    last_row_explored = True
                    break

                elif warehouse[check_y][check_x] == "[":
                    box_lefts.append((check_x, check_y))
                    box_rights.append((check_x + 1, check_y))
                    new_check_xs.append(check_x + 1)
                    last_row_explored = False

                elif warehouse[check_y][check_x] == "]":
                    box_lefts.append((check_x - 1, check_y))
                    box_rights.append((check_x, check_y))
                    new_check_xs.append(check_x - 1)
                    last_row_explored = False

                else:
                    # if it is empty, do not check on the next row.
                    # this took an hour of debugging to find
                    new_check_xs.remove(check_x)

            check_xs = list(set(new_check_xs))
            if last_row_explored:
                break

        if not can_move:
            # print("\n" * 5)
            # print(idx, f"Move: {movement}")
            # for row in warehouse:
            #     print("".join(row).replace(".", "-"))
            continue

        box_lefts = list(set(box_lefts))
        box_rights = list(set(box_rights))

        for box_left in box_lefts:
            x, y = box_left
            warehouse[y][x] = "."
        for box_right in box_rights:
            x, y = box_right
            warehouse[y][x] = "."
        for box_left in box_lefts:
            x, y = box_left
            y += dy
            warehouse[y][x] = "["
        for box_right in box_rights:
            x, y = box_right
            y += dy
            warehouse[y][x] = "]"

        warehouse[robot_y][robot_x] = "."
        warehouse[robot_y + dy][robot_x] = "@"
        robot_x += dx
        robot_y += dy
        # print("\n" * 5)
        # print(idx, f"Move: {movement}")
        # for row in warehouse:
        #     print("".join(row).replace(".", "-"))


s = 0
for ridx, row in enumerate(warehouse):
    for cidx, char in enumerate(row):
        if char == "[":
            s += ridx * 100 + cidx

print(s)
