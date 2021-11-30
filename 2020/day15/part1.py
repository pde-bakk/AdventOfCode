nbs = [int(x) for x in open('input', 'r').read().split(',')]

while len(nbs) < 2020:
	if nbs[-1] not in nbs[:-1]:
		nbs.append(0)
	else:
		nbs.append( len(nbs) - 1 - max(i for i, val in enumerate(nbs[:-1]) if val == nbs[-1]) )
print(nbs[-1])