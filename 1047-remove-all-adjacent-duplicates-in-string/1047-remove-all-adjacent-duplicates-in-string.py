class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for x in s:
            if stack and stack[-1] == x:
                stack.pop()
            else:
                stack.append(x)
        return ''.join(stack)

        # s = list(s)
        # left, right = 0, 0
        # while right <= len(s)-1:
        #     s[left] = s[right]
        #     if left > 0 and s[left] == s[left-1]:
        #         left -= 1
        #     else:
        #         left += 1
        #     right += 1 
        # return ''.join(s[:left])