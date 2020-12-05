highest = 0
with open("input") as myfile:
	for line in myfile:
		highest = max(highest, int(line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2))
print(highest)
#896
