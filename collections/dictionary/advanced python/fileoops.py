class Readfile:
        def __init__(self,name,age):
            self.age=age
            self.name=name
        def printvalue(self):
            print("name: ",self.name)
            print("age: ",self.age)
        def __str__(self):
            return self.name
f = open("fileoops", "r")
for lines in f:
    data = lines.split(",")
    name=data[0]
    age=data[1]
    ob=Readfile(name,age)
    print(ob)
    ob.printvalue()


