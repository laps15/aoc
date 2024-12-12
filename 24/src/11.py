#!/usr/bin/python3

import math
import re
import sys

INPUT_FILE="in/" + sys.argv[0].split('/')[1].split('.')[0] + ".in"

with open(INPUT_FILE) as f:
    data = f.readlines()

stones = [int(i) for i in data[0].strip().split()]

def upsert(d, i, v):
    if i in d:
        d[i] += v
    else:
        d[i] = v

def update_stones_dict(stones):
    result = {}
    for stone in stones:
        n_as_string = str(stone)

        if stone == 0:
            upsert(result, 1, stones[stone])
        elif not len(n_as_string) & 1:
            split = int(len(n_as_string)/2)
            left = int(n_as_string[0:split])
            right = int(n_as_string[split:])

            upsert(result, left, stones[stone])
            upsert(result, right, stones[stone])
        else:
            upsert(result, stone*2024, stones[stone])

    return result

def solve1():
    acc = 0

    stones_copy = {}
    for i in stones:
        upsert(stones_copy, i, 1)
    
    for i in range(25):
        stones_copy = update_stones_dict(stones_copy)

    for stone in stones_copy:
        acc += stones_copy[stone]
    print(f"First result: {acc}")

def solve2():
    acc = 0

    stones_copy = {}
    for i in stones:
        upsert(stones_copy, i, 1)

    for i in range(25):
        stones_copy = update_stones_dict(stones_copy)
        
    for stone in stones_copy:
        acc += stones_copy[stone]
    print(f"First result: {acc}")

    for i in range(50):
        stones_copy = update_stones_dict(stones_copy)

    acc = 0
    for stone in stones_copy:
        acc += stones_copy[stone]
    print(f"Second result: {acc}")

# solve1()
solve2()
