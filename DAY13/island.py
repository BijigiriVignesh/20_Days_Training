def fun(i, j):
    if i < 0 or i >= n or j < 0 or j >= n or l[i][j] != 1:
        return 0
    l[i][j] = 0  
    s = 1
    s += fun(i + 1, j)
    s += fun(i - 1, j)
    s += fun(i, j + 1)
    s += fun(i, j - 1)
    return s
n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

c = 0  
area = 0 
for i in range(n):
    for j in range(n):
        if l[i][j] == 1:
            c += 1 
            current_area = fun(i, j)  
            area = max(area, current_area)  
print(c)
print(area)
