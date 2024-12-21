# Numeric keypad
# 7 8 9
# 4 5 6
# 1 2 3
#   0 A
from functools import cache

A = "A"
numeric_keypad = {
    "7": (0, 0), "8": (1, 0), "9": (2, 0),
    "4": (0, 1), "5": (1, 1), "6": (2, 1),
    "1": (0, 2), "2": (1, 2), "3": (2, 2),
    "0": (1, 3), A: (2, 3)
}


# Directional keypad
#   ^ A
# < v >
directional_keypad = {"^": (1, 0), "A": (2, 0), "<": (0, 1), "v": (1, 1), ">": (2, 1)}


class Node:
    def __init__(self, position, direction, g, h, came_from=None):
        self.position = position
        self.direction = direction  # > < ^ v
        self.g = g
        self.h = h
        self.f = g + h
        self.came_from = came_from
    def __repr__(self):
        return f"Node({self.position}, {self.direction}, {self.g}, {self.h}, {self.f})"


with open(0) as f:
    lines = f.read().splitlines()

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
    return path[::-1]


def path_to_moves(path):
    moves = ""
    for p in path[1:]:
        moves += p.direction
    return moves

def a_star2(start, goal, positions):
    result = []
    open_list = [
        Node(start, None, 0, abs(start[0] - goal[0]) + abs(start[1] - goal[1]), None)
    ]
    closed_list = {}

    i = 0
    while open_list:
        i += 1
        current = min(open_list, key=lambda x: x.f)
        open_list.remove(current)
        closed_list[(current.position, current.direction)] = current.g
        if current.position == goal:
            if not result or current.f <= result[-1].f:
                result.append(current)
            continue
        for direction in [">", "<", "^", "v"]:
            new_position = get_new_position(direction, current.position)
            if new_position not in positions:
                continue
            g = current.g + 1 + (0 if current.direction is None or (direction == current.direction) else 1000)
            if (new_position, direction) in closed_list:
                if closed_list[(new_position, direction)] < g:
                    continue
            h = abs(new_position[0] - goal[0]) + abs(new_position[1] - goal[1])
            open_list.append(Node(new_position, direction, g, h, current))
    return result

def get_moves_from_keypad(seq, keypad):
    moves = [""]
    pos = keypad[A]

    for key in seq:
        new_moves = []
        for n in a_star2(pos, keypad[key], keypad.values()):
            m = path_to_moves(reconstruct_path(n))
            for i in moves:
                new_moves.append(i + m + "A")
        moves = new_moves
        pos = keypad[key]
    return moves

complexity = 0
for line in lines:
    seqs = get_moves_from_keypad(line, numeric_keypad)
    for i in range(2):
        seqs2 = []
        for seq in seqs:
            seqs2.extend(get_moves_from_keypad(seq, directional_keypad))
        seqs = seqs2

    complexity += min(len(seq) for seq in seqs)*int(line[:-1])
print(complexity)
