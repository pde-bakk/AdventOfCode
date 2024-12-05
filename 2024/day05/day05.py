import sys
from typing import *

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *


def parse(data: str) -> Tuple[Dict[int, Set[int]], List[List[int]]]:
	l1, l2 = split_on_double_newlines(data)
	l1 = [ints(line) for line in l1]
	l2 = [ints(line) for line in l2]
	rules = {}
	for a, b in l1:
		rules[a] = rules.get(a, set()) | {b}
	return rules, l2

def is_ordered(rules, update: List[int]) -> bool:
	for idx, item in enumerate(update):
		if item not in rules:
			continue
		for item2 in rules[item]:
			if item2 in update and update.index(item2) < idx:
				return False
	return True

def fix_update(rules, update: List[int]) -> List[int]:
	go_again = True
	while go_again:
		go_again = False
		for idx, item in enumerate(update):
			if item not in rules:
				continue
			for item2 in rules[item]:
				if item2 in update and update.index(item2) < idx:
					idx2 = update.index(item2)
					update[idx], update[idx2] = update[idx2], update[idx]
					go_again = True
	return update

def solve_part1(rules: Dict[int, Set[int]], updates: List[List[int]]) -> Tuple[int, int]:
	p1, p2 = 0, 0
	for update in updates:
		if is_ordered(rules, update):
			p1 += update[len(update) // 2]
		else:
			update2 = fix_update(rules, update)
			p2 += update[len(update2) // 2]
	return p1, p2


def aoc(data: str, prefix: str) -> None:
	a, b = parse(data)
	part1, part2 = solve_part1(a, b)
	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
