"""
intervals: [(1,3),(5,5),(4,6),(6,7),(5,8),(7,9)]
profits: [5,6,5,4,11,2]
"""
interval = [(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
p = [5,6,5,4,11,2]
n = len(interval)
for i in range(n-1):
    for j in range(n-i-1):
        if interval[j][0] > interval[j+1][0]:
            interval[j],interval[j+1] = interval[j+1],interval[j]
            p[j],p[j+1] = p[j+1],p[j]
print(interval)
print(p)
ps = 0
for i in range(n):
    ending = 0
    pr = 0
    for j in range(i, n):
        if ending <= interval[j][0]:
            ending = interval[j][1]
            pr += p[j]
    ps = max(ps,pr)
print(ps)