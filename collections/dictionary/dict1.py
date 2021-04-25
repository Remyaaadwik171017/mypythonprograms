student1={"roll":1001,"name":"arun","age":25,"cpp":25}
for i in student1:
        print(i,":" ,student1[i])
student1["name"]="arjun"
student1["age"]=30
student1["cpp"]+=5
print(student1)
del student1["cpp"]
print(student1)
student1["total"]=150
print(student1)