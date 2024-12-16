import heapq
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


Node = namedtuple('Node', 'score pos dir path')


def visualize(lines, path) -> None:
	for y, line in enumerate(lines):
		s = ''
		for x, c in enumerate(line):
			if Position(y, x) in path:
				s += 'o'
			else:
				s += c
		print(s)
	print()

def solve(lines: list[str], part: int = 1) -> int:
	start, = find_positions_where(lines, target='S')
	end, = find_positions_where(lines, target='E')
	seen = {(start, EAST): 0}
	q = []
	best_tiles = {start, end}
	best_score = float('inf')
	heapq.heappush(q, Node(pos=start, dir=EAST, score=0, path=[start]))
	while q:
		node = heapq.heappop(q)
		assert node.pos.index(lines) != '#'
		if node.pos == end:
			if part == 1:
				return node.score
			if node.score > best_score:
				break
			best_score = node.score
			best_tiles.update(node.path)
		for d, extra_score in [(node.dir, 1), (node.dir.turn_left(), 1001), (node.dir.turn_right(), 1001)]:
			nei = node.pos + d
			if not nei.checkvalid(lines) or nei.index(lines) == '#':
				continue
			if seen.get((nei, d), float('inf')) < node.score + extra_score:
				continue
			seen[(nei, d)] = node.score + extra_score
			heapq.heappush(q, Node(pos=nei, dir=d, score=node.score + extra_score, path=node.path.copy() + [nei]))
	return len(best_tiles)

def aoc(data: str, prefix: str) -> None:
	lines = parse(data)
	part1 = solve(lines, part=1)
	print(f'{prefix} part 1: {part1}')
	part2 = solve(lines, part=2)
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
