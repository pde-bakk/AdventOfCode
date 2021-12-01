def part1(rows: list) -> int:
	return len([i for i, _ in enumerate(rows) if i != 0 and rows[i] > rows[i - 1]])


def part2(rows: list) -> int:
	increases = 0
	for i in range(len(rows) - 2):
		prev = sum(rows[i: i + 3])
		curr = sum(rows[i + 1: i + 4])
		print(f'prev={prev}, curr={curr}, i = {i}')
		if curr > prev:
			increases += 1
	return increases


lines = open('input.txt', 'r').read().splitlines()
lines = [int(x) for x in lines]

print(lines)
print(part1(lines))
print(part2(lines))
