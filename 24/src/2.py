#!/usr/bin/python3

import math
import sys

INPUT_FILE="in/" + sys.argv[0].split('/')[1].split('.')[0] + ".in"

with open(INPUT_FILE) as f:
    data = f.readlines()


levels = []
for line in data:
    levels.append([int(i) for i in ' '.join(line.strip().split()).split(' ')])

print(data)

def is_safe(level):
    if abs(level[1] - level[0]) == 0:
        return False
    
    direction = (level[1] - level[0])/abs(level[1] - level[0])
    for e in range(1,len(level)):
        gap = abs(level[e] - level[e-1])
        if not ((gap in range(1,4)) and (direction == (level[e] - level[e-1])/gap)):
            return False
    
    return True

def solve1():
    acc = 0
    for level in levels:
        safe = is_safe(level)
        if safe:
            acc += 1

    print(f"First result: {acc}")

def solve2():
    acc = 0
    for level in levels:
        safe = is_safe(level)

        if not safe:
            for i in range(len(level)):
                safe = safe or is_safe(level[0:i] + level[i+1:])

        if safe:
            acc += 1


    print(f"Second result: {acc}")

solve1()
solve2()
