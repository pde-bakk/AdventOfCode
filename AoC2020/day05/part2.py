highest = seat = 0
mylist = [i for i in range(53, 896 + 1)]
with open("input") as myfile:
	for line in myfile:
		mylist.remove(int(line.replace('B', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2))
print(mylist)
#659
