import sys
import math

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def parse(data: str) -> tuple[list[int], list[int]]:
	lines = split_data_on_newlines(data)
	l1 = []
	l2 = []
	print(list(map(str.split, lines)))
	for a, b in map(str.split, lines):
		l1.append(int(a))
		l2.append(int(b))
	return l1, l2


def solve_1(l1: list[int], l2: list[int]) -> int:
	l1.sort(); l2.sort()
	return sum(abs(y - z) for y, z in zip(l1, l2))


def solve_2(l1: list[int], l2: list[int]) -> int:
	return sum(a * l2.count(a) for a in l1)

def aoc(data: str, prefix: str) -> None:
	l1, l2 = parse(data)
	part1 = solve_1(l1, l2)
	part2 = solve_2(l1, l2)
	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
