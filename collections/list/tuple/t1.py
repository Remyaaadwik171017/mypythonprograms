#tuple packing and unpacking

#tuple packing

a=10
b=9
c=11
d=23
t=(a,b,c,d)
print(t)

#tuple un packing

t=(1,2,3,4,5)
a,b,c,d,e=t
print('a={},b={},c={},d={},e={}'.format(a,b,c,d,e))