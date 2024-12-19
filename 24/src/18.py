#!/usr/bin/python3

import math
import re
import sys

INPUT_FILE="in/" + sys.argv[0].split('/')[1].split('.')[0] + ".in"
DEBUG = False

MOVES = [(1,0), (-1,0), (0,1), (0,-1)]
falling_bytes = []

with open(INPUT_FILE) as f:
    data = f.readlines()

for line in data:
    x = line.strip().split(',')[0]
    y = line.strip().split(',')[1]
    falling_bytes.append((int(y), int(x)))

BYTES = {byte: (i+1) for i,byte in enumerate(falling_bytes)}

def valid(mem_size, pos):
    return (pos[0] >= 0 and pos[0] < mem_size[0]) and (pos[1] >= 0 and pos[1] < mem_size[1])

def is_corrupted(pos, byte_iteration):
    return pos in BYTES and BYTES[pos] <= byte_iteration

def bfs(mem_size, pos, byte_iteration):

    Q = [(0,pos, pos)]
    visited = {}
    prev = {}

    while len(Q) > 0:
        dist, current_pos, previous_pos = Q.pop(0)
        if current_pos in visited:
            continue

        visited[current_pos] = dist
        prev[current_pos] = previous_pos

        for move in MOVES:
            target = (current_pos[0] + move[0], current_pos[1] + move[1])

            if valid(mem_size, target) and not is_corrupted(target, byte_iteration):
                Q.append((dist+1, target, current_pos))

    return visited, prev

def solve1():
    acc = 0

    visited, path = bfs((71, 71), (0,0), 1024)
    print_mem(path, 1024)
    acc = visited[(70,70)]

    print(f"First result: {acc}")

def print_mem(path, byte_iteration):
    if not DEBUG:
        return
    
    exit_path = []

    curr = (70,70)
    while curr in path and curr != (0,0):
        exit_path.append(curr)
        curr = path[curr] 

    exit_path.append((0,0))

    for i in range(71):
        for j in range(71):
            if (i,j) in exit_path:
                print('O', end='')
            elif is_corrupted((i,j), byte_iteration):
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()

def solve2():
    mem = []
    for _ in range(71):
        tmp = []
        for __ in range(71):
            tmp.append('.')
        mem.append(tmp)


    start = 0
    end = len(falling_bytes)

    while start <= end:
        mid = (start + end) // 2

        visited, path = bfs((71,71), (0,0), mid)

        can = "can" if (70,70) in visited else "can't"
        if DEBUG: print(f"On iteration: {mid} you {can} reach the destination")
        print_mem(path, mid)

        if (70,70) in visited:
            start = mid + 1
        else:
            end = mid - 1


    ans = falling_bytes[mid-1]
    print(f"Second result: {(ans[1],ans[0])}")

solve1()
solve2()
