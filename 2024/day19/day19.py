import heapq
import sys
import math
from collections import namedtuple
from functools import lru_cache

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def parse(data: str) -> tuple[ set[str], list[str]]:
	patterns, designs = split_on_double_newlines(data)
	patterns = set(patterns[0].split(', '))
	return patterns, designs


def solve(patterns: set[str], designs: list[str], part: int = 1) -> int:
	@lru_cache(maxsize=None)
	def amount_combinations(design_left: str) -> int:
		if design_left == '':
			return 1
		x = 0
		for pattern in patterns:
			if design_left.startswith(pattern):
				amount = amount_combinations(design_left[len(pattern):])
				x += amount
		return x

	possible = 0
	for d in designs:
		a = amount_combinations(d)
		if part == 1:
			possible += int(a > 0)
		else:
			possible += a
	return possible


def aoc(data: str, prefix: str) -> None:
	patterns, designs = parse(data)
	part1 = solve(patterns, designs, part=1)
	print(f'{prefix} part 1: {part1}')
	part2 = solve(patterns, designs, part=2)
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
