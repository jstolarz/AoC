left_list = []
right_list = []

with open("input1") as f:
    for line in f:
        l_value, r_value = line.split()
        left_list.append(int(l_value))
        right_list.append(int(r_value))

left_list.sort()
right_list.sort()

print(sum(abs(l-r) for l, r in zip(left_list, right_list)))