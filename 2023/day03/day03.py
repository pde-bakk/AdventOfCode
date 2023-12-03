import math
import sys
sys.path.append('../..')
from aoc_lib.get_input import get_input_file
from aoc_lib.utilities import *

lines = get_input_file()
# lines = open('sample.txt').read().splitlines()
print(lines)
part1 = 0
gears = {}
for y, line in enumerate(lines):
	x = [(int(m.group(0)), m.start()) for m in re.finditer(r'\d+', line)]
	print(f'{x=}')
	for d, idx in x:
		# idx = line.index(str(d))
		has_symbol = False
		for x in range(idx, idx + len(str(d))):
			neighbours = get_neighbours(y, x, diagonal=True)
			for n in neighbours:
				if 0 <= n[0] < len(lines) and 0 <= n[1] < len(line) and lines[n[0]][n[1]] not in '.1234567890':
					has_symbol = True
					gears[n] = gears.get(n, []) + [d]
					print(f'{d=}, {n=}, {gears[n]=}')
					break
		if has_symbol:
			part1 += d

part2 = 0
for k, v in gears.items():
	v = list(set(v))
	if len(v) == 2:
		part2 += math.prod(v)
		print(k, v, math.prod(v))
print(part1)
print(part2)
