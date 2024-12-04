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

def horizontal(lines: list[str], y: int, x: int):
	word = lines[y][x]

def word_search(lines: list[str], word_to_find: str = 'XMAS') -> int:
	found = 0
	for y, line in enumerate(lines):
		for x, c in enumerate(line):
			for d in [EAST, SOUTH, WEST, NORTH, SOUTHWEST, SOUTHEAST, NORTHEAST, NORTHWEST]:
				p = Position(y, x)
				w = c
				for _ in range(len(word_to_find) - 1):
					p += d
					if not p.isvalid(len(lines), len(lines[0])):
						break
					w += lines[p.y][p.x]
				if w == word_to_find:
					found += 1
	return found


def diag(lines: list[str], p: Position, da: Position, db: Position) -> str:
	pa = p + da
	pb = p + db
	if not pa.isvalid(len(lines), len(lines[0])) or not pb.isvalid(len(lines), len(lines[0])):
		return ''
	return lines[pa.y][pa.x] + lines[p.y][p.x] + lines[pb.y][pb.x]

def word_search_2(lines: list[str], word_to_find: str = 'MAS') -> int:
	found = 0
	for y, line in enumerate(lines):
		for x, c in enumerate(line):
			mas_found = 0
			p = Position(y, x)
			a = diag(lines, p, SOUTHWEST, NORTHEAST)
			b = diag(lines, p, SOUTHEAST, NORTHWEST)
			if all(s in ['MAS', 'SAM'] for s in [a, b]):
				found += 1
	return found

def aoc(data: str, prefix: str) -> None:
	lines = parse(data)
	part1 = word_search(lines)
	part2 = word_search_2(lines)
	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
