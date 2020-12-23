mycups = [9, 5, 2, 3, 1, 6, 4, 8, 7]
# mycups = [3, 8, 9, 1, 2, 5, 4, 6, 7]  # sample


def game(cups, currentcup, gamelength):
	for i in range(1, gamelength + 1):
		# print(f'-- move {i} --')
		pickone = cups[currentcup]
		picktwo = cups[pickone]
		pickthree = cups[picktwo]
		cups[currentcup] = cups[pickthree]

		destination = currentcup - 1
		while destination in [pickone, picktwo, pickthree] or destination < 1:
			destination -= 1
			if destination < 1:
				destination = max(cups.values())
		# print(f'destination: {destination}\n')

		cups[pickthree] = cups[destination]
		cups[destination] = pickone
		currentcup = cups[currentcup]
	print(cups[1] * cups[cups[1]])
	return cups


def score(cups):
	print(f'-- final --')
	st, tmp = str(), cups[1]
	print(f'cups: {cups}')
	while tmp != 1:
		st += str(tmp)
		tmp = cups[tmp]
	return st


def score2(cups):
	print(f'-- final --')
	print(f'cups[1]: {cups[1]}, cups[{cups[1]}]: {cups[cups[1]]}')
	return cups[1] * cups[cups[1]]


d = {k: mycups[i+1] for i, k in enumerate(mycups) if i < len(mycups) - 1}
d[mycups[-1]] = mycups[0]
print(f'Part 1: {score(game(d, mycups[0], 100))}')
extracups = [x for x in range(10, 1000000 + 1)]
mycups += extracups
d = {k: mycups[i+1] for i, k in enumerate(mycups) if i < len(mycups) - 1}
d[mycups[-1]] = mycups[0]
print(score2(game(d, mycups[0], 10000000)))
