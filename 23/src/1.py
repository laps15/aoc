#!/usr/bin/python3

import math
import sys

INPUT_FILE="in/" + sys.argv[0].split('/')[1] + ".in"

with open(INPUT_FILE) as f:
    data = f.readlines()

print(data)

def solve1():
    solution = 0

    values = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    ]
    to_result = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }

    for line in data:
        first_amount = [sys.maxsize, 0]
        second_amount = [sys.maxsize, 0]
        for value in values:
            from_start = line.find(value)
            if from_start != -1 and from_start < first_amount[0]:
                first_amount = [from_start, to_result[value]]
                
            from_end = line[::-1].find(value[::-1])
            if from_end != -1 and from_end < second_amount[0]:
                second_amount = [from_end, to_result[value]]
            
        solution += first_amount[1]*10 + second_amount[1]
            
    print("First answer:", solution)

def solve2():
    solution = 0

    values = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
    ]
    to_result = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    for line in data:
        first_amount = [sys.maxsize, 0]
        second_amount = [sys.maxsize, 0]
        for value in values:
            from_start = line.find(value)
            if from_start != -1 and from_start < first_amount[0]:
                first_amount = [from_start, to_result[value]]
                
            from_end = line[::-1].find(value[::-1])
            if from_end != -1 and from_end < second_amount[0]:
                second_amount = [from_end, to_result[value]]
            
        solution += first_amount[1]*10 + second_amount[1]
    print("Second answer:", solution)

solve1()
solve2()
