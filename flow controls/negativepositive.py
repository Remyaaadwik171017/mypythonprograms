#if...elif....else(more than 1 condition)

#if(condition1):
    #statement1
#elif(condition2):
     #statement2
#else:
     #statement3

num1=int(input("Enter any no:"))
if num1==0:
    print("The no is Zero:",num1)
elif num1>0:
    print("positive no:",num1)
else:
    print("negative no:",num1)