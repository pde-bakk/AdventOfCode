import re
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


def solve(data: str) -> int:
	total = 0
	muls = re.findall(r'mul\(\d+,\d+\)', data)
	for m in muls:
		a, b = ints(m)
		total += a * b
	return total

def solve2(data: str) -> int:
	total = 0
	muls = list(re.finditer(r'mul\(\d+,\d+\)', data))
	for m in muls:
		idx = m.start()
		do_idx = data.rfind('do()', 0, idx)
		dont_idx = data.rfind('don\'t()', 0, idx)
		if do_idx >= dont_idx:
			a, b = ints(m.group())
			total += a * b
	return total


def aoc(data: str, prefix: str) -> None:
	part1 = solve(data)
	part2 = solve2(data)
	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
