class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        idx = len(s)-1 # cookie
        res = 0
        for i in range(len(g)-1,-1,-1):
            if idx>=0 and s[idx]>=g[i]:
                res += 1
                idx -=1
        return res
        