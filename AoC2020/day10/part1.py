jolts = open("input", 'r').read().split("\n")
jolts = [int(x) for x in jolts]
jolts.append(0)
jolts.append(max(jolts) + 3)
jolts.sort()
ones = threes = 0
for i, jolt in enumerate(jolts):
	if i == 0:
		continue
	# print("comparing {} with previous which is {}".format(jolt, jolts[i - 1]))
	if jolt - 1 == jolts[i - 1]:
		ones += 1
	if jolt - 3 == jolts[i - 1]:
		threes += 1
print("ones is {}, threes is {}, product is {}".format(ones, threes, ones * threes))
print(jolts)

