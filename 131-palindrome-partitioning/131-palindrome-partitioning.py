class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isP(s):
            left,right=0,len(s)-1
            while left<=right:
                if s[left] != s[right]:return False
                left += 1
                right -= 1
            return True
        
        res = []
        path = []
        def dfs(s,start):
            if start>= len(s):
                res.append(path[:])
                return 
            
            for i in range(start,len(s)):
                if isP(s[start:i+1]):
                    path.append(s[start:i+1])
                    dfs(s,i+1)
                    path.pop()
        
        dfs(s,0)
        return res