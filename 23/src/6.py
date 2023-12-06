#!/usr/bin/python3

import math
import sys
import re
from functools import reduce

INPUT_FILE="in/" + sys.argv[0].split('/')[1] + ".in"

with open(INPUT_FILE) as f:
    raw_data = f.readlines()

data = {
    'time': [int(a.strip()) for a in re.sub(r'\W+', ' ', raw_data[0].split(':')[1].strip()).split(' ')],
    'distance': [int(a.strip()) for a in re.sub(r'\W+', ' ', raw_data[1].split(':')[1].strip()).split(' ')],
}

print(data)

def solve1():

    solution = 1

    for _iter in range(len(data['time'])):
        time = data['time'][_iter]
        distance = data['distance'][_iter]

        _min = math.ceil((time - math.sqrt(time**2-4*distance))/2)
        _mid = time/2
        _max = math.floor((time + math.sqrt(time**2-4*distance))/2)

        _min = _min + 1 if (_min*(time-_min)) == distance else _min

        _max = _max - 1 if (_max*(time-_max)) == distance else _max

        solution *= _max - _min + 1

    print("First answer:", solution)

def solve2():
    solution = 1

    time = int(''.join([str(a) for a in data['time']]))
    distance = int(''.join([str(a) for a in data['distance']]))
    print(time, distance)
    
    _min = math.ceil((time - math.sqrt(time**2-4*distance))/2)
    _mid = time/2
    _max = math.floor((time + math.sqrt(time**2-4*distance))/2)

    _min = _min + 1 if (_min*(time-_min)) == distance else _min

    _max = _max - 1 if (_max*(time-_max)) == distance else _max

    solution *= _max - _min + 1

    print("Second answer:", solution)

solve1()
solve2()
