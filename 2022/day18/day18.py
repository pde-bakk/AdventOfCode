def get_adjacent_cubes(c: tuple[int]) -> tuple[int]:
	for i in range(3):
		for sign in [1, -1]:
			yield tuple([x if i2 != i else x + sign for i2,x in enumerate(c)])


with open('test.txt', 'r') as f:
	lines = [tuple(map(int, x.split(','))) for x in f]

cubes = set()
part_1 = 0

for line in lines:
	part_1 += 6
	for adjacent_cube in get_adjacent_cubes(line):
		if adjacent_cube in cubes:
			part_1 -= 2
	cubes.add(line)
print(f'Part 1: {part_1}')
