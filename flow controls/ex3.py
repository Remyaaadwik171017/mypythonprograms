num1=int(input("Enter first no:"))
num2=int(input("Enter first no:"))
num3=int(input("Enter first no:"))
if num1>num2>num3:
    print("Greatest no:",num1)
elif(num1>num3>num2):
    print("Greatest no:", num1)
elif num3>num2>num1:
    print("Greatest no:", num3)
elif num3>num1>num2:
    print("Greatest no:", num3)
elif num2>num1>num3:
    print("Greatest no:", num2)
elif num2>num3>num1:
    print("Greatest no:", num2)
elif num1==num2>num3:
    print("The entered first 2 no.s are same",num1)
elif num1==num2<num3:
    print("The greatest no",num3)
elif num1>num2==num3:
    print ("The greatest no is",num1)
elif num1<num2==num3:
    print("The last entered 2 nos are same",num2)
elif num1==num3>num2:
    print("The entered first and 3rd nos are same",num1)
elif num1==num3<num2:
    print("The greatest no is",num2)
else:
    print("The no.s are eual")

