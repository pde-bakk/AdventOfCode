import sys
import math
from functools import lru_cache

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def parse(data: str) -> list[int]:
	lines = split_data_on_newlines(data)
	return [int(line) for line in lines]


@lru_cache(maxsize=None)
def evolve(nb: int) -> int:
	def mix(val: int):
		nonlocal nb
		nb = nb ^ val
	def prune():
		nonlocal nb
		nb = nb % 16777216
	result = nb * 64
	mix(result)
	prune()
	result = nb // 32
	mix(result)
	prune()
	result = 2048 * nb
	mix(result)
	prune()
	return nb


def solve(nbs: list[int], part: int = 1) -> int:
	result = 0
	for nb in nbs:
		for _ in range(2000):
			old_nb = nb
			nb = evolve(nb)
			# print(f'{old_nb=}, {nb=}')
		result += nb
	return result

def solve2(nbs: list[int], part: int = 1) -> int:
	prices_changes = []
	for nb in nbs:
		items = [nb % 10]
		diffs = []
		prices: dict[tuple[int], int] = {}
		for i in range(1999):
			old_nb = nb
			nb = evolve(nb)
			items.append(nb % 10)
			diffs.append(items[-1] - items[-2])
			if i >= 3:
				t = tuple(diffs[-4:])
				# print(f'{t=}: {nb % 10 = }')
				# print(f'{items=}')
				# print(f'{diffs=}')
				# print(f'{t=}, {nb % 10=}')
				if t not in prices:
					prices[t] = nb % 10
		# print(f'{items = }')
		prices_changes.append(prices)
		# print(f'{prices = }')
	all_keys = set()
	for d in prices_changes:
		all_keys |= set(d.keys())
	results = []
	for key in all_keys:
		result = 0
		for i in range(len(nbs)):
			res = prices_changes[i].get(key, 0)
			# print(f'{key=}, {i=}, {res=}')
			result += res
		# result = sum(prices_changes[i].get(key, 0) for i in range(len(nbs)))
		results.append(result)
	# print(f'{all_keys=}')
	return max(results)


def aoc(data: str, args, prefix: str) -> None:
	nbs = parse(data)
	if '1' in args.part:
		part1 = solve(nbs, part=1)
		print(f'{prefix} part 1: {part1}')
	if '2' in args.part:
		part2 = solve2(nbs, part=2)
		print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	program_args = parse_args()
	if 'example' in program_args.mode:
		aoc(get_example_file(), program_args, 'Example')
	if 'solution' in program_args.mode:
		aoc(get_input_file(), program_args, 'Solution')
