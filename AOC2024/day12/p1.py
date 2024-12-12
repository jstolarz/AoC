with open("input") as f:
    map = f.read().splitlines()

groups = []

def find_group(groups, position):
    for group in groups:
        if position in group:
            return group
    return None

def merge_groups(groups, group1, group2):
    if group1 != group2:
        group1.update(group2)
        groups.remove(group2)

def calculate_perimeter(group):
    perimeter = 0
    for position in group:
        i, j = position
        if i == 0 or (i > 0 and (i-1, j) not in group):
            perimeter += 1
        if i == len(map) - 1 or (i < len(map) - 1 and (i+1, j) not in group):
            perimeter += 1
        if j == 0 or (j > 0 and (i, j-1) not in group):
            perimeter += 1
        if j == len(map[i]) - 1 or (j < len(map[i]) - 1 and (i, j+1) not in group):
            perimeter += 1
    return perimeter

for i, line in enumerate(map):
    for j, label in enumerate(line):
        current_position = (i, j)
        neighbors = []
        if i > 0 and map[i-1][j] == label:
            neighbors.append((i-1, j))
        if i < len(map) - 1 and map[i+1][j] == label:
            neighbors.append((i+1, j))
        if j > 0 and map[i][j-1] == label:
            neighbors.append((i, j-1))
        if j < len(line) - 1 and map[i][j+1] == label:
            neighbors.append((i, j+1))

        neighbor_groups = [find_group(groups, neighbor) for neighbor in neighbors]
        neighbor_groups = [group for group in neighbor_groups if group]

        if not neighbor_groups:
            groups.append(set([current_position]))
        else:
            current_group = neighbor_groups[0]
            current_group.add(current_position)
            for neighbor_group in neighbor_groups:
                merge_groups(groups, current_group, neighbor_group)


def calculate_sides(group):
    if len(group) <= 2:
        return 4
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    no_corners = 0
    for position in group:
        i, j = position
        for neighbor in [(i + d[0], j + d[1]) for d in directions]:
            if neighbor not in group:
                continue
            for d in directions:
                if (i+d[0], j+d[1]) not in group and (neighbor[0] + d[0], neighbor[1] + d[1]) not in group:
                    no_corners += 1
        
    return calculate_perimeter(group) - no_corners//2


print(sum([len(g)*calculate_perimeter(g) for g in groups]))

print(sum([len(g)*calculate_sides(g) for g in groups]))
