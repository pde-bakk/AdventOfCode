with open('input.txt', 'r') as f:
	lines = f.read().splitlines()

cwd = ''
directories = {
	'/': 0
}
for line in lines:
	tokens = line.split()
	if tokens[0] == '$':
		if tokens[1] == 'cd':
			path = tokens[-1]
			if path == '..':
				last_slash_idx = cwd.rfind('/')
				cwd = cwd[:last_slash_idx]
				if not cwd:
					cwd = '/' + cwd
			else:
				if cwd and cwd[-1] != '/':
					cwd += '/'
				cwd += path
	else:
		if tokens[0] == 'dir':
			continue
		size, filename = int(tokens[0]), tokens[1]
		subpath = cwd
		while subpath:
			directories[subpath] = directories.get(subpath, 0) + size
			new_subpath = subpath[:subpath.rfind('/')]
			if subpath != '/' and new_subpath == '':
				subpath = '/'
			else:
				subpath = new_subpath

part_1 = part_2 = 0
for directory, size in directories.items():
	if size <= 100000 and directory != '/':
		part_1 += size
print(f'Part_1: {part_1}')


TOTAL_SPACE, WANTED_UNUSED_SPACE = 70_000_000, 30_000_000
USED_SPACE, UNUSED_SPACE = directories['/'], TOTAL_SPACE - directories['/']
for size in sorted(directories.values()):
	if UNUSED_SPACE + size >= WANTED_UNUSED_SPACE:
		print(f'Part 2: {size}')
		break
