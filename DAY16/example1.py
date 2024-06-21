"""
inp
7 
1 school
1 world
1 word 
1 scholar
2 word
2 wood
3 sch
inp 2:
5
1 word
1 word
3 wo
4 word
2 word

"""
n = int(input())
l = []
for _ in range(n):
    i, j = input().split()
    l.append((int(i), j))
print(l)
w = []
r = []
for i in range(n):
    if l[i][0] == 1:
        w.append(l[i][1])
    elif l[i][0] == 2:
        f = False
        for k in w:
            if l[i][1] in k:
                f = True
                break
        r.append(f)
    elif l[i][0] == 4:
        if l[i][1] in w:
            w.remove(l[i][1])
    else:
        prefix = l[i][1]
        f = False
        for k in w:
            if k.startswith(prefix):
                f = True
                break
        r.append(f)
print(w)
print(r)