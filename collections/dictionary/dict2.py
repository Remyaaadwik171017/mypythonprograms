employee={"id":1001,"employee_name":"remya","designation":"manager","salary":20000}
print(employee["employee_name"])
print("company" in employee)
employee["company"]="luminar"
print(employee)
employee["salary"]+=15000
print(employee)
for i in employee:
    print(i,":",employee[i])
