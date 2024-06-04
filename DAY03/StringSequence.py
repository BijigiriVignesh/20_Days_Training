# 4
# abcd
# xyze
# pqrw
# stuv

# "cyptdzsayq"
# op:NO
from collections import Counter
nu=int(input())
l=[]
for i in range(nu):
    l.append(input())
ch=input()
r=0
no=0
count ={}
for i in l:
    count[i] = Counter(i)
for i in range(len(ch)):
    if i in l[r] and count[l[r]][i]:
        count[l[]]
        r=(r+1)%nu
    else:
        no=1
        break
if no:
    print("NO")
else:
    print("YES")
    
    

    