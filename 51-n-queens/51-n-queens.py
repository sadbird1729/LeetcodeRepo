class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        path = []
        array = [['.']*n for i in range(n)] # 棋盘
        
        def isValid(array,row,col):
            for i in range(row): # 列重复
                if array[i][col] == 'Q':return False
            for i in range(1,row+1):
                if col-i>=0 and array[row-i][col-i]=='Q':return False # 左上角重复
                if col+i < n and array[row-i][col+i] == 'Q':return False # 右上角重复
            return True
        
        def dfs(array,row):
            if row==n:
                path=[]
                for i in range(n):
                    path.append(''.join(array[i]))
                res.append(path[:])
                return 
            
            for i in range(n):
                if isValid(array,row,i):
                    array[row][i]='Q'
                    dfs(array,row+1)
                    array[row][i]='.'
        
        dfs(array,0)
        return res