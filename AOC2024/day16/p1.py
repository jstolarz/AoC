# flake8: noqa: E501

walls = []


class Node:
    def __init__(self, position, direction, g, h, came_from=None):
        self.position = position
        self.direction = direction  # > < ^ v
        self.g = g
        self.h = h
        self.f = g + h
        self.came_from = came_from


with open("input") as f:
    lines = f.read().splitlines()
    size = (len(lines[0]), len(lines))
    for j, line in enumerate(lines):
        for i, s in enumerate(line):
            if s == "#":
                walls.append((i, j))
            elif s == "S":
                start_positon = (i, j)
            elif s == "E":
                end_positon = (i, j)


def get_new_position(move: str, positon: tuple[int]):
    x, y = positon
    if move == "^":
        return x, y - 1
    elif move == "v":
        return x, y + 1
    elif move == "<":
        return x - 1, y
    elif move == ">":
        return x + 1, y


def reconstruct_path(node):
    path = []
    while node:
        path.append(node)
        node = node.came_from
    return path


def a_star(start, goal, walls):
    open_list = [Node(start, ">", 0, abs(start[0] - goal[0]) + abs(start[1] - goal[1]))]
    closed_list = []
    while open_list:
        current = min(open_list, key=lambda x: x.f)
        open_list.remove(current)
        closed_list.append(current)
        if current.position == goal:
            return current
        for direction in [">", "<", "^", "v"]:
            new_position = get_new_position(direction, current.position)
            if new_position in walls:
                continue
            if any(node.position == new_position for node in closed_list):
                continue
            g = current.g + 1 + (0 if direction == current.direction else 1000)
            h = abs(new_position[0] - goal[0]) + abs(new_position[1] - goal[1])
            f = g + h
            if any(node.position == new_position and node.f > f for node in open_list):
                continue
            open_list.append(Node(new_position, direction, g, h, current))
    return None


r = a_star(start_positon, end_positon, walls)
path = reconstruct_path(r)
points = 0
for p in path:
    points += 1
    if p.came_from and p.direction != p.came_from.direction:
        points += 1000
print(points - 1)


for j in range(size[1]):
    for i in range(size[0]):
        if (i, j) in walls:
            print("#", end="")
        elif (i, j) == start_positon:
            print("S", end="")
        elif (i, j) == end_positon:
            print("E", end="")
        elif any(node.position == (i, j) for node in path):
            print([p.direction for p in path if p.position == (i, j)][0], end="")
        else:
            print(".", end="")
    print()
