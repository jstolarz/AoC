from collections import defaultdict

walls = []
track = []
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


with open("input") as f:
    lines = f.read().splitlines()
    size = (len(lines[0]), len(lines))
    for j, line in enumerate(lines):
        for i, s in enumerate(line):
            if s == "#":
                walls.append((i, j))
            elif s == ".":
                track.append((i, j))
            elif s == "S":
                start_positon = (i, j)
            elif s == "E":
                end_positon = (i, j)


def sort_track(track, start_positon, end_positon):
    sorted_track = [start_positon]
    current = start_positon
    while current != end_positon:
        for direction in DIRECTIONS:
            new_position = (current[0] + direction[0], current[1] + direction[1])
            if (
                new_position in track and new_position not in sorted_track
            ) or new_position == end_positon:
                sorted_track.append(new_position)
                current = new_position
                break
        else:
            break
    return sorted_track


def search_cheat(position, sorted_track):
    cheats = []
    for direction in DIRECTIONS:
        new_position = (position[0] + direction[0], position[1] + direction[1])
        if new_position in walls:
            for direction2 in DIRECTIONS:
                new_position2 = (
                    new_position[0] + direction2[0],
                    new_position[1] + direction2[1],
                )
                if new_position2 != position and new_position2 in sorted_track:
                    cheats.append(
                        sorted_track.index(new_position2)
                        - sorted_track.index(position)
                        - 2
                    )
    return cheats


count = defaultdict(int)

pat = sort_track(track, start_positon, end_positon)
print(search_cheat((7, 1), pat))
for position in pat:
    for result in search_cheat(position, pat):
        if result > 0:
            count[result] += 1

print(sort_track(track, start_positon, end_positon))
print(end_positon)
print(count)

c = 0
for k, v in count.items():
    if k >= 100:
        c += v
print(c)
