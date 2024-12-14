#!/usr/bin/python3

import math
import re
import sys

INPUT_FILE="in/" + sys.argv[0].split('/')[1].split('.')[0] + ".in"

DBUG=False
LENGTH = 101
# LENGTH = 11
HEIGHT = 103
# HEIGHT = 7

with open(INPUT_FILE) as f:
    data = f.readlines()

pattern = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"

robots = []
for line in data:
    match = re.search(pattern, line, re.DOTALL)
    if match:
        robots.append((
            (int(match.group(2)), int(match.group(1))),
            (int(match.group(4)), int(match.group(3))),
        ))

def move(pos, vel):
    mod_guard = (HEIGHT * abs(vel[0]), LENGTH * abs(vel[1]))

    return ((pos[0]+vel[0]+mod_guard[0]) % HEIGHT, (pos[1]+vel[1]+mod_guard[1]) % LENGTH)

def debug_print(s, robots, should_print=True):
    if not should_print:
        return

    print(s)
    for i in range(HEIGHT):
        for j in range(LENGTH):
            count = 0
            for robot in robots:
                if robot[0][0] == i and robot[0][1] == j:
                    count += 1
            if count > 0:
                print(count, end='')
            else:
                print(' ', end='')
        print()
    print()

def solve1():
    robots_copy = robots.copy()
    for second in range(100):
        for i in range(len(robots_copy)):
            pos, vel = robots_copy[i]

            pos = move(pos, vel)

            robots_copy[i] = (pos,vel)

        debug_print(f"Iteration {second+1}", robots_copy, DBUG)

    quadrants = [[0,0],[0,0]]

    counter = [0,0]
    for i in range(HEIGHT):
        if i == int(HEIGHT/2):
            counter[0] = 1
            continue
        counter[1] = 0
        for j in range(LENGTH):
            if j == int(LENGTH/2):
                counter[1] = 1
                continue
            for robot in robots_copy:
                if robot[0][0] == i and robot[0][1] == j:
                    quadrants[counter[0]][counter[1]] += 1

    print(f"First result: {quadrants[0][0] * quadrants[0][1] * quadrants[1][0] * quadrants[1][1]}")

def solve2():
    acc = "TBD"
    robots_copy = robots.copy()

    for second in range(6669):
        for i in range(len(robots)):
            pos, vel = robots_copy[i]

            pos = move(pos, vel)

            robots_copy[i] = (pos,vel)

        if second == 6667:
            debug_print(f"Iteration {second+1}", robots_copy)

    print(f"Second result: {acc}")


solve1()
solve2()
