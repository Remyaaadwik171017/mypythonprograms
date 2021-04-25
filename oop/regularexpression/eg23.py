import re
x="a{4}"
r="aaa aab aaan"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())
#only 4 a print