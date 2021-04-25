lst=[10,12,3,4,5,7,8,9,6,1]
lst.sort()
print(lst)
low=0
upp = len(lst) - 1
n=int(input("Enter searching element: "))
flag=0
while (low<=upp):
    mid=(low+upp)//2
    if (n>lst[mid]):
        low=mid+1
    elif(n<lst[mid]):
        upp=mid-1
    elif(n==lst[mid]):
        flag=1
        break
if flag>0:
    print("element found")
else:
    print("element not found")