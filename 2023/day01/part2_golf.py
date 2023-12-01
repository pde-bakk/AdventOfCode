L='one two three four five six seven eight nine'.split()
S=0
for r in open(0):
	for i,l in enumerate(L):r=r.replace(l,l[0]+str(i+1)+l[2:])
	d=[(i,int(c))for i,c in enumerate(r)if'/'<c<':']
	S+=min(d)[1]*10+max(d)[1]
print(S)
