with open('input.txt', 'r') as f:
	lines = f.read().splitlines()


def update_cycle():
	global cycle, cycles
	cycle += 1
	cycles[cycle] = X


X = 1
cycle = 1
cycles = {}
for line in lines:
	tokens = line.split()
	match tokens[0]:
		case 'noop':
			update_cycle()
		case 'addx':
			update_cycle()
			X += int(tokens[1])
			# print(f'Cycle is {cycle},{tokens[1]=} {X=}')
			update_cycle()

for c in [20, 60, 100, 140, 180, 220]:
	print(f'During cycle {c}, {X=}, {c * X =}')

print(f'Part 1:', sum(cycles[c] * c for c in [20, 60, 100, 140, 180, 220]))
