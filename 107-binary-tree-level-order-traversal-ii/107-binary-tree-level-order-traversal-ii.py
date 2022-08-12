# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = []
        if not root:
            return results
        
        que = collections.deque([root])
        while que:
            size = len(que)
            res = []
            for _ in range(size):
                cur = que.popleft()
                res.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            results.append(res)

        return results[::-1]