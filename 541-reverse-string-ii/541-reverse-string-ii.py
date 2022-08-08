# 分析：如s = ['a','b','c','d','e','f','g']
# 剩余字符数 < k ：s[cur:cur+k] = s[5:10]=s[5:7]=['f','g'] 符合全部反转
# k <= 剩余字符数 < 2*k : s[cur:cur+k]只反转前k
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        # 定义一个反转字串函数
        def re(x):
            left, right = 0, len(x)-1
            while left <= right:
                x[left], x[right] = x[right], x[left]
                left += 1
                right -= 1
            return x
        
        # for循环步长 2*k
        for cur in range(0,len(s),2*k):
            s[cur:cur+k] = re(s[cur:cur+k])
        return ''.join(s)


