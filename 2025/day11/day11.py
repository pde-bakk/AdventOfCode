import sys
from functools import lru_cache
from typing import Tuple

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *

def parse(data: str) -> list[str]:
	lines = split_data_on_newlines(data)
	return lines

def solve(lines: list[str]) -> Tuple[int, int]:
	d = {}
	for line in lines:
		key, values = line.split(': ', maxsplit=1)
		v = values.split()
		d[key] = v

	@lru_cache(maxsize=None)
	def count(pos: str, has_dac: bool, has_fft: bool) -> int:
		if pos == 'out':
			return int(has_dac and has_fft)
		if pos == 'dac':
			has_dac = True
		if pos == 'fft':
			has_fft = True
		return sum(count(outgoing, has_dac, has_fft) for outgoing in d[pos])

	p1 = count('you', True, True)
	p2 = count('svr', False, False)
	return p1, p2

def aoc(data: str, _, prefix: str) -> None:
	lines = parse(data)
	part1, part2 = solve(lines)
	print(f'{prefix} part 1: {part1} and part 2: {part2}')


if __name__ == '__main__':
	program_args = parse_args()
	if 'example' in program_args.mode:
		aoc(get_example_file(), program_args, 'Example')
	if 'solution' in program_args.mode:
		aoc(get_input_file(), program_args, 'Solution')
