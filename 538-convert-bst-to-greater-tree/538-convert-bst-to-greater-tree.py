# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sum_ = 0
        def dfs(root):
            nonlocal sum_
            if not root:return
            
            dfs(root.right)
            sum_ += root.val
            root.val=sum_
            
            dfs(root.left)
            
        dfs(root)
        return root
        