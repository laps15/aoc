#!/usr/bin/python3

import math
import re
import sys

INPUT_FILE="in/" + sys.argv[0].split('/')[1].split('.')[0] + ".in"

with open(INPUT_FILE) as f:
    data = f.readlines()

eqs = []
for line in data:
    factors = []
    r = int(line.strip().split(':')[0])
    for n in line.strip().split(':')[1].strip().split(' '):
        factors.append(int(n.strip()))
    eqs.append((r, factors))


def is_solvable_v1(eq):
    (r, factors) = eq

    if len(factors) == 1:
        return factors[0] == r

    return (is_solvable_v1((r, [factors[0] + factors[1]] + factors[2:])) 
            or is_solvable_v1((r, [factors[0] * factors[1]] + factors[2:])))

def solve1():
    acc = 0

    for eq in eqs:
        if is_solvable_v1(eq):
            acc += eq[0]

    print(f"First result: {acc}")

def is_solvable_v2(eq):
    (r, factors) = eq

    if len(factors) == 1:
        return factors[0] == r

    return (is_solvable_v2((r, [factors[0] + factors[1]] + factors[2:])) 
            or is_solvable_v2((r, [factors[0] * factors[1]] + factors[2:]))
            or is_solvable_v2((r, [int(f'{factors[0]}{factors[1]}')] + factors[2:])))

def solve2():
    acc = 0

    for eq in eqs:
        if is_solvable_v2(eq):
            acc += eq[0]

    print(f"Second result: {acc}")

solve1()
solve2()
