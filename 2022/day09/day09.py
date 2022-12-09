with open('input.txt') as f:
	lines = f.read().splitlines()


def move_head(rope, d, length):
	match d:
		case 'U': rope[0][0] -= length
		case 'D': rope[0][0] += length
		case 'R': rope[0][1] += length
		case 'L': rope[0][1] -= length


def distance(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])


def touching(a, b) -> bool:
	return all(abs(p - q) <= 1 for p, q in zip(a, b))


def solve(ropelength: int):
	visited = set()
	rope = [[0, 0] for _ in range(ropelength)]
	for line_i, line in enumerate(lines):
		direction, amount = line.split()
		for _ in range(int(amount)):
			move_head(rope, direction, 1)
			for i in range(1, ropelength):
				diff = [p - q for p, q in zip(rope[i - 1], rope[i])]
				if not touching(rope[i], rope[i - 1]):
					diff = [d // abs(d)if d else 0 for d in diff]
					rope[i] = [p + q for p, q in zip(rope[i], diff)]
			visited.add(tuple(rope[-1]))
	return len(visited)


print(f'Part 1: {solve(2)}')
print(f'Part 2: {solve(10)}')
