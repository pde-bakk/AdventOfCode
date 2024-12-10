import sys
import math
from collections import namedtuple

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


class File:
	def __init__(self, size: int, offset: int, index: int):
		self.size = size
		self.offset = offset
		self.id = index


	def __repr__(self):
		return f'File(size={self.size}, offset={self.offset}, index={self.id})'


def parse(data: str) -> list[File]:
	l1 = []
	offset = 0
	i = 0
	for idx, item in enumerate(data.strip()):
		if idx % 2 == 0:
			l1.append(File(size=int(item), offset=offset, index=i))
			i += 1
		offset += int(item)
	return l1


def move(file_idx: int, l: list[File]) -> bool:
	file = l[file_idx]
	for i, (a, b) in enumerate(zip(l, l[1:])):
		if a.offset > file.offset:
			continue
		available_space = b.offset - (a.offset + a.size)
		if available_space >= file.size:
			# new_size = min(available_space, file.size)
			new_size = file.size
			new_file = File(size=new_size, offset=a.offset + a.size, index=file.id)
			if file.size == new_size:
				l.pop(file_idx)
			else:
				l[file_idx].size -= new_size
				# print(f'Updated file, {l[file_idx]}')
			l.insert(i + 1, new_file)
			return True
	return False


def show(l1: list[File]) -> None:
	prev_offset = 0
	for i, file in enumerate(l1):
		free_space = file.offset - prev_offset
		print(free_space * '.' + str(file.id) * file.size, end='')
		prev_offset = file.offset + file.size
	print()

def solve(l1: list[File], part: int = 1) -> int:
	fuck = True
	while fuck:
		fuck = False
		for file_idx in range(len(l1) - 1, 0, -1):
			# print(f'{file_idx=}')
			move(file_idx, l1)
				# fuck = True
				# break
		# show(l1)
		# break
	# show(l1)
	# print(l1)
	result = []
	for file in l1:
		for i in range(file.offset, file.offset + file.size):
			result.append(file.id * i)
	# print(result)
	return sum(result)


def aoc(data: str, prefix: str) -> None:
	lines = parse(data)
	part1 = solve(lines, part=1)
	# part2 = solve(lines, part=2)
	print(f'{prefix} part 1: {part1}')
	# print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
