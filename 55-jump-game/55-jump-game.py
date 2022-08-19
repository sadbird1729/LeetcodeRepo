class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mostfar = 0
        for i in range(len(nums)):
            if i<=mostfar:
                mostfar = max(mostfar,i+nums[i])
            if mostfar>=len(nums)-1:return True
        return None