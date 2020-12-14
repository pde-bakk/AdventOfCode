import re


def replace_x():
	tmp = set()
	for r in results:
		tmp.add(r)
		tmp.add(r + bit)
	return tmp


d = dict()
rows = [x for x in open("input", 'r').read().split("\n")]
total, value = 0, 0
for row in rows:
	if row[:4] == 'mask':
		mask = row[7:]
	else:
		slet = set()
		pos, value = map(int, re.findall(r'\d+', row))
		bit = int(2 ** (len(mask) - 1))
		xs = set()
		for i, m in enumerate(mask):
			if m == '1' and pos & bit == 0:
				pos += bit
			elif m == 'X':
				xs.add(bit)
				if pos & bit > 0:
					pos -= bit
			bit = int(bit / 2)
		results = {pos}
		for bit in xs:
			results = replace_x()
		for res in results:
			d[res] = value

print(sum(d.values()))
