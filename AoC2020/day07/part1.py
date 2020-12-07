from collections import defaultdict


def clean(s):
	return s.split('bag')[0].strip()


lines = open("input", 'r').read().split("\n")
parents = defaultdict(list)
# parents = {}
golds = set()
S = ['shiny gold']
for line in lines:
	parent, rest = line.split(" bags contain ")
	parent = clean(parent)
	if 'no other' in rest:
		continue
	for child in map(clean, rest.split(", ")):
		count, child = child.split(' ', 1)
		child = clean(child)
		parents[child].append(parent)

while S:
	cur = S.pop()
	for parent in parents[cur]:
		golds.add(parent)
		S.append(parent)
print("Part 1: ", len(golds))  # 208
