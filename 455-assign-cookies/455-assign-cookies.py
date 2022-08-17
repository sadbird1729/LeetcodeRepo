class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        idx = 0 # child
        for i in range(len(s)):
            if idx<len(g) and s[i]>=g[idx]:
                idx +=1
        return idx
        