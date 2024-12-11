from itertools import permutations

data = {}
with open("input") as f:
    file_content = f.read().splitlines()
    max_y = len(file_content)
    for i, line in enumerate(file_content):
        max_x = len(line)
        for j, c in enumerate(line):
            if c == ".":
                continue
            if c not in data:
                data[c] = [(i, j)]
            else:
                data[c].append((i, j))

antinodes = []
for k, v in data.items():
    for x1, x2 in permutations(v, 2):
        antinodes.append(x1)
        d = (x1[0] - x2[0], x1[1] - x2[1])
        antinode = (x1[0] + d[0], x1[1] + d[1])
        while 0 <= antinode[0] < max_y and 0 <= antinode[1] < max_x:
            antinodes.append(antinode)
            antinode = (antinode[0] + d[0], antinode[1] + d[1])

print(len(set(antinodes)))
