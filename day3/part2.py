with open("input.txt") as file:
    f = file.read().strip()
to_process = list(reversed(f))


s = 0

state = 0
buf_a = None
buf_b = None
en = True

while True:
    if not to_process:
        break
    char = to_process.pop()
    print(char, state)

    if state == 1:
        if char == "u":
            state = 2
            continue

    elif state == 2:
        if char == "l":
            state = 3
            continue

    elif state == 3:
        if char == "(":
            state = 4
            continue

    elif state == 4:
        if char.isdigit():
            buf_a = char
            state = 5
            continue

    elif state == 5:
        if char.isdigit():
            buf_a += char
            continue
        elif char == ",":
            state = 6
            continue

    elif state == 6:
        if char.isdigit():
            buf_b = char
            state = 7
            continue

    elif state == 7:
        if char.isdigit():
            buf_b += char
            continue
        elif char == ")":
            state = 0
            if en:
                s += int(buf_a) * int(buf_b)
            continue

    elif state == 8:
        if char == "o":
            state = 9
            continue

    elif state == 9:
        if char == "(":
            state = 10
            continue
        elif char == "n":
            state = 11
            continue

    elif state == 10:
        if char == ")":
            en = True
            state = 0
            continue

    elif state == 11:
        if char == "'":
            state = 12
            continue

    elif state == 12:
        if char == "t":
            state = 13
            continue

    elif state == 13:
        if char == "(":
            state = 14
            continue

    elif state == 14:
        if char == ")":
            en = False
            state = 0
            continue

    # automatically reset state back to 0
    state = 0
    if char == "m":
        state = 1
        continue
    elif char == "d":
        state = 8
        continue


print(s)
