class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def findPreSuc(self, root, key):
        self.pre = None
        self.suc = None

        def helper(node):
            if not node:
                return
            
            if node.data == key:

                if node.left:
                    temp = node.left
                    while temp.right:
                        temp = temp.right
                    self.pre = temp

                if node.right:
                    temp = node.right
                    while temp.left:
                        temp = temp.left
                    self.suc = temp

            elif node.data > key:
                self.suc = node  # possible successor
                helper(node.left)
            else:
                self.pre = node  # possible predecessor
                helper(node.right)
        
        helper(root)
        
        pre_val = self.pre.data if self.pre else -1
        suc_val = self.suc.data if self.suc else -1
        return (self.pre, self.suc)
