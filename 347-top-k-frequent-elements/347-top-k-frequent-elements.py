#时间复杂度：O(nlogk)
#空间复杂度：O(n)
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 小顶堆
        '''
        要统计元素出现频率
        对频率排序
        找出前K个高频元素
        
        什么是优先级队列呢？
        其实就是一个披着队列外衣的堆，因为优先级队列对外接口只是从队头取元素，从队尾添加元素，再无其他取元素的方式，看起来就是一个队列。

        堆是一棵完全二叉树，树中每个结点的值都不小于（或不大于）其左右孩子的值。 如果父亲结点是大于等于左右孩子就是大顶堆，小于等于左右孩子就是小顶堆。大顶堆（堆头是最大元素），小顶堆（堆头是最小元素）

        要用小顶堆，因为要统计最大前k个元素，只有小顶堆每次将最小的元素弹出，最后小顶堆里积累的才是前k个最大元素。
        '''
        #要统计元素出现频率
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i],0)+1 #get()函数操作时当字典中不存在输入的键时会返回一个None,0为初值仅第一次有用

        #对频率排序
        #定义一个小顶堆，大小为k
        que = [] #小顶堆
        for key, freq in dic.items():
            heapq.heappush(que, (freq, key))
            if len(que) > k: #如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
                heapq.heappop(que)
        
        #找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        res = [0]*k
        for i in range(k-1,-1,-1):
            res[i] = heapq.heappop(que)[1]
        return res
