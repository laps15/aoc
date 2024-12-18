#!/usr/bin/python3

import math
import re
import sys

INPUT_FILE="in/" + sys.argv[0].split('/')[1].split('.')[0] + ".in"

with open(INPUT_FILE) as f:
    data = f.readlines()

Registers = {
    "A": int(data[0].strip().split(':')[1].strip()),
    "B": int(data[1].strip().split(':')[1].strip()),
    "C": int(data[2].strip().split(':')[1].strip()),
}

prog = [int(i) for i in data[4].strip().split(':')[1].strip().split(',')]

def _raise(e):
    raise e

ComboOps = lambda v : {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: Registers['A'],
    5: Registers['B'],
    6: Registers['C'],
}[v]

print(data)

def truncate(v):
    TRUNCATE_VAL = 0xFFFFFFFF
    return int(v) & TRUNCATE_VAL

def run(program):
    ip = 0
    out = []
    
    while ip < len(prog):
        opcode = program[ip]
        operand = program[ip+1]

        if opcode == 0:
                Registers['A'] = truncate(Registers['A'] >> ComboOps(operand))
                
        elif opcode == 1: 
            Registers['B'] = Registers['B'] ^ operand

        elif opcode == 2:
            Registers['B'] = ComboOps(operand) % 8

        elif opcode == 3:
            if Registers['A'] != 0:
                ip = operand
                continue

        elif opcode == 4:
            Registers['B'] ^= Registers['C']

        elif opcode == 5:
            out.append(ComboOps(operand) % 8)

        elif opcode == 6:
            Registers['B'] = truncate(Registers['A'] >> ComboOps(operand))

        elif opcode == 7:
            Registers['C'] = truncate(Registers['A'] >> ComboOps(operand))

        ip += 2
    
    return out

def solve1():
    acc = 0

    out = run(prog)

    print(Registers)
    acc = ','.join([str(o) for o in out])
    print(f"First result: {acc}")

# def run_algorithm(A):
#     out = []
#     while A:
#         B = A % 8
#         B ^= 5
#         C = A>>B
#         B ^= C
#         B ^= 6
#         out.append(B)

#         A = A >> 3

#     return out

def solve2():

    valid_a = [0]

    for i in range(len(prog)):
        target_output = prog[-(i+1)]
        next_values = []

        for a in valid_a:
            A = a*8

            for to_try in range(0, 8):
                Registers['A'] = A + to_try
                Registers['B'] = 0
                Registers['C'] = 0

                r = run(prog)
                if r and r[0] == target_output:
                    next_values.append(A + to_try)

        valid_a = next_values

    acc = min(valid_a)

    print(f"Second result: {acc}")

solve1()
solve2()
