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
for i, pair in enumerate(pairs, start=1):
	first, second = pair.splitlines()
	left, right = eval(first), eval(second)
	print(f'{left=}, {right=}')
	in_order = cmp(left, right)
	if in_order <= 0:
		part_1.append(i)
		print(f'Pair {i} is in order, boss!, result={in_order}')
	else:
		print(f'Pair {i} is not in order, sorry. result={in_order}')
	print()

print(f'Part 1: {sum(part_1)}')
