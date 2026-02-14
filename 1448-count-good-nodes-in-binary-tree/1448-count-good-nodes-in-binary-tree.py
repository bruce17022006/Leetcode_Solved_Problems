# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#        self.right = right
class Solution:
    def count(root,path):
        global num
        if not root:
            return
        path.append(root.val)
        if root.left:
            Solution.count(root.left,path)
        if root.right:
            Solution.count(root.right,path)
        if root.val >= max(path):
            num+=1
        path.pop()
        return
    def goodNodes(self, root: TreeNode) -> int:
          global num
          num=0
          path=[]
          Solution.count(root,path)
          return num
num=0          