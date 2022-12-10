with open('input.txt', 'r') as f:
	lines = f.read().splitlines()


def update_cycle():
	global cycle, cycles
	cycle += 1
	cycles[cycle] = X


def draw_on_crt(c):
	char = '#' if abs(X - (c % 40)) <= 1 else '.'
	crt[c // 40][c % 40] = char


X = 1
cycle = 1
cycles = {}
crt = [['.'] * 40 for _ in range(6)]
for line in lines:
	tokens = line.split()
	match tokens[0]:
		case 'noop':
			draw_on_crt(cycle - 1)
			update_cycle()
		case 'addx':
			draw_on_crt(cycle - 1)
			update_cycle()
			draw_on_crt(cycle - 1)
			X += int(tokens[1])
			update_cycle()


print(f'Part 1:', sum(cycles[c] * c for c in [20, 60, 100, 140, 180, 220]))
print(f'Part 2:')
for row in crt:
	print(''.join(row))
