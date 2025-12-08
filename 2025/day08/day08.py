import itertools
import sys
import math
from typing import Tuple
from collections import namedtuple

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


Point = namedtuple('Point', ['x', 'y', 'z'])
Pair = namedtuple('Pair', ['a', 'b', 'distance'])


def parse(data: str) -> list[Tuple[int, ...]]:
	lines = split_data_on_newlines(data)
	return [tuple(map(int, line.split(','))) for line in lines]


def solve(points: list[Tuple[int, ...]], amount: int) -> Tuple[int, int]:
	points = [Point(*p) for p in points]
	pairs = []
	circuits: list[set[Point]] = [{p} for p in points]
	for a, b in itertools.combinations(points, 2):
		pairs.append(Pair(a, b, distance_3d(a, b)))
	pairs.sort(key=lambda p: p.distance)

	def find(pp: Point):
		for i, c in enumerate(circuits):
			if pp in c:
				return i
		return -1
	strings = 0
	p1 = p2 = 0
	for a, b, dist in pairs:
		aid, bid = find(a), find(b)
		strings += 1
		if aid != bid:
			circuits[aid] |= circuits[bid]
			circuits.pop(bid)
			if len(circuits) == 1:
				p2 = a.x * b.x
				break
		if strings == amount:
			p1 = math.prod(len(c) for c in sorted(circuits, key=len)[-3:])
	return p1, p2

def aoc(data: str, _, prefix: str, amount: int) -> None:
	lines = parse(data)
	part1, part2 = solve(lines, amount)
	print(f'{prefix} part 1: {part1} and part 2: {part2}')


if __name__ == '__main__':
	program_args = parse_args()
	if 'example' in program_args.mode:
		aoc(get_example_file(), program_args, 'Example', 10)
	if 'solution' in program_args.mode:
		aoc(get_input_file(), program_args, 'Solution', 1000)
