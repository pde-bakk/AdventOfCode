import sys
import math
import networkx as nx

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def parse(data: str) -> list[str]:
	lines = split_data_on_newlines(data)
	return lines


def solve(lines: list[str]) -> tuple[int, str]:
	graph = nx.Graph()
	for line in lines:
		a, b = line.split('-')
		graph.add_edge(a, b)
		graph.add_edge(b, a)
	maxipad = []
	part1 = 0
	for clique in nx.enumerate_all_cliques(graph):
		if len(clique) == 3 and any(c[0] == 't' in c for c in clique):
			part1 += 1
		if len(clique) > len(maxipad):
			maxipad = clique
	return part1, ''.join(sorted(maxipad))


def aoc(data: str, _, prefix: str) -> None:
	lines = parse(data)
	part1, part2 = solve(lines)
	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	program_args = parse_args()
	if 'example' in program_args.mode:
		aoc(get_example_file(), program_args, 'Example')
	if 'solution' in program_args.mode:
		aoc(get_input_file(), program_args, 'Solution')
