import functools

with open("input.txt") as file:
    sections = [x.strip() for x in file.read().split("\n\n") if x.strip()]

patterns = [x.strip() for x in sections[0].strip().split(",")]
designs = [x.strip() for x in sections[1].strip().split("\n")]


@functools.cache
def solve(_design: str):
    if not _design:
        return 1

    ways = 0
    for pattern in patterns:
        if _design.startswith(pattern):
            ways += solve(_design[len(pattern):])
    return ways


s = 0
for design in designs:
    s += solve(design)
print(s)
