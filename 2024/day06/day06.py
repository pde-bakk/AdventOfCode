import sys
import math
from copy import copy

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def parse(data: str) -> list[str]:
	lines = split_data_on_newlines(data)
	return lines

def obstacle_in_front(pos: Position, d: Position, lines: list[str], extra_obstacle: Position = None) -> bool:
	front_pos = pos + d
	if extra_obstacle and extra_obstacle == front_pos:
		return True
	if not front_pos.isvalid(len(lines), len(lines[0])):
		return False
	return lines[front_pos.y][front_pos.x] == '#'

def print_map(lines: list[str], path: list[Position], time_paradoxes: set[Position]):
	for y, line in enumerate(lines):
		l = ''
		for x, c in enumerate(line):
			p = Position(y, x)
			if p in time_paradoxes:
				l += 'O'
			elif p in path:
				l += 'X'
			else:
				l += c
		# line = ''.join(['O' if p in time_paradoxes  else c for x, c in enumerate(line) if (p := Position(y, x))])
		print(l)
	print('\n')


def get_path(lines: list[str]):
	seen = set()
	pos = [Position(y, line.index('^')) for y, line in enumerate(lines) if ('^' in line)][0]
	path: list[Position] = [pos]
	direction = NORTH
	seen.add((pos, direction))
	time_paradoxes = set()
	while pos.isvalid(len(lines), len(lines[0])):
		if obstacle_in_front(pos, direction, lines):
			direction = direction.turn_right()
		if not obstacle_in_front(pos, direction, lines) and (pos, direction.turn_right()) in seen:
			time_paradoxes.add(pos + direction)
			print(f'Added {pos + direction}')
		seen.add((pos, direction))
		pos += direction
		path.append(pos)
		print_map(lines, path, time_paradoxes)
	return set(path), time_paradoxes

def detect_cycle(lines: list[str], extra_obstacle: Position, startpos: Position):
	pos = copy(startpos)
	seen = set()
	direction = NORTH
	seen.add((pos, direction))
	while pos.isvalid(len(lines), len(lines[0])):
		if obstacle_in_front(pos, direction, lines, extra_obstacle):
			direction = direction.turn_right()
		# if (pos, right) in seen and pos != startpos:
		# 	time_paradoxes.add(pos + direction)
		# 	print(f'{pos, right} in seen ({direction=}), added {pos + direction} to time paradoxes')
		# 	print_map(lines, time_paradoxes)

		pos += direction
		if (pos, direction) in seen:
			return True
		seen.add((pos, direction))
	return False



def solve_part2(lines: list[str], path: set[Position]):
	time_paradoxes = set()
	startpos = [Position(y, line.index('^')) for y, line in enumerate(lines) if ('^' in line)][0]
	path.remove(startpos)
	for p in path:
		if detect_cycle(lines, p, startpos):
			time_paradoxes.add(p)
	return len(time_paradoxes)


def aoc(data: str, prefix: str) -> None:
	lines = parse(data)
	path, paradoxes = get_path(lines)
	print(f'{prefix} part 1: {len(path)}')
	# part2 = solve_part2(lines, path)
	print(f'{prefix} part 2: {len(paradoxes)}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	# aoc(get_input_file(), 'Solution')
