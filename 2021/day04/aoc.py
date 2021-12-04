import numpy as np
import math


class Board:
	def __init__(self, string):
		nbs = [int(x) for x in string.split()]
		size = int(math.sqrt(len(nbs)))
		self.matrix = np.array(nbs, dtype=np.int16).reshape((size, size))

	def mark_nb(self, nb: int):
		found = np.where(self.matrix == nb)
		try:
			y, x = found[0][0], found[1][0]
			self.matrix[y][x] = -1
		except IndexError:
			pass

	def is_solved(self) -> bool:
		for i in range(self.matrix.shape[0]):
			if np.all(self.matrix[i] == self.matrix[i][0]):  # row i contains only marked numbers
				return True
			if np.all(self.matrix[:, i] == self.matrix[:, i][0]):  # column i contains only marked nbs
				return True
		return False

	def get_score(self):
		return sum([x[1] for x in np.ndenumerate(self.matrix) if x[1] != -1])


def setup_boards() -> list[Board]:
	return [Board(b) for b in lines]


def part1(bingoboards: list[Board]):
	for x in nbs_todraw:
		for b in bingoboards:
			b.mark_nb(x)
			if b.is_solved():
				return b.get_score() * x
	return 0


def part2(bingoboards: list[Board]):
	for x in nbs_todraw:
		for b in bingoboards:
			b.mark_nb(x)
		if len(bingoboards) >= 2:
			bingoboards = [b for b in bingoboards if not b.is_solved()]
		elif bingoboards[0].is_solved():
			return bingoboards[0].get_score() * x


lines = open('input.txt').read().split('\n\n')
nbs_todraw = [int(x) for x in lines.pop(0).split(',')]
boards = setup_boards()
print(f'Part1: {part1(boards)}')
print(f'Part2: {part2(boards)}')
