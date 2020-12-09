lines = open("input", 'r').read().split("\n")
i = 0
nbs = sums = list()

while i < 25:
	nbs.append(int(lines[i]))
	i += 1

while i < len(lines):
	sums = [(x + y) for x in nbs for y in nbs if x != y]
	value = int(lines[i])
	if value not in sums:
		print("False for {} at line number {}.".format(value, i))
	nbs.pop(0)
	nbs.append(value)
	i += 1
