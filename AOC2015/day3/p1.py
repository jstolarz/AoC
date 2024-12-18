from collections import defaultdict


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


with open("input") as f:
    moves = f.read().strip()

position = (0, 0)
houses = defaultdict(int)

houses[position] += 1
for move in moves:
    position = get_new_position(move, position)
    houses[position] += 1
print(len(houses))

santa_position = (0, 0)
robo_position = (0, 0)
houses = defaultdict(int)

houses[robo_position] += 1
for i, move in enumerate(moves):
    if i % 2 == 0:
        santa_position = get_new_position(move, santa_position)
        houses[santa_position] += 1
    else:
        robo_position = get_new_position(move, robo_position)
        houses[robo_position] += 1


print(len(houses))
