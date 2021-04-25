#arguments

#positional arg : calc(a,b)

#keyword arg : calc(a=100,b=50) or calc(b=50,a=100) or calc(100,b=50)

#default arg:
#def wish(msg,name="guest"):pass

#variable length arg:

#def sum(a,b):
    #print(a+b)
#sum(10,20)
#sum(50,60,10)-not possible 3 variable value

def sum(*a):
    result=0
    for x in a:
        result=result+x
    print("the sum",result)
sum()
sum(10)
sum(10,20,30)
sum(2,3,4,5,6,7,8)
