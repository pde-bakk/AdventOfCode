import sys
import math
sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import split_on_double_newlines_instead


def parse(lines: list[str]):
	return lines[0].split(',')


def hash_algo(string):
	s = 0
	for c in string:
		s = ((s + ord(c)) * 17) % 256
	return s


def loop(items: list[str]):
	arr = []
	for item in items:
		arr.append(hash_algo(item))
	return sum(arr)


def aoc(lines: list[str], prefix: str) -> None:
	part1 = 0
	part2 = 0
	items = parse(lines)
	print(f'{prefix} part 1: {loop(items)}')
	boxes = {}

	for item in items:
		if '-' in item:
			label = item[:item.index('-')]
		elif '=' in item:
			label, focal_length = item.split('=')
			focal_length = int(focal_length)
		else:
			raise NotImplementedError
		print(f'{label=}, {hash_algo(label)}')
		h = hash_algo(label)
		box = boxes.get(h, [])
		if '-' in item:
			box = [(lbl, lens) for lbl, lens in box if lbl != label]
			boxes[h] = box
		else:
			found = False
			for i, (lbl, lens) in enumerate(box):
				if lbl == label:
					box[i] = (label, focal_length)
					found = True
					break
			if not found:
				box.append((label, focal_length))
			boxes[h] = box

	for key, box in boxes.items():
		if box:
			print(f'{key}, {box}')
			for slot, (lbl, lens) in enumerate(box):
				part2 += (key + 1) * (slot + 1) * lens
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
