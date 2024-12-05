import sys
import math
from typing import Tuple

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def parse(data: str) -> Tuple[dict[int,set[int]], list[list[int]]]:
	l1, l2 = split_on_double_newlines(data)
	l1 = [tuple(map(int, line.split('|'))) for line in l1]
	rules = {}
	for a, b in l1:
		if a not in rules:
			rules[a] = set()
		rules[a].add(b)

	l2 = [list(map(int, line.split(','))) for line in l2]
	return rules, l2

def check(rules, update: list[int]) -> bool:
	for idx, item in enumerate(update):
		if item not in rules:
			continue
		for item2 in rules[item]:
			if item2 in update and update.index(item2) < idx:
				return False
	return True

def fix(rules, update: list[int]) -> list[int]:
	go_again = True
	while go_again:
		go_again = False
		for idx, item in enumerate(update):
			if item not in rules:
				continue
			for item2 in rules[item]:
				if item2 in update and update.index(item2) < idx:
					idx2 = update.index(item2)
					# update.insert(idx2, )
					update[idx], update[idx2] = update[idx2], update[idx]
					go_again = True
	return update

def solve_part1(rules: dict[int,set[int]], updates: list[list[int]]) -> tuple[int, int]:
	total = 0
	total2 = 0
	for update in updates:
		if check(rules, update):
			total += update[len(update) // 2]
			# print(f'{update} in right order')
		else:
			update2 = fix(rules, update)
			total2 += update[len(update2) // 2]
			print(f'{update} became {update2}')

	return total, total2

def solve_part2(a, b) -> int:
	return 0


def aoc(data: str, prefix: str) -> None:
	a, b = parse(data)
	part1, part2 = solve_part1(a, b)
	# part2 = solve_part2(a, b)
	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
