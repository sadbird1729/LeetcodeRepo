class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 0:
            return False
        next = self.getNext(s)
        if next[-1] != -1 and len(s) % (len(s) - next[-1] -1) == 0:
            return True
        else:
            return False


    def getNext(self,s):
        next = ['']*len(s)
        j = -1
        next[0] = j
        for i in range(1,len(s)):
            while j >= 0 and s[i] != s[j+1]:
                j = next[j]
            if s[i] == s[j+1]:
                j += 1
            next[i] = j
        return next