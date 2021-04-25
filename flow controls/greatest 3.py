num1=int(input("Enter first no:"))
num2=int(input("Enter first no:"))
num3=int(input("Enter first no:"))
if (num1>num2)& (num1>num3):
    print("greatest no: ",num1)
elif(num2>num1)&(num2>num3):
    print("Greatest no:",num2)
elif(num3>num2)&(num3>num1):
    print("The greatest no:",num3)
else:
    print("The nos are equal")
