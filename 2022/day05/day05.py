import re
from copy import deepcopy


def simulate_instructions(containers: list, part: int) -> str:
	for line in instructions.splitlines():
		ints = [*map(int, re.findall(r'\d+', line))]
		if part == 1:
			for i in range(ints[0]):
				top = containers[ints[1] - 1].pop()
				containers[ints[2] - 1].append(top)
		else:
			for i in range(ints[0], 0, -1):
				top = containers[ints[1] - 1].pop(-i)
				containers[ints[2] - 1].append(top)
	return ''.join(container[-1] for container in containers)


with open('input.txt', 'r') as f:
	lines = f.read()
C, instructions = lines.split('\n\n')
C = C.splitlines()[::-1]
idxs = {i: int(c) for i, c in enumerate(C[0]) if c.isdigit()}
conts = [[] for _ in idxs.keys()]
for line_c in C[1:]:
	for k, v in idxs.items():
		if k < len(line_c) and line_c[k].isupper():
			conts[v - 1].append(line_c[k])

print('Part 1:' + simulate_instructions(deepcopy(conts), part=1))
print('Part 2:' + simulate_instructions(deepcopy(conts), part=2))
