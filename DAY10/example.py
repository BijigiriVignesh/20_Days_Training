# l = list(map(int, input().split()))
# for i in range(len(l)-2):
#     a,b,c = l[i],l[i+1],l[i+2]
#     mi = min(l[i],min(l[i+1],l[i+2]))
#     ma = max(l[i],max(l[i+1],l[i+2]))
#     mid = a+b+c-mi-ma
#     l[i] = mi
#     l[i+1] = mid
#     l[i+2] = ma
# print(l)
l = list(map(int, input().split()))
for i in range(2):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
print(l)