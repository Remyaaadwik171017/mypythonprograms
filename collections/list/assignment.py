lst=[1,2,3,4,5,6,7,8,9,10]
print(lst)
n=int(input("Enter any no form 1-10: "))
low=0
upp=len(lst)-1
while low<=upp:
    mid=(low+upp)//2
    if (n>lst[mid]):
        low=mid+1
        print((lst[0],lst[n-2]), (lst[1], lst[n-3]),(lst[n-4],lst[2]),(lst[3],lst[n-5]))
        break

    elif(n<lst[mid]):
        upp = mid-1
        print((lst[n-2], lst[0]))
        break
    elif(n==lst[mid]):
        print((lst[mid - 1], lst[0]), (lst[1], lst[mid - 2]))
        break
