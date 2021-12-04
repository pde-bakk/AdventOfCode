import numpy as np
import math


class Board:
	def __init__(self, string):
		self.matrix = []
		nbs = [int(x) for x in string.split()]
		size = int(math.sqrt(len(nbs)))
		self.matrix = np.array(nbs, dtype=np.int16).reshape((size, size))

	def mark_nb(self, nb: int):
		found = np.where(self.matrix == nb)
		try:
			y, x = found[0][0], found[1][0]
			# print(f'found {nb} at {x, y}')
			self.matrix[y][x] = -1
		except IndexError:
			pass

	def is_solved(self) -> bool:
		for i in range(self.matrix.shape[0]):
			# print(f'self.matrix[{i}] = {self.matrix[i]}')
			if np.all(self.matrix[i] == self.matrix[i][0]):  # row i contains only marked numbers
				return True
			# print(f'self.matrix[:{i}] = {self.matrix[:, i]}')
			if np.all(self.matrix[:, i] == self.matrix[:, i][0]):  # column i contains only marked nbs
				return True
		return False

	def get_score(self):
		total = 0
		for item in np.ndenumerate(self.matrix):
			if item[1] != -1:
				# print(f'adding {item[1]}')
				total += item[1]  # item[0] is the index
		return total


def setup_boards():
	for b in lines:
		boards.append(Board(b))


def part1():
	for x in nbs_todraw:
		for b in boards:
			b.mark_nb(x)

		for b in boards:
			if b.is_solved():
				return b.get_score() * x
	return 0


def part2(bingoboards):
	for x in nbs_todraw:
		for b in bingoboards:
			b.mark_nb(x)
		if len(bingoboards) >= 2:
			bingoboards = [b for b in bingoboards if not b.is_solved()]
		elif bingoboards[0].is_solved():
			return bingoboards[0].get_score() * x


lines = open('input.txt').read().split('\n\n')
nbs_todraw = [int(x) for x in lines.pop(0).split(',')]
print(lines)
boards = []
setup_boards()
# print(f'Part1: {part1()}')
print(f'Part2: {part2(boards)}')
