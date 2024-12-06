#!/usr/bin/python3

import math
import re
import sys
import functools

INPUT_FILE="in/" + sys.argv[0].split('/')[1].split('.')[0] + ".in"

with open(INPUT_FILE) as f:
    data = f.readlines()

rules = {}
updates = []

idx = 0
while idx < len(data) and data[idx].strip() != '':
    [a,b] = [int(i) for i in data[idx].strip().split('|')]
    if not a in rules:
        rules[a] = []

    rules[a].append(b)
    idx += 1
    
idx += 1
while idx < len(data) and data[idx].strip() != '':
    updates.append([int(i) for i in data[idx].strip().split(',')])
    idx += 1
 

invalid_updates = []

def solve1():
    acc = 0

    for update in updates:
        already_printed = {}
        valid = True
        for page in update:
            already_printed[page] = True
            if not page in rules:
                continue

            for rule in rules[page]:
                valid = valid and (not rule in already_printed)
        if valid:
            acc += update[math.floor(len(update)/2)]
        else:
            invalid_updates.append(update)
        
    print(f"First result: {acc}")

def solve2():
    acc = 0
    def cmp(a, b):
        if a in rules and b in rules[a]:
            return -1
        if b in rules and a in rules[b]:
            return 1
        return 0
    
    for update in invalid_updates:
        update.sort(key=functools.cmp_to_key(cmp))
        acc += update[math.floor(len(update)/2)]

    print(f"Second result: {acc}")

solve1()
solve2()
