l=[int(x) for x in open('input.txt').read()[::2]]
f={x:l.count(x) for x in range(9)}
for d in range(256):
	f={x-1:f[x] for x in f}
	f[8]=f.pop(-1)
	f[6]+=f[8]
print(sum(f.values()))