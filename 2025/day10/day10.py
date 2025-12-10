import re
import sys
from collections import namedtuple
# from scipy.optimize import milp, LinearConstraint, Bounds
import z3

import math
import heapq
from typing import Tuple

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def parse(data: str) -> list[str]:
	lines = split_data_on_newlines(data)
	return lines


Node = namedtuple('Node', 'presses state')


def bfs_1(buttons: list[tuple[int, ...]], lights: tuple[bool, ...]) -> int:
	start = Node(state=tuple(False for _ in range(len(lights))), presses=0)
	q = [start]
	visited = {start.state}
	while q:
		node = heapq.heappop(q)
		if node.state == lights:
			return node.presses
		for button in buttons:
			new_state = [x for x in node.state]
			for nb in button:
				new_state[nb] = not new_state[nb]
			new_state = tuple(new_state)
			if new_state not in visited:
				visited.add(new_state)
				heapq.heappush(q, Node(state=new_state, presses=node.presses+1))
	return 0


# def solve_joltage(buttons: list[tuple[int, ...]], joltages: list[int]) -> int:
# 	num_counters = len(joltages)
# 	num_buttons = len(buttons)
#
# 	# Build matrix A where each column is a button
# 	A = np.zeros((num_counters, num_buttons), dtype=int)
# 	for j, button in enumerate(buttons):
# 		for idx in button:
# 			A[idx, j] = 1
#
# 	# Minimize sum of all x_i (coefficients all 1)
# 	c = np.ones(num_buttons)
#
# 	# Constraint: A @ x == target
# 	constraints = LinearConstraint(A, joltages, joltages)
#
# 	# x_i >= 0, must be integers
# 	integrality = np.ones(num_buttons)  # 1 = integer
# 	bounds = Bounds(lb=0, ub=np.inf)
#
# 	result = milp(c, constraints=constraints, integrality=integrality, bounds=bounds)
#
# 	if result.success:
# 		return int(round(result.fun))
# 	return -1

def solve_joltage_z3(buttons: list[tuple[int, ...]], joltages: list[int]) -> int:
	x = [z3.Int(f'x_{i}') for i in range(len(buttons))]
	opt = z3.Optimize()

	for xi in x:
		opt.add(xi >= 0)

	for counter_idx in range(len(joltages)):
		counter_sum = z3.Sum([x[j] for j in range(len(buttons)) if counter_idx in buttons[j]])
		opt.add(counter_sum == joltages[counter_idx])

	opt.minimize(z3.Sum(x))

	if opt.check() == z3.sat:
		model = opt.model()
		return sum(model[xi].as_long() for xi in x)
	return -1

def solve(lines: list[str]) -> Tuple[int, int]:
	p1 = p2 = 0
	for line in lines:
		lights, *buttons, joltage = line.split()
		bs = [tuple(map(int, button[1:-1].split(','))) for button in buttons]
		a = bfs_1(bs, tuple(c == '#' for c in lights[1:-1]))
		print(f'{lights}, done in {a}\n')
		b = solve_joltage_z3(bs, list(map(int, joltage[1:-1].split(','))),)
		print(f'{joltage}, done in {b}\n')
		p1 += a
		p2 += b

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
