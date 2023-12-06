#!/usr/bin/python3

import math
import sys

INPUT_FILE="in/" + sys.argv[0].split('/')[1] + ".in"

with open(INPUT_FILE) as f:
    data = f.readlines()

print(data)

def is_number(symbol):
    return symbol >= '0' and symbol <= '9'

def is_symbol(symbol):
    return not is_number(symbol) and symbol != '.'

def parse_data1():
    padded_data = ['' for a in range(len(data)+2)]

    for _iter in range(len(data)+2):
        padded_data[0] += '.'
        padded_data[len(data)+1] += '.'
    
    for x in range(1,len(data)+1):
        padded_data[x] += '.'
        for c in data[x-1].strip():
            padded_data[x] += c
            
        padded_data[x] += '.'
    
    data_set = {
        'data': padded_data,
        'numbers': {},
        'number_symbol': {},
    }

    for x in range(1, len(padded_data)-1):
        reading_number = -1
        data_set['numbers'][x] = {}
        data_set['number_symbol'][x] = {}

        for y in range(1,len(padded_data[x])):
            
            # Started to read number
            if is_number(padded_data[x][y]) and reading_number == -1:
                reading_number = y

            # Finished reading number
            if not is_number(padded_data[x][y]) and reading_number != -1:
                value = int(padded_data[x][reading_number:y])

                data_set['numbers'][x][reading_number] = value

                symbols = []
                if is_symbol(padded_data[x-1][reading_number-1]):
                    symbols.append([x-1, reading_number-1])

                if is_symbol(padded_data[x][reading_number-1]):
                    symbols.append([x, reading_number-1])

                if is_symbol(padded_data[x+1][reading_number-1]):
                    symbols.append([x+1, reading_number-1])

                    
                if is_symbol(padded_data[x-1][y]):
                    symbols.append([x-1, y])

                if is_symbol(padded_data[x][y]):
                    symbols.append([x, y])

                if is_symbol(padded_data[x+1][y]):
                    symbols.append([x+1, y])

                for _iter in range(reading_number, y):
                    if is_symbol(padded_data[x-1][_iter]):
                        symbols.append([x-1, _iter])
                    
                    if is_symbol(padded_data[x+1][_iter]):
                        symbols.append([x+1, _iter])

                data_set['number_symbol'][x][reading_number] = symbols

                reading_number = -1

    return data_set


def solve1():
    solution = 0

    data_set = parse_data1()

    for number_x in data_set['numbers']:
        for number_y in data_set['numbers'][number_x]:
            if len(data_set['number_symbol'][number_x][number_y]) == 0:
                print(data_set['numbers'][number_x][number_y], 'on', str(number_x)+',', number_y, 'is not a part number')
            else:
                solution += data_set['numbers'][number_x][number_y]

            # consumed = {}
            # for symbol in data_set['number_symbol'][number_x][number_y]:
            #     [symbol_x, symbol_y] = symbol
            #     dict_key = str(symbol_x)+str(symbol_y)

            #     if not consumed.get(dict_key, False):
            #         solution += data_set['numbers'][number_x][number_y]
            #         consumed[dict_key] = True
                

    print("First answer:", solution)

def is_gear(symbol):
    return symbol == '*'

def parse_data2():
    padded_data = ['' for a in range(len(data)+2)]

    for _iter in range(len(data)+2):
        padded_data[0] += '.'
        padded_data[len(data)+1] += '.'
    
    for x in range(1,len(data)+1):
        padded_data[x] += '.'
        for c in data[x-1].strip():
            padded_data[x] += c
            
        padded_data[x] += '.'
    
    data_set = {
        'data': padded_data,
        'gears': [],
        'gear_number': {},
    }

    
    for x in range(1, len(padded_data)-1):
        data_set['gear_number'][x] = {}
        for y in range(1,len(padded_data[x])):
            if is_gear(padded_data[x][y]):
                data_set['gears'].append([x,y])
                if not data_set['gear_number'][x].get(y, False):
                    data_set['gear_number'][x][y] = []

    for x in range(1, len(padded_data)-1):
        reading_number = -1

        for y in range(1,len(padded_data[x])):
            
            # Started to read number
            if is_number(padded_data[x][y]) and reading_number == -1:
                reading_number = y

            # Finished reading number
            if not is_number(padded_data[x][y]) and reading_number != -1:
                value = int(padded_data[x][reading_number:y])

                if is_gear(padded_data[x-1][reading_number-1]):
                    data_set['gear_number'][x-1][reading_number-1].append(value)

                if is_gear(padded_data[x][reading_number-1]):
                    data_set['gear_number'][x][reading_number-1].append(value)

                if is_gear(padded_data[x+1][reading_number-1]):
                    data_set['gear_number'][x+1][reading_number-1].append(value)

                    
                if is_gear(padded_data[x-1][y]):
                    data_set['gear_number'][x-1][y].append(value)

                if is_gear(padded_data[x][y]):
                    data_set['gear_number'][x][y].append(value)

                if is_gear(padded_data[x+1][y]):
                    data_set['gear_number'][x+1][y].append(value)

                for _iter in range(reading_number, y):
                    if is_gear(padded_data[x-1][_iter]):
                        data_set['gear_number'][x-1][_iter].append(value)
                    
                    if is_gear(padded_data[x+1][_iter]):
                        data_set['gear_number'][x+1][_iter].append(value)

                reading_number = -1

    return data_set



def solve2():
    solution = 0

    data_set = parse_data2()

    for gear in data_set['gears']:
        [gear_x, gear_y] = gear

        if len(data_set['gear_number'][gear_x][gear_y]) == 2:
            solution += data_set['gear_number'][gear_x][gear_y][0] * data_set['gear_number'][gear_x][gear_y][1]

    print("Second answer:", solution)

solve1()
solve2()
