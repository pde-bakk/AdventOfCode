def get_adjacent_cubes(c: tuple[int]) -> tuple[int]:
	for i in range(3):
		for sign in [1, -1]:
			yield tuple([x if i2 != i else x + sign for i2,x in enumerate(c)])


def part_1() -> int:
	result = 0
	cubes = set()
	for line in lines:
		result += 6
		for adjacent_cube in get_adjacent_cubes(line):
			if adjacent_cube in cubes:
				result -= 2
		cubes.add(line)
	return result


def part_2() -> int:
	r = range(22)
	all_space = {(x, y, z) for x in r for y in r for z in r}
	empty_space = all_space - lines
	visited = set()
	to_visit = {min(empty_space)}
	result = 0

	while to_visit:
		pos = to_visit.pop()
		visited.add(pos)
		for adj in get_adjacent_cubes(pos):
			if adj in lines:
				result += 1
			elif adj in empty_space and adj not in visited:
				to_visit.add(adj)
	return result


with open('input.txt', 'r') as f:
	lines = set([tuple(map(int, x.split(','))) for x in f])

print(f'Part 1: {part_1()}')
print(f'Part 2: {part_2()}')
