import sys
import math

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


class Robot:
	def __init__(self, s: str):
		x, y, vx, vy = ints(s)
		self.position = Position(y=y, x=x)
		self.velocity = Direction(y=vy, x=vx)


def parse(data: str) -> list[Robot]:
	lines = split_data_on_newlines(data)
	return [Robot(line) for line in lines]


def print_map(robots: list[Robot], max_height: int, max_width: int) -> None:
	d: dict[Position, int] = {}
	for robot in robots:
		if robot.position not in d:
			d[robot.position] = 0
		d[robot.position] += 1
	for y in range(max_height):
		if map_to_binary(y, max_height) == 1:
			print()
			continue
		s = ''
		for x in range(max_width):
			if map_to_binary(x, max_width) == 1:
				s += ' '
			elif Position(y, x) in d:
				s += str(d[Position(y, x)])
			else:
				s += '.'
		print(s)
	print()

def map_to_binary(x: int, total_range: int) -> int:
	midpoint = total_range // 2
	if x < midpoint:
		return 0
	if x == midpoint:
		return 1
	return 2


def solve(robots: list[Robot], max_height: int, max_width: int, part: int = 1) -> int:
	duration = 100
	for robot in robots:
		robot.position += duration * robot.velocity
		robot.position.y %= max_height
		robot.position.x %= max_width
	print_map(robots, max_height, max_width)
	counts = { i: [0, 0, 0] for i in range(3) }
	for robot in robots:
		y = map_to_binary(robot.position.y, max_height)
		x = map_to_binary(robot.position.x, max_width)
		counts[y][x] += 1
		# print(f'{robot.position=}, {y=}, {x=}')
	result = 1
	# print(f'{counts=}')
	for y in [0, 2]:
		for x in [0, 2]:
			result *= counts[y][x]
	return result


def aoc(data: str, prefix: str, max_height: int, max_width: int) -> None:
	lines = parse(data)
	part1 = solve(lines, max_height, max_width, part=1)
	print(f'{prefix} part 1: {part1}')
	# part2 = solve(lines, part=2)
	# print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example', max_height=7, max_width=11)
	aoc(get_input_file(), 'Solution', max_height=103, max_width=101)
