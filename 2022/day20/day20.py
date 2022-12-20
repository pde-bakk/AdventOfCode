import copy


def solve(old_ints: list, key: int = 1, iterations: int = 1):
	ints = [(i, key * x) for i, x in old_ints]
	length = len(ints)
	for iteration in range(iterations):
		for i in range(length):
			for idx in range(length):
				if ints[idx][0] == i:  # got the right index
					_, val = ints[idx]

					ints.pop(idx)
					new_idx = (idx + val) % (length - 1)
					ints.insert(new_idx, (i, val))
					break

	index_0 = [i for i, (_, x) in enumerate(ints) if x == 0][0]
	return sum([ints[(index_0 + G) % length][1] for G in [1000, 2000, 3000]])


with open('input.txt', 'r') as f:
	integers = [(i, int(x)) for i, x in enumerate(f)]
decryption_key = 811589153

print(f'Part 1: {solve(integers)}')
print(f'Part 2: {solve(integers, key=decryption_key, iterations=10)}')
