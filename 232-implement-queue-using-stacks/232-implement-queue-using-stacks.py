# 先入先出队列
# list [] pop() 先入后出 nums=[1,2,3,4,5],nums.pop()=5
# 2个栈实现先入先出队列。pop时stackout.append(stackin.pop())

class MyQueue:

    def __init__(self):
        """
        in主要负责push，out主要负责pop
        """
        self.stackin = []
        self.stackout = []


    def push(self, x: int) -> None:
        """
        有新元素就往stackin里push
        """
        self.stackin.append(x)


    def pop(self) -> int:
        """
        从队列开头移除并返回元素
        """
        if self.empty():return None
        if not self.stackout: # out栈为空
            for _ in range(len(self.stackin)):
                self.stackout.append(self.stackin.pop())
        return self.stackout.pop()


    def peek(self) -> int:
        """
        返回队列开头元素
        """
        ans =self.pop()
        self.stackout.append(ans) # 只要返回，不要移除，所以再append上
        return ans

    def empty(self) -> bool:
        """
        只要in或者out有元素，说明队列不为空
        """
        if self.stackin or self.stackout:return False
        else:return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()