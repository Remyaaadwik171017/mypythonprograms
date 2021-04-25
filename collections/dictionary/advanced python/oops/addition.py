class Addition:
    def add(self):
        num1=int(input("Enter any no:"))
        num2=int(input("Enter second no:"))
        self.num1=num1
        self.num2=num2
    def printvalue(self):
        num3=self.num1+self.num2
        self.num3=num3
        print(self.num1,"+",self.num2,"=",self.num3)
obj= Addition()
obj.add()
obj.printvalue()