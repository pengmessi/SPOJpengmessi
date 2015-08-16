__author__ = 'pengmessi'

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}

    def convert(self, v, val):
        if v == val:
            return str(val)
        else:
            return "->"+str(val)

    def binaryTreePathsHelper(self, v, node):
        if node == None:
            return []
        else:
            #print(node.val)
            arr = self.binaryTreePathsHelper(v, node.left) + self.binaryTreePathsHelper(v, node.right)
            if arr == []:
                arr = [self.convert(v, node.val)]
            else:
                arr = [self.convert(v, node.val) + s for s in arr]
            return arr

    def binaryTreePaths(self, root):
        return self.binaryTreePathsHelper(root.val, root)

if __name__ == '__main__':
    tn = TreeNode(1)
    tn.left = TreeNode(2)
    tn.left.left = TreeNode(3)
    tn.left.right = TreeNode(5)

    sln = Solution()
    print( sln.binaryTreePaths(tn) )