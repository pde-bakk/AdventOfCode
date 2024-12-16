import gzip
import itertools
import os
import sys
import math
from copy import deepcopy, copy

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


def create_robot_dict(robots: list[Robot]) -> dict[Position, int]:
	robot_dict: dict[Position, int] = {}
	for robot in robots:
		if robot.position not in robot_dict:
			robot_dict[robot.position] = 0
		robot_dict[robot.position] += 1
	return robot_dict


def print_map(robot_dict: dict[Position, int], max_height: int, max_width: int) -> str:
	s = ''
	for y in range(max_height):
		for x in range(max_width):
			s += str(robot_dict.get(Position(y=y, x=x), '.'))
		s += '\n'
	return s + '\n'


def map_to_binary(x: int, total_range: int) -> int:
	midpoint = total_range // 2
	if x < midpoint:
		return 0
	if x == midpoint:
		return 1
	return 2


def p1(robots: list[Robot], max_height: int, max_width: int) -> int:
	duration = 100
	p1_robots: list[Robot] = [copy(robot) for robot in robots]
	for robot in p1_robots:
		robot.position += duration * robot.velocity
		robot.position.y %= max_height
		robot.position.x %= max_width
	counts = { i: [0, 0, 0] for i in range(3) }
	for robot in p1_robots:
		y = map_to_binary(robot.position.y, max_height)
		x = map_to_binary(robot.position.x, max_width)
		counts[y][x] += 1
	result = 1
	for y in [0, 2]:
		for x in [0, 2]:
			result *= counts[y][x]
	return result


def p2(robots: list[Robot], max_height: int, max_width: int) -> int:
	smallest = 0, float('inf')
	offset = 1
	for iteration in itertools.count(start=1):
		new_robots = [robot for robot in robots]
		for robot in new_robots:
			robot.position += robot.velocity
			robot.position.y %= max_height
			robot.position.x %= max_width
		robot_dict = create_robot_dict(new_robots)
		if len(robot_dict) == len(new_robots):
			gridmap = print_map(robot_dict, max_height, max_width)
			x = len(gzip.compress(bytes(gridmap, 'utf-8')))
			if x < smallest[1]:
				smallest = (iteration, x)
				print(f'So far, iteration {iteration * offset} is the smallest with compressed size of {x}')
			with open(f'/tmp/robots/{iteration}', 'w') as f:
				f.write(f'gzipped encoded this has size: {x}\n\n')
				f.write(gridmap)
			if x < 500:
				return iteration
		iteration += 1


def aoc(data: str, prefix: str, max_height: int, max_width: int) -> None:
	os.mkdir('/tmp/robots/')
	lines = parse(data)
	part1 = p1(lines, max_height, max_width)
	print(f'{prefix} part 1: {part1}')
	part2 = p2(lines, max_height, max_width)
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example', max_height=7, max_width=11)
	aoc(get_input_file(), 'Solution', max_height=103, max_width=101)
