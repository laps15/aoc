#!/usr/bin/python3

import math
import re
import sys

INPUT_FILE="in/" + sys.argv[0].split('/')[1].split('.')[0] + ".in"

data = []
with open(INPUT_FILE) as f:
    for line in f.readlines():
        data.append([c for c in line.strip()])

WORD='XMAS'

def valid(i, j):
    return (i >= 0 and i < len(data)) and ((j >= 0) and (j < len(data[0])))

def count_word(i, j):
    counter = 0

    for i_iter in [-1, 0, 1]:
        for j_iter in [-1, 0, 1]:
            n_i = i+i_iter
            n_j = j+j_iter

            if not valid(n_i, n_j):
                continue

            if data[n_i][n_j] == WORD[1]:
                counter += find_letter(n_i, n_j, 2, (i_iter, j_iter))

    return counter

def find_letter(i, j, target, direction):
    n_i = i+direction[0]
    n_j = j+direction[1]

    if not valid(n_i, n_j):
        return 0

    if data[n_i][n_j] == WORD[target]:
        if target == len(WORD) - 1:
            return 1
        return find_letter(n_i, n_j, target+1, direction)

    return 0


def solve1():
    acc = 0

    for line in range(len(data)):
        for char in range(len(data[0])):
            if data[line][char] == WORD[0]:
                count = count_word(line, char)

                acc += count

    print(f"First result: {acc}")    

def check_diagonal(diagonal):
    ((top_i, top_j), (down_i, down_j)) = diagonal
    if not valid(top_i, top_j) or not valid(down_i, down_j):
        return False
    
    return ((data[top_i][top_j] == 'S' and data[down_i][down_j] == 'M')
            or (data[top_i][top_j] == 'M' and data[down_i][down_j] == 'S'))


def is_x_mas(i, j):
    first_diagonal = ((i-1, j-1), (i+1, j+1))
    second_diagonal = ((i-1, j+1), (i+1, j-1))

    return check_diagonal(first_diagonal) and check_diagonal(second_diagonal)
            

def solve2():
    acc = 0

    for line in range(len(data)):
        for char in range(len(data[0])):
            if data[line][char] == 'A':
                if is_x_mas(line, char):
                    acc += 1

    print(f"Second result: {acc}")

solve1()
solve2()
