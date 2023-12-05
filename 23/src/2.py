#!/usr/bin/python3

import math
import sys
from functools import reduce

INPUT_FILE="in/" + sys.argv[0].split('/')[1] + ".in"

with open(INPUT_FILE) as f:
    data = f.readlines()

print(data)

def parse_data():
    game_set = {}
    for line in data:
        [game_name, rounds_desc] = line.split(':')
        game_number = game_name.strip().split(' ')[1]
        rounds = []
        for actions in rounds_desc.strip().split(';'):
            _round = {}
            for action in actions.strip().split(','):
                [amount, color] = action.strip().split(' ')
                _round[color] = int(amount)
            rounds.append(_round)
        game_set[game_number] = rounds
    
    return game_set


def solve1():
    solution = 0

    limits = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    data_set = parse_data()
    
    for game_name in data_set:
        possible = True
        for rounds in data_set[game_name]:
            for color in rounds:
                if rounds[color] > (limits.get(color, False) or 0):
                    possible = False
        
        if possible:
            solution += int(game_name)

    print("First answer:", solution)

def solve2():
    solution = 0
    
    data_set = parse_data()
    
    for game_name in data_set:
        optimal = {
            'red': 0,
            'blue': 0,
            'green': 0,
        }
        for rounds in data_set[game_name]:
            for color in rounds:
                if rounds[color] > (optimal.get(color, False) or 0):
                    optimal[color] = rounds[color]
        
        solution += reduce(lambda x, value: x * value, optimal.values(), 1)
    print("Second answer:", solution)

solve1()
solve2()
