import sympy


def get_item(key: str):
	value = d[key]
	if value.isdigit():
		return value
	a, op, b = value.split()
	a_value, b_value = get_item(a), get_item(b)
	return eval(f'{a_value} {op} {b_value}')


def get_item_2(key: str):
	value = d[key]
	if key == 'humn':
		return 'x'
	if value.isdigit():
		return value
	a, op, b = value.split()
	if key == 'root':
		op = '='
	return f'({get_item_2(a)} {op} {get_item_2(b)})'


with open('input.txt', 'r') as f:
	lines = f.read().splitlines()
	d = {a[0]: a[1] for line in lines if (a := line.split(': '))}

print(f'Part 1:', int(get_item('root')))
lhs, rhs = get_item_2("root")[1:-1].replace(' ', '').split('=')
p2 = sympy.sympify(f'Eq({lhs}, {rhs})')
print(f'Part 2:', sympy.p1(p2, sympy.Symbol('x')))
