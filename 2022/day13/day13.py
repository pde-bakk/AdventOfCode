from functools import cmp_to_key


def cmp(a: int | list, b: int | list) -> int:
	if isinstance(a, int) and isinstance(b, int):
		return a - b
	if isinstance(a, list) and isinstance(b, list):
		for A, B in zip(a, b):
			result: int = cmp(A, B)
			if result != 0:
				return result
		return len(a) - len(b)
	if isinstance(a, int):
		return cmp([a], b)
	else:
		return cmp(a, [b])


with open('input.txt', 'r') as f:
	pairs = f.read().split('\n\n')
part_1 = []
total = [[[2]], [[6]]]
for i, pair in enumerate(pairs, start=1):
	first, second = pair.splitlines()
	left, right = eval(first), eval(second)
	in_order = cmp(left, right)
	if in_order <= 0:
		part_1.append(i)
	total.extend([left, right])

print(f'Part 1: {sum(part_1)}')
total.sort(key=cmp_to_key(cmp))
decoder_key = (total.index([[2]]) + 1) * (total.index([[6]]) + 1)
print(f'Part 2: {decoder_key}')
