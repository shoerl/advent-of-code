#!/usr/bin/env python
import os 

dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\"
file = open(dir_path + "input.txt", "r")
lines = file.readlines()

# 2.1

def break_line(line):
    pair = line.split(' ')
    return pair[0], int(pair[1])

pairs = list(map(break_line, lines))

translations = { 'down': 1, 'up': -1 }

horizontal_pos, depth = 0, 0

for pair in pairs:
    command, amount = pair[0], pair[1]
    if command == 'forward':
        horizontal_pos += amount
    else:
        depth += (translations[command] * amount)
    
print(horizontal_pos * depth)

# 2.2

aim, horizontal_pos, depth = 0, 0, 0

for pair in pairs:
    command, amount = pair[0], pair[1]
    if command == 'forward':
        horizontal_pos += amount
        depth += (amount * aim)
    else:
        aim += (translations[command] * amount)

print(horizontal_pos * depth)