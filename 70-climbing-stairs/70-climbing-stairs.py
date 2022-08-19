class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:return n
        
        a1 = 1
        a2 = 2
        for i in range(3,n+1):
            temp=a1+a2
            a1=a2
            a2=temp
        return a2
        