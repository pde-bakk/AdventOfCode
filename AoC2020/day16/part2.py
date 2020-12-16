from collections import defaultdict
import re

row = open('input', 'r').read().split('\n')
row = [x for x in row if x != '']
ranges = defaultdict(list)
mine = True
error_rate = 0
validtickets = list()
myticket = list()
for i, r in enumerate(row):
	if 'or' in r:
		k, v = [x.strip() for x in r.split(':')]
		for ran in [x.strip() for x in v.split('or')]:
			start, end = map(int, re.findall(r'\d+', ran))
			ranges[k].append( (start, end) )
	elif 'nearby tickets' in r:
		mine = False
	elif mine:
		if 'your ticket' not in r:
			myticket = r
		continue
	else:
		validticket = True
		for nb in map(int, re.findall(r'\d+', r)):
			valid = False
			for k in ranges:
				for subrange in ranges[k]:
					if nb in range(subrange[0], subrange[1] + 1):
						valid = True
			if not valid:
				error_rate += nb
				validticket = False
		if validticket:
			validtickets.append(r)

positions = defaultdict(list)
for k in ranges:
	for i in range(len(ranges)):
		positions[k].append(i)
# print(positions)
# print(error_rate)
# print(ranges)
# print(validtickets)

for ticket in validtickets:
	for pos in positions:
		for i, nb in enumerate(map(int, re.findall(r'\d+', ticket))):
			if i in positions[pos] and nb not in range(ranges[pos][0][0], ranges[pos][0][1] + 1) and nb not in range(ranges[pos][1][0], ranges[pos][1][1] + 1):
				positions[pos].remove(i)

GoOn = True
while GoOn:
	GoOn = False
	for pos in positions:
		if len(positions[pos]) == 1:
			index = positions[pos][0]
			for p in positions:
				if pos != p and index in positions[p]:
					positions[p].remove(index)
	for pos in positions:
		if len(positions[pos]) > 1:
			GoOn = True

print(positions)
print(myticket)
MyTicket = list()
for i, item in enumerate(map(int, re.findall(r'\d+', myticket))):
	MyTicket.append(item)
print(MyTicket)

part2 = 1
for p in positions:
	print(p)
	if 'departure' in p:
		part2 *= MyTicket[positions[p][0]]
print(part2)
