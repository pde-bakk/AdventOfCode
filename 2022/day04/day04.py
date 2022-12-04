import re

with open('input.txt', 'r') as f:
	lines = f.read().splitlines()

part_1 = part_2 = 0
for line in lines:
	ints = [*map(int, re.findall(r'\d+', line))]
	sets = set(range(ints[0], ints[1] + 1)), set(range(ints[2], ints[3] + 1))
	if sets[0].issubset(sets[1]) or sets[0].issuperset(sets[1]):
		part_1 += 1
	if sets[0] & sets[1]:
		part_2 += 1

print(f'Part 1: {part_1}')
print(f'Part 2: {part_2}')
