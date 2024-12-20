from collections import defaultdict

track = []
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


with open("input") as f:
    lines = f.read().splitlines()
    size = (len(lines[0]), len(lines))
    for j, line in enumerate(lines):
        for i, s in enumerate(line):
            if s == ".":
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
    distances = []
    track = [t for t in sorted_track if (abs(t[0] - position[0]) + abs(t[1] - position[1])) <= 20]
    for new_position in track:
        new_distance = abs(new_position[0] - position[0]) + abs(new_position[1] - position[1])
        distance = sorted_track.index(new_position)- sorted_track.index(position) - new_distance
        if distance > 0:
            distances.append(distance)
    return distances


count = defaultdict(int)

pat = sort_track(track, start_positon, end_positon)
print(len(pat))
for i, position in enumerate(pat):
    print(i, position)
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
