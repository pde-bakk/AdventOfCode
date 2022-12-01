with open('input.txt', 'r') as f:
	lines = f.read()
elfs = [[*map(int, x.split())] for x in lines.split('\n\n')]

totals = sorted([sum(x) for x in elfs])
print(max(totals))  # Part 1
print(sum(totals[-3:]))  # Part 2
