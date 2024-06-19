# # k = []
# # def fun(x, l, s):
# #     global m
# #     l.append(x)
# #     if x == 2 :
# #         k.append((l[:], s))
# #         l.pop()
# #         return
# #     for i, j in d[x]:
# #         if i not in l:
# #             fun(i, l, s + j)
# #     l.pop()
# # d = { 
# #     5: [(7, 1), (3, 2)],
# #     7: [(5, 1), (4, 3), (3, 4)],
# #     3: [(5, 2), (7, 4), (8, 4)],
# #     4: [(7, 3), (8, 2), (2, 6)],
# #     8: [(3, 4), (4, 2), (2, 2)],
# #     2: [(4, 6), (8, 2)]
# # }
# # r = []
# # fun(5, r, 0)
# # print(k)
# # m = float('inf')
# # for i, j in k:
# #     if j < m:
# #         m = j
# #         mp = i
# # print("Minimum score:", m)
# # print("Path with minimum :", mp)


# k = []
# m = float('inf')
# def fun(x, l, s):
#     global m
#     l.append(x)
#     if x == 2:
#         if s < m:
#             k.clear()
#             k.append((l[:], s))
#             m = s  
#         elif s == m:
#             k.append((l[:], s)) 
#         l.pop()
#         return
#     # if x == 2:
#     #     if s < m:
#     #         min_path = (l[:], s)
#     #         m = s 
#     #     elif s == m:
#     #         k.append((l[:], s)) 
#     #     l.pop()
#     #     return
#     for i, j in d[x]:
#         if i not in l:
#             fun(i, l, s + j)
#     l.pop()

# d = { 
#     5: [(7, 1), (3, 2)],
#     7: [(5, 1), (4, 3), (3, 4)],
#     3: [(5, 2), (7, 4), (8, 4)],
#     4: [(7, 3), (8, 2), (2, 6)],
#     8: [(3, 4), (4, 2), (2, 2)],
#     2: [(4, 6), (8, 2)]
# }

# r = []
# fun(5, r, 0)
# print(k)
# # if min_path:
# #     k.append(min_path)

k = []
m = float('inf')
def fun(x, l, s, n):
    global m
    l.append(x)
    if x == n:
        k.append((l[:], s))
        l.pop()
        return
    for i, j in d[x]:
        if i not in l:
            fun(i, l, s + j, n)
    l.pop()

d = { 
    5: [(7, 1), (3, 2)],
    7: [(5, 1), (4, 3), (3, 4)],
    3: [(5, 2), (7, 4), (8, 4)],
    4: [(7, 3), (8, 2), (2, 6)],
    8: [(3, 4), (4, 2), (2, 2)],
    2: [(4, 6), (8, 2)]
}
for i in d.keys():
    for j in d.keys():
        k=[]
        v=set()
        fun(i, [], 0, j)
        for row,cost in k:
            print(row,cost)
# print(k)