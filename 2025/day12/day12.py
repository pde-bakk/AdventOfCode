import sys
import math
from collections import namedtuple
from typing import Tuple

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


Region = namedtuple('Region', ['dimension', 'presents'])


def parse(data: str) -> Tuple[list[list[str]], list[Region]]:
	*shapes, regions = split_on_double_newlines(data)
	shapes = [shape[1:] for shape in shapes]
	r: list[Region] = []
	for region in regions:
		dimension, presents = region.split(': ')
		dimension = tuple(map(int, dimension.split('x')))
		presents = tuple(map(int, presents.split()))
		r.append(Region(dimension=dimension, presents=presents))
	return shapes, r


def solve(shapes: list[list[str]], regions: list[Region]) -> Tuple[int, int]:
	p1, p2 = 0, 0
	for region in regions:
		total_space = 0
		for i, present in enumerate(region.presents):
			total_space += region.presents[i] * sum(line.count('#') for line in shapes[i])
		if total_space <= region.dimension[0] * region.dimension[1]:
			p1 += 1
	return p1, 0


def aoc(data: str, _, prefix: str) -> None:
	shapes, regions = parse(data)
	part1, part2 = solve(shapes, regions)
	print(f'{prefix} part 1: {part1} and part 2: {part2}')


if __name__ == '__main__':
	program_args = parse_args()
	if 'example' in program_args.mode:
		aoc(get_example_file(), program_args, 'Example')
	if 'solution' in program_args.mode:
		aoc(get_input_file(), program_args, 'Solution')
