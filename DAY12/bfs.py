def bfs(x, v):
    q = [x]
    while q:
        c = q.pop(0)
        if c not in v:
            v.append(c)
            if c == 2:
                return 
            for i,j in d[c]:
                q.append(i)

d = { 
    5: [(7, 1), (3, 2)],
    7: [(5, 1), (4, 3), (3, 4)],
    3: [(5, 2), (7, 4), (8, 4)],
    4: [(7, 3), (8, 2), (2, 6)],
    8: [(3, 4), (4, 2), (2, 2)],
    2: [(4, 6), (8, 2)]
}

v = []
bfs(5, v)
print("Visited nodes:", v)
