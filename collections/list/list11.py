lst=[3,4,8]
lst1=[]
sum=lst[0]+lst[1]+lst[2]
n1=sum-lst[0]
n2=sum-lst[1]
n3=sum-lst[2]
lst1.extend((n1,n2,n3))

print(lst1)

