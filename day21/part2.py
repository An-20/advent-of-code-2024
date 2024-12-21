import functools

with open("input.txt") as file:
    data = [x.strip() for x in file.read().split("\n") if x.strip()]


NUMERIC_KEYPAD = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["", "0", "A"]]
DIRECTIONAL_KEYPAD = [["", "^", "A"], ["<", "v", ">"]]


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
        necessary_moves += (">" * abs(dx)) if dx > 0 else ("<" * abs(dx))
        necessary_moves += ("v" * abs(dy)) if dy > 0 else ("^" * abs(dy))

        new_possible = []
        #for m in set(itertools.permutations(necessary_moves)):
        if not dx or not dy:
            to_check = (necessary_moves,)
        else:
            to_check = (necessary_moves, list(reversed(necessary_moves)))
        for m in to_check:
            # check that it never points an empty gap
            works = True
            cx, cy = x, y
            for move in m:
                dx, dy = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}[move]
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


@functools.lru_cache()
def optimal_transition_len(a: str, b: str, depth: int):# -> tuple[int, str]:
    ax, ay = get_xy(DIRECTIONAL_KEYPAD, a)
    bx, by = get_xy(DIRECTIONAL_KEYPAD, b)
    if depth == 0:
        return 1#, a

    dx = bx - ax
    dy = by - ay

    necessary_moves = []
    necessary_moves += (">" * abs(dx)) if dx > 0 else ("<" * abs(dx))
    necessary_moves += ("v" * abs(dy)) if dy > 0 else ("^" * abs(dy))

    to_check = (necessary_moves, list(reversed(necessary_moves)))
    working = []
    for m in to_check:
        # check that it never points an empty gap
        works = True
        cx, cy = ax, ay
        for move in m:
            dx, dy = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}[move]
            cx += dx
            cy += dy
            if not DIRECTIONAL_KEYPAD[cy][cx]:
                works = False
                break
        if not works:
            continue
        working.append(m)
    minimum = float("inf")
    #mval = ''
    for m in working:
        m = ["A"] + m + ["A"]
        s = 0
        # print(depth, m)
        for i in range(len(m) - 1):
            s += optimal_transition_len(m[i], m[i+1], depth - 1)#[0]
        if s < minimum:
            minimum = s
            #mval = "".join([optimal_transition_len(m[i], m[i+1], depth - 1)[1] for i in range(len(m)-1)])
    return minimum#, mval


s = 0
for code in data:
    m = float("inf")
    for a in get_numeric_moves(code):
        a = "A" + a
        v = sum(optimal_transition_len(a[i], a[i + 1], 25) for i in range(len(a) - 1)) * int(code[:-1])
        if v < m:
            m = v
        # s += sum(optimal_transition_len(a[i], a[i + 1], 2)[0] for i in range(len(a) - 1)) * int(code[:-1])
        # print(sum(optimal_transition_len(a[i], a[i + 1], 25)[0] for i in range(len(a) - 1)), int(code[:-1]))
        # print("".join([optimal_transition_len(a[i], a[i + 1], 25)[1] for i in range(len(a) - 1)]))
    s += m
print(s)


def test(x):
    a = "A" + x
    print(sum(optimal_transition_len(a[i], a[i + 1], 1)[0] for i in range(len(a) - 1)))
    print("".join([optimal_transition_len(a[i], a[i + 1], 1)[1] for i in range(len(a) - 1)]))


# a[0] = "A" + a[0]
# sum(optimal_transition_len(a[0][i], a[0][i + 1], 25) for i in range(len(a[0]) - 1))
#print("".join(optimal_transition_len(a[0][i], a[0][i + 1], 2)[1] for i in range(len(a[0]) - 1)))