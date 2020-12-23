mycups = [9, 5, 2, 3, 1, 6, 4, 8, 7]
mycups = [3, 8, 9, 1, 2, 5, 4, 6, 7]  # sample


def game(cups, gamelength):
	cur = 0
	for i in range(1, gamelength + 1):
		print(f'-- move {i} --')
		currentcup = cups[cur % len(cups)]
		cur = cups.index(currentcup)
		# print(f'cups: {cups} ({currentcup})')
		threecups = cups[cur + 1: cur + 4]
		if len(threecups) < 3:
			threecups += cups[:3 - len(threecups)]
		# print(f'pick up: {threecups}')
		cups = [x for x in cups if x not in threecups]
		# cups = cups[:cur + 1] + cups[cur + 4:]
		destination = currentcup - 1
		while True:
			if destination in cups:
				break
			if destination == 0:
				destination = max(cups)
			else:
				destination -= 1
		# print(f'destination: {destination}\n')
		cups = cups[:cups.index(destination) + 1] + threecups + cups[cups.index(destination) + 1:]
		cur = cups.index(currentcup) + 1
	return cups


def score(cups):
	print(f'-- final --')
	print(f'cups: {cups}')
	s = ''.join([str(x) for x in cups]).split('1')
	return s[1] + s[0]


# print(f'Part 1: {score(game(mycups, 100))}')
maxcup = max(mycups)
extracups = [x for x in range(max(mycups), 1000000)]
print(len(extracups) + len(mycups))
ret = game(mycups + extracups, 10)
after = ret[ret.index(1):]
print(after)