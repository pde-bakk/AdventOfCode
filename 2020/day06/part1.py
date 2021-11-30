total = 0
answers = set()
with open("input") as myfile:
	for line in myfile:
		answers.update({c for c in line.strip()})
		if len(line) < 2:
			total += len(answers)
			answers.clear()
print(total)
# 6686
