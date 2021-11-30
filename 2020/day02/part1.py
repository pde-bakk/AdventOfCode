lines = open("day02/input", 'r').readlines()
valid = 0
for line in lines:
	Range, Letter, Password = line.replace(':', '').strip().split()
	LowerBound, UpperBound = Range.split('-')
	if int(LowerBound) <= Password.count(Letter) <= int(UpperBound):
		valid += 1

print(valid)
