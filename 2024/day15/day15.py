import copy
import itertools
import sys
import math

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


BOXES = 'O[]'

def parse(data: str, part: int = 1):
	grid, moves = split_on_double_newlines(data)
	if part == 2:
		translation = str.maketrans({
			'#': '##',
			'.': '..',
			'O': '[]',
			'@': '@.'
		})
		grid = [list(line.translate(translation)) for line in grid]
	else:
		grid = [list(line) for line in grid]
	moves = ''.join(moves)
	return grid, moves


def solve(grid: list[list[str]], moves: str, part: int = 1) -> int:
	def print_grid() -> None:
		print(*[''.join(l) for l in grid], sep='\n', end='\n\n')

	def move(p: Position, d: Direction) -> bool:
		np = p + d
		c2 = grid[np.y][np.x]
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
				else:
					other = np + WEST
					assert grid[other.y][other.x] == '['
				if not move(np, d) or not move(other, d):
					return False
		grid[np.y][np.x], grid[p.y][p.x] = grid[p.y][p.x], grid[np.y][np.x]
		return True

	result = 0
	robot_pos = find_positions_where(grid, target='@')[0]
	for m in moves:
		move_direction = ascii_to_direction(m)
		g2 = copy.deepcopy(grid)
		if move(robot_pos, move_direction):
			robot_pos += move_direction
		else:
			grid = g2
	for y, line in enumerate(grid):
		for x, c in enumerate(line):
			if c in '[O':
				result += 100 * y + x
	return result


def aoc(data: str, prefix: str) -> None:
	grid, moves = parse(data, part=1)
	part1 = solve(grid, moves, part=1)
	print(f'{prefix} part 1: {part1}')
	grid2, moves = parse(data, part=2)
	part2 = solve(grid2, moves, part=2)
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
