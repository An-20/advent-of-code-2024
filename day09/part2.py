from utils.sortedcontainers import SortedList


with open("input.txt") as file:
    data = file.read().strip()


layout = []
files = []
holes = SortedList()
is_file = True
last_file_id = 0
for char in data:
    if is_file:
        file_len = int(char)
        if file_len:
            files.append((len(layout), file_len, last_file_id))
        layout.extend(file_len * [last_file_id])
        last_file_id += 1
    else:
        hole_len = int(char)
        if hole_len:
            holes.add((len(layout), hole_len))
        layout.extend(hole_len * [None])
    is_file = not is_file


defragmented = layout[:]
for file in reversed(files):
    file_idx, file_len, file_id = file
    for hole in holes:
        hole_idx, hole_len = hole
        if hole_len >= file_len and hole_idx < file_idx:
            holes.remove(hole)

            # create new hole if needed
            if hole_len > file_len:
                holes.add((hole_idx + file_len, hole_len - file_len))

            for idx in range(hole_idx, hole_idx+file_len):
                defragmented[idx] = file_id
            for idx in range(file_idx, file_idx+file_len):
                defragmented[idx] = None
            break


s = 0
for idx, val in enumerate(defragmented):
    if val:
        s += idx * val
print(s)
