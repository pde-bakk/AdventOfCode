import sys
import math
import typing

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *


def parse_input(lines: list[str]) -> typing.Tuple[str, dict[str, dict[str, str]]]:
	instr, _, *nodes = lines
	d = {}
	for node in nodes:
		node = replace_all(node, '(),')
		key, _, left, right = node.split()
		d[key] = {'L': left, 'R': right}
	return instr, d


def p1(instr, d, key='AAA') -> int:
	part1 = 0
	while key != 'ZZZ':
		x = instr[part1 % len(instr)]
		key = d[key][x]
		part1 += 1
	return part1


def p2_route(instr, d, key) -> int:
	i = 0
	while not key.endswith('Z'):
		x = instr[i % len(instr)]
		key = d[key][x]
		i += 1
	return i


def aoc(data: str, prefix: str) -> None:
	lines = split_data_on_newlines(data)
	instr, d = parse_input(lines)
	print(f'{prefix} part 1: {p1(instr, d)}')

	p2_dists = [p2_route(instr, d, key) for key in d if key.endswith('A')]
	print(f'{prefix} part 2: {math.lcm(*p2_dists)}')


if __name__ == '__main__':
	# aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
