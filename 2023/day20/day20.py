import functools
import sys
import math

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def print_details(key, pulse, outgoing_module) -> None:
	print(f'{key} -{["low", "high"][pulse]}-> {outgoing_module}')


def solve(d: dict[str, str, int, list[str,]]) -> tuple[int, int]:
	conjunctions = {key: {} for key in d if d[key][0] == '&'}
	for key, (_, _, modules) in d.items():
		for conj in conjunctions:
			if conj in modules:
				conjunctions[conj][key] = 0
		# print(f'{key=}, {modules=}')
	# print(f'{conjunctions=}')
	targets = list(conjunctions['dg'])
	targets_d = {target: 0 for target in targets}
	pulses = [0, 0]
	for i in range(1, 7001):
		new_pulses = [0, 0]
		q = [('broadcaster', 0)]
		# print_details('button', 0, 'broadcaster')
		new_pulses[0] += 1
		while q:
			key, pulse = q.pop(0)
			if key not in d:
				continue
			button_type, button_state, modules = d[key]

			match button_type:
				case '':
					for mod in modules:
						q += (mod, pulse),
						new_pulses[pulse] += 1
						if mod in conjunctions:
							conjunctions[mod][key] = pulse
						# print_details(key, pulse, mod)
				case '%':
					if pulse == 0:
						button_state = int(not button_state)
						d[key][1] = button_state
						for mod in modules:
							new_pulses[button_state] += 1
							q += (mod, button_state),
							if mod in conjunctions:
								conjunctions[mod][key] = button_state
							# print_details(key, button_state, mod)
				case '&':
					button_conjunctions = conjunctions[key]
					# print(f'{key=}, {button_conjunctions=}')
					new_pulse = int(not all(button_conjunctions.values()))
					for mod in modules:
						# new_pulse = int(not pulse)
						if mod in targets and targets_d[mod] == 0 and new_pulse == 0:
							targets_d[mod] = i
							print(f'{key=}, {mod=}, {new_pulse=}')
						q += (mod, new_pulse),
						new_pulses[new_pulse] += 1
						if mod in conjunctions:
							conjunctions[mod][key] = new_pulse
						# print_details(key, new_pulse, mod)
		if i < 1000:
			pulses[0] += new_pulses[0]
			pulses[1] += new_pulses[1]
	return math.prod(pulses), math.lcm(*targets_d.values())


def parse(lines: list[str]):
	result = {}
	for line in lines:
		name, mods = line.split(' -> ')
		modules = mods.split(', ')
		operator = ''
		if name[0] in '%&':
			operator = name[0]
			name = name[1:]
		result[name] = [operator, 0, modules]
		# print(f'for {line}, d[{name}] = {result[name]}')
	return result


def aoc(data: str, prefix: str) -> None:
	d = parse(split_data_on_newlines(data))
	part1, part2 = solve(d)
	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	# aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
