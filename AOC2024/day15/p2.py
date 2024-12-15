# flake8: noqa: E501
import copy

walls: list[tuple[int]] = []
boxes = []
robot_positon: tuple[int]  # (x, y)
moves = ""  # ^v<>


class Box:
    def __init__(self, x1, x2, y):
        self.x1 = x1
        self.x2 = x2
        self.y = y

    def __repr__(self):
        return f"Box(({self.x1}, {self.x2}), {self.y})"

    def __contains__(self, item):
        return item == (self.x1, self.y) or item == (self.x2, self.y)

    def move(self, move: str):
        if move == "^":
            self.y -= 1
        elif move == "v":
            self.y += 1
        elif move == "<":
            self.x1 -= 1
            self.x2 -= 1
        elif move == ">":
            self.x1 += 1
            self.x2 += 1


with open("input") as file:
    for i, line in enumerate(file.read().splitlines()):
        if "#" not in line:
            moves += line
            continue
        for j, s in enumerate(line):
            if s == "#":
                walls.append((j * 2, i))
                walls.append((j * 2 + 1, i))
            elif s == "O":
                boxes.append(Box(j * 2, j * 2 + 1, i))
            elif s == "@":
                robot_positon = (j * 2, i)


def print_map():
    max_x = max(walls)[0]
    max_y = max(walls, key=lambda x: x[1])[1]
    lines = []
    y = 0
    while y <= max_y:
        line = ""
        x = 0
        while x <= max_x:
            if (x, y) in walls:
                line += "#"
            elif (x, y) == robot_positon:
                line += "@"
            elif any((x, y) in box for box in boxes):
                line += "[]"
                x += 1
            else:
                line += "."
            x += 1
        y += 1
        lines.append(line)
    for line in lines:
        print(line)


print_map()


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


def get_box_from_position(position: tuple[int], boxes: list[Box]):
    for box in boxes:
        if position in box:
            return box
    return None


def is_in_boxes(position: tuple[int], boxes: list[tuple[tuple[int], int]]):
    return any(position in box for box in boxes)


def move_box(move: str, robot_positon: tuple[int], boxes: list[tuple[tuple[int], int]]):
    moved_boxes = copy.deepcopy(boxes)
    boxes_to_move = [
        get_box_from_position(get_new_position(move, robot_positon), moved_boxes)
    ]
    can_move_boxes = False
    while not can_move_boxes:
        n_boxes = []
        for box in set(boxes_to_move):
            new_positions = get_new_position(move, (box.x1, box.y)), get_new_position(
                move, (box.x2, box.y)
            )
            if new_positions[0] in walls or new_positions[1] in walls:
                return robot_positon, boxes
            b1 = get_box_from_position(new_positions[0], moved_boxes)
            b2 = get_box_from_position(new_positions[1], moved_boxes)
            if b1:
                n_boxes.append(b1)
            if b2:
                n_boxes.append(b2)

        can_move_boxes = set(boxes_to_move) == set(n_boxes) | set(boxes_to_move)
        boxes_to_move += n_boxes
    for box in set(boxes_to_move):
        box.move(move)
    return get_new_position(move, robot_positon), moved_boxes


def do_move(move: str, robot_positon: tuple[int], boxes: list[Box]):
    new_position = get_new_position(move, robot_positon)
    if new_position in walls:
        return robot_positon, boxes
    if new_position not in walls and not is_in_boxes(new_position, boxes):
        return new_position, boxes
    return move_box(move, robot_positon, boxes)


for move in moves:
    robot_positon, boxes = do_move(move, robot_positon, boxes)


print(sum([100 * box.y + box.x1 for box in boxes]))
