# 思路：滑动窗口+双指针.
# snums，pnums分别使用长为 26 的数组记录s,p每个字母出现的次数，
# 初始pnums，同时snums初始p串长，接下来while r<len(s), 
# 滑窗移动判断snums=pnums. O(s)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) >len(s):return []
        snums,pnums = [0]*26, [0]*26 # s串和p串的字母出现次数数字
        l,r = 0, 0 # s串的滑窗左右边界
        res = []
        for i in range(len(p)): # 初始len(p)的pnums,snums
            pnums[ord(p[i])-ord('a')] += 1
            snums[ord(s[r])-ord('a')] += 1
            r += 1
        if snums == pnums:
            res.append(l)
        while r < len(s):
            # 上面退出for时r=3
            snums[ord(s[r])-ord('a')] += 1
            r += 1
            snums[ord(s[l])-ord('a')] -= 1
            l += 1
            if snums==pnums:
                res.append(l)
        return res