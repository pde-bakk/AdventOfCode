import functools
import sys
import math

import numpy as np

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *


def np_move_rock(lines: np.ndarray, start: tuple[int, int]):
	width, height = len(lines[0]), len(lines)
	y, x = start
	dy, dx = (-1, 0)  # Because I'm calling np.rot90 to handle my rotations, I just move upwards
	while 0 <= y + dy < height and 0 <= x + dx < width and lines[y+dy][x+dx] == '.':
		y = y + dy
		x = x + dx
	if start == (y, x):
		return
	lines[y][x] = 'O'
	lines[start[0]][start[1]] = '.'


def roll_upwards(lines: np.ndarray) -> np.ndarray:
	for y, line in enumerate(lines):
		for x, c in enumerate(line):
			if c == 'O':
				np_move_rock(lines, start=(y, x))
	return lines


def solve_p2(i: int, seenkey: int, max_cycles: int) -> int:
	cycle_length = i - seenkey
	return seenkey + (max_cycles - seenkey) % cycle_length


def calculate_load(lines: np.ndarray) -> int:
	load = 0
	for i, line in enumerate(lines):
		load_level = len(lines) - i
		load += load_level * np.count_nonzero(line == 'O')
	return load


def aoc(data: str, prefix: str) -> None:
	lines = split_data_on_newlines(data)
	data = np.array([list(line) for line in lines])
	seen, scores = {}, {}
	part2 = 0
	max_cycles = 1_000_000_000
	print(f'{prefix} part 1: {calculate_load(roll_upwards(data))}')
	for i in range(max_cycles):
		key = data.tobytes()
		if key in seen:
			idx = solve_p2(i, seen[key], max_cycles)
			part2 = scores[idx]
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
