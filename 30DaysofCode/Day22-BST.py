class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        if root.right is None or root.left is None:
            return 1
        else:
            return max(self.getHeight(root.right)+1,
                       self.getHeight(root.left)+1)


T = int(raw_input())
myTree = Solution()
root = None
for i in range(T):
    data = int(raw_input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print height


# 9
# 20
# 50
# 35
# 44
# 9
# 15
# 62
# 11
# 13  --returns 4