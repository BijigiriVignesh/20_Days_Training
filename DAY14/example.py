l = list(map(int, input().split()))
n = len(l)
lb = [0]*n
rb = [0]*n
lb[0] = l[0]
rb[n-1] = l[n-1]
for i in range(1,n):
    lb[i] = max(lb[i-1],l[i])
print(lb)
for i in range(n-2,-1,-1):
    rb[i] = max(rb[i+1],l[i])
print(rb)
w = 0
for i in range(n):
    w+=min(lb[i],rb[i])-l[i]
print(w)