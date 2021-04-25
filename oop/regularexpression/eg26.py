import re
x="a$"
r="aaa aab aaana" #ending with a
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())
#starting with a