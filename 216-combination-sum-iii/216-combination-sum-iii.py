class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(k,n,start):
            if n<0:return 
            if len(path)==k:
                if n==0:
                    res.append(path[:])
                    return 
            for i in range(start,10-(k-len(path))+1):
                path.append(i)
                dfs(k,n-i,i+1)
                path.pop()
        
        dfs(k,n,1)
        return res