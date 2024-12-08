#!/usr/bin/python3

import math
import re
import sys

INPUT_FILE="in/" + sys.argv[0].split('/')[1].split('.')[0] + ".in"

with open(INPUT_FILE) as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = data[i].strip()

map = []
antenas = {}
for i in range(len(data)):
    tmp = []
    for j in range(len(data[i])):
        tmp.append(data[i][j])
        if data[i][j] != '.':
            if not data[i][j] in antenas:
                antenas[data[i][j]] = []
            antenas[data[i][j]].append((i,j))
    map.append(tmp)

def valid(p):
    return (p[0] >= 0 and p[0] < len(map)) and (p[1] >= 0 and p[1] < len(map[0]))

def solve1():
    visi = {}
    for key in antenas:
        for i in range(len(antenas[key])-1):
            for j in range(i+1,len(antenas[key])):
                if i == j:
                    continue
                (a1, a2) = (antenas[key][i], antenas[key][j])
                d = (a1[0]-a2[0], a1[1]-a2[1])

                p1 = (a1[0] + d[0], a1[1] + d[1])
                p2 = (a2[0] + d[0], a2[1] + d[1])
                p3 = (a1[0] - d[0], a1[1] - d[1])
                p4 = (a2[0] - d[0], a2[1] - d[1])

                if valid(p1) and p1 != a2:
                    visi[p1] = True

                if valid(p2) and p2!= a1:
                    visi[p2] = True

                if valid(p3) and p3 != a2:
                    visi[p3] = True

                if valid(p4) and p4 != a1:
                    visi[p4] = True

    print(f"First result: {len(visi)}")

def solve2():
    visi = {}
    for key in antenas:
        for i in range(len(antenas[key])-1):
            for j in range(i+1,len(antenas[key])):
                if i == j:
                    continue
                (a1, a2) = (antenas[key][i], antenas[key][j])
                d = (a1[0]-a2[0], a1[1]-a2[1])

                p1 = (a1[0] - d[0], a1[1] - d[1])
                p2 = (a2[0] + d[0], a2[1] + d[1])

                while valid(p1):
                    visi[p1] = True
                    p1 = (p1[0] - d[0], p1[1] - d[1])


                while valid(p2):
                    visi[p2] = True
                    p2 = (p2[0] + d[0], p2[1] + d[1])


    print(f"Second result: {len(visi)}")

def print_map(visi):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if (i,j) in visi and map[i][j] == '.':
                print('#', end='')
            else:
                print(map[i][j], end='')

        print()

solve1()
solve2()
