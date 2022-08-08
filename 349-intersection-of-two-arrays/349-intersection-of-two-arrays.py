# 建两个字典， if num in dic1 --> if num in dic2:res.append(num)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1, dic2 = {}, {} # {1:出现几次，2:出现几次} key：前面的数字
        res = []
        for num in nums1:
            if num in dic1:dic1[num] += 1
            else:dic1[num] = 1
        for num in nums2:
            if num in dic2:dic2[num] += 1
            else:dic2[num] = 1
        for num in dic1:
            if num in dic2:res.append(num)
        return res