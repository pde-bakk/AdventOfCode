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


def solve(lines: list[str], battery_amount: int) -> int:
	total_output_joltage = 0
	for line in lines:
		joltage = ''
		for i in range(battery_amount - 1, -1, -1):
			joltage += max(line) if i == 0 else max(line[:-i])
			line = line[line.index(joltage[-1])+1:]
		total_output_joltage += int(joltage)
	return total_output_joltage


def aoc(data: str, args, prefix: str) -> None:
	lines = parse(data)
	part1 = solve(lines, battery_amount=2)
	part2 = solve(lines, battery_amount=12)
	print(f'{prefix} part 1: {part1} and part 2: {part2}')


if __name__ == '__main__':
	program_args = parse_args()
	if 'example' in program_args.mode:
		aoc(get_example_file(), program_args, 'Example')
	if 'solution' in program_args.mode:
		aoc(get_input_file(), program_args, 'Solution')
