# FILE_NAME = "input_test"
# READ_BYTES = 12
# SIZE = (6, 6)

FILE_NAME = "input"
READ_BYTES = 1024
SIZE = (70, 70)

walls = []


class Node:
    def __init__(self, position, g, h, came_from=None):
        self.position = position
        self.g = g
        self.h = h
        self.f = g + h
        self.came_from = came_from

    def __repr__(self):
        return f"{self.position}"


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


def is_in_bounds(position: tuple[int], size: tuple[int] = SIZE):
    x, y = position
    return 0 <= x <= size[0] and 0 <= y <= size[1]


def a_star(start, goal, walls, memory_size=SIZE):
    open_list = [Node(start, 0, abs(start[0] - goal[0]) + abs(start[1] - goal[1]))]
    closed_list: list[Node] = []
    while open_list:
        current = min(open_list, key=lambda x: x.f)
        open_list.remove(current)
        if any(node.position == current.position for node in closed_list):
            continue
        closed_list.append(current)

        if current.position == goal:
            return current
        for direction in [">", "<", "^", "v"]:
            new_position = get_new_position(direction, current.position)
            if (new_position in walls) or not is_in_bounds(new_position, memory_size):
                continue
            if any(node.position == new_position for node in closed_list):
                continue
            g = current.g + 1
            h = abs(new_position[0] - goal[0]) + abs(new_position[1] - goal[1])
            f = g + h
            if any(node.position == new_position and node.f > f for node in open_list):
                continue
            open_list.append(Node(new_position, g, h, current))
    return None


with open(FILE_NAME) as f:
    lines = f.read().splitlines()

endpoints = (READ_BYTES, len(lines))
while True:
    midpoint = (endpoints[0] + endpoints[1]) // 2
    print(midpoint)
    walls = []
    for line in lines[:midpoint]:
        walls.append(tuple(int(x) for x in line.split(",")))
    r = a_star((0, 0), SIZE, walls)

    if r:
        endpoints = (midpoint, endpoints[1])
    else:
        endpoints = (endpoints[0], midpoint)
    if endpoints[1] - endpoints[0] <= 1:
        print(endpoints)
        print(lines[endpoints[0]])
        break
