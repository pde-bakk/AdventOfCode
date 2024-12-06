import sys
import math
from copy import copy
from typing import List, Set

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


def get_path(lines: list[str]) -> Set[Position]:
	seen = set()
	pos = [Position(y, line.index('^')) for y, line in enumerate(lines) if ('^' in line)][0]
	# path: list[Position] = [pos]
	direction = NORTH
	seen.add(pos)
	while pos.isvalid(len(lines), len(lines[0])):
		if obstacle_in_front(pos, direction, lines):
			direction = direction.turn_right()
		pos += direction
		if pos.isvalid(len(lines), len(lines[0])):
			seen.add(pos)
		# path.append(pos)
		# print_map(lines, path, time_paradoxes)
	return seen

def detect_cycle(lines: list[str], extra_obstacle: Position, startpos: Position):
	pos = copy(startpos)
	seen = set()
	direction = NORTH
	seen.add((pos, direction))
	while pos.isvalid(len(lines), len(lines[0])):
		while obstacle_in_front(pos, direction, lines, extra_obstacle):
			direction = direction.turn_right()

		pos += direction
		if (pos, direction) in seen:
			return True
		seen.add((pos, direction))
	return False



def solve_part2(lines: list[str], path: set[Position]):
	time_paradoxes = set()
	startpos = [Position(y, line.index('^')) for y, line in enumerate(lines) if ('^' in line)][0]
	path.remove(startpos)
	for i, p in enumerate(path):
		print(f'{i / len(path) * 100:.1f}%', end='\r')
		if detect_cycle(lines, p, startpos):
			time_paradoxes.add(p)
	return len(time_paradoxes)


def aoc(data: str, prefix: str) -> None:
	lines = parse(data)
	path = get_path(lines)
	print(f'{prefix} part 1: {len(path)}')
	part2 = solve_part2(lines, path)
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
