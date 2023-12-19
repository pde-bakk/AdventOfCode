import sys
import math
import copy

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


class AocRange:
	def __init__(self, lower_bound: int, upper_bound: int):
		self.lower = lower_bound
		self.upper = upper_bound

	def do_intersection(self, value: int, operator: str) -> tuple:
		where_true = None
		where_false = None
		if operator == '<':
			if self.lower < value:
				where_true = AocRange(self.lower, value - 1)
			if self.upper >= value:
				where_false = AocRange(value, self.upper)
		elif operator == '>':
			if self.upper > value:
				where_true = AocRange(value + 1, self.upper)
			if self.lower <= value:
				where_false = AocRange(self.lower, value)
		return where_true, where_false

	def size(self):
		return self.upper - self.lower + 1

	def __str__(self):
		return f'AocRange(lower={self.lower}, upper={self.upper})'

	def __repr__(self):
		return f'AocRange({self.lower}, {self.upper})'


def parse_line(line: str) -> dict[str, int]:
	items = line[1:-1].split(',')
	return {part[0]: int(part[2:]) for part in items}


def get_from_dict(wd: dict, key: str, line: dict[str, int]):
	*checks, last = wd[key]
	for (check, result) in checks:
		letter = check[0]
		if f'{line[letter]}{check[1:]}':
			if result in 'RA':
				return result
			else:
				return get_from_dict(wd, result, line)
	if last in 'RA':
		return last
	else:
		return get_from_dict(wd, last, line)


def solve(wd: dict, inputs: list[str]) -> int:
	total = 0
	for line in inputs:
		line = parse_line(line)
		if get_from_dict(wd, 'in', line) == 'A':
			total += sum(line.values())
	return total


def check_route(wd: dict, key: str, ranges: dict[str, AocRange], depth: int):
	*checks, last = wd[key]
	total = 0
	for (letter, operator, *value), result in checks:
		value = int(''.join(value))
		where_true, where_false = ranges[letter].do_intersection(value, operator)
		if where_true:
			r2 = ranges.copy()
			r2[letter] = where_true
			if result in 'AR':
				if result == 'A':
					total += math.prod([r.size() for r in r2.values()])
			else:
				r2[letter] = where_true
				total += check_route(wd, result, r2, depth + 1)
		if where_false:
			ranges[letter] = where_false
	if last in 'AR':
		if last == 'A':
			total += math.prod([r.size() for r in ranges.values()])
	else:
		total += check_route(wd, last, ranges, depth + 1)
	return total


def solve2(wd: dict) -> int:
	ranges = {
		key: AocRange(1, 4000) for key in 'xmas'
	}
	total = check_route(wd, 'in', ranges, depth=0)
	return total


def aoc(data: str, prefix: str) -> None:
	workflows, other = split_on_double_newlines(data)
	wd = {}
	for workflow in workflows:
		name, rest = workflow.removesuffix('}').split('{', maxsplit=1)
		rest = rest.split(',')
		wd[name] = [tuple(i.split(':')) if ':' in i else i for i in rest]
	part1 = solve(wd, other)
	part2 = solve2(wd)
	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
