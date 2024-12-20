# https://leetcode.com/problems/kth-smallest-element-in-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            nonlocal k
            if node.left:
                result = inorder(node.left)
                if result is not None:
                    return result
            k -= 1
            if k == 0:
                return node.val
            if node.right:
                result = inorder(node.right)
                if result is not None:
                    return result
        
        return inorder(root)