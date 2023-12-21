import sys
import math

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *
from collections import deque


def print_map_with_distances(grid: list[str], new_q: set) -> None:
	for y, line in enumerate(grid):
		new_line = ''
		for x, c in enumerate(line):
			p = Position(y, x)
			if p in new_q:
				new_line += 'O'
			else:
				new_line += c
		print(new_line)
	print(end='\n')


def bfs(grid: list[str], target_distance: int, part2: bool=False) -> int:
	height, width = len(grid), len(grid[0])
	obstacles = set([Position(y, x) for y in range(height) for x in range(width) if grid[y][x] == '#'])
	start = [Position(y, x) for y in range(height) for x in range(width) if grid[y][x] == 'S'][0]
	q = [start]

	wows = []

	for i in range(1, target_distance + 1):
		new_q = set()
		while q:
			pos = q.pop()
			for n in pos.get_neighbours(diagonal=False):
				if Position(n.y % height, n.x % width) not in obstacles:
					new_q.add(n)
		q = list(new_q)
		if (i - 65) % 131 == 0:
			wows.append(len(q))
	if part2:
		return wows
	return len(q)


def solve2(nbs: list[int]):
	# https://owlcation.com/stem/Quadratic-Sequences-The-nth-term-of-a-quadratic-number-sequence
	# https://www.radfordmathematics.com/algebra/sequences-series/difference-method-sequences/quadratic-sequences.html
	def get_differences(x: list[int]):
		result = []
		for item1, item2 in zip(x, x[1:]):
			result.append(item2 - item1)
		return result
	max_steps = 26501365
	nth_term = (max_steps - 65) // 131 + 1
	n = nth_term
	first_diffs = get_differences(nbs)
	second_diffs = get_differences(first_diffs)
	a = second_diffs[0] // 2
	b = first_diffs[0] - 3 * a
	c = nbs[0] - b - a
	return a*n**2 + b*n + c


def aoc(data: str, prefix: str) -> None:
	total = 26501365
	map_width = 131
	print((total - 65) // map_width)
	lines = split_data_on_newlines(data)
	part1 = bfs(lines, 65)
	print(f'{prefix} part 1: {part1}')
	part2 = bfs(lines, target_distance=65 + 131 * 2, part2=True)
	print(f'{part2=}')
	print(f'{prefix} part 2: {solve2(part2)}')


if __name__ == '__main__':
	# aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
