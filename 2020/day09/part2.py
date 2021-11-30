lines = open("input", 'r').read().split("\n")

nbs = [int(lines[i]) for i in range(25)]

for i in range(len(lines)):
	sums = [(x + y) for x in nbs for y in nbs if x != y]
	value = int(lines[i])
	if value not in sums:
		weakness = value
	nbs.append(value)
	nbs.pop(0)
print("weakness is", weakness)

summy = i = start = 0
for start in range(len(lines)):
	nbs.clear()
	summy = 0
	for i in range(start, len(lines)):
		if summy >= weakness:
			break
		nbs.append(int(lines[i]))
		summy += int(lines[i])
		if summy == weakness and int(lines[i]) != weakness:
			print("Got it. smol is {}, big is {}, sum is {}".format(min(nbs), max(nbs), min(nbs) + max(nbs)))
