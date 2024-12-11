from functools import cache

with open("input") as f:
    stones = [int(i) for i in f.read().split()]
    
BLINKS = 25

@cache
def blink_on_stone(stone):
    if stone == 0:
        return [1]
    elif (l:=len(str(stone))) % 2 ==0:
        left, right = str(stone)[:l//2], str(stone)[l//2:]
        return [int(left), int(right)] 
    else:
        return [stone*2024]
    

for i in range(BLINKS):
    print(i)
    new_stones = []
    for stone in stones:
        new_stones += blink_on_stone(stone)
    stones = new_stones

print(len(stones))
