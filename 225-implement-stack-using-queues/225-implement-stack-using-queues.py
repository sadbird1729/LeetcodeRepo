# 队列先进先出，栈后进先出
# deque（双端队列）来模拟一个队列,popleft
# 用两个队列que1和que2实现队列的功能，que2其实完全就是一个备份的作用，
# 把que1最后面的元素以外的元素都备份到que2，然后弹出最后面的元素，再把其他元素从que2导回que1

class MyStack:

    def __init__(self):
        """
        Python普通的Queue或SimpleQueue没有类似于peek的功能
        也无法用索引访问，在实现top的时候较为困难。

        用list可以，但是在使用pop(0)的时候时间复杂度为O(n)
        因此这里使用双向队列，我们保证只执行popleft()和append()，因为deque可以用索引访问，可以实现和peek相似的功能

        in - 存所有数据
        out - 仅在pop的时候会用到
        """
        self.queuein = deque()
        self.queueout = deque()


    def push(self, x: int) -> None:
        """
        直接append即可
        """
        self.queuein.append(x)


    def pop(self) -> int:
        """
        1. 首先确认不空
        2. 因为队列的特殊性，FIFO，所以我们只有在pop()的时候才会使用queue_out
        3. 先把queue_in中的所有元素（除了最后一个），依次出列放进queue_out
        4. 交换in和out，此时out里只有一个元素()
        5. 把out中的pop出来，即是原队列的最后一个
        
        tip：这不能像栈实现队列一样，因为另一个queue也是FIFO，如果执行pop()它不能像
        stack一样从另一个pop()，所以干脆in只用来存数据，pop()的时候两个进行交换
        """
        # in:[1,2,3,4,5] out:[]
        # in:[5] out:[1,2,3,4]   # <--out.append(in.popleft())
        # in:[1,2,3,4] out:[5]    # in, out =  out, in
        # out.popleft就ok了
        if self.empty():return None
        for i in range(len(self.queuein)-1):
            self.queueout.append(self.queuein.popleft())# deque,popleft
        self.queuein, self.queueout = self.queueout, self.queuein
        return self.queueout.popleft()


    def top(self) -> int:
        """
        1. 首先确认不空
        2. 我们仅有in会存放数据，所以返回第一个即可
        """
        if self.empty():return None
        return self.queuein[-1]


    def empty(self) -> bool:
        # if not self.queuein:return True
        # else:return False
        """
        因为只有in存了数据，只要判断in是不是有数即可
        """
        return len(self.queuein) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()