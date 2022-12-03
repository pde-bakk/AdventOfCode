import string
print(sum([string.ascii_letters.index(*(set(i[:l])&set(i[l:])))for i in open(0)if(l:=len(i)//2)]))
