lst=[1,2,3,4]
a=int(input("ENTER INDEX"))
try:
    print(lst[a])
except:
    print("exception")
finally:
    print("inside finally")