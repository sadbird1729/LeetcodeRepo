# 思路：每次getnum的数若在字典中出现就是不快乐
class Solution:
    def isHappy(self, n: int) -> bool:
        def getnum(n):#获取每个位置上的数字的平方和
            num = 0
            while n:
                num += (n%10)**2
                n=n//10
            return num
        # 循环出现就是不快乐数，False
        record={}
        while True:
            n = getnum(n)
            if n==1:return True
            if n in record:return False
            else:record[n] = 1