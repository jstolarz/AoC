with open("input") as f:
    topo_map = f.read().splitlines()
trails = []
for i in range(len(topo_map)):
    for j in range(len(topo_map)):
        if topo_map[i][j] == "9":
            trails.append([(i, j)])


for x in range(8, -1, -1):
    new_trails = []
    for i in range(len(topo_map)):
        for j in range(len(topo_map)):
            if topo_map[i][j] == str(x):
                for trail in trails:
                    if trail[-1] in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        new_trails.append(trail + [(i, j)])
    trails = new_trails


sums = {}
for trail in trails:
    if trail[-1] not in sums:
        sums[trail[-1]] = [trail[0]]
    else:
        sums[trail[-1]].append(trail[0])

result = sum(len(set(v)) for v in sums.values())  # 1st part
# result = sum(len(v) for v in sums.values())  # 2nd part
print(result)
