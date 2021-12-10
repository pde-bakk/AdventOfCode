def check(s: str, part: int):
	stack = []
	open_list = ['(', '[', '{', '<']
	close_list = [')', ']', '}', '>']
	summy = 0
	values = {k: v for k, v in zip(close_list, [3, 57, 1197, 25137])}
	for i, c in enumerate(s):
		if c in open_list:
			stack.append(c)
		elif c in close_list:
			pos = close_list.index(c)
			if len(stack) > 0 and open_list[pos] == stack[-1]:
				stack.pop()
			else:
				summy += values[c]
				break
	if part == 2:
		if summy != 0:
			return 0
		res = 0
		for c in stack[::-1]:
			res *= 5
			res += open_list.index(c) + 1
		return res
	return summy


lines = open('input.txt').read().splitlines()
p2 = sorted([check(line, part=2) for line in lines])
while 0 in p2:
	p2.remove(0)
print(f'Part2: {p2[len(p2)//2]}')
