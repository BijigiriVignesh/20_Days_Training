def fun(i, j, c):
    if i < 0 or i >= n or j < 0 or j >= m or (i == k and j == l):
        return c
    if i == n - 1 and j == m - 1:
        c += 1
        return c
    vi.append((i, j))
    if (i - 1, j) not in vi:
        c = fun(i - 1, j, c)
    if (i, j - 1) not in vi:
        c = fun(i, j - 1, c)
    if (i + 1, j) not in vi:
        c = fun(i + 1, j, c)
    if (i, j + 1) not in vi:
        c = fun(i, j + 1, c)
    vi.pop()
    return c

m = int(input())
n = int(input())
k = int(input())
l = int(input())
vi = []
c = 0
r = fun(0, 0, c)
print(r)
