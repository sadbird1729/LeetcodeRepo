class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [0]*len(nums)
        def dfs(nums,used):
            if len(path)==len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                #同树层去重,[1,1,2]选了第一个1做开头，就不要再选第二个1做开头
                if i>0 and used[i-1]==0 and nums[i-1]==nums[i]:
                    continue
                if used[i]==0:
                    used[i] = 1
                    path.append(nums[i])
                    dfs(nums,used)
                    path.pop()
                    used[i] = 0

        
        nums.sort()
        dfs(nums,used)
        return res
    
        