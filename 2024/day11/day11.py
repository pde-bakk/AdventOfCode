import functools
import sys
import math

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def parse(data: str) -> list[int]:
	stones = ints(data)
	return stones


@functools.lru_cache(maxsize=None)
def count_stones_rec(stone: int, blinks_left: int) -> int:
	if blinks_left == 0:
		return 1
	if stone == 0:
		return count_stones_rec(stone=1, blinks_left=blinks_left-1)
	s = str(stone)
	if len(s) % 2:
		return count_stones_rec(stone * 2024, blinks_left=blinks_left-1)
	return count_stones_rec(int(s[:len(s) // 2]), blinks_left=blinks_left-1) + \
			count_stones_rec(int(s[len(s) // 2:]), blinks_left=blinks_left-1)


def solve(stones: list[int], max_blinks: int) -> int:
	result = 0
	for stone in stones:
		result += count_stones_rec(stone, max_blinks)
	return result

def aoc(data: str, prefix: str) -> None:
	stones = parse(data)
	part1 = solve(stones, 25)
	part2 = solve(stones, 75)
	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
