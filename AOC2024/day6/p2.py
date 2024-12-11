from itertools import cycle

DIR = cycle(((-1, 0), (0, 1), (1, 0), (0, -1)))  # ^(-1,0) v(1,0) <(0,-1) >(0,1)

with open("input") as f:
    map = f.read().splitlines()

for i, line in enumerate(map):
    x = line.find("^")
    if x >= 0:
        break
start_position = (i, x)


def get_visited_position():
    DIR = cycle(((-1, 0), (0, 1), (1, 0), (0, -1)))  # ^(-1,0) v(1,0) <(0,-1) >(0,1)

    position = start_position
    direction = next(DIR)
    visited = [position]

    while True:
        new_position = (position[0] + direction[0], position[1] + direction[1])
        if not (0 <= new_position[0] < len(map) and 0 <= new_position[1] < len(map[0])):
            break
        if map[new_position[0]][new_position[1]] == "#":
            direction = next(DIR)
        else:
            visited.append(new_position)
            position = new_position
    return visited


corect_obstacle_position = []
for obstacle_position in get_visited_position()[1:]:
    DIR = cycle(((-1, 0), (0, 1), (1, 0), (0, -1)))  # ^(-1,0) v(1,0) <(0,-1) >(0,1)

    position = start_position
    direction = next(DIR)
    visited = [(position, direction)]

    while True:
        new_position = (position[0] + direction[0], position[1] + direction[1])
        if not (0 <= new_position[0] < len(map) and 0 <= new_position[1] < len(map[0])):
            break
        if (
            map[new_position[0]][new_position[1]] == "#"
            or new_position == obstacle_position
        ):
            direction = next(DIR)
        else:
            position = new_position
        if (new_position, direction) in visited:
            corect_obstacle_position.append(obstacle_position)
            print(obstacle_position)
            break
        visited.append((new_position, direction))

print(len(set(x for x in corect_obstacle_position if x != start_position)))
