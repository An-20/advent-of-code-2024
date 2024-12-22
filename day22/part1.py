with open("input.txt") as file:
    INPUT_DATA = [x.strip() for x in file.readlines() if x.strip()]


def get_next_number(num: int):
    num = (num ^ (num * 64)) % 16777216
    num = (num ^ (num // 32)) % 16777216
    num = (num ^ (num * 2048)) % 16777216
    return num


s = 0
for datum in INPUT_DATA:
    number = int(datum)
    for _ in range(2000):
        number = get_next_number(number)
    s += number
print(s)
