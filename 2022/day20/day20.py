with open('input.txt', 'r') as f:
	ints = [(i, int(x)) for i, x in enumerate(f)]
length = len(ints)

for i in range(length):
	for idx in range(length):
		if ints[idx][0] == i:  # got the right index
			_, val = ints[idx]

			ints.pop(idx)
			new_idx = (idx + val) % (length - 1)
			ints.insert(new_idx, (i, val))
			break

index_0 = [i for i, (_, x) in enumerate(ints) if x == 0][0]
part_1 = [ints[(index_0 + G) % length][1] for G in [1000, 2000, 3000]]
print(f'Part 1: {sum(part_1)}')
