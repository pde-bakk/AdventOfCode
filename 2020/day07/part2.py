from collections import defaultdict


def clean(s):
	return s.split('bag')[0].strip()


lines = open("input", 'r').read().split("\n")
children = defaultdict(list)
for line in lines:
	parent, rest = line.split(" bags contain ")
	parent = clean(parent)
	if 'no other' in rest:
		continue
	for child in map(clean, rest.split(", ")):
		count, child = child.split(' ', 1)  # only splits on the first space
		child = clean(child)
		children[parent].append((int(count), child))

S = [('shiny gold', 1)]
res2 = 0
while len(S):
	cur, mult = S.pop()
	for count, child in children[cur]:
		res2 += count * mult
		S.append((child, count * mult))
print("Part 2: ", res2)  # 1664
