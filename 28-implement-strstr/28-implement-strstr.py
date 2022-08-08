class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:return 0
        next = self.getNext(needle)
        # j 指向模式串起始位置，i指向文本串起始位置。
        j = -1
        for i in range(len(haystack)):
            while j >= 0 and haystack[i] != needle[j+1]: # 不匹配了
                j = next[j]
            if haystack[i] == needle[j+1]:
                j += 1 # i的增加在for循环里
            # 如果j指向了模式串t的末尾，那么就说明模式串t完全匹配文本串s里的某个子串了。
            # 本题要在文本串字符串中找出模式串出现的第一个位置 (从0开始)，所以返回当前在文本串匹配模式串的位置i 减去 模式串的长度，就是文本串字符串中出现模式串的第一个位置
            if j == len(needle)-1:
                return i-len(needle)+1
        return -1


    def getNext(self,needle):
        '''
        构造next数组其实就是计算模式串s，前缀表的过程。
        1.初始化
        2.处理前后缀不相同的情况
        3.处理前后缀相同的情况
        '''
        next = ['' for i in range(len(needle))]  # next = ['']*len(needle)
        # j指向前缀起始位置，i指向后缀起始位置
        j = -1 # 前缀表统一减一
        next[0] = j # next[i] 表示 i（包括i）之前最长相等的前后缀长度（其实就是j）
        for i in range(1,len(needle)):
            while j >= 0 and needle[i] != needle[j+1]: # 前后缀不相同了
                j = next[j] # 向前回退
            if needle[i] == needle[j+1]: # 找到相同的前后缀
                j += 1
            next[i] = j # 将j（前缀的长度）赋给next[i]
        return next

'''
# KMP的经典思想就是:当出现字符串不匹配时，可以记录一部分之前已经匹配的文本内容，利用这些信息避免从头再去做匹配。

# 字符串的前缀是指不包含最后一个字符的所有以第一个字符开头的连续子串。
# 后缀是指不包含第一个字符的所有以最后一个字符结尾的连续子串。

最长相等前后缀
# 什么是前缀表：记录下标i之前（包括i）的字符串中，有多大长度的相同前缀后缀。
 
# 下标5之前这部分的字符串（也就是字符串aabaa）的最长相等的前缀 和 后缀字符串是 子字符串aa ，因为找到了最长相等的前缀和后缀，匹配失败的位置是后缀子串的后面，那么我们找到与其相同的前缀的后面从新匹配就可以了。

    # 下标      0,1,2,3,4,5
    # 模式串   [a,a,b,a,a,f]
    # 前缀表    0,1,0,1,2,0
    # next数组  -1,0,-1,0,1,-1
    看出模式串与前缀表对应位置的数字表示的就是：下标i之前（包括i）的字符串中，有多大长度的相同前缀后缀
    next数组：不涉及到KMP的原理,具体实现，next数组即可以就是前缀表，也可以是前缀表统一减一（右移一位，初始位置为-1）。
'''