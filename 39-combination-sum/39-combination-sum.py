class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(candidates,target,start):
            if target==0:
                res.append(path[:])
                return
            
            for i in range(start,len(candidates)):
                if target-candidates[i]<0:return
                path.append(candidates[i])
                dfs(candidates, target-candidates[i],i)
                path.pop()
        
        candidates.sort()
        dfs(candidates,target,0)
        return res
        