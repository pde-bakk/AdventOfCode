import functools
import sys
import math

import numpy as np

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import split_on_double_newlines_instead


def np_move_rock(lines: np.ndarray, start: tuple[int, int]):
	direction = (-1, 0)
	width, height = len(lines[0]), len(lines)
	y, x = start
	dy, dx = direction
	while 0 <= y + dy < height and 0 <= x + dx < width and lines[y+dy][x+dx] == '.':
		y = y + dy
		x = x + dx
	# if direction == (0, -1):
	# 	print(f'{width=}, {height=}, {y,x=}, {start=}, {dy, dx=}')
	if start == (y, x):
		return
	# if direction == (0, -1):
	# 	print(f'{start=}, {y, x=}, {dy, dx=}, end_char={lines[y][x]}')
	lines[y][x] = 'O'
	lines[start[0]][start[1]] = '.'


def roll_upwards(lines: np.ndarray) -> np.ndarray:
	for y, line in enumerate(lines):
		for x, c in enumerate(line):
			if c == 'O':
				np_move_rock(lines, start=(y, x))
	return lines


def solve_p2(data, i, seenkey, scores, max_cycles):
	cycle_length = i - seenkey
	idx = seenkey + (max_cycles - seenkey) % cycle_length
	print(f'{i=}, {cycle_length=}, seen[key]={seenkey}, {idx=}')
	return scores[idx]


def calculate_load(lines: np.ndarray) -> int:
	load = 0
	for i, line in enumerate(lines):
		load_level = len(lines) - i
		load += load_level * np.count_nonzero(line == 'O')
		# print(f'{load_level=}, {line=="O"}', np.count_nonzero(line == 'O'))
	return load


def aoc(lines: list[str], prefix: str) -> None:
	data = np.array([list(line) for line in lines])
	seen, scores = {}, {}
	part2 = 0
	max_cycles = 1_000_000_000
	print(f'{prefix} part 1: {calculate_load(roll_upwards(data))}')
	for i in range(max_cycles):
		key = data.tobytes()
		if key in seen:
			part2 = solve_p2(data, i, seen[key], scores, max_cycles)
			break
		seen[key] = i
		scores[i] = calculate_load(data)
		for rot in 'NWSE':
			data = roll_upwards(data)
			data = np.rot90(data, k=3)
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
