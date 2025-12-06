import itertools
import sys
import math
from typing import Tuple

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def parse(data: str) -> list[str]:
	lines = split_data_on_newlines(data)
	return lines


def solve(lines: list[str]) -> Tuple[int, int]:
	p1 = p2 = 0
	l = []
	operators = []
	for line in lines:
		x = line.split()
		if any(c.isdigit() for c in line):
			l.append(list(map(int, x)))
		else:
			operators = x
	formulas = list(zip(*l[::-1]))
	# print(formulas)
	for i, f in enumerate(formulas):
		if operators[i] == '+':
			p1 += sum(f)
		elif operators[i] == '*':
			p1 += math.prod(f)

	nbs = []
	operator = '+'
	def add():
		nonlocal p2
		if operator == '+':
			p2 += sum(nbs)
			print(f'summing {nbs} -> {sum(nbs)}')
		elif operator == '*':
			p2 += math.prod(nbs)
			print(f'product {nbs} -> {math.prod(nbs)}')
	for i in range(len(lines[0])):
		if lines[-1][i] in '+*':
			add()
			nbs.clear()
			operator = lines[-1][i]
		nb = ''.join(lines[j][i] for j in range(len(lines) - 1))
		if nb.strip():
			nbs.append(int(nb))
			print(f'appending {nb} -> {int(nb)}')
	add()

	return p1, p2

def aoc(data: str, _, prefix: str) -> None:
	lines = parse(data)
	part1, part2 = solve(lines)
	print(f'{prefix} part 1: {part1} and part 2: {part2}')


if __name__ == '__main__':
	program_args = parse_args()
	if 'example' in program_args.mode:
		aoc(get_example_file(), program_args, 'Example')
	if 'solution' in program_args.mode:
		aoc(get_input_file(), program_args, 'Solution')
