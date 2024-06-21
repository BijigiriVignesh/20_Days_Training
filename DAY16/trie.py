class Node:
    def __init__(self):
        self.d = {}
        self.flag = 0

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, s):
        t = self.root
        for i in s:
            if i not in t.d:
                t.d[i] = Node()
            t = t.d[i]
        t.flag = 1

    def search(self, s):
        t = self.root
        for i in s:
            if i not in t.d:
                return False
            t = t.d[i]
        return t.flag == 1
    
    def search_prefix(self, prefix):
        t = self.root
        for i in prefix:
            if i not in t.d:
                return False
            t = t.d[i]
        return True

    def search_all_elements_with_prefix(self, prefix):
        def fun(t, s):
            if t.flag == 1:
                print(s)
            for i in t.d:
                fun(t.d[i], s + i)

        t = self.root
        s = ""
        for i in prefix:
            if i in t.d:
                s += i
                t = t.d[i]
            else:
                return  
        fun(t, s)

t1 = Trie()
n = int(input())
for i in range(n):
    a, s = input().split()
    if a == '1':
        t1.insert(s)
    elif a == '2':
        print(t1.search(s))
    elif a == '3':
        print(t1.search_prefix(s))
    elif a == '4':
        t1.search_all_elements_with_prefix(s)
