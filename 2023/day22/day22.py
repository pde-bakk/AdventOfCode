import sys
import math
import copy

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


class Brick:
	def __init__(self, arg):
		if isinstance(arg, str):
			(x1, y1, z1), (x2, y2, z2) = [lmap(int, p.split(',')) for p in arg.split('~')]
			self.x = [x1, x2]
			self.y = [y1, y2]
			self.z = [z1, z2]
			if x1 > x2 or y1 > y2 or z1 > z2:
				print(f'Not sorted, {self=}')
		elif isinstance(arg, Brick):
			self.x = arg.x.copy()
			self.y = arg.y.copy()
			self.z = arg.z.copy()
		else:
			raise NotImplementedError

	def __str__(self):
		# return f'Brick: side1={self.x1, self.y1, self.z1}, side2={self.x2, self.y2, self.z2}'
		return f'Brick(x={self.x}, y={self.y}, z={self.z})'

	def is_equal(self, other):
		if not isinstance(other, Brick):
			return NotImplemented
		return (self.x, self.y, self.z) == (other.x, other.y, other.z)

	def __eq__(self, other):
		if not isinstance(other, Brick):
			return NotImplemented
		return all([max(a[0], b[0]) < min(a[1] + 1, b[1] + 1) for a, b in zip([self.x, self.y, self.z], [other.x, other.y, other.z])])
		# return (self.x, self.y, self.z) == (other.x, other.y, other.z)

	def sim_down(self):
		new_brick = Brick(self)
		new_brick.z = [z - 1 for z in new_brick.z]
		return new_brick

	def __repr__(self):
		return str(self)


def make_brickies_fall(bricks: list[Brick]) -> tuple[int, list[Brick]]:
	set_bricks = []
	d = {i: set() for i in range(len(bricks))}
	amount_fell = 0
	for brick in bricks:
		# print(f'Checking {brick}')
		# og_brick = copy.deepcopy(brick)
		down = 0
		assert brick not in set_bricks
		while min(brick.z) > 1 and (brick_down := brick.sim_down()) not in set_bricks:
			brick = brick_down
			down += 1
		if down > 0:
			amount_fell += 1
		set_bricks.append(brick)
	return amount_fell, set_bricks


def solve2(lines: list[str], prefix):
	sort_bricks = lambda br: min(br.z)
	bricks = lmap(Brick, lines)
	bricks.sort(key=sort_bricks)
	_, bricks = make_brickies_fall(bricks)
	# ans_1 = 0
	# for i in range(len(bricks)):
	# 	bricks_copy = copy.copy(bricks)
	# 	bricks.sort(key=sort_bricks)
	# 	bricks_copy.pop(i)
	# 	amount_fell, _ = make_brickies_fall(bricks_copy)
	# 	if amount_fell == 0:
	# 		ans_1 += 1
	# print(f'{prefix} part 1: {ans_1}')

	ans_2 = 0
	for i in range(len(bricks)):
		bricks_copy = bricks.copy()
		bricks_copy.pop(i)
		brick_copy_2 = bricks_copy.copy()
		amount_fell = 1
		while amount_fell > 0:
			amount_fell, bricks_copy = make_brickies_fall(bricks_copy)
		mm = 0
		for a, b in zip(bricks_copy, brick_copy_2):
			if not a.is_equal(b):
				mm += 1
		print(f'When removing brick {i}, {mm=}')
		ans_2 += mm
	print(f'{prefix} part 2: {ans_2}')

# def solve(lines: list[str]) -> int:
# 	bricks = lmap(Brick, lines)
# 	bricks.sort(key=lambda br: min(br.z))
# 	# print(bricks)
# 	set_bricks = []
# 	d = {i: set() for i in range(len(bricks))}
# 	for brick in bricks:
# 		# print(f'Checking {brick}')
# 		# og_brick = copy.deepcopy(brick)
# 		down = 0
# 		assert brick not in set_bricks
# 		while min(brick.z) > 1 and (brick_down := brick.sim_down()) not in set_bricks:
# 			brick = brick_down
# 			down += 1
# 		if min(brick.z) > 1:
# 			one_more_down = brick.sim_down()
# 			for i, b in enumerate(set_bricks):
# 				if one_more_down == b:
# 					d[len(set_bricks)].add(i)
# 		# if down > 0:
# 		# 	print(f'Moved {og_brick} {down} down to become {brick}')
# 		# else:
# 		# 	print(f'Didnt move {brick}')
# 		set_bricks.append(brick)
# 	# print(set_bricks)
# 	disintegrable = 0
# 	# print(f'{d=}')
# 	for i in range(len(set_bricks)):
# 		if {i} not in d.values():
# 			disintegrable += 1
# 	# for i, supports in d.items():
# 	# 	if len(supports) == 1:
# 	# 		disintegrable += 1
# 	return disintegrable


def aoc(data: str, prefix: str) -> None:
	lines = split_data_on_newlines(data)
	solve2(lines, prefix)
	# part1 = solve(lines)
	# part2 = 0
	# print(f'{prefix} part 1: {part1}')
	# print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
