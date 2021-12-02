#!/usr/bin/env python
import os 
dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\"

# 1.1

file = open(dir_path + "input.txt", "r")
lines = file.readlines()
nums = list(map(int, lines))

previous = -1
output_array = []
for num in nums:
	if previous != -1 and num > previous:
		output_array.append("increased")
	previous = num
	

print(len(output_array))


# 1.2

output_array = []
for idx, num in enumerate(nums):
	if idx + 3 < len(nums) and nums[idx + 3] > num:
		output_array.append("increased")

print(len(output_array))


    			
			
    	
    	
	

