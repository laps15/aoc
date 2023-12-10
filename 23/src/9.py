#!/usr/bin/python3

import math
import sys

INPUT_FILE="in/" + sys.argv[0].split('/')[1] + ".in"

with open(INPUT_FILE) as f:
    raw_data = f.readlines()

print(raw_data)

data = raw_data

def done(values):
    for v in values:
        if v != 0:
            return False

    return True

def calculateHistory(history):        
    curr = [int(a) for a in history.strip().split(' ')]
    lines = [curr]

    while not done(lines[-1]):
        line = []
        prev_value = lines[-1][0]

        for current_value in lines[-1][1:]:
            line.append(current_value-prev_value)
            prev_value = current_value

        lines.append(line)

    return lines


def solve1():
    solution = 0

    for history in raw_data:
        lines = calculateHistory(history)
        lines[-1].append(0)

        previous_line = lines[-1]
        for line in lines[::-1][1:]:
            next_value = line[-1] + previous_line[-1]
            line.append(next_value)
            previous_line = line

        solution += previous_line[-1]

    print("First answer:", solution)

def solve2():
    solution = 0

    for history in raw_data:
        lines = calculateHistory(history)

        previous_line = [0] + lines[-1] + [0]
        for line in lines[::-1][1:]:

            previous_value = line[0] - previous_line[0]
            previous_line = [previous_value] + line

        solution += previous_line[0]

    print("Second answer:", solution)

solve1()
solve2()