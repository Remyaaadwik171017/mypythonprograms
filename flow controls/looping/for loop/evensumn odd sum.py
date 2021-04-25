lower_limit=int(input("Enter lower limit:"))
upper_limit=int(input("Enter Upper limit: "))
even_sum=0
odd_sum=0
for i in range(lower_limit,(upper_limit+1)):
    if i%2==0:
        even_sum=even_sum+i

    else:
        odd_sum+=i
print("even sum=",even_sum)
print("Odd sum=",odd_sum)