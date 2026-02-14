# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def inorder(node, result):
            if node:
                inorder(node.left, result)
                result.append(node.val)
                inorder(node.right, result)
        
        # Step 1: Get inorder traversal
        result = []
        inorder(root, result)
        
        # Step 2: Find swapped elements
        sorted_result = sorted(result)
        swapped = []
        for i in range(len(result)):
            if result[i] != sorted_result[i]:
                swapped.append(result[i])
        
        # Step 3: Fix the tree by swapping back the wrong nodes
        def fix_tree(node):
            if node:
                if node.val == swapped[0]:
                    node.val = swapped[1]
                elif node.val == swapped[1]:
                    node.val = swapped[0]
                fix_tree(node.left)
                fix_tree(node.right)
        
        fix_tree(root)
