highest = seat = 0
mylist = list()
for i in range(896 + 1):
	mylist.append(i)

with open("input") as myfile:
	for line in myfile:
		row = int(line[0:7].replace('F', '0').replace('B', '1'), 2)
		column = int(line[7:-1].replace('L', '0').replace('R', '1'), 2)
		seatid = row * 8 + column
		# print(row, column)
		# print(seatid)
		mylist.remove(seatid)

print(mylist)
#659

