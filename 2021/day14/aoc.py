from collections import Counter


polymer, second = open('input.txt').read().split('\n\n')
instructions = {f[0]: f[1] for inst in second.split('\n') if inst and (f := inst.split(' -> '))}
pairs = Counter((polymer[i:i+2]) for i in range(len(polymer) - 1))

for step in range(40000):
	newnewpolymer = Counter()
	for pair, count in pairs.items():
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
