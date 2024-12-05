#!/usr/bin/python3

import math
import re
import sys

INPUT_FILE="in/" + sys.argv[0].split('/')[1].split('.')[0] + ".in"

with open(INPUT_FILE) as f:
    data = f.read()


def get_instructions(regex):
    return re.finditer(regex, data, re.DOTALL)


def solve1():
    acc = 0

    instructions = get_instructions(r"mul\((\d{1,3}),(\d{1,3})\)")

    for i in instructions:
        acc += int(i.group(1)) * int(i.group(2))

    print(f"First result: {acc}")

def solve2():
    acc = 0

    instructions = get_instructions(r"(do\(\))|(don't\(\))|mul\((\d{1,3}),(\d{1,3})\)")

    enabled = True
    for i in instructions:
        instruction = i.group(0)

        if "don't" in instruction:
            enabled = False
        elif "do" in instruction:
            enabled = True
        elif "mul" in instruction and enabled:
            acc += int(i.group(3)) * int(i.group(4))

    print(f"Second result: {acc}")

solve1()
solve2()
