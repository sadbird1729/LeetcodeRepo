class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 记录t中所有字母频次
        dic = defaultdict(int) # 不加int报错
        for char in t:
            dic[char] += 1
        
        tlen = len(t)
        left = 0
        minLeft, minRight = 0, len(s)
        for right in range(len(s)):
            if dic[s[right]] > 0:
                tlen -= 1
            dic[s[right]] -= 1
            
            # t_len == 0时，此时窗口中t的对应字符的频次 必都<= 0,
            # 说明此时窗口遇到了所有需要的字符 . 开始移动left，收缩窗口。
            if tlen == 0: 
                # 找左边界：可以缩的情况：
                # 1. t串中没有的字符，窗口中有，字典值为负
                # 2. t串中有3个A，窗口中有10个A，字典值为-7
                while dic[s[left]] < 0:
                    dic[s[left]] += 1
                    left += 1

                if right-left < minRight-minLeft: #记录最小窗口
                    minLeft = left
                    minRight = right
                
                dic[s[left]] += 1 # 顺序！先字典值增加
                tlen += 1
                left += 1

        return '' if minRight==len(s) else s[minLeft:minRight+1]

        """
        s = "ADOBECODEBANC", t = "ABC"
        tlen 控制窗口内有足够的t串字符ABC
        tlen==0时才开始收缩，记录窗口，释放一个s[left]
        dic内除t串字符ABC外，其他字符恒<=0
        """