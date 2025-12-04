import sys
import math
from typing import Tuple

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def parse(data: str) -> list[str]:
	lines = split_data_on_newlines(data)
	return lines


def solve(lines: list[list[str]], part: int) -> int:
	total = 0
	removed = True
	while removed:
		removed = False
		for y, line in enumerate(lines):
			for x, char in enumerate(line):
				if char != '@':
					continue
				pos = Position(y, x)
				count = 0
				for n in pos.get_neighbours(diagonal=True):
					if n.isvalid(len(lines), len(line)) and lines[n.y][n.x] == '@':
						count += 1
				if count < 4:
					total += 1
					if part == 2:
						lines[y][x] = '.'
						removed = True
	return total

def aoc(data: str, _, prefix: str) -> None:
	lines = parse(data)
	lines = [list(line) for line in lines]
	part1 = solve(lines, part=1)
	part2 = solve(lines, part=2)
	print(f'{prefix} part 1: {part1} and part 2: {part2}')


if __name__ == '__main__':
	program_args = parse_args()
	if 'example' in program_args.mode:
		aoc(get_example_file(), program_args, 'Example')
	if 'solution' in program_args.mode:
		aoc(get_input_file(), program_args, 'Solution')
