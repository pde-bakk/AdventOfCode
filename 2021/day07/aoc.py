def part1():
	return min([sum(abs(x - i) for x in poses)for i in poses])


def part2():
	return min([sum(((x - i) ** 2 + abs(x - i)) // 2 for x in poses) for i in poses])


poses = [int(x) for x in open("input.txt").read().split(',')]
print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
