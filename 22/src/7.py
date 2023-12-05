#!/usr/bin/python3

import math

INPUT_FILE="in/7.in"

MAX_SIZE = 70000000
NEEDED_SPACE = 30000000

with open(INPUT_FILE) as f:
    data = f.readlines()


file_tree = {
    'root': {
        'name': 'root',
        'size': None,
        'children': {
            '/': {
            'name': '/',
            'size': None,
            'children': {}
            }
        },
    }
}

file_tree['root']['children']['/']['children']['..'] = file_tree['root']

def calc_size(node):
    if node['size'] != None:
        return node['size']
    
    size = 0
    for child in node['children']:
        if child != '..':
            size += calc_size(node['children'][child])
    
    node['size'] = size

    return size

def init():
    root = file_tree['root']
    for line in data:
        line = line.strip('\n')
        if '$ cd ' in line:
            dirname = line.split(' ')[2]
            root = root['children'][dirname]
            continue
        if '$ ls' in line:
            continue

        [size, name] = line.split(' ')
        
        if size == 'dir':
            root['children'][name] = {
                'name': name,
                'size': None,
                'children': {
                    '..': root,
                },
            }
            continue
        
        root['children'][name] = {
            'name': name,
            'size': int(size),
            'children': None,
        }
            
    calc_size(file_tree['root'])

def getSol1(node):
    if node['children'] == None:
        return 0
    
    ans = 0 if node['size'] > 100000 else node['size']
    for child in node['children']:
        if child != '..':
            ans += getSol1(node['children'][child])
    return ans

def getSol2(node, target):
    if node['children'] == None or node['size'] < target:
        return []
    
    if node['size'] >= target:
        ans = [node['size']]
    else:
        ans = []

    for child in node['children']:
        if child != '..':
            ans += getSol2(node['children'][child], target)
    return ans


def print_tree(node, level):
    if node['children'] == None:
        for i in range(level):
            print('.', end='')
        print(node['name'], '(', node['size'], ')')
        return
    
    for i in range(level):
        print('.', end='')
    print(node['name'], '(', node['size'], ')')
    for child in node['children']:
        if child != node['name'] and child != '..':
            print_tree(node['children'][child], level+1)


def solve1():
    solution = 0
    print("First answer:",  getSol1(file_tree['root']))

def solve2():
    free_space = (MAX_SIZE - file_tree['root']['size'])
    target = NEEDED_SPACE - free_space

    solution = getSol2(file_tree['root'], target)
    solution.sort()
    print("Second answer:", min(solution))

init()
solve1()
solve2()