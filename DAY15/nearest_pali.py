# def pali(n):
#     k = str(n)
#     return k == k[::-1]

# def np(n):
#     if pali(n):
#         return n
#     else:
#         while True:
#             n += 1
#             if pali(n):
#                 return n
# n = int(input())
# r = np(n)
# print(r)


















n = input()
k = len(n)//2
k = n[::k]
print(k)
m = k+k
if m<n:
    a = int(k)+1
m = str(a)+str(a)[::-1]
print(m)