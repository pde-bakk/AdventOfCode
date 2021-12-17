def isintarget(x: int, y: int) -> bool:
	return tx[0] <= x <= tx[1] and ty[0] <= y <= ty[1]


def couldhit(x: int, y: int, vx: int, vy: int) -> bool:
	if tx[0] - (x + vx) > tx[0] - x:
		return False
	if tx[1] - (x + vx) > tx[1] - x:
		return False
	if ty[0] - (y + vy) > ty[0] - y:
		return False
	if ty[1] - (y + vy) > ty[1] - y:
		return False
	return True


def drawtrajectory(vx: int, vy: int) -> bool:
	x, y = 0, 0
	maxy = y
	# print(f'speed={vx, vy}')

	while y > ty[0]:  # or y + sum([b for b in range(vy)]) > ty[0]:
		x += vx
		y += vy
		if vx > 0:
			vx -= 1
		elif vx < 0:
			vx += 1
		vy -= 1
		maxy = max(y, maxy)
		# print(f'in loop, maxy={maxy}, pos={x, y}, speed={vx, vy}')
		if isintarget(x, y):
			# print(f'returning {True, maxy}')
			return True
	return False


puzzle_input = open('input.txt').read().split(': ')[1].split(', ')
tx = [int(x) for x in puzzle_input[0].lstrip('x=').split('..')]
ty = [int(y) for y in puzzle_input[1].lstrip('y=').split('..')]
print(f'range={sum(a for a in range(0, -ty[1]))}')
print(f'Part1: {ty[0] * (ty[0] + 1) // 2}')
# print(f'range={range(-ty[0], ty[0])}')

test = open('test.txt').read().split()
testset = set()
for item in test:
	a = item.split(',')
	testset.add((int(a[0]), int(a[1])))


count = 0
myset = set()
for xxx in range(0, tx[1]+1):
	for yyy in range(ty[0] - 1, -ty[0] + 1):
		hit = drawtrajectory(xxx, yyy)
		if hit:
			count += 1
			myset.add((xxx, yyy))
print(f'Part2: {count}')
print(f'Diff1={myset - testset}, diff2={testset - myset}')
