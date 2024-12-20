# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = []
        if root:
            queue.append((root, 0))

        while queue:
            cur, lev = queue[0]
            if cur.left:
                queue.append((cur.left, lev + 1))
            if cur.right:
                queue.append((cur.right, lev + 1))
            try:
                res[lev].append(cur.val)
            except IndexError as e:
                res.append([cur.val])
            queue.remove((cur, lev))
        return res