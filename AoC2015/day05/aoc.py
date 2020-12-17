nice = 0
rows = open('input', 'r').read().split('\n')
for string in rows:
	if any(i in string for i in ['ab', 'cd', 'pq', 'xy']): continue
	if sum(map(string.count, ['a', 'e', 'i', 'o', 'u'])) < 3: continue
	if not any(True for i in range(len(string) - 1) if string[i] == string[i + 1]): continue
	nice += 1
print(f'{nice} nice strings in part 1')
nice = 0
for string in rows:
	if not any(True for i in range(len(string) - 2) if string[i] == string[i+2] != string[i+1]): continue
	if not any([string.count(string[i:i+2]) >= 2 for i in range(len(string) - 2)]): continue
	nice += 1
print(f'{nice} nice strings in part 2')