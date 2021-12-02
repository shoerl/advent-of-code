#!/usr/bin/env python

# 1.1
file = open("input.txt", "r")
lines = file.readlines()

previous = -1
output_array = []
for line in lines:
	current = int(line.strip())
	if previous == -1 or current == previous:
		output_array.append("N/A")
	elif current > previous:
		output_array.append("increased")
	else:
		output_array.append("decreased")
	previous = current
	

print(output_array.count("increased"))


# 1.2

	



