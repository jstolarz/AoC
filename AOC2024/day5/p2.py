with open("input") as f:
    f = f.readlines()
    rules = [tuple(int(x) for x in line.split("|")) for line in f if "|" in line]
    updates = [tuple(int(x) for x in line.split(",")) for line in f if "," in line]

def get_rules(rules: list[tuple[int]], number: int) -> list[tuple[int]]:
    return [rule for rule in rules if rule[1] == number]

def is_correctly_ordered(update):
    its_ok = True
    for i, x in enumerate(update):
        r = (r[0] for r in get_rules(rules, x))
        its_ok = not bool(set(update[i + 1 :]) & set(r))
        if not its_ok:
            break
    return its_ok

wrong_ordered_updates = []
for update in updates:
    if not is_correctly_ordered(update):
        wrong_ordered_updates.append(update)
better = []

for update in wrong_ordered_updates:
    update = list(update)
    f = True
    while f:
        for i, x in enumerate(update):
            r = (r[0] for r in get_rules(rules, x))
            common_part = set(update[i + 1 :]) & set(r)
            if common_part:
                for c in common_part:
                    update.remove(c)
                update = update[:i] + list(common_part) + update[i:]
            if is_correctly_ordered(update):
                better.append(update)
                f = False
                break



print(sum(x[(len(x) - 1) // 2] for x in better))
