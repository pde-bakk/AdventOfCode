lines = open("input", 'r').read().split("\n")
nbs = sums = list()
for i in range(25):
	nbs.append(int(lines[i]))
for i in range(25, len(lines)):
	print(lines[i]) if int(lines[i]) not in [(x + y) for x in nbs for y in nbs if x != y] else ''
	nbs.pop(0)
	nbs.append(int(lines[i]))
