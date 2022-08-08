# 如果对空文本输入退格字符，文本继续为空。
# elif left > 0: left -= 1

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        s_left, s_right = 0, 0
        while s_right <= len(s)-1:
            if s[s_right] != '#':
                s[s_left] = s[s_right]
                s_left += 1
            elif s_left > 0:
                s_left -= 1    
            s_right += 1

        t_left, t_right = 0, 0
        while t_right <= len(t)-1:
            if t[t_right] != '#':
                t[t_left] = t[t_right]
                t_left += 1
            elif t_left > 0:
                t_left -= 1
            t_right += 1
        
        if s_left != t_left: return False
        else:
            for i in range(s_left):
                if s[i] != t[i]:return False
        return True