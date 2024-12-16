import itertools
import sys
import math

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


BOXES = 'O[]'

def parse(data: str):
	grid, moves = split_on_double_newlines(data)
	grid = [list(line) for line in grid]
	moves = ''.join(moves)
	return grid, moves


def parse2(data: str):
	grid, moves = split_on_double_newlines(data)
	g = []
	for line in grid:
		l = []
		for c in line:
			if c == '@':
				l.extend(['@', '.'])
			elif c in '#.':
				l.extend([c, c])
			elif c == 'O':
				l.extend(['[', ']'])
			else:
				assert False, c
		g.append(l)
	#
	# grid = [list(line) for line in grid]
	moves = ''.join(moves)
	return g, moves


def solve(grid: list[list[str]], moves: str, part: int = 1) -> int:
	def print_grid() -> None:
		print(*[''.join(l) for l in grid], sep='\n', end='\n\n')

	# def move(p, d):
	# 	p += d
	# 	if all([
	# 		grid[p.y][p.x] != '[' or move(p + EAST, d) and move(p, d),
	# 		grid[p.y][p.x] != ']' or move(p + WEST, d) and move(p, d),
	# 		grid[p.y][p.x] != 'O' or move(p, d), grid[p.y][p.x] != '#']):
	# 		old_p = p - d
	# 		grid[p.y][p.x], grid[old_p.y][old_p.x] = grid[old_p.y][old_p.x], grid[p.y][p.x]
	# 		return True
	def move(p: Position, d: Direction) -> bool:
		np = p + d
		c1 = grid[p.y][p.x]
		c2 = grid[np.y][np.x]
	#
	# 	if not (grid[np.y][np.x] != '[' or move(np + EAST, d) and move(np, d)):
	# 		return
	# 	if not (grid[np.y][np.x] != ']' or move(np + WEST, d) and move(np, d)):
	# 		return
	# 	if not (grid[np.y][np.x] != 'O' or move(np, d)):
	# 		return
	# 	if grid[np.y][np.x] == '#':
	# 		return
		# if all([
		# 	grid[np.y][np.x] != '[' or move(np + EAST, d) and move(np, d),
		# 	grid[np.y][np.x] != ']' or move(np + WEST, d) and move(np, d),
		# 	grid[np.y][np.x] != 'O' or move(np, d), grid[np.y][np.x] != '#'
		# ]):
		# grid[np.y][np.x], grid[p.y][p.x] = grid[p.y][p.x], grid[np.y][np.x]
		# return True
		# print(f'{p=} {c1=}, {d=}, {np=}, {c2}')
		if c2 == '#':
			return False
		if c2 == 'O' and move(np, d) == False:
			return False
		elif c2 in '[]':
			if d in [EAST, WEST]:
				if not move(np, d):
					return False
			else:
				if c2 == '[':
					other = np + EAST
					assert grid[other.y][other.x] == ']'
					# if not move(np, d) or not move(np + EAST, d):
					# 	return False
				else:
					other = np + WEST
					assert grid[other.y][other.x] == '['
				if not move(np, d) or not move(other, d):
					return False
		grid[np.y][np.x], grid[p.y][p.x] = grid[p.y][p.x], grid[np.y][np.x]
		return True

	result = 0
	robot_pos = find_positions_where(grid, target='@')[0]
	print(f'{robot_pos = }')
	print(f'Initial state:')
	print_grid()
	for m in moves:
		move_direction = ascii_to_direction(m)
		g2 = grid.copy()
		if move(robot_pos, move_direction):
			robot_pos += move_direction
		else:
			grid = g2
		print(f'Move {m} ({move_direction}):')
		print_grid()
	for y, line in enumerate(grid):
		for x, c in enumerate(line):
			if c in '[O':
				result += 100 * y + x
	return result


def aoc(data: str, prefix: str) -> None:
	grid, moves = parse(data)
	# part1 = solve(grid, moves, part=1)
	# print(f'{prefix} part 1: {part1}')
	grid2, moves = parse2(data)
	part2 = solve(grid2, moves, part=2)
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	# aoc(get_input_file(), 'Solution')
