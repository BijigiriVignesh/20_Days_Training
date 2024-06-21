l = [2, 3, 5, 6]
n = len(l)
t = int(input())
m = [[1 if j == 0 else 0 for j in range(t + 1)] for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, t + 1):
        if l[i-1] > j:
            m[i][j] = m[i-1][j]
        else:
            m[i][j] = m[i-1][j] or m[i-1][j-l[i-1]]
print(bool(m[n][t]))
