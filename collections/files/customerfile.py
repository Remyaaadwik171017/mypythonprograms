f=open("C:/Users/User/Desktop/customer","r")
dict={}
dict1={}
dict2={}
for lines in f:
    data = lines.rstrip("\n").split(",")
    print(data)
    fname=data[1]
    age=data[3]
    loc=data[-1]
    prof=data[-2]
    print(fname,age,loc,prof)
    for i in data:
        if loc not in dict:
            dict[loc] = 1
        else:
            dict[loc] += 1
    print(dict)
    for i in data:
        if age not in dict1:
            dict1[age] = 1
        else:
            dict1[age] += 1
    print(dict1)
    for i in data:
        if prof not in dict2:
            dict2[prof] = 1
        else:
            dict2[prof] += 1
    print(dict2)
