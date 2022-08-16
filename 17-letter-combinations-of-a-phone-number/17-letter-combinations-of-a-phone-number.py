class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        res =[]
        s =''
        def dfs(digits,s,idx):
            if idx==len(digits):
                res.append(s)
                return 
            
            for x in dic[digits[idx]]:
                dfs(digits,s+x,idx+1)
        
        if not digits:return res
        dfs(digits,s,0)
        return res
                