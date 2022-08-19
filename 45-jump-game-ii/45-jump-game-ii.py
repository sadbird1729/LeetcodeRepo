class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:return 0
        res = 0
        curdistance=0
        nextdistance=0
        for i in range(len(nums)):
            nextdistance=max(nextdistance,i+nums[i])
            if i == curdistance:
                if curdistance !=len(nums)-1:
                    res += 1
                    curdistance=nextdistance
                    if nextdistance>=len(nums)-1:break
        return res
        