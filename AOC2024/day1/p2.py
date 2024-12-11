from collections import Counter

left_list = []
right_list = []

with open("input1") as f:
    for line in f:
        l_value, r_value = line.split()
        left_list.append(int(l_value))
        right_list.append(int(r_value))

count = Counter(right_list)
print(sum(value*count[value] for value in left_list))