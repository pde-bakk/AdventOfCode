import re

d = dict()
rows = [x for x in open("input", 'r').read().split("\n")]
total, value = 0, 0
for row in rows:
    if row[:4] == 'mask':
        mask = row[7:]
    else:
        pos, value = map(int, re.findall(r'\d+', row))
        for i in range(1, len(mask) + 1):
            if mask[-i] == '0':
                value &= ~(1 << i - 1)
            elif mask[-i] == '1':
                value |= (1 << i - 1)
        d[pos] = value

print(sum(d.values()))

# This here is my addition code, but I also wanted to make it work with bitwise operations
# for row in rows:
# 	if row[:4] == 'mask':
# 		mask = row[7:]
# 	else:
# 		pos, value = map(int, re.findall(r'\d+', row))
# 		bit = 1
# 		for i in range(1, len(mask) + 1):
# 			if mask[-i] == '0' and value & bit > 0:
# 				value -= bit
# 			elif mask[-i] == '1' and value & bit == 0:
# 				value += bit
# 			bit *= 2
# 		d[pos] = value
