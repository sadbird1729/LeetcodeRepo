# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            node = TreeNode(val)
            return node
        
        parent = root
        cur = root
        while cur:
            parent = cur
            if cur.val>val:cur=cur.left
            else:cur=cur.right
        
        
        node = TreeNode(val)
        if parent.val>val:parent.left=node
        else:parent.right=node
        return root