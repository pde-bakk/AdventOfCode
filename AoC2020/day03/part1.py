lines = open("day03/input", 'r').readlines()
trees = 0
index = -3
llen = len(lines[0]) - 1
for line in lines:
	index += 3
	index = index % llen
	if line[index] == '#':
		trees += 1

print(trees)
