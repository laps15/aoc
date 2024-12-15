#!/usr/bin/python3

import math
import re
import sys

DEBUG = False
INPUT_FILE="in/" + sys.argv[0].split('/')[1].split('.')[0] + ".in"

with open(INPUT_FILE) as f:
    data = f.readlines()

Graph = []
line_idx = 0
INITIAL_R_POS = (-1,-1)
while line_idx < len(data) and data[line_idx].strip() != "":
    tmp = []
    for i,c in enumerate(data[line_idx].strip()):
        tmp.append(c)
        if c == '@':
            INITIAL_R_POS = (line_idx, i)
    Graph.append(tmp)
    line_idx += 1

moves = []
line_idx += 1
while line_idx < len(data) and data[line_idx].strip() != "":
    for c in data[line_idx].strip():
        moves.append(c)
    line_idx += 1


if DEBUG:
    print(Graph)
    print(moves)
    print(INITIAL_R_POS)

def valid(graph, position):
    return (position[0] >= 0 and position[0] < len(graph)) and (position[1] >= 0 and position[1] < len(graph[position[0]]))

def process_single_move(graph, r_pos, move):
    initial_target = (r_pos[0]+move[0], r_pos[1]+move[1])
    if not valid(graph, initial_target):
        return graph, r_pos
    
    target = initial_target
    move_boxes = False

    while graph[target[0]][target[1]] == 'O':
        target = (target[0]+move[0], target[1]+move[1])
        move_boxes = True

    if graph[target[0]][target[1]] == '.':
        graph[r_pos[0]][r_pos[1]] = '.'
        if move_boxes:
            graph[target[0]][target[1]] = 'O'
        graph[r_pos[0]+move[0]][r_pos[1]+move[1]] = '@'

        return graph, (r_pos[0]+move[0], r_pos[1]+move[1])
    
    if graph[target[0]][target[1]] == '#':
        return graph, r_pos
    

def process_moves(graph, r_pos, moves, move_handler):
    move_map = {
        '>': (0,+1),
        'v': (+1,0),
        '<': (0,-1),
        '^': (-1,0),
    }

    for i, m in enumerate(moves):
        move = move_map[m]

        graph, r_pos = move_handler(graph, r_pos, move)
        nxt = f"next {moves[i+1]}" if i < len(moves)-1 else ""
        if DEBUG:
            print(f"{m}: {r_pos} {nxt} {i+1}/{len(moves)}")
            print_graph(graph)
            if i > 188 and not skip:
                inp = input()


    return graph

def solve1():
    acc = 0

    graph = []
    for line in Graph:
        tmp = []
        for c in line:
            tmp.append(c)
        graph.append(tmp)
    graph = process_moves(graph, INITIAL_R_POS, moves, process_single_move)

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 'O':
                acc += 100*i+j

    print(f"First result: {acc}")

def print_graph(g):
    if not DEBUG:
        return 
    for line in g:
        for c in line:
            print(c, end='')
        print()

def get_v2(graph):
    result = []
    r_pos = (-1,-1)
    for i, line in enumerate(graph):
        tmp = []
        for c in line:
            if c == '#':
                tmp.extend(['#', '#'])
            elif c == '.':
                tmp.extend(['.', '.'])
            elif c == '@':
                r_pos = (i, len(tmp))
                tmp.extend(['@', '.'])
            elif c == 'O':
                tmp.extend(['[', ']'])
        result.append(tmp)

    return result, r_pos

def is_box(item):
   return item == '[' or item == ']' 

def can_move(graph, pos, move):
    target = (pos[0]+move[0], pos[1]+move[1])

    return graph[target[0]][target[1]] != '#'

def move_large_box_horizontally(graph, r_pos, move):
    initial_target = (r_pos[0] + move[0], r_pos[1] + move[1])
    target = initial_target

    while is_box(graph[target[0]][target[1]]):
        target = (target[0] + move[0], target[1] + move[1])
    
    if graph[target[0]][target[1]] == '#':
        return graph, r_pos
    
    destination = target
    source = (destination[0]-move[0], destination[1]-move[1])
    while source[1] != r_pos[1]:
        graph[destination[0]][destination[1]] = graph[source[0]][source[1]]

        destination = source
        source = (source[0]-move[0], source[1]-move[1])

    graph[destination[0]][destination[1]] = graph[source[0]][source[1]]
    graph[r_pos[0]][r_pos[1]] = '.'

    return graph, destination
 
def move_large_box_vertically(graph, r_pos, move):
    boxes = []
    queue = [(r_pos[0]+move[0], r_pos[1]+move[1])]
    visited = {}
    while len(queue) > 0:
        pos = queue.pop(0)

        if graph[pos[0]][pos[1]] == '[':
            box = (pos, (pos[0], pos[1]+1))
        else:
            box = ((pos[0], pos[1]-1), pos)
        
        if box in visited:
            continue

        visited[box] = True
        boxes.append(box)

        if can_move(graph, box[0], move) and can_move(graph, box[1], move):
            if is_box(graph[box[0][0]+move[0]][box[0][1] + move[1]]):
                queue.append((box[0][0] + move[0], box[0][1] + move[1]))
            if is_box(graph[box[1][0]+move[0]][box[1][1] + move[1]]):
                queue.append((box[1][0] + move[0], box[1][1] + move[1]))
        else:
            return graph, r_pos

    boxes.sort(key=lambda a: a[0][0] if move[0] == -1 else abs(a[0][0] - len(graph)))

    for box in boxes:
        destination = ((box[0][0]+move[0], box[0][1] + move[1]), (box[1][0]+move[0], box[1][1] + move[1]))

        graph[destination[0][0]][destination[0][1]] = graph[box[0][0]][box[0][1]]
        graph[destination[1][0]][destination[1][1]] = graph[box[1][0]][box[1][1]]
        graph[box[0][0]][box[0][1]] = '.'
        graph[box[1][0]][box[1][1]] = '.'

    n_r_pos = (r_pos[0] + move[0], r_pos[1] + move[1])
    graph[n_r_pos[0]][n_r_pos[1]] = '@'
    graph[r_pos[0]][r_pos[1]] = '.'
    return graph, n_r_pos

def move_large_box(graph, r_pos, move):
    if move[0] == 0:
        return move_large_box_horizontally(graph, r_pos, move)

    return move_large_box_vertically(graph, r_pos, move)
            

def process_single_move_v2(graph, r_pos, move):
    target = (r_pos[0]+move[0], r_pos[1]+move[1])
    
    if not valid(graph, target):
        return graph, r_pos

    if is_box(graph[target[0]][target[1]]):
        return move_large_box(graph, r_pos, move)

    if graph[target[0]][target[1]] == '.':
        graph[r_pos[0]][r_pos[1]] = '.'
        graph[r_pos[0]+move[0]][r_pos[1]+move[1]] = '@'

        return graph, (r_pos[0]+move[0], r_pos[1]+move[1])
    
    if graph[target[0]][target[1]] == '#':
        return graph, r_pos

def solve2():
    acc = 0

    print_graph(Graph)
    g, r_pos = get_v2(Graph)
    g = process_moves(g, r_pos, moves, process_single_move_v2)
    print_graph(g)

    for i in range(len(g)):
        j = 0
        while j < len(g[i]):
            if is_box(g[i][j]):
                acc += i*100 + j
                j += 1
            j += 1

    print(f"Second result: {acc}")

solve1()
solve2()
