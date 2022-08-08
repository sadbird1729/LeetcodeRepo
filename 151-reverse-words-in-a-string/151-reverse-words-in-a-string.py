class Solution:
    def removeSpaces(self,s):
        left, right = 0, len(s)-1
        # 去除开头和结尾空格
        while left<right and s[left]==' ':left += 1
        while left<right and s[right]==' ':right -= 1
        # new_s 存储去掉多余空格剩下的东西
        new_s = []
        while left <= right:
            if s[left] != ' ':
                new_s.append(s[left])
            # 如果当前是空格，且前一个字符不是空格，则添加
            elif s[left] == ' ' and new_s[-1] != ' ':
                new_s.append(s[left])
            left += 1
        return new_s
    
    def reverseString(self,s):
        left, right = 0, len(s)-1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

    def reserveEachWord(self,s):
        # 双指针指向每个单词的首尾
        left, right = 0, 0
        n = len(s)-1
        while right <= n:
            while right <= n and s[right] != ' ':# right走到当前单词尾巴的下一个' '
                right += 1
            s[left:right] = self.reverseString(s[left:right])
            # 反转完一个单词，该反转下个单词了
            left = right + 1
            right += 1
        return s

    def reverseWords(self, s: str) -> str:
        # 源字符串为："the sky is blue "
        # 移除多余空格 : "the sky is blue"
        # 字符串反转："eulb si yks eht"
        # 单词反转："blue is sky the"
        s = self.removeSpaces(s)
        s = self.reverseString(s)
        s = self.reserveEachWord(s)
        return ''.join(s)

# 空间复杂度依照你所用的编程语言来确定，因为有的编程语言存在字符串不可修改的情况，比如 Python、Java，这就需要额外用一个数组来存储，那么它的空间复杂度就成了 O(n)。

# 如果所用编程语言字符串支持修改，比如 C++，那空间复杂度为 O(1)。