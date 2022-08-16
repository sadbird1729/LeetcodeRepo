# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        count = 0
        maxcount = 0
        pre = None
        def dfs(cur):
            nonlocal res,count,pre,maxcount
            if not cur:return None
            dfs(cur.left)
            
            if not pre:count=1
            elif pre.val==cur.val:count += 1
            else:count = 1
            
            pre = cur
            if count==maxcount:res.append(cur.val)
            elif count>maxcount:
                res= [cur.val]
                maxcount=count
            
            dfs(cur.right)
        
        dfs(root)
        return res
        
            
                
        