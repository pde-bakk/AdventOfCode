with open('input.txt') as f:
	allfish = [int(x) for x in f.read().strip().split(',')]


def part1():
	for day in range(80):
		extrafish = 0
		for i, fish in enumerate(allfish):
			allfish[i] -= 1
			if allfish[i] == -1:
				allfish[i] = 6
				extrafish += 1
		for i in range(extrafish):
			allfish.append(8)
		# print(f'After\t{day} days: {allfish}')
	return len(allfish)


def part2(fishies):
	fishies = {x: fishies.count(x) for x in range(9)}
	for day in range(256):
		fishies = {x - 1: fishies[x] for x in fishies}
		day0fish = fishies.pop(-1)
		fishies[6] += day0fish
		fishies[8] = day0fish
		# print(f'After\t{day} days: {fishies}')
	return sum(fishies.values())


print(f'Part1: {part1()}')
print(f'Part2: {part2(allfish)}')
