print(open('input', 'r').read().count('(') - open('input', 'r').read().count(')'))

ret = 0
for i, b in enumerate(open('input', 'r').read()):
	ret += 1 if b == '(' else -1
	if ret == -1:
		print(i + 1)
		break
