import math
import sys
sys.path.append('../..')
from aoc_lib.get_input import get_input_file
from aoc_lib.utilities import *

lines = get_input_file()
# lines = open('sample.txt').read().splitlines()
print(lines)
part1 = 0
d = {i: 1 for i in range(len(lines))}
for i, line in enumerate(lines):
	_, tickets = line.split(':')
	a, b = tickets.split('|')
	a = list(map(int, a.split()))
	b = list(map(int, b.split()))
	winning_nbs = [x for x in b if x in a]
	if winning_nbs:
		part1 += 2 ** (len(winning_nbs) - 1)
print(part1)
part2 = 0
for i, line in enumerate(lines):
	_, tickets = line.split(':')
	a, b = tickets.split('|')
	a = list(map(int, a.split()))
	b = list(map(int, b.split()))
	winning_nbs = [x for x in b if x in a]
	for i2 in range(i+1, i + 1 + len(winning_nbs)):
		d[i2] += 1 * d[i]
print(sum(d.values()))
