import sys
import math

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def parse(data: str) -> list[list[str]]:
	lines = split_on_double_newlines(data)
	return lines

def convert(l: list[str]) -> list[int]:
	rotated = [''.join(x) for x in zip(*l[1:-1])]
	return [line.count('#') for line in rotated]

def fit(key: list[int], lock: list[int]) -> bool:
	# Doesn't have to fit perfectly, just has to not overlap
	return all(a + b <= 5 for a, b in zip(key, lock))

def solve(parts: list[list[str]]) -> int:
	keys = []
	locks = []
	for x in parts:
		o = convert(x)
		if '#' in x[0]:
			locks.append(o)
		else:
			keys.append(o)
	return sum(fit(key, lock) for lock in locks for key in keys)

def aoc(data: str, prefix: str) -> None:
	# Day 25 never has a part 2
	lines = parse(data)
	part1 = solve(lines)
	print(f'{prefix}: {part1}')


if __name__ == '__main__':
	program_args = parse_args()
	if 'example' in program_args.mode:
		aoc(get_example_file(), 'Example')
	if 'solution' in program_args.mode:
		aoc(get_input_file(), 'Solution')
