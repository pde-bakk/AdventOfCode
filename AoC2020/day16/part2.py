from collections import defaultdict
import re

row = open('input', 'r').read().split('\n')
row = [x for x in row if x != '']
ranges = defaultdict(list)
mine = True
error_rate = 0
for i, r in enumerate(row):
	if 'or' in r:
		k, v = [x.strip() for x in r.split(':')]
		for ran in [x.strip() for x in v.split('or')]:
			start, end = map(int, re.findall(r'\d+', ran))
			ranges[k].append( (start, end) )
	elif 'nearby tickets' in r:
		mine = False
	elif mine:
		continue
	else:
		for nb in map(int, re.findall(r'\d+', r)):
			valid = False
			for k in ranges:
				for subrange in ranges[k]:
					if nb in range(subrange[0], subrange[1] + 1):
						valid = True
			if not valid:
				error_rate += nb

print(error_rate)