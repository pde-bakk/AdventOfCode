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


def get_wirevalue(d: dict[str, int], startswith: str) -> str:
	result = ''
	for k, v in sorted(d.items()):
		# print(f'{k}: {v}')
		if k[0] == startswith:
			result = str(v) + result
	return result



def get_operations(wires, gates: list[str]) -> list[list[str]]:
	ordered_gates = []
	d = {}
	for wire in wires:
		w, value = wire.split(': ')
		d[w] = int(value)
	i = 0
	while gates:
		if i >= len(gates):
			i = 0
		g1, op, g2, _, g3 = gates[i].split()
		if g1 in d and g2 in d:
			d[g3] = 1
			ordered_gates.append([g1, op, g2, g3])
			gates.pop(i)
		else:
			i += 1
	return ordered_gates


def solve1(wires: list[str], gates: list[str], part: int = 1) -> int:
	d = {}
	for wire in wires:
		w, value = wire.split(': ')
		d[w] = int(value)
	max_z = max(l.split()[-1] for l in gates)
	print(f'{max_z = }')
	def process():
		if op == 'AND':
			d[g3] = d[g1] & d[g2]
		elif op == 'OR':
			d[g3] = d[g1] | d[g2]
		elif op == 'XOR':
			d[g3] = d[g1] ^ d[g2]
	pg = [g.split() for g in gates]
	wrong = set()
	for g1, op, g2, _, g3 in pg:
		print(f'{g1} {op} {g2} => {g3}')
		if g3[0] == 'z' and op != 'XOR' and g3 != max_z:
			wrong.add(g3)
			print(f'1. wrong.add({g3}')
		# if op == 'XOR' and all(c not in 'xyz' for c in [g1, g2, g3]):
		if (
				op == "XOR"
				and g3[0] not in ["x", "y", "z"]
				and g1[0] not in ["x", "y", "z"]
				and g2[0] not in ["x", "y", "z"]
		):
			wrong.add(g3)
			print(f'2. wrong.add({g3})')
		if op == 'AND' and 'x00' not in [g1, g2]:
			for sg1, sop, sg2, _, sg3 in pg:
				if g3 in [sg1, sg2] and sop != 'OR':
					wrong.add(sg3)
					print(f'3. wrong.add({sg3})')
		if op == 'XOR':
			for sg1, sop, sg2, _, sg3 in pg:
				if (g3 == sg1 or g3 == sg2) and sop == 'OR':
					wrong.add(sg3)
					print(f'4. wrong.add({sg3})')

	while pg:
		g1, op, g2, _, g3 = pg.pop()
		if g1 in d and g2 in d:
			process()
		else:
			pg.append([g1, op, g2, '->', g3])
	if part == 1:
		return int(get_wirevalue(d, 'z'), 2)
	print(f'{wrong=}')
	return ','.join(sorted(wrong))


def aoc(data: str, args, prefix: str) -> None:
	w, g = parse(data)
	if args.part in [0, 1]:
		part1 = solve1(w, g, part=1)
		print(f'{prefix} part 1: {part1}')
	if args.part in [0, 2]:
		part2 = solve1(w, g, part=2)
		print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	program_args = parse_args()
	if 'example' in program_args.mode:
		aoc(get_example_file(), program_args, 'Example')
	if 'solution' in program_args.mode:
		aoc(get_input_file(), program_args, 'Solution')
