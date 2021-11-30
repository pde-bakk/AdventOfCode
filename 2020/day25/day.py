card, door = 2084668, 3704642  # real input
# card, door = 5764801, 17807724  # sample input
card_loopsize, door_loopsize = 0, 0

cardtmp, doortmp = 1, 1
while cardtmp != card or doortmp != door:
	if cardtmp != card:
		cardtmp *= 7  # subject number
		cardtmp %= 20201227
		card_loopsize += 1
	if doortmp != door:
		doortmp *= 7  # subject number
		doortmp %= 20201227
		door_loopsize += 1
print(f'card_loopsize = {card_loopsize}, door_loopsize = {door_loopsize}')
encryptionkey = 1
if card_loopsize < door_loopsize:
	loop_size = card_loopsize
	mult = door
else:
	loop_size = door_loopsize
	mult = card
for i in range(loop_size):
	encryptionkey *= mult
	encryptionkey %= 20201227
print(f'encryption1 = {encryptionkey}')
