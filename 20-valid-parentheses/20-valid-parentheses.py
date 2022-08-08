class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x == '(':
                stack.append(')')
            elif x == '[':
                stack.append(']')
            elif x == '{':
                stack.append('}')
            elif not stack or stack[-1] != x:
                return False
            else:
                stack.pop()

            # if i in "([{":
            #    stack.append(i)
            # else:
            #     if not stack: return False # 栈空
            #     tmp = stack.pop()
            #     if (tmp == "(" and i != ")") or (tmp == "[" and i != "]") or (tmp == "{" and i != "}"): # 不匹配
            #        return False
        return True if not stack else False

