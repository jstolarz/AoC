from math import prod

with open("input") as f:
    boxes = [tuple(int(d) for d in line.split("x")) for line in f.read().splitlines()]

paper = 0
ribon = 0
for box in boxes:
    sides = (box[0] * box[1], box[1] * box[2], box[0] * box[2])
    paper += 2 * sum(sides) + min(sides)
    ribon += 2 * sum(box) - 2 * max(box) + prod(box)
print(paper)
print(ribon)
