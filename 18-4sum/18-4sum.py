# 思路：同三数之和
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        if len(nums)<4:return []
        nums.sort()
        n = len(nums)
        for i in range(n-3):
            if i>0 and nums[i] == nums[i-1]:continue
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target:break
            if nums[i]+nums[n-1]+nums[n-2]+nums[n-3]<target:continue
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]:continue
                if nums[i]+nums[j]+nums[j+1]+nums[j+2]>target:break
                if nums[i]+nums[j]+nums[n-1]+nums[n-2]<target:continue

                l, r = j+1, n-1
                while l < r:
                    tmp = nums[i]+nums[j]+nums[l]+nums[r]
                    if tmp==target:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        while l+1<r and nums[l+1]==nums[l]:l += 1
                        while l<r-1 and nums[r-1]==nums[r]:r -= 1
                        l += 1
                        r -= 1
                    elif tmp<target:
                        l += 1
                    else:
                        r -= 1

        return res