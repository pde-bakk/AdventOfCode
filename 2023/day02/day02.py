lines = open('input.txt').readlines()

l = []
l2 = []
for line in lines:
	game, dice = line.split(': ')
	nb = int(game.split()[1])
	subset = dice.split(';')
	d = {}
	for s in dice.split(';'):
		for col in s.split(','):
			amount, colour = col.split()
			d[colour] = max(int(amount), d.get(colour, 0))
	if d['red'] <= 12 and d['green'] <= 13 and d['blue'] <= 14:
		l.append(nb)
	power = d['red'] * d['green'] * d['blue']
	l2.append(power)
print(sum(l))
print(sum(l2))
