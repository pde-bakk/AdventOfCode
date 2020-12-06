total = groupsize = 0
answers = {}
with open("input") as myfile:
	for line in myfile:
		for c in line.strip():
			answers[c] = answers.get(c, 0) + 1
		groupsize += 1
		if len(line) < 2:
			for a in answers:
				if answers[a] == groupsize - 1:
					total += 1
			answers.clear()
			groupsize = 0
print(total)
# 3476
