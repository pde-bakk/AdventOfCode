polymer, second = open('input.txt').read().split('\n\n')

polymer = [c for c in polymer]

instructions = {c: {} for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
# instructions = {'B': {}, 'C': {}, 'H': {}, 'N': {}}
for inst in second.split('\n'):
	a, b = inst.split(' -> ')
	instructions[a[0]][a[1]] = b

for step in range(10):
	newpolymer = []
	for i in range(len(polymer) - 1):
		first_char = polymer[i]
		second_char = polymer[i + 1]
		newpolymer.append(first_char)
		# print(f'appending {first_char}')
		if second_char in instructions[first_char]:
			# print(f'appending {instructions[first_char]}')
			newpolymer.append(instructions[first_char][second_char])
		# print(f'appending {second_char}')
		# newpolymer.append(second_char)
	# print(f'appending last char: {polymer[-1]}')
	newpolymer.append(polymer[-1])
	print(f'After step {step + 1}: {newpolymer}')
	polymer = newpolymer

counts = sorted([polymer.count(c) for c in instructions.keys()])
while 0 in counts:
	counts.remove(0)
print(counts, counts[-1] - counts[0])
