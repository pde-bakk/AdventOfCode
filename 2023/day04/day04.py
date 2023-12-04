import math
import sys
sys.path.append('../..')
from aoc_lib.get_input import get_input_file
from aoc_lib.utilities import *

lines = get_input_file()
# lines = open('sample.txt').read().splitlines()
print(lines)
part1 = 0
for line in lines:
	_, tickets = line.split(':')
	a, b = tickets.split('|')
	a = list(map(int, a.split()))
	b = list(map(int, b.split()))
	winning_nbs = [x for x in b if x in a]
	if winning_nbs:
		part1 += 2 ** (len(winning_nbs) - 1)
print(part1)
