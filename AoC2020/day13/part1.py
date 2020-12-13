file = open("input", 'r').read().split('\n')
mytime = int(file[0])
buses = [x for x in file[1].split(',')]
times = dict()

print("mytime = ", mytime)
for bus in buses:
	if bus == 'x': continue
	times[bus] = int(bus) - int(mytime % int(bus))
	print("for bus {}, i only have to wait {} timestamps".format(bus, times[bus]))

bestid = min(times, key=times.get)
print(int(min(times, key=times.get)) * times[min(times, key=times.get)])
