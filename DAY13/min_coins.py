l = list(map(int, input().split()))
n = int(input())
l = sorted(l, reverse=True)
c = 0
for i in l:
    if n == 0:
        break
    c += n // i
    n = n % i
if n!=0:
    print(c)
    print("-1")
else:
    print(c)