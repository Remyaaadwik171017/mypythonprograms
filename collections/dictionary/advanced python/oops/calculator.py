class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def printval(self):
        print("add=", self.num1+self.num2)
        print("sub=",self.num1 - self.num2)
        print("div=",self.num1 / self.num2)
        print("mul=",self.num1 * self.num2)
obj=Calculator(20,10)
obj.printval()
