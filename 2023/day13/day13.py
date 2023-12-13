import sys
import math
import numpy as np
sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import split_on_double_newlines_instead


def check_equality(p: np.ndarray, x: int) -> bool:
	width, height = len(p[0]), len(p)
	length = min(x, width - x)
	arr = [p[y][x + x2] == p[y][x - x2 - 1] for y in range(height) for x2 in range(length)]
	return all(arr)


def check_for_i(p: np.ndarray):
	width, height = len(p[0]), len(p)
	for i in range(1, width):
		if check_equality(p, i):
			print(f'equal for {i=}')
			return i
	return 0


def aoc(lines: list[str], prefix: str) -> None:
	patterns = split_on_double_newlines_instead(lines)
	part1 = 0
	part2 = 0
	for i, p in enumerate(patterns):
		print(p)
		data = np.array([list(r) for r in p])
		horizontal = check_for_i(data)
		vertical = check_for_i(data.T)
		print(f'For pattern {i}, {horizontal=}, {vertical=}')
		part1 += horizontal + 100 * vertical
	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
