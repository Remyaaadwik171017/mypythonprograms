choice=int(input("Enter a choice: 1,2,3,4:"))
if choice==1:
 def add():

    num1=int(input("Enter first no: "))
    num2=int(input("Enter 2nd no: "))
    sum=num1+num2
    print(num1,"+",num2,"=",sum)
 add()

elif choice==2:
 def sub():
    num1 = int(input("Enter first no: "))
    num2 = int(input("Enter 2nd no: "))
    subt = num1 - num2
    print(num1,"-",num2,"=",subt),
 sub()

elif choice==3:
 def mul():
    num1 = int(input("Enter first no: "))
    num2 = int(input("Enter 2nd no: "))
    mult = num1 *num2
    print(num1,"*",num2,"=",mult)
 mul()

elif choice==4:
 def div():
    num1 = int(input("Enter first no: "))
    num2 = int(input("Enter 2nd no: "))
    divt = num1/num2
    print(num1,"/",num2,"=",divt)
 div()

else:
  pass