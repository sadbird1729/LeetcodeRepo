class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        curdiff,prediff=0,0
        res = 1
        for i in range(len(nums)-1):
            curdiff= nums[i+1]-nums[i]
            if (curdiff>0 and prediff<=0) or (curdiff<0 and prediff>=0):
                res += 1
                prediff=curdiff
        return res