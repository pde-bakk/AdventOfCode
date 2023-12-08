import sys
import math
import typing
import numpy as np

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import split_on_double_newlines_instead


def parse_input(lines: list[str]) -> typing.Tuple[str, dict[str, dict[str, str]] ]:
	instr, _, *nodes = lines
	d = {}
	for node in nodes:
		for c in ',()':
			node = node.replace(c, '')
		key, _, left, right = node.split()
		d[key] = {'L': left, 'R': right}
	return instr, d


def p1(instr, d, key='AAA'):
	part1 = 0
	while key != 'ZZZ':
		x = instr[part1 % len(instr)]
		key = d[key][x]
		part1 += 1
	return part1


def p2_route(instr, d, key):
	i = 0
	while key[-1] != 'Z':
		x = instr[i % len(instr)]
		key = d[key][x]
		i += 1
	return i


def aoc(lines: list[str], prefix: str) -> None:
	instr, d = parse_input(lines)
	print(f'{prefix} part 1: {p1(instr, d)}')

	p2_dists = [p2_route(instr, d, key) for key in d if key[-1] == 'A']
	print(p2_dists, np.lcm.reduce(p2_dists))
	part2 = np.lcm.reduce(p2_dists)

	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	# aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
