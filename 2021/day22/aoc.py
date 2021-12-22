import numpy as np
import functools
from collections import Counter, deque
import operator


class Cube:
	def __init__(self, arg=None, onoff='off'):
		self.onoff = onoff
		self.x, self.y, self.z = (0, 0), (0, 0), (0, 0)
		if isinstance(arg, str):
			self.parse(arg)
		elif isinstance(arg, list):
			self.x, self.y, self.z = arg

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y and self.z == other.z

	def __lt__(self, other):
		for c, c2 in zip([self.x, self.y, self.z], [other.x, other.y, other.z]):
			if c < c2:
				return True
			elif c > c2:
				return False
		return False

	def parse(self, row: str):
		self.onoff, coords = row.split(' ')
		coords = [s[2:] for s in coords.split(',')]
		x2, y2, z2 = coords
		self.x = tuple([int(x) for x in x2.split('..')])
		self.y = tuple([int(x) for x in y2.split('..')])
		self.z = tuple([int(x) for x in z2.split('..')])

	def __iter__(self):
		for c in [self.x, self.y, self.z]:
			yield c

	def get_intersection(self, other):
		if not self.does_overlap(other):
			return None
		new_cube = [(max(a[0], b[0]), min(a[1], b[1])) for a, b in zip(self, other)]
		print(f'new_cube = {new_cube}')
		intersection = Cube(new_cube, other.onoff)

	def values(self):
		return [self.x[0], self.x[1], self.y[0], self.y[1], self.z[0], self.z[1]]

	def getvolume(self):
		return abs(self.x[1] - self.x[0]) * abs(self.y[1] - self.y[0]) - abs(self.z[1] - self.z[0])

	def does_overlap(self, other) -> bool:
		return self.x[1] > other.x[0] and self.x[0] < other.x[1] and \
				self.y[1] > other.y[0] and self.y[0] < other.y[1] and \
				self.z[1] > other.z[0] and self.z[0] < other.z[1]

	# def overlap(self, other):
	# 	if self.x[1] > other.x[0] and self.x[0] < other.x[1] and \
	# 			self.y[1] > other.y[0] and self.y[0] < other.y[1] and \
	# 			self.z[1] > other.z[0] and self.z[0] < other.z[1]:
	# 		return T
	# 		pass
	# 	raise ArithmeticError


def parse(filename: str):
	rows = open(filename).read().splitlines()
	return [Cube(row) for row in rows]


def part1(cubes: list[Cube]):
	ons = set()
	for cube in cubes:
		if not all(-50 <= c <= 50 for c in cube.values()):
			continue
		for z in range(cube.z[0], cube.z[1] + 1):
			for y in range(cube.y[0], cube.y[1] + 1):
				for x in range(cube.x[0], cube.x[1] + 1):
					tup = (x, y, z)
					if cube.onoff == 'on':
						ons.add(tup)
					elif tup in ons:
						ons.remove(tup)
	return len(ons)


def part2(lines: list[Cube]) -> int:
	all_cubes = []
	for line in lines:
		new_cubes = []
		for cube in all_cubes:
			if cube.does_overlap(line):
				overlap = cube.get_intersection()
		all_cubes.extend(new_cubes)
		new_cubes.clear()
		pass
	return 0


def main(filename: str) -> tuple:
	rows = parse(filename)
	on_beacons = part1(rows)
	print(f'on_beacons={on_beacons}')
	part2(rows)
	return on_beacons, 0


if __name__ == '__main__':
	example_outcome = main('example.txt')
	assert example_outcome[0] == 474140
	assert example_outcome[1] == 2758514936282235
	real_outcome = main('input.txt')
	print(f'Part1: {real_outcome[0]}')
	print(f'Part2: {real_outcome[1]}')
