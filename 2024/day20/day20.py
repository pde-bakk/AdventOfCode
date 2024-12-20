import heapq
import itertools
import sys
import math
from collections import namedtuple

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def parse(data: str) -> list[str]:
	lines = split_data_on_newlines(data)
	return lines


Node = namedtuple('Node', ['h', 'len', 'cheats', 'pos'])
Cheat = namedtuple('Cheat', ['start', 'end'])


def solve(lines: list[str], part: int = 1) -> int:
	start, = find_positions_where(lines, target='S')
	end, = find_positions_where(lines, target='E')
	print(f'{start=}, {end=}')
	todo = [start]
	distances = {start: 0}
	for pos in todo:
		for nei in pos.get_neighbours(diagonal=False):
			if nei.checkvalid(lines) and lines[nei.y][nei.x] != '#' and nei not in distances:
				distances[nei] = distances[pos] + 1
				todo.append(nei)
	result = 0
	for a, b in itertools.combinations(todo, 2):
		diff = abs(distances[a] - distances[b])
		max_distance = {1: 2, 2: 20}[part]
		dist = a.distance_to(b)
		if dist <= max_distance and diff >= 100 + dist:
			result += 1
	return result


def aoc(data: str, args, prefix: str) -> None:
	lines = parse(data)
	if '1' in args.part:
		part1 = solve(lines, part=1)
		print(f'{prefix} part 1: {part1}')
	elif '2' in args.part:
		part2 = solve(lines, part=2)
		print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	program_args = parse_args()
	if 'example' in program_args.mode:
		aoc(get_example_file(), program_args, 'Example')
	if 'solution' in program_args.mode:
		aoc(get_input_file(), program_args, 'Solution')
