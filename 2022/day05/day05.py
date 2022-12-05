import re

with open('input.txt', 'r') as f:
	lines = f.read()
C, I = lines.split('\n\n')
C = C.splitlines()[::-1]
idxs = {i: int(c) for i, c in enumerate(C[0]) if c.isdigit()}
containers = [[] for _ in idxs.keys()]
for line in C[1:]:
	for k, v in idxs.items():
		if k < len(line) and line[k].isupper():
			containers[v - 1].append(line[k])
print(containers)

for line in I.splitlines():
	ints = [*map(int, re.findall(r'\d+', line))]
	print(ints)
	for i in range(ints[0], 0, -1):
		top = containers[ints[1] - 1].pop(-i)
		containers[ints[2] - 1].append(top)
for c in containers:
	print(c[-1], end='')
