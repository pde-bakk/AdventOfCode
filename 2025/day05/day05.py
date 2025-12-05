import sys
import math
from typing import Tuple


sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.range_analysis import analyze_ranges
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def parse(data: str) -> Tuple[list[str], list[str]]:
	ranges, ids = split_on_double_newlines(data)
	return ranges, ids


def solve(ranges: list[str], ids: list[str]) -> Tuple[int, int]:
	p1 = 0
	ranges_p2: list[range] = []
	for line in ranges:
		start, end = map(int, line.split('-'))
		ranges_p2.append(range(start, end+1))

	for line in ids:
		for r in ranges_p2:
			if r.start <= int(line) <= r.stop:
				p1 += 1
				break
	result = analyze_ranges(ranges_p2)
	return p1, result.unique_count

def aoc(data: str, _, prefix: str) -> None:
	ranges, ids = parse(data)
	part1, part2 = solve(ranges, ids)
	print(f'{prefix} part 1: {part1}, part 2: {part2}')


if __name__ == '__main__':
	program_args = parse_args()
	if 'example' in program_args.mode:
		aoc(get_example_file(), program_args, 'Example')
	if 'solution' in program_args.mode:
		aoc(get_input_file(), program_args, 'Solution')
