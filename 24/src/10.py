#!/usr/bin/python3

import math
import re
import sys

INPUT_FILE="in/" + sys.argv[0].split('/')[1].split('.')[0] + ".in"

with open(INPUT_FILE) as f:
    data = f.readlines()

graph = []
for line in data:
    tmp = []
    for c in line.strip():
        tmp.append(int(c))
    graph.append(tmp)

def valid(i,j):
    return (i >= 0 and i < len(graph)) and (j >= 0 and j < len(graph[i]))

visi_v1 = {}
def dfs_v1(i, j, itter):
    if (i,j) in visi_v1[itter]:
        return 0
    
    if graph[i][j] == 9:
        visi_v1[itter][(i,j)] = True
        return 1
    
    counter = 0
    for move in [(-1,0), (0,-1), (0,1), (1,0)]:
        if valid(i+move[0], j+move[1]) and (graph[i+move[0]][j+move[1]] - graph[i][j]) == 1:
            counter += dfs_v1(i+move[0], j+move[1], itter)

    visi_v1[itter][(i,j)] = True

    return counter

def solve1():
    acc = 0

    for i, line in enumerate(graph):
        for j, node in enumerate(line):
            if node == 0:
                itter = i*len(graph)+j
                visi_v1[itter] = {}
                acc += dfs_v1(i,j, itter)

    print(f"First result: {acc}")

visi_v2 = {}
def dfs_v2(i, j, itter):
    if (i,j) in visi_v2[itter]:
        return visi_v2[itter][(i,j)]

    if graph[i][j] == 9:
        visi_v2[itter][(i,j)] = 1
        return 1
    
    counter = 0
    for move in [(-1,0), (0,-1), (0,1), (1,0)]:
        if valid(i+move[0], j+move[1]) and (graph[i+move[0]][j+move[1]] - graph[i][j]) == 1:
            counter += dfs_v2(i+move[0], j+move[1], itter)

    visi_v2[itter][(i,j)] = counter

    return counter
    

def solve2():
    acc = 0
    for i, line in enumerate(graph):
        for j, node in enumerate(line):
            if node == 0:
                itter = i*len(graph)+j
                visi_v2[itter] = {}
                acc += dfs_v2(i,j, itter)

    print(f"Second result: {acc}")

solve1()
solve2()
