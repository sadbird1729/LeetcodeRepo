"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        results = []
        if not root:
            return results
        
        que = collections.deque([root])
        while que:
            res = []
            for _ in range(len(que)):
                cur = que.popleft()
                res.append(cur.val)
                # cur.children 是 Node 对象组成的列表，也可能为 None
                if cur.children:
                    que.extend(cur.children) # list不要append拼接，要用extend
            results.append(res)

        return results
