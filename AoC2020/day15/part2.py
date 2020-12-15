nbs = [int(x) for x in open('input', 'r').read().split(',')]
d = dict()
for i in range(len(nbs) - 1):
	d[nbs[i]] = i

while len(nbs) < 30000000:
	if nbs[-1] not in d:
		# print("{} is not in dictionary yet".format(nbs[-1]))
		nbs.append(0)
	else:
		nbs.append(len(nbs) - 1 - d[nbs[-1]])
	d[nbs[-2]] = len(nbs) - 2
	if len(nbs) % 3000000 == 0:
		print("10% done")
print(nbs[-1])
