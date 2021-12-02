def part1(rows: list) -> int:
	forwards, depth = 0, 0
	for r in rows:
		match r.split():
			case 'forward', n:
				forwards += int(n)
			case 'down', n:
				depth += int(n)
			case 'up', n:
				depth -= int(n)
	return forwards * depth


def part2(rows: list) -> int:
	forwards, depth, aim = 0, 0, 0
	for r in rows:
		match r.split():
			case 'forward', n:
				forwards += int(n)
				depth += aim * int(n)
			case 'down', n:
				aim -= int(n)
			case 'up', n:
				aim += int(n)
	return forwards * depth


lines = open('input.txt', 'r').read().splitlines()
print(f'Part1: {part1(lines)}')
print(f'Part2: {part2(lines)}')
