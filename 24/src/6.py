#!/usr/bin/python3

import math
import re
import sys

INPUT_FILE="in/" + sys.argv[0].split('/')[1].split('.')[0] + ".in"

with open(INPUT_FILE) as f:
    data = f.readlines()



G = [[c for c in line.strip()] for line in data]
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '^':
            start_pos = (i,j)

next_facing = {
    (-1,0): (0,1),
    (0,1): (1,0),
    (1,0): (0,-1),
    (0,-1): (-1,0),
}
def valid(position):
    return (position[0] >= 0 and position[0] < len(data)) and (position[1] >= 0 and position[1] < len(data[0]))

visi_v1 = {}
def walk_v1(data, position, facing):
    acc = 0

    while valid(position):
        next_pos = (position[0]+facing[0], position[1]+facing[1])
        visi_idx = position

        val = 1
        if visi_idx in visi_v1:
            val = 0

        visi_v1[visi_idx] = True

        while valid(next_pos) and data[next_pos[0]][next_pos[1]] == '#':
            facing = next_facing[facing]
            next_pos = (position[0]+facing[0], position[1]+facing[1])

        acc += val
        position = next_pos

    return acc

def solve1():
    acc = walk_v1(data, start_pos, facing=(-1,0))

    print(f"First result: {acc}")

def hasLoop(data_2, position, facing):
    visi_2 = {}
    while valid(position):
        next_pos = (position[0]+facing[0], position[1]+facing[1])
        visi_idx = (position,facing)

        if visi_idx in visi_2:
            return True

        visi_2[visi_idx] = True

        while valid(next_pos) and data_2[next_pos[0]][next_pos[1]] == '#':
            facing = next_facing[facing]
            next_pos = (position[0]+facing[0], position[1]+facing[1])

        position = next_pos

    return False


def solve2():
    acc = 0
    
    data_copy = []
    for i in range(len(data)):
        line = []
        for j in range(len(data[i])):
            line.append(data[i][j])
        data_copy.append(line)

    junk = []

    for key in visi_v1:
        if key == start_pos:
            continue
        data_copy[key[0]][key[1]] = '#'

        if hasLoop(data_copy, start_pos, facing=(-1,0)):
            junk.append(key)
            acc += 1

        data_copy[key[0]][key[1]] = '.'

    print(f"Second result: {acc}")

solve1()
solve2()
