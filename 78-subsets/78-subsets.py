class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        
        def dfs(nums, start):
            res.append(path[:])
            
            for i in range(start,len(nums)):
                path.append(nums[i])
                dfs(nums, i+1)
                path.pop()
        
        dfs(nums,0)
        return res
        