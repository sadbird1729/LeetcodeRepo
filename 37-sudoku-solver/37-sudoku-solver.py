class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        ninegrid = [[''] for i in range(9)] # 记录9个小九宫格，每个小九宫格已存放的数字
        for i in range(9):# 初始化ninegrid
            for j in range(9):
                if '1' <= board[i][j] <= '9':
                    ninegrid[i//3*3+j//3].append(board[i][j])
        
        def isValid(board,row,col,num,ninegrid):
            for i in range(n):
                if i!=col and board[row][i]==num:return False #列
                if i!=row and board[i][col]==num:return False #行
            if num in ninegrid[row//3*3+col//3]:return False #九宫格
            return True
        
        def dfs(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col]!='.':continue
                    for num in '123456789':
                        if isValid(board,row,col,num,ninegrid):
                            board[row][col]=num
                            ninegrid[row//3*3+col//3].append(num)
                            if dfs(board):return True
                            ninegrid[row//3*3+col//3].pop()
                            board[row][col] = '.'
                    return False
            return True
        
        dfs(board)