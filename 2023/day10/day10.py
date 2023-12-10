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


def check_connect_back(cur_pos, npos, lines):
	ny, nx = npos
	nchar = lines[ny][nx]
	return any([(pn[0] + ny, pn[1] + nx) == cur_pos for pn in get_pipe_neighbours(nchar)])


def solve(lines: list[str]):
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
			if 0 <= ny < len(lines) and 0 <= nx < len(lines[y]) and lines[ny][nx] in '|-LJ7F' and (ny, nx) not in seen and check_connect_back((y, x), (ny, nx), lines):
				q.append((ny, nx))
				dists[ny][nx] = min(dists[ny][nx], dists[y][x] + 1)
	dists = [[[d, 0][d == math.inf] for d in di] for di in dists]
	return max(map(max, dists)), seen


def solve2(lines: list[str], main_pipe: set):
	not_in_main_pipe = set([(y, x) for y in range(len(lines)) for x in range(len(lines[y]))]) - main_pipe
	lines = [list(line) for line in lines]
	# print(f'{main_pipe=}')
	total = 0
	w, h = len(lines[0]), len(lines)
	for y, x in not_in_main_pipe:
		border_crossings = 0
		y2, x2 = y, x
		while x2 < w and y2 < h:
			c2 = lines[y2][x2]
			if (y2, x2) in main_pipe and c2 not in 'L7':
				border_crossings += 1
			x2 += 1
			y2 += 1
		if border_crossings % 2 == 1:
			total += 1
			lines[y][x] = 'I'
	for line in lines:
		print(''.join(line))
	return total


def aoc(lines: list[str], prefix: str) -> None:
	part1, main_pipe = solve(lines)
	part2 = solve2(lines, main_pipe)
	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
