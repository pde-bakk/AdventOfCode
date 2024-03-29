import sys

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def get_new_directions(tile: str, current_dir: tuple[int, int]) -> list[tuple]:
	dy, dx = current_dir
	if tile == '/':
		return [(-current_dir[1], -current_dir[0])]
	elif tile == '\\':
		return [current_dir[::-1]]
	elif tile == '|' and dx:
		return [NORTH, SOUTH]
	elif tile == '-' and dy:
		return [EAST, WEST]
	return [current_dir]


def get_energized(lines, pos, direction) -> int:
	width, height = len(lines[0]), len(lines)
	q = [(pos, direction)]
	energized = set()
	seen = set()
	while q:
		pos, direction = q.pop()
		y, x = pos
		energized.add(pos)
		seen.add((pos, direction))
		new_directions = get_new_directions(lines[y][x], direction)
		for nd in new_directions:
			dy, dx = nd
			new_pos = y + dy, x + dx
			if (new_pos, nd) not in seen and 0 <= new_pos[0] < height and 0 <= new_pos[1] < width:
				q.append((new_pos, nd))
	return len(energized)


def aoc(data: str, prefix: str) -> None:
	lines = split_data_on_newlines(data)
	part1 = get_energized(lines, pos=(0, 0), direction=EAST)
	part2 = []
	width, height = len(lines[0]), len(lines)
	for x in range(width):
		en = get_energized(lines, pos=(0, x), direction=SOUTH)
		part2.append(en)
		en2 = get_energized(lines, pos=(height - 1, x), direction=NORTH)
		part2.append(en2)

	for y in range(height):
		en = get_energized(lines, pos=(y, 0), direction=EAST)
		part2.append(en)
		en2 = get_energized(lines, pos=(y, width - 1), direction=WEST)
		part2.append(en2)

	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {max(part2)}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
