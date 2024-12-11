with open("input") as f:
    stones = [int(i) for i in f.read().split()]
    
BLINKS = 25

for i in range(BLINKS):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif (l:=len(str(stone))) % 2 ==0:
            left, right = str(stone)[:l//2], str(stone)[l//2:]
            new_stones.extend([int(left), int(right)])
        else:
            new_stones.append(stone*2024)
    stones = new_stones

print(len(stones))
