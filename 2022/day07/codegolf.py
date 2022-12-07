C,D,f=[],{},iter(open(0))
for l in f:
 match l.split():
  case'$','cd','..':C.pop()
  case'$','cd',p:C+=[p]
  case['$','ls']|['dir',_]:pass
  case s,_:
   for i in range(len(C)):d=''.join(C[:i+1]);D[d]=D.get(d,0)+int(s)
print(sum(D[k] for k in D if D[k]<=10**5))
print(min(D[k] for k in D if D[k]>=D['/']-4*10**7))