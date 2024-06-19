class node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class root:
    def __init__(self):
        self.root = None
    
    def create(self, root, x):
        if root is None:
            return node(x)
        else:
            if x < root.data:
                root.left = self.create(root.left, x)
            else:
                root.right = self.create(root.right, x)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)
    def preorder(self, root):
        if root:
            print(root.data, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=' ')
    def add(self, root):
        if root is None:
            return 0
        return self.add(root.left) + root.data + self.add(root.right)
    def add_even(self, root):
        s = 0
        if root is None:
            return 0
        # if root.data % 2 == 0:
        #     return root.data + self.add_even(root.left) + self.add_even(root.right)
        # else:
        #     return self.add_even(root.left) + self.add_even(root.right)
        if root.data%2 == 0:
            s+=root.data
        s+=self.add_even(root.left)
        s+=self.add_even(root.right)
        return s
    def abs_diff(self, root):
        # s, s1 = 0, 0
        if root is None:
            return 0
        
        if root.data % 2 == 0:
            # s += root.data
            return root.data + self.abs_diff(root.left) + self.abs_diff(root.right)
        return self.abs_diff(root.left) + self.abs_diff(root.right) - root.data
        # else:
        #     s1 += root.data
        
        # s += self.abs_diff(root.left)
        # s += self.abs_diff(root.right)

        # s1 += self.abs_diff(root.left)
        # s1 += self.abs_diff(root.right)
        # return abs(s - s1)
    def height(self,root):
        if root is None:
            return 0
        return 1+max(self.height(root.left),self.height(root.right))
    def balanced(self, root):
        if root is None:
            return True
        # left = self.height(root.left)
        # right  = self.height(root.right)
        # if left != right:
        #     return False
        # return True
        # return self.height(root.left) == self.height(root.right)
        return abs(self.height(root.left) - self.height(root.right)) <= 1
    def leaf_node_count(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self.leaf_node_count(root.left) + self.leaf_node_count(root.right)
    def search_element(self,root,key):
        if root == None:
            return False
        if root.data == key:
            return True
        elif root.data > key:
            return self.search_element(root.left,key)
        else:
            return self.search_element(root.right,key)
    def depth(self, root, d,x):
        if root is None:
            return -1
        if root.data == d :
            return x
        elif root.data > d:
            return self.depth(root.left,d,x+1)
        else:
            return self.depth(root.right,d,x+1)
        
    # def left_view(self, root):
    #     def left_view_util(root, c, m):
    #         if root is None:
    #             return m
    #         if m[0] < c:
    #             print(root.data)
    #             m[0] = c
    #         m = left_view_util(root.left, c + 1, m)
    #         m = left_view_util(root.right, c + 1, m)
    #         return max_level
    #     left_view_util(root, 1, [0])

    # def right_view(self, root):
    #     def right_view_util(root, c, m):
    #         if root is None:
    #             return m
            
    #         if m[0] < c:
    #             print(root.data)
    #             m[0] = c
            
    #         m = right_view_util(root.right, c + 1, m)
    #         m = right_view_util(root.left, c + 1, m)
    #         return m
        
    #     right_view_util(root, 1, [0])
    def left_view(self,root,c,l):
        if root is None:
            return 
        if c not in l:
            l.append(c)
            print(root.data)
        self.left_view(root.left, c+1, l)
        self.left_view(root.right, c+1, l)
    def right_view(self,root,c,l):
        if root is None:
            return 
        if c not in l:
            l.append(c)
            print(root.data)
        self.right_view(root.right, c+1, l)
        self.right_view(root.left, c+1, l)
    
    def top_view(self, root):
        if root is None:
            return
        d = {}
        q = [(root, 0)]
        while q:
            root, c = q.pop(0)
            if c not in d:
                d[c] = root.data
            if root.left:
                q.append((root.left, c - 1))
            if root.right:
                q.append((root.right, c + 1))
        for i in sorted(d):
            print(d[i], end=" ")
    def bottom_view(self, root):
        if root is None:
            return
        d = {}
        q = [(root, 0)]
        while q:
            node, c = q.pop(0)
            d[c] = node.data  
            if node.left:
                q.append((node.left, c - 1))
            if node.right:
                q.append((node.right, c + 1))
        for i in sorted(d):
            print(d[i], end=" ")

l1 = root()
l1.root = l1.create(l1.root, 5)
l1.root = l1.create(l1.root, 2)
l1.root = l1.create(l1.root, 7)
l1.root = l1.create(l1.root, 1)
l1.root = l1.create(l1.root, 3)
l1.root = l1.create(l1.root, 6)
l1.root = l1.create(l1.root, 8)

print("In order")
l1.inorder(l1.root)
print()
print("Pre order")
l1.preorder(l1.root)
print()
print("Post order")
l1.postorder(l1.root)
print()
print("Sum of all nodes")
print(l1.add(l1.root))
print("Sum of even nodes")
print(l1.add_even(l1.root))
print("Absolute difference of even and odd node sums")
print(l1.abs_diff(l1.root))
print("Height of tree")
print(l1.height(l1.root))
print("Is tree balanced?")
print(l1.balanced(l1.root))
print("Leaf node count")
print(l1.leaf_node_count(l1.root))
print("Search for a node with value 3")
print(l1.search_element(l1.root, 3))
print("Depth of node with value 3")
print(l1.depth(l1.root, 3, 0))
print("Left view of the tree")
l1.left_view(l1.root, 0, [])
print("Right view of the tree")
l1.right_view(l1.root, 0, [])
print("Top view of the tree")
l1.top_view(l1.root)
print()
print("Bottom view of the tree")
l1.bottom_view(l1.root)