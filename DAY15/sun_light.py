l = [3,5,9,6,8,10]
n = len(l)
m = [0]*n
m[0] = 0
for i in range(n):
    m[i] = max(m[i-1],l[i])
print(len(set(m)))
for i in range(n-2,-1,-1):
    m[i] = max(m[i+1],l[i])
print(len(set(m)))