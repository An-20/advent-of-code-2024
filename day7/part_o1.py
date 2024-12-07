import time

from utils.silk import execute_parallel


with open("input.txt") as file:
    rows = [x.strip() for x in file.read().splitlines() if x.strip()]


def fn(row):
    import itertools
    left, data = row.split(":")
    left = int(left)
    data = [int(x.strip()) for x in data.split()]
    for ops in itertools.product(*[[0, 1, 2]] * (len(data) - 1)):
        val = data[0]
        for idx in range(len(ops)):
            if ops[idx] == 0:
                val = val + data[idx + 1]
            elif ops[idx] == 1:
                val = val * data[idx + 1]
            else:
                val = int(str(val) + str(data[idx + 1]))

        if val == left:
            return left
    return 0


ROWS = len(rows)


def main():
    out = execute_parallel(
        [fn] * ROWS, [[x] for x in rows], [{}] * ROWS
    )
    print(sum(x.obj for x in out))


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(end_time - start_time)
