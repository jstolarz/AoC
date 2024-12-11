from itertools import cycle

DIR = cycle(((-1, 0), (0, 1), (1, 0), (0, -1)))  # ^(-1,0) v(1,0) <(0,-1) >(0,1)

with open("input") as f:
    map = f.read().splitlines()

for i, line in enumerate(map):
    x = line.find("^")
    if x >= 0:
        break
position = (i, x)
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

print(len(set(visited)))
