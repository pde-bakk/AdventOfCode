import string
import sys
import math

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def parse(data: str) -> list[str]:
	lines = split_data_on_newlines(data)
	return lines


def search(lines: list[str], positions: list[Position], letter: str, part: int = 2):
	def check_dir(direction: Direction):
		neighbouring_position = side_pos + direction
		while (neighbouring_position, side_direction) in sides:
			l.add(neighbouring_position)
			sides.remove((neighbouring_position, side_direction))
			neighbouring_position += direction

	seen: set[Position] = set()
	part1result = 0
	part2result = 0
	total_area = 0
	for p in positions:
		perimeter, area = 0, 0
		sides = set()
		if p in seen:
			continue
		q = [p]
		seen.add(p)
		while q:
			p = q.pop(0)
			area += 1
			for d in Direction.get_directions():
				n = p + d
				if not n.checkvalid(lines) or lines[n.y][n.x] != letter:
					perimeter += 1
					sides.add((n, d))
				elif n not in seen:
					q.append(n)
					seen.add(n)
		part1result += area * perimeter

		total_area += area
		side_amount = 0
		while sides:
			key = (side_pos, side_direction) = next(iter(sides))
			l = {side_pos}
			sides.remove(key)
			check_dir(side_direction.turn_left())
			check_dir(side_direction.turn_right())
			side_amount += 1
		part2result += side_amount * area
	if part == 1:
		return part1result
	return part2result


def solve(lines: list[str], part: int = 1) -> int:
	all_positions: dict[str, list] = {}
	for y, line in enumerate(lines):
		for x, c in enumerate(line):
			if c not in all_positions:
				all_positions[c] = []
			all_positions[c].append(Position(y=y, x=x))
	result = 0
	for letter, positions in all_positions.items():
		result += search(lines, positions, letter, part)
	return result


def aoc(data: str, prefix: str) -> None:
	lines = parse(data)
	part1 = solve(lines, part=1)
	print(f'{prefix} part 1: {part1}')
	part2 = solve(lines, part=2)
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
