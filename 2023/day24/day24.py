import sys
import math

from collections import namedtuple

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *

Hail = namedtuple('Hail', 'x y z dx dy dz')


def parse(data: str) -> list[Hail]:
	lines = split_data_on_newlines(data)
	arr = []
	for line in lines:
		pos, delta = line.split(' @ ')
		x, y, z = lmap(int, pos.split(', '))
		dx, dy, dz = lmap(int, delta.split(', '))
		arr.append(Hail(x, y, z, dx, dy, dz))
	return arr


def get_slope(h: Hail) -> float:
	if h.dx == 0:
		return float('inf')
	return h.dy / h.dx


def get_intersection(a: Hail, b: Hail):
	c = a.dx * b.dy - b.dx * a.dy
	# print(f'c={c}, want {a.dx * b.dy} - {b.dx * a.dy}')
	if c < 0.01:
		# No Intersection
		return None
	# wa = a.x * (a.y + a.dy) - a.y * (a.x + a.dx)
	# wb = b.x * (b.y + b.dy) - b.y * (b.x + b.dx)
	# x = (wa * b.dx - wb * a.dx) / c
	# y = (wa * b.dy - wb * a.dy) / c
	wa = a.y * (a.x + a.dx) - a.x * (a.y + a.dy)
	wb = b.y * (b.x + b.dx) - b.x * (b.y + b.dy)
	x = (wa * b.dx - wb * a.dx) / c
	y = (wa * b.dy - wb * a.dy) / c
	# x = dx * t + x0
	# (x - x0) = dx * t
	# t = (x - x0) / dx
	t1 = (x - a.x) / a.dx
	t2 = (x - b.x) / b.dx
	print(f'{t1=}, {t2=}')
	if t1 <= 0 or t2 <= 0:
		# Not in the future
		return None
	return x, y


def solve(lines: list[Hail], test_area: tuple[int, int]) -> int:
	tmin, tmax = test_area
	# a, b, *rest = lines
	counts = 0
	for i, a in enumerate(lines):
		for i2, b in enumerate(lines[i + 1:]):
			print(f'{a=}')
			print(f'{b=}')
			intersection = get_intersection(a, b)
			if intersection:
				x, y = intersection
				print(f'Intersection is at {x=}, {y=}')
				if tmin <= x <= tmax and tmin <= y <= tmax:
					counts += 1
					print(f'Intersection is within the bounds')
	return counts


def aoc(data: str, prefix: str, test_area) -> None:
	lines = parse(data)
	# Higher than 15344
	part1 = solve(lines, test_area)
	part2 = 0
	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example', test_area=(7, 27))
	aoc(get_input_file(), 'Solution', test_area=(200000000000000, 400000000000000))
