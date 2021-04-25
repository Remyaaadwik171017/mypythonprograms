import re
n=int(input("Enter mob no:"))
x="[+][9][1]\d{12}"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("not valid")