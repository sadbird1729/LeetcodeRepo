# 思路1：对每个字符串先排序，将排序之后的字符串作为哈希表的键
# 思路2：计数，每个字符串可以使用长为 26 的数组记录每个字母出现的次数，数组作为哈希表的键
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            nums=[0]*26 # 记录每个字符串对应的字母出现次数
            for x in s:
                nums[ord(x)-ord('a')] += 1
            if tuple(nums) in dic: # 数组作为哈希表的键
                dic[tuple(nums)].append(s)
            else:
                dic[tuple(nums)] = [s]
        return list(dic.values())