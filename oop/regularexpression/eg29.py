import re
n="56kg"
x="[a-z"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("not valid")