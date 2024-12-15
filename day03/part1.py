with open("input.txt") as file:
    f = file.read().strip()


s = 0

state = 0
buf_a = None
buf_b = None
en = False
for char in f:

    print(char, state)

    if state == 0:
        if char == "m":
            state = 1
            continue

    elif state == 1:
        if char != "u":
            state = 0
            continue
        elif char == "m":
            state = 1
        state = 2

    elif state == 2:
        if char != "l":
            state = 0
            continue
        elif char == "m":
            state = 1
        state = 3

    elif state == 3:
        if char != "(":
            state = 0
            continue
        elif char == "m":
            state = 1
        state = 4

    elif state == 4:
        if not char.isdigit():
            state = 0
            continue
        elif char == "m":
            state = 1
        state = 5
        buf_a = char

    elif state == 5:
        if not char.isdigit() and char != ",":
            state = 0
            continue
        if char.isdigit():
            buf_a += char
            continue
        elif char == "m":
            state = 1
        else:
            state = 6

    elif state == 6:
        if not char.isdigit():
            state = 0
            continue
        elif char == "m":
            state = 1
        state = 7
        buf_b = char

    elif state == 7:
        if not char.isdigit() and char != ")":
            state = 0
            continue
        if char.isdigit():
            buf_b += char
            continue
        elif char == "m":
            state = 1
        else:
            state = 8

    elif state == 8:
        s += int(buf_a) * int(buf_b)
        state = 0

        if char == "m":
            state = 1
        continue

print(s)
