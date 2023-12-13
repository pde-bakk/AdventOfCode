import sys
import math
import numpy as np
sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import split_on_double_newlines_instead


def check_equality(p: np.ndarray, x: int, p2) -> bool:
	width, height = len(p[0]), len(p)
	length = min(x, width - x)
	arr = [p[y][x + x2] == p[y][x - x2 - 1] for y in range(height) for x2 in range(length)]
	if p2:
		return len(arr) - sum(arr) == 1
	return all(arr)


def check_for_i(p: np.ndarray, p2):
	width, height = len(p[0]), len(p)
	for i in range(1, width):
		if check_equality(p, i, p2):
			return i
	return 0


def aoc(lines: list[str], prefix: str) -> None:
	patterns = split_on_double_newlines_instead(lines)
	part1 = 0
	part2 = 0
	for i, p in enumerate(patterns):
		data = np.array([list(r) for r in p])
		horizontal = check_for_i(data, False)
		vertical = check_for_i(data.T, False)
		part1 += horizontal + 100 * vertical

		horizontal = check_for_i(data, True)
		vertical = check_for_i(data.T, True)
		part2 += horizontal + 100 * vertical

	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
