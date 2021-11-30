lines = open("day02/input", 'r').readlines()
valid = 0
for line in lines:
	Range, Letter, Password = line.replace(':', '').strip().split()
	LowerBound, UpperBound = [int(x) for x in Range.split('-')]
	if bool(Password[LowerBound - 1] == Letter) != bool(Password[UpperBound - 1] == Letter):
		valid += 1

print(valid)
