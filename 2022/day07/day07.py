with open('input.txt', 'r') as f:
	lines = f.read().splitlines()

last_cmd = None
cwd = ''
directories = {
	'/': 0
}
for line in lines:
	print(line)
	if '$ ' in line:
		last_cmd = line
		if '$ cd' in line:
			path = line.split()[-1]
			print(f'{line=}, {path=}')
			if path == '..':
				last_slash_idx = cwd.rfind('/')
				new_cwd = cwd[:last_slash_idx]
				if not new_cwd:
					new_cwd = '/' + new_cwd
				print(f'{cwd=}, {last_slash_idx=}, {new_cwd=}')
				cwd = new_cwd
			else:
				if cwd and cwd[-1] != '/':
					cwd += '/'
				cwd += path
				print(f'cwd = {cwd}')
	else:
		words = line.split()
		if words[0] == 'dir':
			continue
		size = int(words[0])
		filename = words[1]
		subpath = cwd
		while subpath:
			dirsize = directories.get(subpath, 0)
			dirsize += size
			directories[subpath] = dirsize
			print(f'{subpath} = {dirsize} now')
			new_subpath = subpath[:subpath.rfind('/')]
			if subpath != '/' and new_subpath == '':
				subpath = '/'
			else:
				subpath = new_subpath
		# directories['/'] += size
		# print(f'"/" = {directories["/"]} now')

part_1 = part_2 = 0
for directory, size in directories.items():
	print(f'{directory} has size {size}')
	if size <= 100000 and directory != '/':
		part_1 += size
print(f'Part_1: {part_1}')


TOTAL_SPACE = 70_000_000
WANTED_UNUSED_SPACE = 30_000_000
TOTAL_USED_SPACE = directories['/']
UNUSED = TOTAL_SPACE - TOTAL_USED_SPACE
print(f'{TOTAL_SPACE=}, {TOTAL_USED_SPACE=}, {UNUSED=}')
print(f'{UNUSED=} + size >= {WANTED_UNUSED_SPACE=}')
for size in sorted(directories.values()):
	print(f'{size=}')
	if UNUSED + size >= WANTED_UNUSED_SPACE:
		print(f'Part 2: {size}')
		break
