import re
count=0
matcher=re.finditer("ab","ababababbbbbaaaaaaaabaaaab")
for match in matcher:
    print("match avialable at:",match.start())
    print("group=",match.group())
    count+=1
print("count=",count)