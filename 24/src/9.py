#!/usr/bin/python3

import sys

INPUT_FILE="in/" + sys.argv[0].split('/')[1].split('.')[0] + ".in"

with open(INPUT_FILE) as f:
    data = f.readlines()

disk = [int(i) for i in data[0].strip()]

expanded_disk = []
for i in range(len(disk)):
    for j in range(disk[i]):
        expanded_disk.append(int(i/2) if not i&1 else -1) 

def solve1():
    acc = 0

    result = expanded_disk.copy()
    begin, end = 0, len(result) -1
    while begin <= end:
        if result[begin] != -1:
            
            begin += 1
            continue

        if result[end] == -1:
            end -= 1
            continue

        result[begin] = result[end]
        result[end] = -1
        begin += 1
        end -= 1

    i = 0
    while result[i] != -1:
        acc += i*result[i]
        i += 1

    print(f"First result: {acc}")

def solve2():
    acc = 0
    
    gaps = {}
    files = {}

    disk_block_idx = 0
    for i in range(len(disk)):
        if not i & 1:
            files[int(i/2)] = (disk_block_idx, disk[i])
        elif disk[i] > 0:
            gaps[disk_block_idx] = disk[i]

        disk_block_idx += disk[i]

    resulting_files = {}

    while files:
        file_id, (file_start, file_size) = files.popitem()
    
        new_start = -1
        for key in sorted(gaps):
            if key > file_start:
                break
            if gaps[key] > file_size:
                new_start = key
                prev_size = gaps.pop(key)

                gaps[key + file_size] = prev_size - file_size
                break

            elif gaps[key] == file_size:
                new_start = key
                gaps.pop(key)
                break

        if new_start == -1:
            resulting_files[file_id] = (file_start, file_size)
            continue

        resulting_files[file_id] = (new_start, file_size)
        gaps[file_start] = file_size

    result = [-1 for _ in expanded_disk]

    for file_id in resulting_files:
        (start, size) = resulting_files[file_id]

        for i in range(size):
            result[start+i] = file_id

    for i in range(len(result)):
        if result[i] == -1:
            continue

        acc += i*result[i]

    print(f"Second result: {acc}")

solve1()
solve2()
