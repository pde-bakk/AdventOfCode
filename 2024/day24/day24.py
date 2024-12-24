import sys
import math
from collections import defaultdict

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def parse(data: str) -> tuple[list[str], list[str]]:
	w, g = split_on_double_newlines(data)
	return w, g


def solve(wires: list[str], gates: list[str], part: int = 1) -> int:
	result = ''
	d = {}
	for wire in wires:
		w, value = wire.split(': ')
		d[w] = int(value)
	i = 0
	while gates:
		if i >= len(gates):
			i = 0
		print(f'{len(gates)=}, {i=}')
		gate = gates[i]
		g1, op, g2, _, g3 = gate.split()
		if g1 in d and g2 in d:
			match op:
				case 'AND':
					d[g3] = d[g1] & d[g2]
				case 'OR':
					d[g3] = d[g1] | d[g2]
				case 'XOR':
					d[g3] = d[g1] ^ d[g2]
			gates.pop(i)
		else:
			i += 1
	for k, v in sorted(d.items()):
		print(f'{k}: {v}')
		if k[0] == 'z':
			result = str(v) + result
	return int(result, 2)


def aoc(data: str, args, prefix: str) -> None:
	w, g = parse(data)
	if args.part in [0, 1]:
		part1 = solve(w, g, part=1)
		print(f'{prefix} part 1: {part1}')
	if args.part in [0, 2]:
		part2 = solve(w, g, part=2)
		print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	program_args = parse_args()
	if 'example' in program_args.mode:
		aoc(get_example_file(), program_args, 'Example')
	if 'solution' in program_args.mode:
		aoc(get_input_file(), program_args, 'Solution')
