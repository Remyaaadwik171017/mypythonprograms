#used for pattern matching

#re-- package used for regular

import re
count=0
matcher=re.finditer("ab","ababababbbbbaaaaaaaabaaaab")
for match in matcher:
    count+=1
print("count=",count)