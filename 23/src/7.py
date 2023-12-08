#!/usr/bin/python3

import math
import sys
from functools import cmp_to_key

##        CBA9876543210
#ORDER_1 = 'AKQJT98765432'

ORDER_1 = {
    'A': 'C',
    'K': 'B',
    'Q': 'A',
    'J': '9',
    'T': '8',
    '9': '7',
    '8': '6',
    '7': '5',
    '6': '4',
    '5': '3',
    '4': '2',
    '3': '1',
    '2': '0',
}

ORDER_2 = {
    'A': 'C',
    'K': 'B',
    'Q': 'A',
    'T': '9',
    '9': '8',
    '8': '7',
    '7': '6',
    '6': '5',
    '5': '4',
    '4': '3',
    '3': '2',
    '2': '1',
    'J': '0',
}

def toHex(hand, order):
    return ''.join([order[c] for c in hand])

HAND_TYPE_VALUE = {
    'Five': 1000000,
    'Four': 100000,
    'FullHouse': 10000,
    'Three': 1000,
    'TwoPair': 100,
    'Pair': 10,
    'None': 1,
}

def getType1(hand):
    cards = {x:hand.count(x) for x in hand}
    
    count = ''.join([str(a) for a in cards.values()])
    
    if count == '5':
        return 'Five'
    if count == '41' or count == '14':
        return 'Four'
    if count == '32' or count == '23':
        return 'FullHouse'
    if count == '311' or count == '131' or count == '113':
        return 'Three'
    if count == '221' or count == '212' or count == '122':
        return 'TwoPair'
    if '2' in count:
        return 'Pair'

    return 'None'


def getType2(hand):
    cards = {x:hand.count(x) for x in hand}
    
    count = ''.join([str(a) for a in cards.values()])
    jokers = cards.get('J', 0)
    
    if count == '5':
        return 'Five'

    if '4' in count:
        if jokers > 0:
            return 'Five'
        return 'Four'

    if '3' in count and '2' in count:
        if jokers > 0:
            return 'Five'
        return 'FullHouse'

    if '3' in count:
        if jokers > 0:
            return 'Four'
        return 'Three'

    if count == '221' or count == '212' or count == '122':
        if jokers == 2:
            return 'Four'
        if jokers > 0:
            return 'FullHouse'
        return 'TwoPair'

    if '2' in count:
        if jokers > 0:
            return 'Three'
        return 'Pair'

    if jokers > 0:
        return 'Pair'

    return 'None'

INPUT_FILE="in/" + sys.argv[0].split('/')[1] + ".in"

with open(INPUT_FILE) as f:
    raw_data = f.readlines()

# print(raw_data)

data = []

for line in raw_data:
    [hand, bid] = [a.strip() for a in line.split(' ')[:2]]
    data.append({
        'hand': hand,
        'bid': int(bid),
        'ordinary1': int(toHex(hand, ORDER_1), 16),
        'ordinary2': int(toHex(hand, ORDER_2), 16),
        'type1': HAND_TYPE_VALUE[getType1(hand)],
        'type2': HAND_TYPE_VALUE[getType2(hand)],
    })

def compare1(hand1, hand2):
    if hand1['type1'] == hand2['type1']:
        return hand1['ordinary1'] - hand2['ordinary1']

    return hand1['type1'] - hand2['type1']

def compare2(hand1, hand2):
    if hand1['type2'] == hand2['type2']:
        return hand1['ordinary2'] - hand2['ordinary2']

    return hand1['type2'] - hand2['type2']

def solve1():
    solution = 0

    sdata = sorted(data, key=cmp_to_key(compare1))
    print(sdata)

    for rank in range(len(sdata)):
        solution += (rank + 1) * sdata[rank]['bid']

    print("First answer:", solution)

def solve2():
    solution = 0

    sdata = sorted(data, key=cmp_to_key(compare2))
    print(sdata)

    for rank in range(len(sdata)):
        solution += (rank + 1) * sdata[rank]['bid']

    print("Second answer:", solution)

solve1()
solve2()