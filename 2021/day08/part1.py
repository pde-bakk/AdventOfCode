def part1(rows: list[str]) -> int:
	total = 0
	for row in rows:
		_, output = row.split(' | ')
		output = output.split(' ')
		for item in output:
			total += int(len(set(item)) in (2, 3, 4, 7))
	return total


lines = open("input.txt").read().splitlines()
print(f'Part1: {part1(lines)}')
