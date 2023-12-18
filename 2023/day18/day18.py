import copy
import sys
import math
import shapely

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def parse_line(line: str) -> tuple[str, int, int]:
	a, b, c = line.split()
	return a, int(b), int(c[2:-1], 16)


def parse_line2(line: str) -> tuple[str, int, int]:
	a, b, c = line.split()
	return 'RDLU'[int(c[-2])], int(c[2:-2], 16), 0


def solve(lines: list[str], part2: bool) -> int:
	pos = Position(0, 0)
	x_positions = [0]
	y_positions = [0]
	total_length = 0
	for direction, dist, _ in map([parse_line, parse_line2][part2], lines):
		d = {'U': NORTH, 'D': SOUTH, 'R': EAST, 'L': WEST}[direction]
		pos += d * dist
		total_length += dist
		x_positions.append(pos.x)
		y_positions.append(pos.y)

	pgon = shapely.geometry.Polygon(zip(x_positions, y_positions))
	return int(pgon.area) + total_length // 2 + 1


def aoc(data: str, prefix: str) -> None:
	lines = split_data_on_newlines(data)
	part1 = solve(lines, part2=False)
	part2 = solve(lines, part2=True)
	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
