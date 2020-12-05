highest = seat = 0
with open("input") as myfile:
	for line in myfile:
		row = int(line[0:7].replace('F', '0').replace('B', '1'), 2)
		column = int(line[7:-1].replace('L', '0').replace('R', '1'), 2)
		seatid = row * 8 + column
		# print(row, column)
		if seatid > highest:
			highest = seatid

print(highest)
#896
