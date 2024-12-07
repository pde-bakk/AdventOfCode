import itertools
import sys
import math

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def parse(data: str) -> list[list[int]]:
	lines = split_data_on_newlines(data)
	l1 = []
	for line in lines:
		l1.append(ints(line))
	return l1

def solve(l: list[int], ops: tuple[str, ...]) -> int:
	total = l[0]
	for op, item in zip(ops, l[1:]):
		if op == '+':
			total += item
		elif op == '*':
			total *= item
		elif op == '|':
			total = int(str(total) + str(item))
	return total


def solve_day07(lines: list[list[int]], allowed_operators: str) -> int:
	total = 0
	for result, *items in lines:
		product = list(itertools.product(allowed_operators, repeat=len(items)-1))
		for operators in product:
			r2 = solve(items, operators)
			if r2 == result:
				total += result
				break
	return total


def aoc(data: str, prefix: str) -> None:
	lines = parse(data)
	part1 = solve_day07(lines, allowed_operators='+*')
	part2 = solve_day07(lines, allowed_operators='+*|')
	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
