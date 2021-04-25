n=int(input("enter any number")) #153
while n!=0: #153!=0
     x=n%10 #153%10=3
     print(x,end=" ") #3
     y=n//10 #153//10=15 (result 15.3 floor div int only takes.so 15)
     print(y%10,end=" ") #15%10=5
     z=n//100 #153//100=1 (153/10=1.53 //=1)
     print((z%10),end=" ") (1%10=1)
     break


