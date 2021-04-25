def cal(num1,num2):
    sum=num1+num2
    mul=num1*num2
    div=num1/num2
    sub=num1-num2
    return sum,mul,div,sub
t=cal(100,50)
for x in t:
    print(x)