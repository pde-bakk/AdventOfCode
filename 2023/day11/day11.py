import sys
import math
import typing

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *


def expand_galaxies(lines: list[str]):
	width, height = len(lines[0]), len(lines)
	empty_row_indices = [i for i, line in enumerate(lines) if '#' not in line]
	empty_col_indices = [i for i in range(width) if '#' not in [line[i] for line in lines]]
	return empty_row_indices, empty_col_indices


def get_galaxies(lines: list[str]) -> typing.List[typing.Tuple[int, int]]:
	galaxies = []
	for y, line in enumerate(lines):
		for x, c in enumerate(line):
			if c == '#':
				galaxies.append((y, x))
	return galaxies


def solve(lines: list[str], multiplier: int) -> int:
	empty_row_indices, empty_col_indices = expand_galaxies(lines)
	galaxies = get_galaxies(lines)
	amount_galaxies = len(galaxies)
	arr = []
	for a in range(amount_galaxies):
		ay, ax = galaxies[a]
		for b in range(a + 1, amount_galaxies):
			by, bx = galaxies[b]
			d = manhattan_distance(galaxies[a], galaxies[b])
			empty_cols = 0
			for c in range(min(ax, bx), max(ax, bx)):
				if c in empty_col_indices:
					empty_cols += 1
			empty_rows = 0
			for r in range(min(ay, by), max(ay, by)):
				if r in empty_row_indices:
					empty_rows += 1
			arr.append(d + (multiplier-1) * (empty_cols + empty_rows))
	return sum(arr)


def aoc(data: str, prefix: str) -> None:
	lines = split_data_on_newlines(data)
	print(f'{prefix} part 1: {solve(lines, multiplier=2)}')
	print(f'{prefix} part 2: {solve(lines, multiplier=1_000_000)}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
