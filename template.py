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


def solve(lines: list[str], part: int = 1) -> int:
	result = 0
	return result


def aoc(data: str, args, prefix: str) -> None:
	lines = parse(data)
	if 1 in args.part:
		part1 = solve(lines, part=1)
		print(f'{prefix} part 1: {part1}')
	if 2 in args.part:
		part2 = solve(lines, part=2)
		print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	program_args = parse_args()
	if 'example' in program_args.mode:
		aoc(get_example_file(), program_args, 'Example')
	if 'solution' in program_args.mode:
		aoc(get_input_file(), program_args, 'Solution')
