lines = open("input.txt").readline().split(',')
poses = [int(x) for x in lines]
print(poses)


def part1():
	total = 999999999999
	for i in poses:
		subtotal = sum([abs(x - i) for x in poses])
		# print(f'subtotal = {subtotal}')
		if subtotal < total:
			total = subtotal
	return total


def part2():
	total = 999999999999
	for i, item in enumerate(poses):
		subtotal = 0
		for x in poses:
			diff = abs(x - i)
			nonlineardiff = sum([x for x in range(diff + 1)])
			# print(f'{x}=>{i} = {diff} becomes {nonlineardiff}')
			subtotal += nonlineardiff
		# print(f'subtotal = {subtotal}')
		if subtotal < total:
			total = subtotal
	return total


print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
