import sys
import math

import numpy as np

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


class Machine:
	def __init__(self, l: list[str]):
		xa, xb, xp = map(ints, l)
		self.pos = Position(y=0, x=0)
		self.button_a = Direction(x=xa[0], y=xa[1])
		self.button_b = Direction(x=xb[0], y=xb[1])
		self.prize = Position(x=xp[0], y=xp[1])
		self.tokens_spent = 0

	def solve(self) -> np.ndarray:
		# x0 * buttonA + x1 * buttonB = prize
		a = np.array([[self.button_a.x, self.button_b.x], [self.button_a.y, self.button_b.y]])
		b = np.array([self.prize.x, self.prize.y])
		return np.linalg.solve(a, b).round().astype(int)


def parse(data: str) -> list[Machine]:
	portions = split_on_double_newlines(data)
	return [Machine(portion) for portion in portions]


def solve(machines: list[Machine], part: int = 1) -> int:
	conversion_error = 10000000000000
	result = 0
	for m in machines:
		if part == 2:
			m.prize += Direction(conversion_error, conversion_error)
		solution = m.solve()
		if any(x < 0 for x in solution):
			continue
		if int(solution[0]) * m.button_a + int(solution[1]) * m.button_b == m.prize:
			tokens = 3 * int(solution[0]) + int(solution[1])
			# print(f'{tokens = }, {solution=}')
			result += tokens
	return result


def aoc(data: str, prefix: str) -> None:
	lines = parse(data)
	part1 = solve(lines, part=1)
	print(f'{prefix} part 1: {part1}')
	part2 = solve(lines, part=2)
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
