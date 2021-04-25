def prime():
    n=int(input("Enter any no: "))
    flag = 0
    if n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                flag = 1
                break
            else:
                flag = 0
                if (flag==1):
                   print("prime")
                elif flag==0:
                    print("not prime")
        else:
            print("not prime")
prime()
