
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1, dic2 = {}, {}
        res = []
        for num in nums1:
            if num in dic1:dic1[num] += 1
            else:dic1[num] = 1
        
        # 保证总取到最小
        # nums1[1,1,2,2,2] nums2[2,2],nums2遍历完时dic1[2]还>0，但不影响res了
        # nums1[1,1,2],nums2[2,2],在if时dic1[2]已经<0了，不添加res
        for num in nums2:
            if num in dic1 and dic1[num]:
                res.append(num)
                dic1[num] -= 1
        return res