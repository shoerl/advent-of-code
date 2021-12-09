#!/usr/bin/env python
import os 

dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\"
file = open(dir_path + "input.txt", "r")
lines = file.readlines()

def lines_to_bit_arrays(lines):
    bit_arrays = []
    for line in lines:
        bits = list(line)
        if "\n" in bits:
            bits.remove("\n")
        bit_arrays.append(list(map(int, bits)))
    return bit_arrays

bit_arrays = lines_to_bit_arrays(lines)

# 3.1
count = []
for bit in bit_arrays[0]:
    count.append(0)

for bit_array in bit_arrays:
    for idx, bit in enumerate(bit_array):
        if bit == 0:
            count[idx] -= 1
        elif bit == 1:
            count[idx] += 1

gamma = []
epsilon = []
for num in count:
    if num > 0:
        gamma.append(1)
        epsilon.append(0)
    elif num < 0:
        gamma.append(0)
        epsilon.append(1)

gamma = int("".join([str(int) for int in gamma]), 2)
epsilon = int("".join([str(int) for int in epsilon]), 2)

# 3.2

def get_rating(if_zero, if_one):
    bit_arrays = lines_to_bit_arrays(lines)
    ii = 0
    array_to_search = bit_arrays
    while len(array_to_search) != 1:
        count = 0
        for bit_line in array_to_search:
            if bit_line[ii] == 0:
                count -= 1
            elif bit_line[ii] == 1:
                count += 1
        if count < 0:
            search_for = if_zero
        else:
            search_for = if_one
        temp_array = []
        for bit_line in array_to_search:
            if bit_line[ii] == search_for:
                temp_array.append(bit_line)
        array_to_search = temp_array
        ii += 1

    return int("".join([str(int) for int in array_to_search[0]]), 2)

oxygen_rating = get_rating(0, 1)
co2_rating = get_rating(1, 0) 
print(oxygen_rating * co2_rating)

