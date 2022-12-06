i,f=13,next(open(0))
while f:
 i+=1
 if len({*f[i-14:i]})>13:f=0
print(i)