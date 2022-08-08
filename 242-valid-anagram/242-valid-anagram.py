class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sn = [0]*26
        tn = [0]*26
        for x in s:
            sn[ord(x)-97] += 1
        for x in t:
            tn[ord(x)-97] += 1
        for i in range(26):
            if sn[i] != tn[i]:return False
        return True