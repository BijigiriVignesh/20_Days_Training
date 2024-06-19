def fun(i, j, s, s1):
    if i >= n or j >= k:  
        return
    if l[i] % 2 == 0 and m[j] % 2 == 1:
        s1+=l[i]+m[j]
    if j+1 < k:
        fun(i, j + 1, s, s1) 
    else:
        if s1!=0:
            s.append(s1) 
        if i+1 < n:
            fun(i + 1, 0, s, 0)  
l = list(map(int, input().split()))
m = list(map(int, input().split()))
s = []
n = len(l)
k = len(m)
fun(0, 0, s, 0)
print(s)
