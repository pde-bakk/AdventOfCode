import math
from copy import deepcopy
from itertools import permutations


class Pair:
	def __init__(self, x=None, y=None):
		self.x = x
		self.y = y
		self.parent = None

	def append(self, val):
		if self.x is not None and self.y is not None:
			print(f'Error, tried to add {val}, but Pair already has 2 members {self.x, self.y}')
		if self.x is None:
			self.x = val
		else:
			self.y = val

	def __str__(self):
		return f'[{self.x}, {self.y}]'

	def __add__(self, other):
		if isinstance(other, Pair):
			pair = Pair(self, other)
			self.parent = pair
			other.parent = pair
			return pair
		elif isinstance(other, int):
			self.y += other
			return self
		else:
			raise ValueError

	def __sub__(self, other):
		if isinstance(other, Pair):
			pass
		elif isinstance(other, int):
			self.x -= other
			return self
		else:
			raise ValueError

	def giveleft(self, val: int, s):
		# print(f'giveleft, self={self}, val={val}, s={s}')
		if self.y == s:
			self.x += val
		else:
			elm = self.y
			while isinstance(elm.y, Pair):
				elm = elm.y
			elm.y += val

	def giveright(self, val: int, s):
		if self.x == s:
			self.y -= -val
		else:
			elm = self.x
			while isinstance(elm.x, Pair):
				elm = elm.x
			elm.x += val

	def dosplit(self) -> bool:
		for i, item in enumerate([self.x, self.y]):
			if isinstance(item, int) and item >= 10:
				half = item / 2
				print(f'Splitted {item}')
				if i == 0:
					self.x = Pair(item // 2, math.ceil(half))
					self.x.parent = self
				else:
					self.y = Pair(item // 2, math.ceil(half))
					self.y.parent = self
				return True
		return False

	def first_explode(self, depth: int = 0) -> bool:
		for i, item in enumerate([self.x, self.y]):
			if isinstance(item, Pair):
				if depth == 3 and self.doexplode():
					return True
				if item.first_explode(depth + 1):
					return True
		return False

	def then_split(self) -> bool:
		for i, item in enumerate([self.x, self.y]):
			if isinstance(item, Pair) and item.then_split():
				return True
			if self.dosplit():
				return True
		return False

	def doexplode(self) -> bool:
		for item in [self.x, self.y]:
			if isinstance(item, Pair):
				print(f'Exploding {item}')
				left, right = item.x, item.y
				p, s = self.parent, self
				if item == self.x:
					self.y -= -right
					while p:
						if p.x != s:
							p.giveleft(left, s)
							break
						s = p
						p = p.parent
					self.x = 0
				else:
					self.x += left
					while p:
						if p.y != s:
							p.giveright(right, s)
							break
						s = p
						p = p.parent
					self.y = 0
				return True
		return False

	def get_magnitude(self):
		if isinstance(self.x, Pair):
			magn = 3 * self.x.get_magnitude()
		else:
			magn = 3 * self.x
		if isinstance(self.y, Pair):
			magn += 2 * self.y.get_magnitude()
		else:
			magn += 2 * self.y
		return magn


def parse_row(__row: str) -> Pair:

	def parse_pair(s: str, i: int) -> tuple[Pair, int]:
		curr = Pair()
		while i in range(len(s) - 1):
			if s[i] == '[':
				elem, i = parse_pair(s, i + 1)
				elem.parent = curr
				curr.append(elem)
			elif s[i] == ']':
				return curr, i
			elif s[i] != ',':
				curr.append(int(s[i]))
			i += 1
		return curr, i
	pair, idx = parse_pair(__row, 1)
	return pair


def reduce(og: list[Pair]) -> int:
	did_something = True
	adds = 0
	nbs = deepcopy(og)
	while len(nbs) > 1 or did_something:
		did_something = False
		while nbs[0].first_explode(0) or nbs[0].then_split():
			print(f'num={str(nbs[0])}')
			did_something = True
			pass

		if len(nbs) > 1:
			# Reduce nbs[1]
			while nbs[1].first_explode(0) or nbs[1].then_split():
				pass
			nbs[0] = nbs[0] + nbs[1]
			nbs.pop(1)
			print(f'AFTER ADDING NEW ROW, NBS = {str(nbs[0])}')
			adds += 1
			did_something = True
			# print(f'ADDED')
			continue

	# print(f'{nbs[0]}')
	return nbs[0].get_magnitude()


def part2(nbs: list[Pair]) -> int:
	poss = permutations(nbs, 2)
	answer = 0
	for i, p in enumerate(poss):
		tmp = reduce(list(p))
		answer = max(answer, tmp)
		# print(f'{p[0]} + {p[1]} = {tmp}')
	return answer


lines = open('input.txt').read().splitlines()
rows = [parse_row(s) for s in lines]
print(f'Part1: {reduce(rows)}')
# print(f'Part2: {part2(rows)}')
