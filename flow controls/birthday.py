birth_date=int(input("Enter your birth date:"))
birth_month=int(input("Enter your birth month in digits:"))
birth_year=int(input("Enter your birth year:"))
current_date=int(input("Enter current date:"))
current_month=int(input("Enter current month in digits:"))
current_year=int(input("Enter current year"))
age=current_year-birth_year
if current_month>birth_month:
    print("age=",age)
elif current_month<birth_month:
    print("age=",age-1)
else:
    if current_date>birth_date:
       print("age=",age)
    elif current_date<birth_date:
        print("age=",age-1)
        
    else:
       print("age=",age-1)