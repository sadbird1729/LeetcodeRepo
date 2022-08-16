# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        curmax = -float("INF")
        def dfs(root):
            nonlocal curmax
            if not root:return True
            left = dfs(root.left)
            if root.val>curmax:
                curmax=root.val
            else:
                return False
            right = dfs(root.right)
            return left and right
        return dfs(root)
        