salary=float(input("Enter your salary:"))
year_of_service=int(input("Enter your year of service:"))
if year_of_service>5:
    bonus=0.5*salary
    print("bonus:",bonus)
else:
    print("You have no bonus in this year")