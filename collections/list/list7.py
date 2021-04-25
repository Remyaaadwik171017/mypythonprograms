lst=[]
even=[]
odd=[]
i=0
for i in range(50,201):
    lst.append(i)
    i=+1
print(lst)
for i in lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)