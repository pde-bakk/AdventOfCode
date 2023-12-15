import sys
import math
sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import split_data_on_newlines


def hash_algo(string):
	s = 0
	for c in string:
		s = ((s + ord(c)) * 17) % 256
	return s


def part1_loop(items: list[str]):
	arr = []
	for item in items:
		arr.append(hash_algo(item))
	return sum(arr)


def aoc(data: str, prefix: str) -> None:
	lines = split_data_on_newlines(data)
	part2 = 0
	items = lines[0].split(',')
	print(f'{prefix} part 1: {part1_loop(items)}')
	boxes = {}

	for item in items:
		if '-' in item:
			label = item[:item.index('-')]
			h = hash_algo(label)
			box = boxes.get(h, [])
			box = [(lbl, lens) for lbl, lens in box if lbl != label]
			boxes[h] = box
		elif '=' in item:
			label, focal_length = item.split('=')
			focal_length = int(focal_length)
			h = hash_algo(label)
			box = boxes.get(h, [])
			for i, (lbl, lens) in enumerate(box):
				if lbl == label:
					box[i] = (label, focal_length)
					break
			else:  # Only triggers if the for-loop didn't end with a break statement
				box.append((label, focal_length))
			boxes[h] = box

	for key, box in boxes.items():
		for slot, (lbl, lens) in enumerate(box):
			part2 += (key + 1) * (slot + 1) * lens
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
