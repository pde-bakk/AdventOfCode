import sys
import math

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


slopes = {
	'>': EAST,
	'<': WEST,
	'v': SOUTH,
	'^': NORTH
}


def measure(edges, start, head):
	count = 1
	print(f'measure, {head=}')
	while len(edges[head]) == 2:
		count += 1
		next_head = [n for n, dist in edges[head] if n != start][0]
		start, head = head, next_head
	return count, head


def new_bfs(edges, lines):
	width, height = len(lines[0]), len(lines)
	start = Position(0, lines[0].index('.'))
	goal = Position(height - 1, lines[-1].index('.'))
	q = [(start, 0)]
	seen = set()
	routes = []
	while q:
		pos, dist = q.pop()
		if dist == -1:
			seen.remove(pos)
			continue
		if pos == goal:
			routes.append(dist)
			continue
		if pos in seen:
			continue
		seen.add(pos)
		q.append((pos, -1))
		for n, nd in edges[pos]:
			q.append((n, dist + nd))
	return max(routes)


def setup_edges(lines: list[str]):
	width, height = len(lines[0]), len(lines)
	start = Position(0, lines[0].index('.'))
	goal = Position(height - 1, lines[-1].index('.'))
	edges = {}
	for y in range(height):
		for x in range(width):
			pos = Position(y, x)
			if lines[y][x] == '#':
				continue
			for n in pos.get_neighbours():
				if not (0 <= n.y < height and 0 <= n.x < width):
					continue
				if lines[n.y][n.x] != '#':
					edges[pos] = edges.get(pos, set()) | {(n, 1)}
					edges[n] = edges.get(n, set()) | {(pos, 1)}
	while True:
		for node, edg in edges.items():
			if len(edg) == 2:
				a, b = edg
				if node == start:
					print(f'{node=}, {a=}, {b=}')
				na, dist_a = a
				nb, dist_b = b
				# (na, dist_a), (nb, dist_b) = edg
				edges[na].remove( (node, dist_a))
				edges[nb].remove( (node, dist_b))
				edges[na].add( (nb, dist_a + dist_b))
				edges[nb].add( (na, dist_a + dist_b))
				del edges[node]
				break
		else:
			break
	print(new_bfs(edges, lines))


def bfs(lines: list[str]) -> int:
	width, height = len(lines[0]), len(lines)
	start = [Position(0, x) for x in range(width) if lines[0][x] == '.'][0]
	goal = [Position(height - 1, x) for x in range(width) if lines[height-1][x] == '.'][0]
	q = [(start, set())]
	routes = []
	while q:
		node, seen = q.pop(0)
		tile = lines[node.y][node.x]
		if node == goal:
			routes.append(len(seen))
			continue
		# elif tile in slopes:
		# 	n = node + slopes[tile]
		# 	if n not in seen and lines[n.y][n.x] != '#':
		# 		q.append((n, seen | {n}))
		elif tile != '#':
			for n in node.get_neighbours():
				if n not in seen and lines[n.y][n.x] != '#':
					q.append((n, seen | {n}))
	print(f'Possible route lengths: {sorted(routes)}')
	return max(routes)


def aoc(data: str, prefix: str) -> None:
	lines = split_data_on_newlines(data)
	# part1 = bfs(lines)
	part2 = 0
	setup_edges(lines)
	# print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	# aoc(get_input_file(), 'Solution')
