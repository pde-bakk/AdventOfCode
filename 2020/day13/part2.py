file = open("input", 'r').read().split('\n')
buses = [(i, int(bus)) for i, bus in enumerate(file[1].split(',')) if bus != 'x']
timestamp, jump = buses[0]

for delta, busid in buses[1:]:
	while (timestamp + delta) % busid != 0:
		timestamp += jump
	jump *= busid

print(timestamp)
