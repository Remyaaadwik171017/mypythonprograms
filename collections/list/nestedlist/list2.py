lst1=[1,2,3,4,5,6,7]
lst2=[2,4,6,8,9,12,1,13,23]
lst3=[]
#to get list present in list1 not in list2
for i in lst1:
    if (i in lst2) is True:
        pass
    else:
        lst3.append(i)
print(lst3)
lst4=[x for x in lst1 and lst2]
print(lst4)
l="All that glitters is not gold"
k=l.split()
print(k)
result=[[k.upper(),len(k)] for k in l.split()]
print(result)