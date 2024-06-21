s = input()
n = len(s)
max_length = -1
max_str = ""
for i in range(n):
    for j in range(i+2,n+1):
        if s[i:j] == s[i:j][::-1] and j-i > max_length:
            print(s[i:j])
            max_length = len(s[i:j])
            max_str = s[i:j]
print(max_str) 