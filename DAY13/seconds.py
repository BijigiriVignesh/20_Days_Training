"""
ip : 7262
op : 2h 1m 2s
"""
n = int(input())
h = 0
h = n//3600
n = n%3600
m = n//60
n = n%60
print(h)
print(m)
print(n)