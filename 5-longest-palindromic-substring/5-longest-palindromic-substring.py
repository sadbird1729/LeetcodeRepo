# 中心扩散
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 对s中每一个字符向左右扩展
        # 1个元素可以作为中心点，2个元素也可以作为中心点
        def extend(s,i,j,n):
            nonlocal left, right, maxlen
            while i >= 0 and j < n and s[i] == s[j]:
                if j-i+1 > maxlen:
                    left = i
                    right = j
                    maxlen = j-i+1
                i-= 1
                j += 1
        
        left, right, maxlen = 0, 0, 0
        n = len(s)
        for i in range(n):
            extend(s,i,i,n)     # 以i为中心
            extend(s,i,i+1,n)   # 以i和i+1为中心
        
        return s[left:right+1]