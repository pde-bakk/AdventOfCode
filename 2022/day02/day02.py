with open('input.txt', 'r') as f:
	lines = f.read().splitlines()
my_score, elf_score = [], []
for line in lines:
	elf, you = list(map(ord, line.split()))
	print(f'{chr(elf)} vs {chr(you)}')
	if you == ord('Y'):
		you = elf
	elif you == ord('X'):
		if elf == ord('A'):
			you = ord('C')
		else:
			you = elf - 1
		# you = elf - 1 if elf != ord('A') else ord('C')
	elif you == ord('Z'):
		if elf == ord('C'):
			you = ord('A')
		else:
			you = elf + 1
		# you = elf + 1 if elf != ord('C') else ord('A')
	print(f'you chose {chr(you)}')
	my_tmp_score = you - ord('A') + 1
	elf_tmp_score = elf - ord('A') + 1
	if you == elf:
		my_tmp_score += 3
		elf_tmp_score += 3
	elif you == elf + 1 or you == ord('A') and elf == ord('C'):
		my_tmp_score += 6
	else:
		elf_tmp_score += 6
	my_score.append(my_tmp_score)
	elf_score.append(elf_tmp_score)
	print(f'Elf score: {elf_tmp_score} vs My score: {my_tmp_score}')
print(sum(my_score))
