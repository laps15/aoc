#!/usr/bin/python3

import math
import re
import sys

INPUT_FILE="in/" + sys.argv[0].split('/')[1].split('.')[0] + ".in"
DEBUG = False

with open(INPUT_FILE) as f:
    data = f.readlines()

Map = []
START = (-1,-1)
END = (-1,-1)
for i in range(len(data)):
    tmp = []
    for j in range(len(data[i].strip())):
        if data[i][j] == '\n':
            continue
        if data[i][j] == 'S':
            START = (i,j)
        elif data[i][j] == 'E':
            END = (i,j)
            
        tmp.append(data[i][j])
    Map.append(tmp)

def dijikstra(map, start, facing, end):
    cost = {(start, facing): 0}
    queue = {(0, start, facing): start}
    prev = { (start, facing): [(start, facing)]}

    while len(queue) > 0:
        key = min(queue)
        queue.pop(key)

        points, pos, facing = key

        n_pos = (pos[0] + facing[0], pos[1] + facing[1])
        if map[n_pos[0]][n_pos[1]] != '#':
            if not (n_pos, facing) in cost:
                prev[(n_pos, facing)] = [(pos, facing)]
                cost[(n_pos, facing)] = points + 1
                queue[(points + 1, n_pos, facing)] = (n_pos, facing)

            elif cost[(n_pos, facing)] > points + 1:
                prev[(n_pos, facing)] = [(pos, facing)]
                cost[(n_pos, facing)] = points + 1
                queue[(points + 1, n_pos, facing)] = (n_pos, facing)

            elif cost[(n_pos, facing)] == points + 1:
                if (n_pos, facing) not in prev:
                    prev[(n_pos, facing)] = []
                prev[(n_pos, facing)].append((pos, facing))
                queue[(points + 1, n_pos, facing)] = (n_pos, facing)

        for n_facing in [(abs(facing[1]), abs(facing[0])), (-abs(facing[1]), -abs(facing[0]))]:
            if not (pos, n_facing) in cost:
                prev[(pos, n_facing)] = [(pos, facing)]
                cost[(pos, n_facing)] = points + 1000
                queue[(points + 1000, pos, n_facing)] = (pos, n_facing)

            elif cost[(pos, n_facing)] > points + 1000:
                prev[(pos, n_facing)] = [(pos, facing)]
                cost[(pos, n_facing)] = points + 1
                queue[(points + 1000, pos, n_facing)] = (pos, n_facing)

            elif cost[(pos, n_facing)] == points + 1000:
                if (pos, n_facing) not in prev:
                    prev[(pos, n_facing)] = []
                prev[(pos, n_facing)].append((pos, facing))
                queue[(points + 1000, pos, n_facing)] = (pos, n_facing)

    return cost, prev

def solve1():
    acc = 0

    cost, _ = dijikstra(Map, START, (0,1), END)

    costs = []
    for facing in [(1,0),(-1,0), (0,1), (0,-1)]:
        if (END, facing) in cost:
            costs.append(cost[(END, facing)])

    acc = min(costs)

    print(f"First result: {acc}")

def solve2():
    cost, paths = dijikstra(Map, START, (0,1), END)

    initial_state = (END, (0,1))
    for facing in [(1,0),(-1,0), (0,1), (0,-1)]:
        if (END, facing) in cost and cost[(END, facing)] < cost[initial_state]:
            initial_state = (END, facing)

    result = { END: True }

    Q = []
    state = initial_state

    while state != (START, (0,1)):
        for next_state in paths[state]:
            Q.append(next_state)
            result[next_state[0]] = True

        state = Q.pop(0)

    if DEBUG:
        for i in range(len(data)):
            for j in range(len(data[i])):
                c = data[i][j]
                if data[i][j] == '.' and (i,j) in result:
                    c = 'O'
                print(c, end='')
        print()

    print(f"Second result: {len(result)}")

solve1()
solve2()
