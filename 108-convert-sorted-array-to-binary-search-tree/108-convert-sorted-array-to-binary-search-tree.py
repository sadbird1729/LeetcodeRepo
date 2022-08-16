# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(left,right):
            if left>right:return
            mid = left+(right-left)//2
            val = nums[mid]
            root = TreeNode(val)
            root.left = dfs(left,mid-1)
            root.right = dfs(mid+1,right)
            return root
        
        root = dfs(0,len(nums)-1)
        return root
        
        