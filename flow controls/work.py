age=int(input("Enter your age:"))
sex=input("Enter your sex, M/F:")
maritial_status=input("Enter yor maritial status ( Y/N):")
if sex=="F":
    print("You can work only in urban areas")
elif sex=="M":
    if 20<age<40:
        print("You can work anywhere")
    elif 40<age<60:
        print("You can work in urban areas only")
    else:
         print("ERROR")



