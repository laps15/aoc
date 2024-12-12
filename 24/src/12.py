#!/usr/bin/python3

import math
import re
import sys
import functools

INPUT_FILE="in/" + sys.argv[0].split('/')[1].split('.')[0] + ".in"

data = []
with open(INPUT_FILE) as f:
    for line in f.readlines():
        tmp = []
        for c in line.strip():
            tmp.append(c)
        data.append(tmp)


def valid(i, j):
    return (i >= 0 and i < len(data)) and ((j >= 0) and (j < len(data[0])))

def getter(matrix, p):
    if valid(p[0], p[1]):
        return matrix[p[0]][p[1]]
    
    return -1

visi_v1 = {}
def dfs_v1(i, j):
    if (i,j) in visi_v1:
        return 0,0
    
    visi_v1[(i,j)] = True

    area = 1
    perimiter = 0

    for move in [(-1,0), (0,-1), (1,0), (0,1)]:
        if valid(i+move[0], j+move[1]) and data[i][j] == data[i+move[0]][j+move[1]]:
            na, np = dfs_v1(i+move[0], j+move[1])
            area += na
            perimiter += np
        else:
            perimiter += 1

    return area, perimiter


def solve1():
    acc = 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            if not (i,j) in visi_v1:
                a,p = dfs_v1(i,j)
                # print(f"Region {data[i][j]}, price {a}*{p} = {a*p}")
                acc += a*p

    print(f"First result: {acc}")


def dfs(i, j):
    if (i,j) in visi:
        return 0,{},{}
    
    visi[(i,j)] = True

    polygon = {}
    area = 1
    sides = {}

    for move in [(-1,0), (0,-1), (1,0), (0,1)]:
        if valid(i+move[0], j+move[1]) and data[i][j] == getter(data, (i+move[0], j+move[1])):
            na, ns, npoly = dfs(i+move[0], j+move[1])
            area += na
            sides.update(ns)
            polygon.update(npoly)
        else:
            polygon[(i,j)] = 1
            sides[(i+move[0], j+move[1])] = 1

    return area, sides, polygon

'''
Navigate the perimeter clock-wise.
'''
def get_next(state, perimeter):
    (loc, fac) = state

    if fac == (-1,0):
        if (loc[0], loc[1]+1) in perimeter:
            if fac in perimeter[(loc[0], loc[1]+1)]:
                return ((loc[0], loc[1]+1), fac), False
        if (loc[0]-1, loc[1]+1) in perimeter:
            if (0,-1) in perimeter[(loc[0]-1, loc[1]+1)]:
                return ((loc[0]-1, loc[1]+1), (0,-1)), True
        if loc in perimeter and (0,1) in perimeter[loc]:
            return (loc, (0,1)), True
        return state, False

    if fac == (0,1):
        if (loc[0]+1, loc[1]) in perimeter:
            if fac in perimeter[(loc[0]+1, loc[1])]:
                return ((loc[0]+1, loc[1]), fac), False
        if (loc[0]+1, loc[1]+1) in perimeter:
            if (-1,0) in perimeter[(loc[0]+1, loc[1]+1)]:
                return ((loc[0]+1, loc[1]+1), (-1, 0)), True
        if loc in perimeter and (1,0) in perimeter[loc]:
            return (loc, (1,0)), True
        return state, False
        
        
    if fac == (1,0):
        if (loc[0], loc[1]-1) in perimeter:
            if fac in perimeter[(loc[0], loc[1]-1)]:
                return ((loc[0], loc[1]-1), fac), False
        if (loc[0]+1, loc[1]-1) in perimeter:
            if (0,1) in perimeter[(loc[0]+1, loc[1]-1)]:
                return ((loc[0]+1, loc[1]-1), (0, 1)), True
        if loc in perimeter and (0,-1) in perimeter[loc]:
            return (loc, (0,-1)), True
        return state, False
        
    if (loc[0]-1, loc[1]) in perimeter:
        if fac in perimeter[(loc[0]-1, loc[1])]:
            return ((loc[0]-1, loc[1]), fac), False
    if (loc[0]-1, loc[1]-1) in perimeter:
        if (1,0) in perimeter[(loc[0]-1, loc[1]-1)]:
            return ((loc[0]-1, loc[1]-1), (1, 0)), True
    if loc in perimeter and (-1, 0) in perimeter[loc]:
        return (loc, (-1, 0)), True
    return state, False


'''
Get left-most point that has a top border
'''
def get_initial_state(perimeter):
    coords = list(perimeter.keys())
    coords.sort()

    for coord in coords:
        if (-1,0) in perimeter[coord]:
            return (coord, (-1,0))
        
    return (coords[0], list(perimeter[coords[0]].keys())[0])


def solve2(polygons):
    acc = 0

    for polygon in polygons:
        area, sides, polygon  = polygon

        sides = list(polygon.keys())

        perimeter = {}
        for p in sides:
            for move in [(-1,0), (0,-1), (1,0), (0,1)]:
                if getter(data, (p[0]+move[0],p[1]+move[1])) != data[p[0]][p[1]]:
                    if not p in perimeter:
                        perimeter[p] = {}
                    perimeter[p][move] = True

        n_sides = 0
        n_sides_1 = 0

        while len(perimeter) > 0:
            last_move = get_initial_state(perimeter)

            n_sides += 1
            perimeter[last_move[0]].pop(last_move[1])
            if len(perimeter[last_move[0]]) == 0:
                perimeter.pop(last_move[0])
            current_state, new_side = get_next(last_move, perimeter)

            while current_state != last_move:
                if new_side:
                    n_sides += 1

                last_move = current_state
                perimeter[current_state[0]].pop(current_state[1])
                if len(perimeter[current_state[0]]) == 0:
                    perimeter.pop(current_state[0])

                current_state, new_side = get_next(current_state, perimeter)


        acc += area*n_sides

    print(f"Second result: {acc}")

visi = {}

polygons = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if not (i,j) in visi:
            area, sides, polygon  = dfs(i,j)
            polygons.append((area, sides, polygon))
solve1()
solve2(polygons)
