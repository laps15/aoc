#!/usr/bin/python3

import math
import sys

INPUT_FILE="in/" + sys.argv[0].split('/')[1] + ".in"

with open(INPUT_FILE) as f:
    data = f.readlines()

pdata = {
    'seeds': [int(n.strip()) for n in data[0].split(':')[1].strip().split(' ')],
    'seed-to-soil': [],
    'soil-to-fertilizer': [],
    'fertilizer-to-water': [],
    'water-to-light': [],
    'light-to-temperature': [],
    'temperature-to-humidity': [],
    'humidity-to-location': [],
}

target_map = ''
for _iter in range(2, len(data)):
    if len(data[_iter].split(' ')) < 2:
        continue
        
    if 'map' in data[_iter]:
        target_map = data[_iter].split(' ')[0].strip()
        continue

    [drs, srs, rl] = [int(b.strip()) for b in data[_iter].split(' ')]

    node = {
        'from': srs,
        'to': srs + rl-1,
        'delta': drs - srs,
    }

    pdata[target_map].append(node)


def convert(map_name, source):
    for entry in pdata[map_name]:
        if source >= entry['from'] and source <= entry['to']:
            return source + entry['delta']
    return source

def solve1():
    solution = sys.maxsize

    for seed in pdata['seeds']:
        soil = convert('seed-to-soil', seed)
        fertilizer = convert('soil-to-fertilizer', soil)
        water = convert('fertilizer-to-water', fertilizer)
        light = convert('water-to-light', water)
        temperature = convert('light-to-temperature', light)
        humidity = convert('temperature-to-humidity', temperature)
        location = convert('humidity-to-location', humidity)

        if location < solution:
            solution = location      

    print("First answer:", solution)

def solve2():
    solution = -1
    print("Second answer:", solution)

solve1()
solve2()
