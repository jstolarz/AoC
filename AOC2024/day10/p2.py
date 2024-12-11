with open("input") as f:
    topo_map = f.read().splitlines()

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

trails = []
for i in range(len(topo_map)):
    for j in range(len(topo_map)):
        if topo_map[i][j] == "9":
            trails.append([(i, j)])

for x in range(8, -1, -1):
    new_trails = []
    for trail in trails:
        i, j = trail[-1]
        for direction in DIRECTIONS:
            new_i, new_j = i + direction[0], j + direction[1]
            if (
                0 <= new_i < len(topo_map)
                and 0 <= new_j < len(topo_map)
                and topo_map[new_i][new_j] == str(x)
            ):
                new_trails.append(trail + [(new_i, new_j)])
    trails = new_trails


sums = {}
for trail in trails:
    if trail[-1] not in sums:
        sums[trail[-1]] = [trail[0]]
    else:
        sums[trail[-1]].append(trail[0])

# result = sum(len(set(v)) for v in sums.values())  # 1st part
result = sum(len(v) for v in sums.values())  # 2nd part
print(result)
