import math
import sys
sys.path.append('../..')
from aoc_lib.get_input import get_input_file
from aoc_lib.utilities import *

lines = get_input_file()
part1 = 0
part2 = 0
d = {i: 1 for i in range(len(lines))}
for i, line in enumerate(lines):
	_, tickets = line.split(':')
	a, b = tickets.split('|')
	winning_nbs = len(set(a.split()) & set(b.split()))
	if winning_nbs:
		part1 += 2 ** (winning_nbs - 1)
	for i2 in range(i+1, i + 1 + winning_nbs):
		d[i2] += 1 * d[i]
print(f'Part 1: {part1}')
print(f'Part 2: {sum(d.values())}')
