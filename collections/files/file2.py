f=open("numbers","r")
list=[]
evenlist=[]
oddlist=[]
for num in f:
    list.append(int(num.rstrip("\n")))
print(list)
for i in list:
    if i%2==0:
        evenlist.append(i)

    else:
        oddlist.append(i)
print(oddlist)
print(evenlist)
s = sum(list)
evensum=sum(evenlist)
oddsum=sum(oddlist)
print(s)
print(evensum)
print(oddsum)