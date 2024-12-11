import re

enable = 1
with open("input") as f:
    s = f.read()
    x = re.findall(r"(mul\((\d*),(\d*)\))|(do\(\))|(don't\(\))", s)
    print(x)
    sum = 0
    for i in x:
        if i[3] == "do()":
            enable = 1
        elif i[4] == "don't()":
            enable = 0
        elif int(i[1]) < 10000 and int(i[2]) < 10000:
            sum += int(i[1]) * int(i[2]) * enable
    print(sum)
