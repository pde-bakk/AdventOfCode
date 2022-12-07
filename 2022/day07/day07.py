with open('input.txt', 'r') as f:
	lines = f.read().splitlines()

last_cmd = None
cwd = ''
directories = {

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
			subpath = subpath[:subpath.rfind('/')]


part_1 = 0
for directory, size in directories.items():
	print(f'{directory} has size {size}')
	if size <= 100000:
		part_1 += size
print(f'Part_1: {part_1}')
