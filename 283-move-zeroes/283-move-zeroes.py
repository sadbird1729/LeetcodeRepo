class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 0
        while right <= len(nums)-1:
            if nums[right] != 0:
                nums[left],nums[right] = nums[right], nums[left]
                left += 1
            right += 1

