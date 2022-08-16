class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def isGood(s):
            if not s:return False
            elif s[0]=='0' and len(s)>1:return False
            elif int(s)>255:return False
            else:return True
            
            
        def dfs(s,start,num):
            if num ==3:
                if isGood(s[start:]):
                    res.append(s[:])
                    return
            
            for i in range(start,len(s)):
                if isGood(s[start:i+1]):
                    s = s[:i+1]+'.'+s[i+1:]
                    dfs(s,i+2,num+1)
                    s = s[:i+1]+s[i+2:]
                else:break
        
        dfs(s,0,0)
        return res
        