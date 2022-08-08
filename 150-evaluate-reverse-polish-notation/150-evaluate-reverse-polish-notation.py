class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中
        stack = []
        for x in tokens:
            if x not in '+-*/': # 遇到数字直接入栈
                stack.append(int(x))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if x == '+':stack.append(num2+num1)
                elif x == '-':stack.append(num2-num1)
                elif x == '*':stack.append(num2*num1)
                elif x == '/':stack.append(int(num2/num1)) #两个整数之间的除法只保留整数部分。
        return stack[0]