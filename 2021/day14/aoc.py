from collections import Counter


polymer, second = open('input.txt').read().split('\n\n')

instructions = {c: {} for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
# instructions = {'B': {}, 'C': {}, 'H': {}, 'N': {}}
for inst in second.split('\n'):
	a, b = inst.split(' -> ')
	instructions[a] = b

pairs = Counter((polymer[i:i+2]) for i in range(len(polymer) - 1))
print(pairs)

for step in range(40):
	newnewpolymer = Counter()
	for pair, count in pairs.items():
		# print(f'pair={pair}, count={count}')
		inbetweener = instructions[pair]
		newnewpolymer[f'{pair[0]}{inbetweener}'] += count
		newnewpolymer[f'{inbetweener}{pair[1]}'] += count
	pairs = newnewpolymer

counts = {k[0]: 0 for k in pairs}
counts[polymer[-1]] += 1  # The last character never changes
for k, v in pairs.items():
	counts[k[0]] += v
print(counts)
print(max(counts.values()) - min(counts.values()))
