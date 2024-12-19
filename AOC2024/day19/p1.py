with open("input") as f:
    data = f.read().splitlines()
    patterns = data[0].split(", ")
    designs = data[2:]
    patterns.sort(key=len, reverse=True)


def can_form_design(design, towel_patterns):
    queue = [design]
    seen = set()

    while queue:
        current = queue.pop(0)

        if current == "":
            return True

        if current in seen:
            continue
        seen.add(current)

        for pattern in towel_patterns:
            if current.startswith(pattern):
                queue.append(current[len(pattern) :])

    return False


cache = {}


def count_form_design(design, towel_patterns, cache=cache):
    count = 0

    if design == "":
        return 1
    if design in cache:
        return cache[design]

    for pattern in towel_patterns:
        if design.startswith(pattern):
            count += count_form_design(design[len(pattern) :], towel_patterns)

    cache[design] = count
    return count


possible_count = 0
all_count = 0

for i, design in enumerate(designs):
    if can_form_design(design, patterns):
        possible_count += 1
        all_count += count_form_design(design, patterns)
        if i == 4:
            print(cache)
print(possible_count)
print(all_count)
