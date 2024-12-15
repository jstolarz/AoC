walls = []
boxes = []
robot_positon: tuple[int]  # (x, y)
moves = ""  # ^v<>

with open("input") as file:
    for i, line in enumerate(file.read().splitlines()):
        if "#" not in line:
            moves += line
            continue
        for j, s in enumerate(line):
            if s == "#":
                walls.append((j, i))
            elif s == "O":
                boxes.append((j, i))
            elif s == "@":
                robot_positon = (j, i)


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


def move_box(move: str, robot_positon: tuple[int], boxes: list[tuple[int]]):
    moved_boxes = boxes[:]

    box_position = get_new_position(move, robot_positon)
    while box_position in boxes:
        next_position = get_new_position(move, box_position)
        if next_position in walls:
            return robot_positon, boxes
        moved_boxes.remove(box_position)
        moved_boxes.append(next_position)
        box_position = next_position
    return get_new_position(move, robot_positon), moved_boxes


def do_move(move: str, robot_positon: tuple[int], boxes: list[tuple[int]]):
    new_position = get_new_position(move, robot_positon)
    if new_position in walls:
        return robot_positon, boxes
    if new_position not in walls and new_position not in boxes:
        return new_position, boxes
    return move_box(move, robot_positon, boxes)


for move in moves:
    robot_positon, boxes = do_move(move, robot_positon, boxes)

print(robot_positon, boxes)
print(sum([100 * y + x for x, y in boxes]))
