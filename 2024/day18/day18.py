import heapq
import sys
import math
from collections import namedtuple

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def parse(data: str) -> list[Position]:
	l = []
	for line in split_data_on_newlines(data):
		x, y = map(int, line.split(','))
		l.append(Position(x=x, y=y))
	return l


Node = namedtuple('Node', 'h len pos')

def solve(falling_bytes: list[Position], end_pos: Position) -> int:
	valid_bytes = {Position(y=y, x=x) for x in range(end_pos.x + 1) for y in range(end_pos.y + 1)}
	for by in falling_bytes:
		valid_bytes.remove(by)
	start_pos: Position = Position(y=0, x=0)
	seen: dict[Position, int] = {start_pos: 0}
	q: list[Node] = []
	heapq.heappush(q, Node(start_pos.distance_to(end_pos), len=0, pos=start_pos))
	while q:
		node = heapq.heappop(q)
		if node.pos == end_pos:
			return node.len
		for neighbour in node.pos.get_neighbours():
			n_len = node.len + 1
			if neighbour not in valid_bytes or seen.get(neighbour, float('inf')) <= n_len:
				continue
			seen[neighbour] = n_len
			new_node = Node(h=n_len + end_pos.distance_to(neighbour), len=n_len, pos=neighbour)
			heapq.heappush(q, new_node)
	return -1


def bsearch(falling_bytes: list[Position], end_pos: Position) -> Position:
	low, high = 1, len(falling_bytes) - 1
	cutoffs = set()
	while low <= high:
		mid = (low + high) // 2
		if solve(falling_bytes[:mid + 1], end_pos) == -1:
			high = mid - 1
			cutoffs.add(mid)
		else:
			low = mid + 1
	return falling_bytes[min(cutoffs)]


def aoc(data: str, prefix: str, end_pos: Position, amount_falling_bytes: int) -> None:
	falling_bytes = parse(data)
	part1 = solve(falling_bytes[:amount_falling_bytes], end_pos)
	print(f'{prefix} part 1: {part1}')
	part2 = bsearch(falling_bytes, end_pos)
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example', end_pos=Position(y=6, x=6), amount_falling_bytes=12)
	aoc(get_input_file(), 'Solution', end_pos=Position(y=70, x=70), amount_falling_bytes=1024)
