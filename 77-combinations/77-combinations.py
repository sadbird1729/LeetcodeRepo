class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(n,k,start):
            if len(path)==k:
                res.append(path[:])
                return

            for i in range(start,n-(k-len(path))+2):
                path.append(i)
                dfs(n,k,i+1)
                path.pop()
            
        dfs(n,k,1)
        return res