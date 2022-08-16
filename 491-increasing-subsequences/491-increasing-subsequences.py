class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        #不能排序，就用repeat数组进行同层去重
        res= []
        path = []
        def dfs(nums,start):
            repeat= []
            if len(path)>1:
                res.append(path[:])
            
            for i in range(start,len(nums)):
                if nums[i] in repeat:
                    continue
                elif path and nums[i]<path[-1]:
                    continue
                else:
                    repeat.append(nums[i])
                    path.append(nums[i])
                    dfs(nums,i+1)
                    path.pop()
        dfs(nums,0)
        return res