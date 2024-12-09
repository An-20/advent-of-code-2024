with open("input.txt") as file:
    data = file.read().strip()


layout = []
is_file = True
last_file_id = 0
for char in data:
    if is_file:
        layout.extend(int(char) * [last_file_id])
        last_file_id += 1
    else:
        layout.extend(int(char) * [None])
    is_file = not is_file


defragmented = layout[:]
lo = 0
hi = len(layout) - 1
while lo < hi:
    datum = layout.pop()
    hi -= 1
    if datum is None:
        continue

    while defragmented[lo] is not None:
        lo += 1
        if lo >= hi:
            break

    defragmented[lo] = datum
defragmented = defragmented[:lo + 1]


s = 0
for idx, val in enumerate(defragmented):
    s += idx * val
print(s)
