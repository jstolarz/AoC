import re
from math import prod

SIZE_X = 101
SIZE_Y = 103
# SIZE_X = 11
# SIZE_Y = 7


class Robot:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def __repr__(self):
        return f"p={self.x},{self.y} v={self.vx},{self.vy}"

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x < 0:
            self.x = SIZE_X + self.x
        if self.x >= SIZE_X:
            self.x = self.x - SIZE_X
        if self.y < 0:
            self.y = SIZE_Y + self.y
        if self.y >= SIZE_Y:
            self.y = self.y - SIZE_Y


def parse_input(input):
    robots = []
    for line in input:
        x, y, vx, vy = map(int, re.findall(r"-?\d+", line))
        robots.append(Robot(x, y, vx, vy))
    return robots


def count_quadrants(robots: list[Robot]):
    quadrants = {}
    for robot in robots:
        if robot.x < SIZE_X // 2:
            if robot.y < SIZE_Y // 2:
                quadrants[1] = quadrants.get(1, 0) + 1
            elif robot.y > SIZE_Y // 2:
                quadrants[3] = quadrants.get(3, 0) + 1
        elif robot.x > SIZE_X // 2:
            if robot.y < SIZE_Y // 2:
                quadrants[2] = quadrants.get(2, 0) + 1
            elif robot.y > SIZE_Y // 2:
                quadrants[4] = quadrants.get(4, 0) + 1
    return quadrants


def draw_robots(robots: list[Robot]):
    pos = [(r.x, r.y) for r in robots]
    lines = []
    for i in range(SIZE_Y):
        line = ""
        for j in range(SIZE_X):
            c = len([x for x, y in pos if x == j and y == i])
            line += str(c) + " " if c else "0 "
        lines.append(line)

    with open(f"pic/output{z+1}", "w") as f:
        f.write("P1\n")
        f.write(f"{SIZE_X} {SIZE_Y}\n")
        f.write("\n".join(lines))


with open("input") as f:
    robots: list[Robot] = parse_input(f.read().splitlines())

a = [x * 101 + 10 for x in range(100)]
b = [x * 103 + 70 for x in range(100)]

for z in range(8000):
    for robot in robots:
        robot.move()
    if z + 1 in a or z + 1 in b:
        draw_robots(robots)


print("Part 1: ", prod(count_quadrants(robots).values()))

for i in a:
    if i in b:
        print("Part 2: ", i)
