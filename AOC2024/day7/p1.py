from itertools import product

data = []
with open("input") as f:
    for line in f.read().splitlines():
        key, values = line.split(":")
        data.append((int(key), [int(x) for x in values.split()]))


def evaluate_expression(values, operators):
    result = values[0]
    for i, operator in enumerate(operators):
        if operator == "+":
            result += values[i + 1]
        else:
            result *= values[i + 1]
    return result


sum = 0

for test_value, values in data:
    for per in list(product(["+", "*"], repeat=len(values) - 1)):
        if evaluate_expression(values, per) == test_value:
            sum += test_value
            break
print(sum)
