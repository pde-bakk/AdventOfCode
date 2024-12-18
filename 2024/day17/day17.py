import itertools
import sys
import math

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


A, B, C = 0, 1, 2


def parse(data: str) -> tuple[list[int], list[int]]:
	regs, pro = split_on_double_newlines(data)
	registers = [i for line in regs for i in ints(line)]
	program = ints(pro[0])
	return registers, program


def solve(registers: list[int], program: list[int]) -> list[int]:
	def combo() -> int:
		if operand <= 3:
			return operand
		if operand <= 6:
			return registers[operand - 4]
		assert False
	def perform_operand() -> bool:
		if opcode == 0:  # adv
			registers[A] = int(registers[A] / (2 ** combo()))
		if opcode == 1:  # bxl
			registers[B] ^= operand
		if opcode == 2:  # bst
			registers[B] = combo() % 8
		if opcode == 3:  # jnz
			if registers[A] != 0:
				nonlocal i
				i = operand
				# print(f'set i to {operand}')
				return False
		if opcode == 4:  # bxc
			registers[B] = registers[B] ^ registers[C]
		if opcode == 5:  # out
			program_outputs.append(combo() % 8)
		if opcode == 6:  # bdv
			registers[B] = int(registers[A] / (2 ** combo()))
		if opcode == 7:  # cdv
			registers[C] = int(registers[A] / (2 ** combo()))
		return True

	i = 0
	program_outputs = []
	while i < len(program):
		opcode, operand = program[i], program[i + 1]
		if perform_operand():
			i += 2
	return program_outputs


def solve_part2(program: list[int]) -> int:
	target = program[::-1]
	def get_a(starting_a: int, depth: int):
		if depth == len(target):
			return starting_a
		for i in range(8):
			a_val = starting_a * 8 + i
			output = solve(registers=[a_val, 0, 0], program=program)
			if output and output[0] == target[depth]:
				result = get_a(a_val, depth + 1)
				if result:
					return result
	return get_a(starting_a=0, depth=0)


def aoc(data: str, prefix: str) -> None:
	registers, program = parse(data)
	part1 = solve(registers, program)
	print(f'{prefix} part 1: {part1}')
	part2 = solve_part2(program)
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
