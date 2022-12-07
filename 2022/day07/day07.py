with open('input.txt', 'r') as f:
	lines = f.read().splitlines()

cwd = []
directories = {}
for line in lines:
	match line.split():
		case '$', 'cd', '..':
			cwd.pop()
		case '$', 'cd', path:
			cwd += [path]
		case ['$', 'ls'] | ['dir', _]:
			pass
		case filesize, filename:
			for i in range(len(cwd), 0, -1):
				folder = '_'.join(cwd[:i])
				directories[folder] = directories.get(folder, 0) + int(filesize)

print('Part_1:', sum(v for k, v in directories.items() if v <= 100_000))
print('Part_2:', min(v for k, v in directories.items() if v >= directories['/'] - 40_000_000))
