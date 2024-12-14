#!/usr/bin/python3

import math
import re
import sys

INPUT_FILE="in/" + sys.argv[0].split('/')[1].split('.')[0] + ".in"
INF = 0x3f3f3f3f3f3f3f3f

with open(INPUT_FILE) as f:
    data = f.readlines()

pattern = r"Button ([AB]): X[+-]([0-9]+), Y[+-]([0-9]+)$|(Prize): X=([0-9]+), Y=([0-9]+)"

entry = {}
entries = []
for line in data:
    match = re.search(pattern, line, re.DOTALL)
    if match:
        print(match.groups())
        if match.group(1) is not None:
            entry[match.group(1).lower()] = (int(match.group(2)), int(match.group(3)))
        else:
            entry[match.group(4).lower()] = (int(match.group(5)), int(match.group(6)))
    else:
        entries.append(entry)
        entry = {}

entries.append(entry)

print(entries)

def apply_move(x, delta):
    return (x[0] + delta[0], x[0] + delta[0])

def pd(entry, claw):
    if claw[0] == entry['prize'][0] or claw[1] == entry['prize'][1]:
        return 0
    
    if claw[0] > entry['prize'][0] or claw[1] > entry['prize'][1]:
        return INF
    
    return min(3 + pd(entry, apply_move(claw, entry['a'])), 1 + pd(entry, apply_move(claw, entry['b'])))

def intersection(f, g):
    A1, B1, C1 = f
    A2, B2, C2 = g

    coeficients = [[A1, B1], [A2, B2]]
    constants = [-C1, -C2]

    det = A1 * B2 - A2 * B1

    if det == 0:
        return None
    
    x_num = -C1 * B2 + C2 * B1
    y_num = -A1 * C2 + A2 * C1
    
    x = x_num / det
    y = y_num / det
    
    if x.is_integer() and y.is_integer() and x > 0 and y > 0:
        return int(x), int(y)  # Return as integers

    return None
    

def solve1():
    acc = 0

    for entry in entries:
        prize, a, b = entry['prize'], entry['a'], entry['b']

        first_line = (a[0], b[0], -prize[0])
        second_line = (a[1], b[1], -prize[1])

        r = intersection(first_line, second_line)

        if r is not None:
            acc += int(3*r[0]) + int(r[1])

        print(intersection(first_line, second_line))


    print(f"First result: {acc}")

def solve2():
    acc = 0

    for entry in entries:
        prize, a, b = entry['prize'], entry['a'], entry['b']

        prize = (10000000000000 + prize[0], 10000000000000 + prize[1])

        first_line = (a[0], b[0], -prize[0])
        second_line = (a[1], b[1], -prize[1])

        r = intersection(first_line, second_line)

        if r is not None:
            acc += int(3*r[0]) + int(r[1])

        print(intersection(first_line, second_line))

    print(f"Second result: {acc}")

solve1()
solve2()
