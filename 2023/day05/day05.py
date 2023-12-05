import sys
import math
sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *


def parse(lines: list[str]):
	x = '\n'.join(lines).split('\n\n')
	seeds = lmap(int, x[0].replace('seeds: ', '').split())
	seeds_d = {seed: [seed] for seed in seeds}

	for mapping in x[1:]:
		name, *lines = mapping.splitlines()
		print(f'{name=}')
		new_seed_mapping = {seed: [] for seed, arr in seeds_d.items()}
		for line in lines:
			destination_range_start, source_range_start, range_length = map(int, line.split())
			for seed, l in seeds_d.items():
				latest = l[-1]
				if source_range_start <= latest < source_range_start + range_length:
					new_seed_mapping[seed].append(destination_range_start + (latest - source_range_start))
		print(f'{new_seed_mapping=}')
		for seed, arr in new_seed_mapping.items():
			if not arr:
				arr.append(seeds_d[seed][-1])
			seeds_d[seed].append(min(arr))
		print(f'{seeds_d=}')
	ret = [v[-1] for k, v in seeds_d.items()]
	print(ret)
	return min(ret)


def aoc(lines: list[str], prefix: str) -> None:
	part1 = parse(lines)
	part2 = 0

	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
