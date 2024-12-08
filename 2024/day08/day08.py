import itertools
import sys
import math

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def parse(data: str) -> list[str]:
	lines = split_data_on_newlines(data)
	return lines


def print_map(lines: list[str], antinodes: set[Position]):
	for y, line in enumerate(lines):
		s = ''.join('#' if Position(y, x) in antinodes else c for x, c in enumerate(line))
		print(s)

def solve(lines: list[str], part: int = 2) -> int:
	max_y, max_x = len(lines), len(lines[0])
	d: dict[str,list] = {}
	antinodes = set()
	for y, line in enumerate(lines):
		for x, c in enumerate(line):
			if c == '.':
				continue
			d[c] = d.get(c, []) + [Position(y, x)]
	for c, l in d.items():
		for pos_a, pos_b in itertools.combinations(l, 2):
			delta = pos_b - pos_a
			pos_c = pos_a - delta
			pos_d = pos_b + delta
			if part == 2:
				antinodes.add(pos_a)
				antinodes.add(pos_b)
				while pos_c.isvalid(max_y, max_x):
					antinodes.add(pos_c)
					pos_c -= delta
				while pos_d.isvalid(max_y, max_x):
					antinodes.add(pos_d)
					pos_d += delta
			else:
				if pos_c.isvalid(max_y, max_x):
					antinodes.add(pos_c)
				if pos_d.isvalid(max_y, max_x):
					antinodes.add(pos_d)
	return len(antinodes)


def aoc(data: str, prefix: str) -> None:
	lines = parse(data)
	part1 = solve(lines, part=1)
	part2 = solve(lines, part=2)
	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
