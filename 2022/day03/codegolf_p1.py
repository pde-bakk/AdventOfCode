import string
print(sum(string.ascii_letters.index(*({*i[:l]}&{*i[l:]}))+1for i in open(0)if(l:=len(i)//2)))
