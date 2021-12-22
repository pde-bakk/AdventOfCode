import numpy as np
import functools
from collections import Counter, deque
import operator
import math


class Cube:
	def __init__(self, arg=None, state=0):
		self.state = state
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
		state, coords = row.split(' ')
		self.state = bool(state == 'on')
		coords = [s[2:] for s in coords.split(',')]
		x2, y2, z2 = coords
		self.x = tuple([int(x) for x in x2.split('..')])
		self.y = tuple([int(x) for x in y2.split('..')])
		self.z = tuple([int(x) for x in z2.split('..')])

	def __iter__(self):
		for c in [self.x, self.y, self.z]:
			yield c

	def does_overlap(self, other) -> bool:
		return self.x[1] >= other.x[0] and self.x[0] < other.x[1] and \
				self.y[1] >= other.y[0] and self.y[0] < other.y[1] and \
				self.z[1] >= other.z[0] and self.z[0] < other.z[1]

	def get_intersection(self, other):
		if not self.does_overlap(other):
			return None
		new_cube = [(max(a[0], b[0]), min(a[1], b[1])) for a, b in zip(self, other)]
		return Cube(new_cube, other.state)

	def isvalid(self) -> bool:
		return self.x[1] >= self.x[0] and self.y[1] >= self.y[0] and self.z[1] >= self.z[0]

	def get_difference(self, other):
		inter = self.get_intersection(other)
		# print(f'self={self}')
		# print(f'other={other}')
		# print(f'intersection={inter}\n')
		if inter is None:
			return None
		subcubes = [
			Cube([self.x, (self.y[0], inter.y[0] - 1), self.z], state=self.state),
			Cube([self.x, (inter.y[1] + 1, self.y[1]), self.z], state=self.state),
			Cube([(self.x[0], inter.x[0] - 1), inter.y, self.z], state=self.state),
			Cube([(inter.x[1] + 1, self.x[1]), inter.y, self.z], state=self.state),
			Cube([inter.x, inter.y, (self.z[0], inter.z[0] - 1)], state=self.state),
			Cube([inter.x, inter.y, (inter.z[1] + 1, self.z[1])], state=self.state)
		]

		# for i, c in enumerate(subcubes):
		# 	print(f'subcube[{i}]={c}')
		return [c for c in subcubes if c.isvalid()]

	def __repr__(self):
		return f'Cube: {self.x}, {self.y}, {self.z} <= {self.state}, volume = {self.getvolume()}'

	def values(self):
		return [self.x[0], self.x[1], self.y[0], self.y[1], self.z[0], self.z[1]]

	def getvolume(self):
		# if not self.isvalid():
		# 	return -1
		return abs(self.x[1] - self.x[0] + 1) * abs(self.y[1] - self.y[0] + 1) * abs(self.z[1] - self.z[0] + 1)


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
					if cube.state:
						ons.add(tup)
					elif tup in ons:
						ons.remove(tup)
	return len(ons)


def part2(cubes: list[Cube]) -> int:
	all_cubes = []
	for existing_cube in cubes:
		new_cubes = []
		for cube in all_cubes:
			if cube.does_overlap(existing_cube):
				result = cube.get_difference(existing_cube)
				if result is not None:
					new_cubes.extend(result)
				else:
					raise AssertionError
			else:
				new_cubes.append(cube)
		if existing_cube.state:
			new_cubes.append(existing_cube)
		all_cubes = new_cubes
		print(f'ALL_CUBES IS NOW LENGTH {len(all_cubes)}')
	return sum([c.getvolume() for c in all_cubes])


def main(filename: str) -> tuple:
	rows = parse(filename)
	on_beacons = part1(rows)
	print(f'on_beacons={on_beacons}')
	ans = part2(rows)
	print(f'ans={ans}')
	return on_beacons, ans


if __name__ == '__main__':
	example_outcome = main('example.txt')
	assert example_outcome[0] == 474140
	assert example_outcome[1] == 2758514936282235
	real_outcome = main('honey.txt')
	print(f'Part1: {real_outcome[0]}')
	print(f'Part2: {real_outcome[1]}')

# Not 1227345351869917
