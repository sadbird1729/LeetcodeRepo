class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=  []
        path = []
        def dfs(candidates,target,start):
            if target ==0:
                res.append(path[:])
                return 
            
            for i in range(start,len(candidates)):
                if i >start and candidates[i]==candidates[i-1]:
                    continue
                if target-candidates[i]<0:
                    break
                else:
                    path.append(candidates[i])
                    dfs(candidates,target-candidates[i],i+1)
                    path.pop()
        
        candidates.sort()
        dfs(candidates,target,0)
        return res
                
        