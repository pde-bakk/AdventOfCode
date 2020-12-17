total = ribbon = 0
for row in open('input', 'r').read().split('\n'):
	l, w, h = map(int, row.split('x'))
	total += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
	ribbon += 2 * (l + w + h - max(l, w, h)) + l*w*h
print(f'{total} wrapping paper and {ribbon} ribbon')
