lst=[1,2,3,4,5,6,7,8,9,10]
print(lst)
n=int(input("Enter any no form 1-10: "))
for i in lst:
    while n>=i:
        print((lst[n-2],lst[0]),(lst[1],lst[n-3]),(lst[3],lst[n-4]),(lst[4],lst[n-5]))
        break