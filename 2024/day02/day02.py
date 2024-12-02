import sys
import math

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def parse(data: str) -> list[list[int]]:
	lines = split_data_on_newlines(data)
	return [list(map(int, line.split())) for line in lines]


def issafe(line: list[int]) -> bool:
	alldec = True
	allinc = True
	for a, b in zip(line, line[1:]):
		if abs(a - b) < 1 or abs(a - b) > 3:
			alldec = False
			allinc = False
		if a <= b:
			alldec = False
		if b <= a:
			allinc = False
	return alldec or allinc


def solve(lines: list[list[int]], part: int) -> int:
	cunt = 0
	for line in lines:
		if issafe(line):
			cunt += 1
		elif part == 2:
			for i, _ in enumerate(line):
				l = line.copy()
				l.pop(i)
				if issafe(l):
					cunt += 1
					break

	return cunt


def aoc(data: str, prefix: str) -> None:
	lines = parse(data)
	part1 = solve(lines, part=1)
	part2 = solve(lines, part=2)
	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
