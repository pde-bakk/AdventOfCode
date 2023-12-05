import sys
import math
sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import split_on_double_newlines_instead


def do_part1(lines: list[str]):
	seeds, *mappings = lines
	seeds = lmap(int, seeds.split()[1:])
	seeds_d = {seed: [seed] for seed in seeds}

	for mapping in mappings:
		name, *lines = mapping.splitlines()
		new_seed_mapping = {seed: [] for seed, arr in seeds_d.items()}
		for line in lines:
			destination_range_start, source_range_start, range_length = map(int, line.split())
			for seed, l in seeds_d.items():
				latest = l[-1]
				if source_range_start <= latest < source_range_start + range_length:
					new_seed_mapping[seed].append(destination_range_start + (latest - source_range_start))
		for seed, arr in new_seed_mapping.items():
			if not arr:
				arr.append(seeds_d[seed][-1])
			seeds_d[seed].append(min(arr))
	return min([v[-1] for k, v in seeds_d.items()])


def do_part2(lines: list[str]):
	seeds, *mappings = lines
	seeds = lmap(int, seeds.split()[1:])
	mappings = [[lmap(int, line.split()) for line in m.splitlines()[1:]] for m in mappings]

	locations = []
	for i in range(0, len(seeds), 2):
		range_start, range_length = seeds[i:i+2]
		ranges = [(range_start, range_start + range_length)]
		new_ranges = []
		for m in mappings:
			while ranges:
				start_range, end_range = ranges.pop()
				for dest_start, source_start, range_len in m:
					source_end = source_start + range_len
					offset = dest_start - source_start
					if source_end <= start_range or end_range <= source_start:
						continue
					if start_range < source_start:
						ranges.append((start_range, source_start))
						start_range = source_start
					if source_end < end_range:
						ranges.append((source_end, end_range))
						end_range = source_end
					new_ranges.append((start_range + offset, end_range + offset))
					break
				else:
					# Will be called if the for-loop did not end with a break statement
					new_ranges.append((start_range, end_range))
			ranges = new_ranges
			new_ranges = []
		locations += ranges
	return min(loc[0] for loc in locations)


def aoc(lines: list[str], prefix: str) -> None:
	lines = split_on_double_newlines_instead(lines)
	part1 = do_part1(lines)
	part2 = do_part2(lines)

	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
