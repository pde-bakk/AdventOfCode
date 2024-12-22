import itertools
import sys
import math
from collections import namedtuple
from functools import lru_cache

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *

numeric_keypad = {
	Position(y=0, x=0): '7',
	Position(y=0, x=1): '8',
	Position(y=0, x=2): '9',
	Position(y=1, x=0): '4',
	Position(y=1, x=1): '5',
	Position(y=1, x=2): '6',
	Position(y=2, x=0): '1',
	Position(y=2, x=1): '2',
	Position(y=2, x=2): '3',
	Position(y=3, x=1): '0',
	Position(y=3, x=2): 'A',
}
directional_keypad = {
	Position(y=0, x=1): '^',
	Position(y=0, x=2): 'A',
	Position(y=1, x=0): '<',
	Position(y=1, x=1): 'v',
	Position(y=1, x=2): '>',
}

def parse(data: str) -> list[str]:
	lines = split_data_on_newlines(data)
	return lines


Node = namedtuple('Node', 'len moves pos')


@lru_cache(maxsize=None)
def type_keys(start_char: str, target: str, keypad_nb: int) -> set[str]:
	keypad = [numeric_keypad, directional_keypad][keypad_nb != 0]
	start, = [key for key, value in keypad.items() if value == start_char]
	q = [Node(moves='', pos=start, len=0)]
	seen = {start: 0}
	shortests: set[str] = set()
	shortest_length = float('inf')

	while q:
		node = q.pop(0)
		if keypad[node.pos] == target:
			if len(node.moves) + 1 > shortest_length:
				break
			shortests.add(node.moves + 'A')
			shortest_length = len(node.moves) + 1
		for direction in Direction.get_directions():
			new_pos = node.pos + direction
			new_moves = node.moves + direction_to_ascii(direction)
			if new_pos not in keypad or seen.get(new_pos, 0) > len(new_moves):
				continue
			seen[new_pos] = len(new_moves)
			q.append(Node(moves=new_moves, pos=new_pos, len=len(new_moves)))
	return shortests


def get_numeric_part(code: str) -> int:
	numeric = ''.join([c for c in code if c.isdigit()])
	return int(numeric)


def get_possible_strings(x) -> list[str]:
	l = []
	for p in itertools.product(*[list(s) for s in x]):
		l.append(''.join(p))
	return l

@lru_cache(maxsize=None)
def recurse(assignment: str, depth: int, max_depth: int) -> int:
	x = []
	for start, target in zip(assignment, assignment[1:]):
		x.append(type_keys(start_char=start, target=target, keypad_nb=depth))

	if depth == max_depth:  # max depth
		return sum([min(len(item) for item in item_set) for item_set in x])
	result = 0
	for item_set in x:
		options = [recurse(assignment='A' + item, depth=depth+1, max_depth=max_depth) for item in item_set]
		result += min(options)
	return result

def solve(lines: list[str], max_depth: int) -> int:
	result = 0
	for line in lines:
		res = recurse('A' + line, depth=0, max_depth=max_depth)
		complexity = res * get_numeric_part(line)
		print(f'line: {line}, ({res} * {get_numeric_part(line)}), {complexity = }')
		result += complexity
	return result


def aoc(data: str, args, prefix: str) -> None:
	lines = parse(data)
	print(f'{args.part=}')
	if 1 in args.part:
		part1 = solve(lines, max_depth=2)
		print(f'{prefix} part 1: {part1}')
	if 2 in args.part:
		part2 = solve(lines, max_depth=25)
		print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	program_args = parse_args()
	if 'example' in program_args.mode:
		aoc(get_example_file(), program_args, 'Example')
	if 'solution' in program_args.mode:
		aoc(get_input_file(), program_args, 'Solution')
