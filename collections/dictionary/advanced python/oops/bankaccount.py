class Bank:
    bname="sbi"
    def ac_create(self,acno,name,bankname):
        self.acno=acno
        self.name=name
        self.bankname=bankname
        self.mbalance=5000
        self.mbalance=self.mbalance
    def deposit(self,amount):
        self.mbalance+=amount
        print(Bank.bname, "Acc has been credited with amt of ",amount)
        print("current balance:",self.mbalance)
    def withdraw(self,amount):
        if amount>self.mbalance:
            print("you have insufficient money for withdrawal")
        else:
            print("acc is debited with amount of", amount)
            print("balance amount :",self.mbalance-amount)

obj=Bank()
obj.ac_create(25235333633,"Remya","sbi")
obj.deposit(10000)
obj.withdraw(2000)