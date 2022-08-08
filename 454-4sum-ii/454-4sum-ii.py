# 思路：a+b作为key存入dic，记录a+b出现的次数。
# c d双循环中找0-c-d in dic，结果+= 这个次数。
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        dic={}
        # 先统计a+b的和，放入dict
        # key:a+b的数值，value:a+b数值出现的次数
        for a in nums1:
            for b in nums2:
                if a+b in dic:dic[a+b] += 1
                else:dic[a+b] = 1
        # 统计a+b+c+d = 0 出现的次数
        count = 0
        # 在遍历大C和大D数组，找到如果 0-(c+d) 在map中出现过的话，
        # 就把map中key对应的value也就是出现次数统计出来。
        for c in nums3:
            for d in nums4:
                if 0-c-d in dic:
                    count += dic[0-c-d]
        return count