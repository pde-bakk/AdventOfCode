import math


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
		# print(f'giveright, self={self}, val={val}, s={s}')
		if self.x == s:
			# print(f'TRUE')
			self.y -= -val
		else:
			elm = self.x
			while isinstance(elm.x, Pair):
				elm = elm.x
			elm.x += val

	def dosplit(self) -> bool:
		for i, item in enumerate([self.x, self.y]):
			if isinstance(item, int) and item >= 10:
				# print(f'item = {item}')
				half = item / 2
				if i == 0:
					self.x = Pair(item // 2, math.ceil(half))
					self.x.parent = self
					# print(f'SPLIT {item} into {self.x}')
				# print(f'self.x={self.x}')
				else:
					self.y = Pair(item // 2, math.ceil(half))
					self.y.parent = self
					# print(f'SPLIT {item} into {self.y}')
					# print(f'self.y={self.y}')
				return True
		return False

	# def dosomething(self, depth: int = 0) -> bool:
	# 	for i, item in enumerate([self.x, self.y]):
	# 		if isinstance(item, Pair):
	# 			# print(f'depth={depth}, item={item}')
	# 			if depth == 3 and self.doexplode():
	# 				return True
	# 		else:
	# 			if self.dosplit():
	# 				return True
	# 		if isinstance(item, Pair) and item.dosomething(depth + 1):
	# 			return True
	# 	return False

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
			if self.dosplit():
				return True
			if isinstance(item, Pair) and item.then_split():
				return True
		return False

	def doexplode(self) -> bool:
		for item in [self.x, self.y]:
			if isinstance(item, Pair):
				# print(f'Exploding {item}')
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


def reduce(nbs: list[Pair]) -> int:
	did_something = True
	adds = 0
	while len(nbs) > 1 or did_something:
		if adds == 4:
			print(f'num={str(nbs[0])}')
		did_something = False
		if nbs[0].first_explode(0):
			did_something = True
			continue
		# print(f'lets explode')
		if nbs[0].then_split():
			did_something = True
			continue

		if len(nbs) > 1:
			print(f'...={str(nbs[0])}')
			nbs[0] = nbs[0] + nbs[1]
			nbs.pop(1)
			adds += 1
			did_something = True
			# print(f'ADDED')
			continue

	print(f'{nbs[0]}')
	return nbs[0].get_magnitude()


lines = open('input.txt').read().splitlines()
rows = [parse_row(s) for s in lines]
print(f'Part1: {reduce(rows)}')
