import copy
import sys
import math
from collections import namedtuple

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


Node = namedtuple('Node', 'pos length')


def parse(data: str) -> list[list[int]]:
	lines = split_data_on_newlines(data)
	return [list(map(int, line)) for line in lines]



def astar2(lines: list[list[int]], start: Position) -> int:
	q = [[start]]
	# seen = {start}
	reachable: set = set()
	max_value = 0
	while q:
		nodeq = q.pop(0)
		last = nodeq[-1]
		value = lines[last.y][last.x]
		if value == 9:
			reachable.add(tuple(nodeq))
		for nei in last.get_neighbours(diagonal=False):
			if nei.isvalid(len(lines), len(lines[0])) and lines[nei.y][nei.x] == value + 1:
				new_l = copy.deepcopy(nodeq)
				new_l.append(nei)
				q.append(new_l)
				# seen.add(nei)
	print(f'{reachable=}')
	return len(reachable)


def astar(lines: list[list[int]], start: Position) -> int:
	q = [Node(pos=start, length=0)]
	seen = {start}
	reachable = set()
	while q:
		node = q.pop(0)
		value = lines[node.pos.y][node.pos.x]
		if value == 9:
			reachable.add(node.pos)
		for nei in node.pos.get_neighbours(diagonal=False):
			if nei not in seen and nei.isvalid(len(lines), len(lines[0])) and lines[nei.y][nei.x] == value + 1:
				q.append(Node(pos=nei, length=node.length + 1))
				seen.add(nei)
	print(f'{reachable=}')
	return len(reachable)

def solve(lines: list[list[int]], part: int = 1) -> int:
	trailheads = []
	result = 0
	for y, line in enumerate(lines):
		for x, i in enumerate(line):
			if i == 0:
				trailheads.append(Position(y=y, x=x))
	print(f'{trailheads=}')
	for t in trailheads:
		if part == 1:
			result += astar(lines, t)
		else:
			result += astar2(lines, t)
	return result


def aoc(data: str, prefix: str) -> None:
	lines = parse(data)
	part1 = solve(lines, part=1)
	part2 = solve(lines, part=2)
	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
