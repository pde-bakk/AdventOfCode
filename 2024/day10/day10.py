import copy
import sys
import math
from collections import namedtuple
from typing import Any

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


Node = namedtuple('Node', 'pos length')


def parse(data: str) -> list[list[int]]:
	lines = split_data_on_newlines(data)
	return [list(map(int, line)) for line in lines]


def dijkstra(lines: list[list[int]], start: Position) -> tuple[int, int]:
	q = [[start]]
	peaks: set[Position] = set()
	routes: set[tuple[Position, ...]] = set()
	while q:
		nodeq = q.pop(0)
		last = nodeq[-1]
		value = lines[last.y][last.x]
		if value == 9:
			peaks.add(last)
			routes.add(tuple(nodeq))
		for nei in last.get_neighbours(diagonal=False):
			if nei.isvalid(len(lines), len(lines[0])) and lines[nei.y][nei.x] == value + 1:
				new_l = copy.deepcopy(nodeq)
				new_l.append(nei)
				q.append(new_l)
	return len(peaks), len(routes)


def solve(lines: list[list[int]]) -> tuple[int, int]:
	trailheads = find_positions_where(grid=lines, target=0)
	part1 = part2 = 0
	for t in trailheads:
		p1, p2 = dijkstra(lines, t)
		part1 += p1
		part2 += p2
	return part1, part2


def aoc(data: str, prefix: str) -> None:
	lines = parse(data)
	part1, part2 = solve(lines)
	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
