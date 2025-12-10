import itertools
import sys
from collections import namedtuple

import math
from typing import Tuple


from shapely import Polygon, box

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


Rectangle = namedtuple('Rectangle', ['c1', 'c2', 'width', 'height'])


def parse(data: str) -> list[str]:
	lines = split_data_on_newlines(data)
	return lines


def solve(lines: list[str]) -> Tuple[int, int]:
	polygon = [Position(*reversed(list(map(int, line.split(','))))) for line in lines]
	rectangles = [Rectangle(a, b, width=abs(a.x - b.x) + 1, height=abs(a.y - b.y) + 1) for a, b in itertools.combinations(polygon, 2)]
	p1_r = max(rectangles, key=lambda rect: rect.width * rect.height)
	p1_answer = p1_r.width * p1_r.height

	poly = Polygon([p.x, p.y] for p in polygon)
	areas = [r.height * r.width for r in rectangles]
	recs = [(min(r.c1.x, r.c2.x), min(r.c1.y, r.c2.y), max(r.c1.x, r.c2.x), max(r.c1.y, r.c2.y)) for r in rectangles]
	res = itertools.compress(areas, map(poly.contains, itertools.starmap(box, recs)))
	print(res)
	p2_answer = max(res)

	return p1_answer, p2_answer

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
