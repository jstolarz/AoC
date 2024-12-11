import re

with open("input") as f:
    s = f.read()
    x = re.findall(r"(mul\((\d*),(\d*)\))", s)
    print(x)
    sum = 0
    for i in x:
        if int(i[1]) < 10000 and int(i[2]) < 10000:
            sum += int(i[1]) * int(i[2])
    print(sum)
