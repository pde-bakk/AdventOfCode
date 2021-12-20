import numpy as np
import functools
import operator


def parse(filename: str):
	rows = open(filename).read().splitlines()
	return rows


def main(filename: str) -> tuple:
	parsed = parse(filename)
	return 0, 0


if __name__ == '__main__':
	example_outcome = main('example.txt')
	assert example_outcome[0] == 0
	assert example_outcome[1] == 0
	real_outcome = main('input.txt')
	print(f'Part1: {real_outcome[0]}')
	print(f'Part2: {real_outcome[1]}')
