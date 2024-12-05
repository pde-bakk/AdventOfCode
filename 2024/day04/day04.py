import sys
import math

from aoc_lib.word_search import word_search, word_search_diagonal_x

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def parse(data: str) -> list[str]:
	lines = split_data_on_newlines(data)
	return lines

def aoc(data: str, prefix: str) -> None:
	lines = parse(data)
	part1 = word_search(lines, word_to_find='XMAS')
	part2 = word_search_diagonal_x(lines, word_to_find='MAS')
	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
