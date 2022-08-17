class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # 332-339-329-399-299
        # 101-199-099
        a = list(str(n)) # ['3','3','2']
        for i in range(len(a)-1,0,-1):
            if a[i] < a[i-1]:
                a[i:] = '9'*(len(a)-i)
                a[i-1] =str(int(a[i-1])-1)
        return int(''.join(a))
        