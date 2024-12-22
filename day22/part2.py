with open("input.txt") as file:
    INPUT_DATA = [x.strip() for x in file.readlines() if x.strip()]


def get_next_number(num: int):
    num = (num ^ (num * 64)) % 16777216
    num = (num ^ (num // 32)) % 16777216
    num = (num ^ (num * 2048)) % 16777216
    return num


values = {}
for bidx, datum in enumerate(INPUT_DATA):
    number = int(datum)
    prices = [number % 10]
    for _ in range(2000):
        number = get_next_number(number)
        prices.append(number % 10)
    deltas = [prices[i+1] - prices[i] for i in range(2000)]

    for i in range(1996):
        a, b, c, d = deltas[i], deltas[i + 1], deltas[i + 2], deltas[i + 3]
        if (a, b, c, d) not in values:
            values[(a, b, c, d)] = {bidx: prices[i + 4]}
        elif bidx not in values[(a, b, c, d)]:
            values[(a, b, c, d)][bidx] = prices[i + 4]

print(max(sum(x.values()) for x in values.values()))
