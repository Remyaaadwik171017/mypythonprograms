lst=[1,2,3,4,5,6,7,8]
n=int(input("enter no: "))
for i in lst:
    if i==n:
        print("element found")
        i+=1
        break
else:
        print("not found")

        #it is known as linear search programme. to reduce the complexity we use binary search.

