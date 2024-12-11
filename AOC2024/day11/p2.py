from collections import defaultdict

with open("input") as f:
    stones = [int(i) for i in f.read().split()]
    
BLINKS = 75
stone_counts = defaultdict(int)
for stone in stones:
    stone_counts[stone] += 1

for i in range(BLINKS):
    print(i)
    new_stones_count = defaultdict(int)
    for stone, count in stone_counts.items():
        if stone == 0:
            new_stones_count[1] += count
        elif (l:=len(str(stone))) % 2 ==0:
            left, right = str(stone)[:l//2], str(stone)[l//2:]
            new_stones_count[int(left)] += count
            new_stones_count[int(right)] += count
        else:
            new_stones_count[stone*2024] += count
    stone_counts = new_stones_count

print(sum(stone_counts.values()))

