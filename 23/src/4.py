#!/usr/bin/python3

import math
import sys
import re

INPUT_FILE="in/" + sys.argv[0].split('/')[1] + ".in"

with open(INPUT_FILE) as f:
    data = f.readlines()

pdata = []
for line in data:
    c = {
        'win': [],
        'have': [],
    }

    [win, have] = [a.strip() for a in line.replace('  ', ' ').split(':')[1].strip().split('|')]

    c['win'] = [int(n.strip()) for n in win.split(' ')]
    c['have'] = [int(n.strip()) for n in have.split(' ')]
    pdata.append(c)

def solve1():
    solution = 0

    for card in pdata:
        hits = 0
        for target in card['have']:
            if target in card['win']:
                hits += 1

        solution += 0 if (hits == 0) else 1<<(hits-1)


    print("First answer:", solution)

def solve2():
    solution = 0
    
    amounts = [1 for a in pdata]
    for idx in range(len(pdata)):
        card = pdata[idx]
        c_amout = amounts[idx]

        hits = 0
        for target in card['have']:
            if target in card['win']:
                hits += 1
        
        next_idx = idx + 1
        for _iter in range(next_idx, next_idx+hits):
            amounts[_iter] += c_amout

    for a in amounts:
        solution += a  
    

    print("Second answer:", solution)

solve1()
solve2()
