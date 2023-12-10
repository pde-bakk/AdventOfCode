import sys
import math
sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *


def get_pipe_neighbours(char: str):
	items = {
		'|': (get_direction_('North'), get_direction_('South')),
		'-': (get_direction_('East'), get_direction_('West')),
		'L': (get_direction_('North'), get_direction_('East')),
		'J': (get_direction_('North'), get_direction_('West')),
		'7': (get_direction_('South'), get_direction_('West')),
		'F': (get_direction_('South'), get_direction_('East')),
		'S': (get_direction_('North'), get_direction_('South'), get_direction_('East'), get_direction_('West'))
	}
	return items[char]


def solve(lines: list[str]):
	# print(*lines, sep='\n')
	start_y, start_x = [(y, x) for y in range(len(lines)) for x in range(len(lines[y])) if lines[y][x] == 'S'][0]
	seen = set()
	q = [(start_y, start_x)]
	dists = [[math.inf for _ in range(len(lines[y]))] for y in range(len(lines))]
	dists[start_y][start_x] = 0
	while q:
		y, x = q.pop(0)
		seen.add((y, x))
		for neighbour in get_pipe_neighbours(lines[y][x]):
			ny, nx = y + neighbour[0], x + neighbour[1]
			if 0 <= ny < len(lines) and 0 <= nx < len(lines[y]) and lines[ny][nx] in '|-LJ7F' and (ny, nx) not in seen:
				q.append((ny, nx))
				dists[ny][nx] = min(dists[ny][nx], dists[y][x] + 1)
	dists = [[[d, 0][d == math.inf] for d in di] for di in dists]
	# print(*lines, sep='\n')
	print(*dists, sep='\n')
	return max(map(max, dists))


def aoc(lines: list[str], prefix: str) -> None:
	part1 = solve(lines)
	part2 = 0
	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
