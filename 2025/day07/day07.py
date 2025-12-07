import sys
import math
from typing import Tuple
from collections import defaultdict

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def parse(data: str) -> list[str]:
	lines = split_data_on_newlines(data)
	return lines


def solve(lines: list[str]) -> Tuple[int, int]:
	start_index = lines[0].index('S')
	tachyon_beams = {start_index: 1}
	splits = 0
	for line in lines[1:]:
		new_beams = defaultdict(int)
		for position in tachyon_beams:
			beam_amount = tachyon_beams[position]
			if line[position] == '^':
				new_beams[position + 1] += beam_amount
				new_beams[position - 1] += beam_amount
				splits += 1
			else:
				new_beams[position] += beam_amount
		tachyon_beams = new_beams

	return splits, sum(tachyon_beams.values())

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
