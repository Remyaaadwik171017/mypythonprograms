n=int(input("Enter n value: ")) #if n =4,
for i in range(n): #i=0,1,2,3
    print("  "*(n-i-1)+"* ",end=" ")#space*(4-0-1)+*=3space

    if i>=1: #from second row onwards
        print("  "*(2*i-1)+"* ",end=" ") #space*1+*, space*3+*,space*5+*
    print()