import aoc
import re
myinput = aoc.get_input(18)
# myinput = open('sample', 'r').read().splitlines()


class T:
	def __init__(self, val):
		self.val = val

	def __truediv__(self, other):  # Not really divison, just addition
		return T(self.val + other.val)

	def __add__(self, other):
		return T(self.val + other.val)

	def __mul__(self, other):
		return T(self.val * other.val)

	def __sub__(self, other):
		return T(self.val * other.val)

	def __str__(self):
		return str(self.val)

	def __radd__(self, other):
		if isinstance(other, int):
			return self.val + other
		elif isinstance(other, T):
			return T(self.val + other.val)


def parse_and_eval(line, secondpart=False):
	line = re.sub(r'(\d+)', r'T(\1)', line)
	line = line.replace('+', '/')
	if secondpart:
		line = line.replace('*', '-')
	return eval(line)


print(sum(parse_and_eval(line) for line in myinput))
print(sum(parse_and_eval(line, True) for line in myinput))
