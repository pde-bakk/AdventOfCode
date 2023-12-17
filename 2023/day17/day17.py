import heapq
import sys
import math

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def pathfind(lines: list[list[int]], min_straightline: int, max_straightline: int) -> int:
	width, height = len(lines[0]), len(lines)
	q = [(0, 0, (0, 0), (0, 0))]
	heapq.heapify(q)
	goal = (height - 1, width - 1)
	seen = {}
	while q:
		cost_plus_dist, cost, position, old_direction = heapq.heappop(q)
		if position == goal:
			return cost
		for d in [SOUTH, EAST, NORTH, WEST]:
			added_cost = 0
			if lmap(abs, d) == lmap(abs, old_direction):
				continue
			y, x = position
			for dist in range(1, max_straightline + 1):
				ny, nx = y + d[0] * dist, x + d[1] * dist
				if 0 <= ny < height and 0 <= nx < width:
					newpos = ny, nx
					added_cost += lines[ny][nx]
					if dist < min_straightline:
						continue
					new_cost = cost + added_cost
					if seen.get((newpos, d), new_cost + 1) <= new_cost:
						continue
					seen[(newpos, d)] = new_cost
					heapq.heappush(q, (new_cost + manhattan_distance(newpos, goal), new_cost, newpos, d))
	return 0


def aoc(data: str, prefix: str) -> None:
	lines = [list(map(int, line)) for line in split_data_on_newlines(data)]
	part1 = pathfind(lines, 1, 3)
	part2 = pathfind(lines, 4, 10)
	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
