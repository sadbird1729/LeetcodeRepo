# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 入栈中左右，出栈中右左，反转为左右中即后序
        if not root:
            return []
        
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            # mid
            res.append(node.val)
            # left
            if node.left:
                stack.append(node.left)
            # right
            if node.right:
                stack.append(node.right)
        
        return res[::-1]