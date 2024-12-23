import itertools

with open("input.txt") as file:
    INPUT_DATA = [x.strip() for x in file.readlines() if x.strip()]


def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    xs = list(iterable)
    # note we return an iterator rather than a list
    return itertools.chain.from_iterable(itertools.combinations(xs,n) for n in range(len(xs)+1))


connections = {}
for row in INPUT_DATA:
    a, b = row.split("-")
    if len(a) == 1 or len(b) == 1:
        print(a, b)
    if a not in connections:
        connections[a] = {b}
    else:
        connections[a].add(b)
    if b not in connections:
        connections[b] = {a}
    else:
        connections[b].add(a)
for k in connections:
    connections[k].add(k)


# O(n 2^k) where n = number of computers, k = number of connections per computer
max_comp = 0
max_val = []
for i, a in enumerate(connections):
    bs = connections[a].copy()
    for subset in powerset(bs):
        target = set(subset)
        target.add(a)
        for b in subset:
            if connections[b].intersection(target) != target:
                break
        else:
            if len(subset) > max_comp:
                max_comp = len(subset)
                max_val = target
print(",".join(sorted(list(max_val))))
