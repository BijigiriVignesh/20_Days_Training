# a = list(input().split(","))
# m = []
# l = []
# for i in a:
#     d = []
#     b,c = i.split(':')
#     m.append(b)
#     for i in c:
#         d.append(int(i))
#     l.append(d)
# print(m,l)
# s = ""
# for i in range(len(m)):
#     k = len(m[i])
#     if k in l[0][i]:
a = list(input().split(","))
s = ""
for i in a:
    b = i.split(":")
    l = len(b[0])
    if str(l) in b[1]:
        s = s+b[0][-1]
    else:
        for i in range(l-1,0,-1):
            if str(i) in b[1]:
                s=s+b[0][i-1]
                break
        else:
            s=s+'X'
print(s)