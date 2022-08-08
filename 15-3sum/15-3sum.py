# 思路：数不重复！！
# tmp=0去重，left+1和left，right-1和right。
# 剪枝，i和i-1continue，
# i，i+1，i+2三数之和>0break,
# i，n-1，n-2三数之和<0continue
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # 下标不重复
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i >0 and nums[i]==nums[i-1]:continue
            if i+2<n and nums[i]+nums[i+1]+nums[i+2]>0:break
            if i!=n-2 and nums[i]+nums[n-1]+nums[n-2]<0:continue 
            left, right = i+1, n-1
            while left<right:
                tmp = nums[i]+nums[left]+nums[right]
                if tmp == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    while left+1<right and nums[left+1]==nums[left]:left += 1
                    while left<right-1 and nums[right-1]==nums[right]:right -=1
                    left += 1
                    right -= 1
                elif tmp<0:left += 1
                else:right -= 1

        return res