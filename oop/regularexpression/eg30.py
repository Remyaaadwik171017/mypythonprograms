
import re
n=int(input("Enter mob no:"))
x="\d{10}"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("not valid")