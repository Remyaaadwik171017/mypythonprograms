f=open("numbers","r")
list=[]
for num in f:
    list.append(int(num.rstrip("\n")))
print(list)
s=sum(list)
print(s)


