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
	a_value, b_value = get_item_2(a), get_item_2(b)
	return f'({a_value} {op} {b_value})'
	# return eval(f'{a_value} {op} {b_value}')


with open('input.txt', 'r') as f:
	lines = f.read().splitlines()
	d = {}
	for line in lines:
		k, v = line.split(': ')
		d[k] = v

# print(f'Part 1:', get_item('root'))
lhs, rhs = get_item_2("root")[1:-1].replace(' ', '').split('=')
lhs, rhs = lhs[1:-1], rhs[1:-1]
print(lhs, rhs)
sympy_string = f'Eq({lhs}, {rhs})'
print(sympy_string)
p2 = sympy.sympify(sympy_string)
print(f'Part 2:', sympy.solve(p2, sympy.Symbol('x')))
