import sys
from typing import Tuple

import math

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def parse(data: str) -> list[str]:
	lines = data.rstrip('\n').split(',')
	return lines


def solve(lines: list[str]) -> Tuple[int, int]:
	p1 = p2 = 0
	for line in lines:
		start, end = map(int, line.split('-'))
		for nb in range(start, end + 1):
			if re.fullmatch(r'(\d+)\1', str(nb)):
				p1 += nb
			if re.fullmatch(r'(\d+)\1+', str(nb)):
				p2 += nb
	return p1, p2

def aoc(data: str, args, prefix: str) -> None:
	lines = parse(data)
	part1, part2 = solve(lines)
	print(f'{prefix} part 1: {part1}, part 2: {part2}')

if __name__ == '__main__':
	program_args = parse_args()
	if 'example' in program_args.mode:
		aoc(get_example_file(), program_args, 'Example')
	if 'solution' in program_args.mode:
		aoc(get_input_file(), program_args, 'Solution')
