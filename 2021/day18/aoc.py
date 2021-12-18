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
		print(f'giveleft, self={self}, val={val}, s={s}')
		if self.y == s:
			self.x += val
		else:
			elm = self.y
			while isinstance(elm.y, Pair):
				elm = elm.y
			elm.y += val

	def giveright(self, val: int, s):
		print(f'giveright, self={self}, val={val}, s={s}')
		if self.x == s:
			print(f'TRUE')
			self.y -= -val
		else:
			elm = self.x
			while isinstance(elm.x, Pair):
				elm = elm.x
			elm.x += val

	def split(self) -> bool:
		ret = False
		for i, item in enumerate([self.x, self.y]):
			if isinstance(item, Pair):
				tmpret = item.split()
				if tmpret:
					ret = True
			else:
				if item >= 10:
					# print(f'item = {item}')
					if i == 0:
						self.x = Pair(math.floor(item / 2), math.ceil(item / 2))
						self.x.parent = self
						# print(f'self.x={self.x}')
					else:
						self.y = Pair(math.floor(item / 2), math.ceil(item / 2))
						self.y.parent = self
						# print(f'self.y={self.y}')
					ret = True
		return ret

	def explode(self, depth: int = 0) -> bool:
		ret = False
		for item in [self.x, self.y]:
			# print(f'checking {item}')
			if isinstance(item, Pair):
				if depth == 3:
					# print(f'depth is 3, item ={item}')
					left, right = item.x, item.y
					p = self.parent
					s = self
					kkdepth = depth
					if item == self.x:
						print(f'item = self.x')
						self.y -= -right
						while p:
							if p.x != s:
								print(f'giving left, p={p}, s={s}, left={left}')
								p.giveleft(left, s)
								break
							s = p
							p = p.parent
							kkdepth -= 1
						self.x = 0
					else:
						self.x += left
						while p:
							# print(f'in p loop, p={p}, s={s} ,kkdepth={kkdepth}')
							if p.y != s and kkdepth != 0:
								# print(f'lets give right, p={p}, s={s}')
								p.giveright(right, s)
								break
							s = p
							p = p.parent
							kkdepth -= 1
						self.y = 0
					return True
				else:
					if item.explode(depth + 1):
						ret = True
						break
		return ret

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
	# print(str(pair))
	return pair


def reduce(nbs: list[Pair]) -> int:
	did_something = True
	while len(nbs) > 1 or did_something:
		print(f'nbs={str(nbs[0])}')
		did_something = False
		if nbs[0].explode(0):
			did_something = True
			continue

		if nbs[0].split():
			did_something = True
			continue

		if len(nbs) > 1:
			nbs[0] = nbs[0] + nbs[1]
			nbs.pop(1)
			did_something = True
			print(f'ADDED')
			continue

	print(f'{nbs[0]}')
	return nbs[0].get_magnitude()


lines = open('input.txt').read().splitlines()
rows = [parse_row(s) for s in lines]
# for row in rows:
# 	print(row)
# 	row.explode()
print(f'Part1: {reduce(rows)}')
