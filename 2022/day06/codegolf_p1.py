i,f=3,next(open(0))
while f:
 i+=1
 if len({*f[i-4:i]})>3:f=0
print(i)