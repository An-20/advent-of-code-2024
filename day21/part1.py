with open("input.txt") as file:
    data = [x.strip() for x in file.read().split("\n") if x.strip()]


NUMERIC_KEYPAD = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["", "0", "A"]]
DIRECTIONAL_KEYPAD = [["", "^", "A"], ["<", "v", ">"]]
DIRS = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}


def get_xy(keypad: list[list[str]], char: str):
    x = [x.index(char) for x in keypad if char in x][0]
    y = [y for y in range(len(keypad)) if char in keypad[y]][0]
    return x, y


def get_moves(keypad: list[list[str]], initial: tuple[int, int], target: str) -> list[str]:
    x, y = initial
    possible = [""]
    for char in target:
        tx, ty = get_xy(keypad, char)
        dx = tx - x
        dy = ty - y
        necessary_moves = []
        necessary_moves += (">" if dx > 0 else "<") * abs(dx)
        necessary_moves += ("v" if dy > 0 else "^") * abs(dy)

        new_possible = []
        if not dx or not dy:
            to_check = (necessary_moves,)
        else:
            to_check = (necessary_moves, list(reversed(necessary_moves)))
        for m in to_check:
            # check that it never points an empty gap
            works = True
            cx, cy = x, y
            for move in m:
                dx, dy = DIRS[move]
                cx += dx
                cy += dy
                if not keypad[cy][cx]:
                    works = False
                    break

            if not works:
                continue

            for p in possible:
                new_possible.append(p + "".join(m) + "A")
        possible = new_possible

        x = tx
        y = ty

    return possible


def get_numeric_moves(target: str) -> list[str]:
    return get_moves(NUMERIC_KEYPAD, (2, 3), target)


def get_directional_moves(target: str) -> list[str]:
    return get_moves(DIRECTIONAL_KEYPAD, (2, 0), target)


s = 0
for code in data:
    a = get_numeric_moves(code)
    b = []
    for av in sorted(a):
        b.extend(get_directional_moves(av))
    c = []
    for bv in sorted(b):
        c.extend(get_directional_moves(bv))
    s += min(len(x) for x in c) * int(code[:-1])
print(s)
