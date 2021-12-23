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

	# @functools.lru_cache(maxsize=None)
	def does_overlap(self, other) -> bool:
		return all(a[0] <= b[1] and a[1] >= b[0] for a, b in zip(self, other))

	def get_intersection(self, other):
		assert self.does_overlap(other)

		new_cube = [(max(a[0], b[0]), min(a[1], b[1])) for a, b in zip(self, other)]
		return Cube(new_cube, other.state)

	def isvalid(self) -> bool:
		return all(c[1] >= c[0] for c in self.__iter__())

	def get_difference(self, other):
		inter = self.get_intersection(other)
		assert inter is not None
		subcubes = [
			Cube([self.x, (self.y[0], inter.y[0] - 1), self.z], state=True),
			Cube([self.x, (inter.y[1] + 1, self.y[1]), self.z], state=True),
			Cube([(self.x[0], inter.x[0] - 1), inter.y, self.z], state=True),
			Cube([(inter.x[1] + 1, self.x[1]), inter.y, self.z], state=True),
			Cube([inter.x, inter.y, (self.z[0], inter.z[0] - 1)], state=True),
			Cube([inter.x, inter.y, (inter.z[1] + 1, self.z[1])], state=True)
		]
		return [c for c in subcubes if c.isvalid()]

	def __repr__(self):
		return f'Cube: {self.x}, {self.y}, {self.z} <= {self.state}'

	def values(self):
		return [self.x[0], self.x[1], self.y[0], self.y[1], self.z[0], self.z[1]]

	def getvolume(self):
		if not self.isvalid():
			raise IndexError
		return math.prod([c[1] - c[0] + 1 for c in self.__iter__()])


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
	for kkkubus in cubes:
		new_cubes = []
		for cube in all_cubes:
			if cube.does_overlap(kkkubus):
				new_cubes.extend(cube.get_difference(kkkubus))
			else:
				new_cubes.append(cube)
		if kkkubus.state:
			new_cubes.append(kkkubus)
		all_cubes = new_cubes
	print(len(all_cubes))
	return sum([c.getvolume() for c in all_cubes])


def main(filename: str) -> tuple:
	rows = parse(filename)
	on_beacons = part1(rows)
	# print(f'on_beacons={on_beacons}')
	ans = part2(rows)
	print(f'ans={ans}')
	return on_beacons, ans


if __name__ == '__main__':
	example_outcome = main('example.txt')
	assert example_outcome[0] == 474140
	assert example_outcome[1] == 2758514936282235
	real_outcome = main('input.txt')
	print(f'Part1: {real_outcome[0]}')
	print(f'Part2: {real_outcome[1]}')

# Not 1227345351869917
