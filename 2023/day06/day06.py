import sys
import math
sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *


def calculate_ways_to_win(times: list[int], distances: list[int]) -> int:
	ways_to_win = []
	for time, dist in zip(times, distances):
		winnings = 0
		for t in range(time):
			if t * (time - t) > dist:
				winnings += 1
		ways_to_win.append(winnings)
	return math.prod(ways_to_win)


def aoc(data: str, prefix: str) -> None:
	lines = split_data_on_newlines(data)
	times = lmap(int, lines[0].split()[1:])
	distances = lmap(int, lines[1].split()[1:])
	part1 = calculate_ways_to_win(times, distances)

	times = [int(''.join(map(str, times)))]
	distances = [int(''.join(map(str, distances)))]
	part2 = calculate_ways_to_win(times, distances)

	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
