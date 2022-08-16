class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def dfs(nums,start):
            res.append(path[:])
            for i in range(start,len(nums)):
                if i>start and nums[i-1]==nums[i]:
                    continue
                path.append(nums[i])
                dfs(nums,i+1)
                path.pop()
                
        nums.sort()
        dfs(nums,0)
        return res
        