# flake8: noqa: E501

import random

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


def a_star(start, goal, walls):
    open_list = [Node(start, ">", 0, random.choice([0, 2000]))]
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
            h = (
                random.choice([0, 2000])
                + abs(new_position[0] - goal[0])
                + abs(new_position[1] - goal[1])
            )
            f = g + h
            if new_position == (2, 11):
                print(f"new_position={new_position} g={g} h={h} f={f}")
            if new_position == (1, 10):
                print(f"new_position={new_position} g={g} h={h} f={f}")
            if any(node.position == new_position and node.f > f for node in open_list):
                continue
            open_list.append(Node(new_position, direction, g, h, current))
    return None


def reconstruct_path(node):
    path = []
    while node:
        path.append(node.position)
        node = node.came_from
    return path


path = []
for i in range(10):
    r = a_star(start_positon, end_positon, walls)
    c = r.came_from
    points = 0
    while c:
        points += 1
        if c.came_from and c.direction != c.came_from.direction:
            points += 1000
        c = c.came_from
    if points == 108504:
        path.extend(reconstruct_path(r))
        print(len(set(path)))


for j in range(size[1]):
    for i in range(size[0]):
        if (i, j) in walls:
            print("#", end="")
        elif (i, j) == start_positon:
            print("S", end="")
        elif (i, j) == end_positon:
            print("E", end="")
        elif (i, j) in set(path):
            print("O", end="")
        else:
            print(".", end="")
    print()
