players = open('input', 'r').read().split('\n\n')
decks = dict()


for player in players:
	playerid, cards = player.split(':\n')
	playerid = int(playerid[playerid.find(' ') + 1:])
	decks[playerid] = [int(x) for x in cards.split()]


def score(deck):
	res = 0
	for i, val in enumerate(deck[::-1]):
		res += val * (i + 1)
	return res


def combat(deck1, deck2):
	seen = set()
	# global gamecount
	# gamenb, turn = gamecount, 1
	while len(deck1) > 0 and len(deck2) > 0:
		# print(f'-- Round {turn} (Game {gamenb}) --')
		# print(f'Player 1\'s deck: {deck1}')
		# print(f'Player 2\'s deck: {deck2}')
		# print(f'Player 1 plays: {deck1[0]}')
		# print(f'Player 2 plays: {deck2[0]}')

		current_setup = str(deck1) + '|' + str(deck2)
		if current_setup in seen:
			return 1, score(deck1)
		seen.add(current_setup)

		card1 = deck1.pop(0)
		card2 = deck2.pop(0)
		if len(deck1) >= card1 and len(deck2) >= card2:
			# print(f'Playing a sub-game to determine the winner...\n')
			# gamecount += 1
			roundwinner, _ = combat(deck1[:card1], deck2[:card2])
			if roundwinner == 1:
				deck1 += [card1, card2]
			else:
				deck2 += [card2, card1]
			# print(f'...anyway, back to game {gamenb}.')
		# print(f'Player {roundwinner} wins round {turn} of game {gamenb}\n')
		else:
			if card1 > card2:
				deck1 += [card1, card2]
			else:
				deck2 += [card2, card1]
		# turn += 1
	if len(deck1) > 0:
		return 1, score(deck1)
	return 2, score(deck2)


gamecount = 1
print(combat(decks[1], decks[2]))
print(f'\n== Post-game results ==')
