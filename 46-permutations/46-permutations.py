class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res= []
        path=[]
        used = [0]*len(nums)
        def dfs(root,used):
            if len(path)==len(nums):
                res.append(path[:])
            for i in range(len(nums)):
                if used[i]==0:
                    used[i]=1
                    path.append(nums[i])
                    dfs(nums,used)
                    path.pop()
                    used[i]=0
        
        dfs(nums,used)
        return res
        