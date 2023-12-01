L='one 1 two 2 three 3 four 4 five 5 six 6 seven 7 eight 8 nine 9'.split()
S=0
for r in open(0):
	l=[];for a in L:l+=[(i,1+(L.index(a)//2))for i in range(len(r))if a==r[i:i+len(a)]];S+=10*min(l)[1]+max(l)[1]
print(S)
