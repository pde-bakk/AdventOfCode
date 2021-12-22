import numpy as np
import functools
from collections import Counter, deque
import operator
#import decorators


class Cube:
	def __init__(self):
		self.onoff = 'off'
		self.x, self.y, self.z = (0, 0), (0, 0), (0, 0)

	def parse(self, row: str):
		self.onoff, coords = row.split(' ')
		coords = [s[2:] for s in coords.split(',')]
		x2, y2, z2 = coords
		self.x = tuple([int(x) for x in x2.split('..')])
		self.y = tuple([int(x) for x in y2.split('..')])
		self.z = tuple([int(x) for x in z2.split('..')])

	def values(self):
		return [self.x[0], self.x[1], self.y[0], self.y[1], self.z[0], self.z[1]]

	def getvolume(self):
		return abs(self.x[1] - self.x[0]) * abs(self.y[1] - self.y[0]) - abs(self.z[1] - self.z[0])

	def does_overlap(self, other) -> bool:
		return self.x[1] > other.x[0] and self.x[0] < other.x[1] and \
			self.y[1] > other.y[0] and self.y[0] < other.y[1] and \
			self.z[1] > other.z[0] and self.z[0] < other.z[1]

	def overlap(self, other):
		if self.x[1] > other.x[0] and self.x[0] < other.x[1] and \
		self.y[1] > other.y[0] and self.y[0] < other.y[1] and \
		self.z[1] > other.z[0] and self.z[0] < other.z[1]:
				x
			pass
		raise ArithmeticError

def parse(filename: str):
	rows = open(filename).read().splitlines()
	parsed = []
	for row in rows:
		cube = Cube()
		cube.parse(row)
		parsed.append(cube)
	return parsed


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


def part2(cubes: list[Cube]) -> int:
	for cube in cubes:



def main(filename: str) -> tuple:
	rows = parse(filename)
	on_beacons = part1(rows)
	print(f'on_beacons={on_beacons}')
	return on_beacons, 0


if __name__ == '__main__':
	example_outcome = main('example.txt')
	assert example_outcome[0] == 47140
	assert example_outcome[1] == 2758514936282235
	real_outcome = main('input.txt')
	print(f'Part1: {real_outcome[0]}')
	print(f'Part2: {real_outcome[1]}')
