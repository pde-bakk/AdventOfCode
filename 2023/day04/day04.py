import sys
import math

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *


def aoc(data: str, prefix: str) -> None:
	lines = split_data_on_newlines(data)
	part1 = 0
	d = {i: 1 for i in range(len(lines))}
	for i, line in enumerate(lines):
		_, tickets = line.split(':')
		a, b = tickets.split('|')
		winning_nbs = len(set(a.split()) & set(b.split()))
		if winning_nbs:
			part1 += 2 ** (winning_nbs - 1)
		for i2 in range(i+1, i + 1 + winning_nbs):
			d[i2] += 1 * d[i]
	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {sum(d.values())}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
