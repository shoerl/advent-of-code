#!/usr/bin/env python
import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"
file = open(dir_path + "input.txt", "r")
lines = file.readlines()

class BingoBoard:
    def __init__(self, lines):
        self.board_real = []
        self.board_binary = []
        for line in lines:
            temp_array_real = []
            temp_array_binary = []
            for item in line.split(' '):
                temp_array_real.push(int(item.trim()))
                temp_array_binary.push(0)
            self.board_real.push(temp_array_real)
            self.board_binary.push(temp_array_binary)

order = lines[0]
lines.remove(0)
lines.remove(1)

for line in lines



