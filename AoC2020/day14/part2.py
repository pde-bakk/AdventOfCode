import re


def replace_x():
	tmp = set()
	for r in results:
		tmp.add(r)  # This is number with the current bit flipped off
		tmp.add(r | (1 << bit))  # And here it's on
	return tmp


d = dict()
rows = [x for x in open("input", 'r').read().split("\n")]
total, value = 0, 0
for row in rows:
	if row[:4] == 'mask':
		mask = row[7:]
	else:
		pos, value = map(int, re.findall(r'\d+', row))
		xs = set()
		for i in range(1, len(mask) + 1):
			if mask[-i] == '1':
				pos |= (1 << i - 1)  # setting the bit ON
			elif mask[-i] == 'X':
				xs.add(i - 1)  # Saving the position of the bit so we can flip it on later
				pos &= ~(1 << i - 1)  # I set the bit to 0
		results = {pos}
		for bit in xs:
			results = replace_x()
		for res in results:
			d[res] = value

print(sum(d.values()))


# Here too, I wanted to make it work with bitwise operations instead of addition and subtraction
# Even though in modern systems addition and subtraction are very optimised, this is still faster
# import re
#
#
# def replace_x():
# 	tmp = set()
# 	for r in results:
# 		tmp.add(r)
# 		tmp.add(r + bit)
# 	return tmp
#
#
# d = dict()
# rows = [x for x in open("input", 'r').read().split("\n")]
# total, value = 0, 0
# for row in rows:
# 	if row[:4] == 'mask':
# 		mask = row[7:]
# 	else:
# 		pos, value = map(int, re.findall(r'\d+', row))
# 		bit = int(2 ** (len(mask) - 1))
# 		xs = set()
# 		for i, m in enumerate(mask):
# 			if m == '1' and pos & bit == 0:
# 				pos += bit
# 			elif m == 'X':
# 				xs.add(bit)
# 				if pos & bit > 0:
# 					pos -= bit
# 			bit = int(bit / 2)
# 		results = {pos}
# 		for bit in xs:
# 			results = replace_x()
# 		for res in results:
# 			d[res] = value
#
# print(sum(d.values()))
# #4197941339968
