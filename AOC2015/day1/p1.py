with open("input") as f:
    instructions = f.read().strip()

print(sum((1 if x == "(" else -1) for x in instructions))


floor = 0
for i, inst in enumerate(instructions):
    floor += 1 if inst == "(" else -1
    if floor == -1:
        print(i + 1)
        break
