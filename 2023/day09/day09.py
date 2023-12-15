import sys
import math
sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *


def aoc(data: str, prefix: str) -> None:
	lines = split_data_on_newlines(data)
	part1 = 0
	part2 = 0
	lines = [lmap(int, line.split()) for line in lines]
	for line in lines:
		history = [line]
		while any(i != 0 for i in history[-1]):
			diffs = [b - a for a, b in zip(history[-1], history[-1][1:])]
			history.append(diffs)
		history = history[::-1]
		for i, his in enumerate(history):
			if i == 0:
				history[i] = [0] + his + [0]
			else:
				history[i] = [his[0] - history[i - 1][0]] + his + [history[i-1][-1] + his[-1]]
			if i == len(history) - 1:
				part1 += history[i][-1]
				part2 += history[i][0]
	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
