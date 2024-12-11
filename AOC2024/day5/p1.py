with open("input_test") as f:
    f = f.readlines()
    rules = [tuple(int(x) for x in line.split("|")) for line in f if "|" in line]
    updates = [tuple(int(x) for x in line.split(",")) for line in f if "," in line]

def get_rules(rules: list[tuple[int]], number: int) -> list[tuple[int]]:
    return [rule for rule in rules if rule[1] == number]


right_ordered_updates = []
for update in updates:
    its_ok = True
    for i, x in enumerate(update):
        r = (r[0] for r in get_rules(rules, x))
        its_ok = not bool(set(update[i + 1 :]) & set(r))
        if not its_ok:
            break
    if its_ok:
        right_ordered_updates.append(update)

print(sum(x[(len(x) - 1) // 2] for x in right_ordered_updates))
