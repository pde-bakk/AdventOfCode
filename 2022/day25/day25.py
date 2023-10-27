import math

def convert_from_snafu(s: str) -> int:
	snafu_value = 0
	for i, c in enumerate(s):
		power = 5 ** (len(s) - i - 1)
		if c.isdigit():
			n = int(c)
		else:
			n = -1 if c == '-' else -2
		snafu_value += n * power
	return snafu_value


def convert_to_snafu(n: int) -> str:
	compare = lambda x: abs(n - x[0])
	max_power = int(math.log(n, 5))
	options = [(c, convert_from_snafu(c)) for c in '210-=']
	snafu = ''
	for i in range(max_power, -1, -1):
		possibilities = sorted([(value * (5 ** i), c) for c, value in options], key=compare)
		value, c = possibilities[0]
		snafu += c
		n -= value

	assert n == 0
	return snafu


with open('input.txt', 'r') as f:
	lines = f.read().splitlines()
total = sum(map(convert_from_snafu, lines))
print(total)
print(convert_to_snafu(total))
