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
	# c = a.dx * b.dy - b.dx * a.dy
	# # print(f'c={c}, want {a.dx * b.dy} - {b.dx * a.dy}')
	# if c < 0.01:
	# 	# No Intersection
	# 	return None
	# wa = a.y * (a.x + a.dx) - a.x * (a.y + a.dy)
	# wb = b.y * (b.x + b.dx) - b.x * (b.y + b.dy)
	# x = (wa * b.dx - wb * a.dx) / c
	# y = (wa * b.dy - wb * a.dy) / c
	# in_future = ((x - a.x) > 0) == (a.dx > 0) and ((x - b.x) > 0) == (b.dx > 0)
	# return in_future, x, y

	slope_a, slope_b = get_slope(a), get_slope(b)
	if math.isclose(slope_a, slope_b):
		return None
	ayi = a.y - slope_a * a.x
	byi = b.y - slope_b * b.x
	x = (byi - ayi) / (slope_a - slope_b)
	y = slope_a * (byi - ayi) / (slope_a - slope_b) + ayi

	in_future = True
	for c in [a,b]:
		dx, dy = x - c.x, y - c.y
		if (dx > 0) != (c.dx > 0) or (dy > 0) != (c.dy > 0):
			in_future = False
	return in_future, x, y


def solve(lines: list[Hail], test_area: tuple[int, int]) -> int:
	tmin, tmax = test_area
	# a, b, *rest = lines
	counts = 0
	for i, a in enumerate(lines):
		for i2, b in enumerate(lines[i + 1:]):
			intersection = get_intersection(a, b)
			print(f'{a=}, {b=}')
			if intersection:
				in_future, x, y = intersection
				within_bounds = (tmin <= x <= tmax and tmin <= y <= tmax)
				print(f'Intersection will be {["outside", "inside"][within_bounds]} bounds at {x=}, {y=}, {in_future=}')
				if in_future and within_bounds:
					counts += 1
					# print(f'Intersection is within the bounds')
			else:
				print('No intersection')
			print()
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
