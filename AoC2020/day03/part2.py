lines = open("day03/input", 'r').readlines()
trees = 0
x = 1, 3, 5, 7, 1
y = 1, 1, 1, 1, 2
llen = len(lines[0]) - 1
result = 1
for slope in range(len(x)):
	trees = index = downslope = 0
	for line in lines:
		index = index % llen
		if line[index] == '#' and downslope % y[slope] == 0:
			trees += 1
		if downslope % y[slope] == 0:
			index += x[slope]
		downslope += 1
	print("found {} trees".format(trees))
	result *= trees

print(result)
