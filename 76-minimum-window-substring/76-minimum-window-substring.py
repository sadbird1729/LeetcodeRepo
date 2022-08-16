class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = collections.defaultdict(int)
        for char in t:
            dic[char]+= 1
        
        tlen = len(t)
        left = 0
        minl,minr = 0,len(s)
        for right in range(len(s)):
            if dic[s[right]]>0:
                tlen -= 1
            dic[s[right]] -= 1
            
            if tlen == 0:
                while dic[s[left]] <0:
                    dic[s[left]] += 1
                    left += 1
                
                if right-left<minr-minl:
                    minr=right
                    minl=left
            
                dic[s[left]] += 1
                tlen += 1
                left += 1
        return '' if minr==len(s) else s[minl:minr+1]