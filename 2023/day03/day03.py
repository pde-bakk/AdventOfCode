import math
import sys
sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *


def aoc(data: str, prefix: str) -> None:
	lines = split_data_on_newlines(data)
	part1 = 0
	part2 = 0
	gears = {}
	for y, line in enumerate(lines):
		x = [(int(m.group(0)), m.start()) for m in re.finditer(r'\d+', line)]
		for d, idx in x:
			has_symbol = False
			gear = None
			for x in range(idx, idx + len(str(d))):
				neighbours = get_neighbours(y, x, diagonal=True)
				for n in neighbours:
					if 0 <= n[0] < len(lines) and 0 <= n[1] < len(line) and lines[n[0]][n[1]] not in '.1234567890':
						has_symbol = True
						gear = n
			if gear:
				gears[gear] = gears.get(gear, []) + [d]
			if has_symbol:
				part1 += d

	for k, v in gears.items():
		if len(v) == 2:
			part2 += math.prod(v)
	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
