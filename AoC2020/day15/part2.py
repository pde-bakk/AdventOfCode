nbs = [int(x) for x in open('input', 'r').read().split(',')]
d = dict()
for i in range(len(nbs) - 1):
	d[nbs[i]] = i
val = nbs[-1]
# print(d)
for i in range(len(nbs) - 1, 30000000 - 1):
	try:
		d[val], val = i, i - d[val]
	except KeyError:
		d[val], val = i, 0
print(val)
