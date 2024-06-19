def prime(n):
    for j in range(2,(n//2)+1):
        if n%j==0:
            return 0
    return 1
l = list(map(int, input().split()))
k = []
for i in range(len(l)-1):
    for j in range(l[i+1],l[i],-1):
        if prime(j):
            k.append(j)
            break
print(sum(k))