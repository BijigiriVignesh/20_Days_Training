s1 = "tu5g2k1h8"
s2 = "g5g8gd6h3"
s1 = s1+s2
print(s1)
l = []
for i in s1:
    if i.isdigit():
        l.append(i)
l = list(set(l))
l.sort(reverse=True)
if int(l[-1]) % 2 == 0:
    print("".join(l))
else:
    for i in range(len(l)-1, -1, -1):
        if int(l[i]) % 2 == 0:
            l.append(l.pop(i))
            print("".join(l))
            break
    else:
        print("-1")