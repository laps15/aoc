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

print(data)


def valid(i, j):
    return (i >= 0 and i < len(data)) and ((j >= 0) and (j < len(data[0])))

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
                print(f"Region {data[i][j]}, price {a}*{p} = {a*p}")
                acc += a*p

    print(f"First result: {acc}")


visi_v2 = {}
def dfs_v2(i, j):
    if (i,j) in visi_v2:
        return 0,{},{}
    
    visi_v2[(i,j)] = True

    polygon = {}
    area = 1
    sides = {}

    for move in [(-1,0), (0,-1), (1,0), (0,1)]:
        if valid(i+move[0], j+move[1]) and data[i][j] == data[i+move[0]][j+move[1]]:
            na, ns, npoly = dfs_v2(i+move[0], j+move[1])
            area += na
            sides.update(ns)
            polygon.update(npoly)
        else:
            polygon[(i,j)] = 1
            sides[(i+move[0], j+move[1])] = 1

    return area, sides, polygon

def is_same_side_h(a,b):
    return a[0] == b[0] and abs(b[1]-a[1]) < 2

def is_same_side_v(a,b):
    return a[1] == b[1] and abs(b[0]-a[0]) < 2

def join_lines(points, checker, key=None):
    points.sort(key=key)

    reduced_points = []
    lines = []
    idx = 0
    while idx < len(points):
        start = points[idx]
        line = [start]
        while idx < len(points) - 1 and checker(points[idx], points[idx+1]):
            idx += 1
            line.append(points[idx])
        idx += 1
        lines.append(line)
        # reduced_points.append(start)

    return lines

def merge_lines(lines):
    result = []
    i = 0
    print(lines)
    while i < len(lines):
        j = i+1
        new_line = {p: 1 for p in lines[i]}
        while j < len(lines):
            merge_candidate = {p: 1 for p in lines[j]}
            increment = 1
            for p in merge_candidate:
                if p in new_line:
                    new_line.update(merge_candidate)
                    lines.pop(j)
                    increment = 0
                    break

            j+= increment
        
        i+= 1

        result.append(list(new_line.keys()))

    return result 



def solve2():
    acc = 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            if not (i,j) in visi_v2:
                area, sides, polygon  = dfs_v2(i,j)

                sides = list(sides.keys())

                h_lines = join_lines(sides, is_same_side_h)
                # print(h_lines)
                v_lines = join_lines(sides, is_same_side_v, key=lambda p: (p[1],p[0]))
                # print(v_lines)

                lines = []
                for line in h_lines:
                    if len(line) > 1:
                        lines.append(line)
                        continue
                    
                    midline = False
                    for check in v_lines:
                        midline = midline or (len(check) > 1 and line[0] in check)

                    if not midline:
                        lines.append(line)
                        
                for line in v_lines:
                    if len(line) > 1:
                        lines.append(line)
                        continue
                    
                    midline = False
                    for check in h_lines:
                        midline = midline or (len(check) > 1 and line[0] in check)

                    if not midline and line not in lines:
                        lines.append(line)

                lines = merge_lines(lines)

                print(lines)
                n_sides = 0

                for line in lines:
                    for move in [(-1,0), (0,-1), (1,0), (0,1)]:
                        add = 0
                        for p in line:
                            if (p[0]+move[0], p[1]+move[1]) in polygon:
                                add = 1
                        if add == 1:
                            print(f"Side found on line {line}{move}")
                        n_sides += add

                print(f"Region {data[i][j]}, price {area}*{n_sides} = {area*n_sides}")
                acc += area*n_sides

    print(f"Second result: {acc}")

solve1()
solve2()
