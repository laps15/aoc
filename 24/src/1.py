#!/usr/bin/python3

import math
import sys

INPUT_FILE="in/" + sys.argv[0].split('/')[1].split('.')[0] + ".in"

with open(INPUT_FILE) as f:
    data = f.readlines()


first, second = [], []
for line in data:
    [a,b] = ' '.join(line.strip().split()).split(' ')
    first.append(int(a))
    second.append(int(b))

first.sort()
second.sort()

def solve1():
    acc = 0
    for idx in range(len(first)):
        acc += abs(first[idx] - second[idx])

    print(f"First result: {acc}")

def solve2():
    acc = 0
    lut = {i:second.count(i) for i in first}
    for i in first:
        acc += i * lut[i]

    print(f"Second result: {acc}")

solve1()
solve2()
