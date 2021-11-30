lines = open("day03/input", 'r').read().splitlines()
trees = index = 0
for line in lines:
	if line[index] == '#': trees += 1
	index = (index + 3) % len(line)
print(trees)
