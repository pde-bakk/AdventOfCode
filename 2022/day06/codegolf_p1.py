i,f=4,open(0).read()
while 1:
 if len(set(f[i-4:i]))==4:exit(print(i))
 i+=1